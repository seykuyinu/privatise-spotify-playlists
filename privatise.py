import sys
import spotipy
import spotipy.util as util

def filter_public(playlist_items):
    ''' 
        Returns all public playlsits present in the given playlist array
    '''

    public_playlists = list(filter(lambda playlist: playlist['public'] == True, playlist_items))
    return public_playlists

def pretty_print_playlists(playlists):
    list(map(lambda playlist: print(playlist['name']), playlists))

def make_playlists_private(sp: spotipy.Spotify, username, playlists):
    list(map(lambda playlist: sp.user_playlist_change_details(username, playlist['id'], public=False), playlists))

def main():
    scope = 'user-library-read playlist-modify-public'

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print(f"Usage: {sys.argv[0]} username")
        sys.exit()

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)

        offset = 0
        limit = 20
        count = 0
        while True:
            playlists = sp.current_user_playlists(offset=offset, limit=limit)
            public_playlists = filter_public(playlists['items'])

            if len(public_playlists) > 0:
                print("Privatising the following public playlists.. \n")
                pretty_print_playlists(public_playlists)
                make_playlists_private(sp, username, public_playlists)
                count += len(public_playlists)

            next_page = playlists['next']
            if next_page:
                offset += limit
            else:
                if count == 0: 
                    print("No public playlists were found.")
                else:
                    print(f"{count} public playlists have been made private.")
                break
    else:
        print ("Can't get token for", username)

if __name__ == "__main__":
    main()
