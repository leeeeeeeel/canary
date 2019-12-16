""" """

import get_history

def suggest(spotify_username='',
            deezer_username='',
            googleplay_username=''):

    history = []
    history.append(get_history.spotify(spotify_username))
    history.append(get_history.deezer(deezer_username))
    history.append(get_history.googleplay(googleplay_username))

    return create_playlist(history)

def create_playlist(history):
    pass
