# Privatise Spotify Playlists

A simple Python (Python 3) script to make all public Spotify playlists private.

## Setup
* Follow the instructions [here](https://developer.spotify.com/documentation/general/guides/app-settings/) to register your app with Spotify. 
* Open ```creds.sh``` and set the values for SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET and SPOTIPY_REDIRECT_URI
* The ```SPOTIPY_REDIRECT_URI``` does not have to be a working url, recommend leaving that value as is.

## Usage:

On first run of the script, you will be directed to a webpage to grant the app access to your Spotify account. Once authorised, copy the url you are redirected to, into the terminal window as prompted.

username = your Spotify userid

```bash
source creds.sh

pip install -r requirements.txt

python3 privatise.py [username]
```
**Current limitation:** Only updates first 50 public playlists

## To-do list: 
- [ ] Address playlist limit issue!
- [ ] Add dry-run feature
- [ ] Process in batches/by playlist group
- [ ] Web app to allow flexibility (e.g. select/deselect playlists)