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
        playlists = sp.current_user_playlists()
        public_playlists = filter_public(playlists['items'])
        if len(public_playlists) > 0:
            pretty_print_playlists(public_playlists)
            confirm = input("Make the above listed playlists private? (yes/no) ")

            if confirm == 'yes':
                make_playlists_private(sp, username, public_playlists)
                print('Playlists updated!')
            else:
                print("No playlists updated.")
        else:
            print("No public playlists to update!")
    else:
        print ("Can't get token for", username)


if __name__ == "__main__":
    main()
