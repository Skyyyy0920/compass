
### Environment Interaction 1
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='spotify'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_genres",
  "description": "Show the list of all music genres."
 },
 {
  "name": "search_songs",
  "description": "Search for songs with a query."
 },
 {
  "name": "show_song",
  "description": "Get details of a specific song."
 },
 {
  "name": "show_song_privates",
  "description": "Show information about the song that is private to the user."
 },
 {
  "name": "like_song",
  "description": "Like a song."
 },
 {
  "name": "unlike_song",
  "description": "Unlike a song."
 },
 {
  "name": "show_liked_songs",
  "description": "Get a list of songs you have liked."
 },
 {
  "name": "search_albums",
  "description": "Search for albums with a query."
 },
 {
  "name": "show_album",
  "description": "Get details of a specific album."
 },
 {
  "name": "show_album_privates",
  "description": "Show information about the album that is private to the user."
 },
 {
  "name": "like_album",
  "description": "Like a album."
 },
 {
  "name": "unlike_album",
  "description": "Unlike a album."
 },
 {
  "name": "show_liked_albums",
  "description": "Get a list of albums you have liked."
 },
 {
  "name": "show_playlist_library",
  "description": "Get a list of playlists in the user's playlist library."
 },
 {
  "name": "search_playlists",
  "description": "Search for playlists with a query. It will search over all public playlists and your own private playlists."
 },
 {
  "name": "create_playlist",
  "description": "Create a new playlist."
 },
 {
  "name": "show_playlist",
  "description": "Get detailed information about a specific playlist. You can view your own playlists or others' playlists if they are public."
 },
 {
  "name": "delete_playlist",
  "description": "Delete a playlist."
 },
 {
  "name": "update_playlist",
  "description": "Update a playlist title or privacy."
 },
 {
  "name": "show_playlist_privates",
  "description": "Show information about the playlist that is private to the user."
 },
 {
  "name": "like_playlist",
  "description": "Like a playlist."
 },
 {
  "name": "unlike_playlist",
  "description": "Unlike a playlist."
 },
 {
  "name": "show_liked_playlists",
  "description": "Get a list of playlists you have liked."
 },
 {
  "name": "search_artists",
  "description": "Search for artists with a query."
 },
 {
  "name": "show_artist",
  "description": "Get details of a specific artist."
 },
 {
  "name": "show_artist_following",
  "description": "Show if the user is following the artist."
 },
 {
  "name": "show_song_library",
  "description": "Get a list of songs in the user's song library."
 },
 {
  "name": "add_song_to_library",
  "description": "Add a song to the user's song library."
 },
 {
  "name": "remove_song_from_library",
  "description": "Remove a song from the user's song library."
 },
 {
  "name": "show_album_library",
  "description": "Get a list of albums in the user's album library."
 },
 {
  "name": "add_album_to_library",
  "description": "Add an album to the user's album library."
 },
 {
  "name": "remove_album_from_library",
  "description": "Remove an album from the user's album library."
 },
 {
  "name": "add_song_to_playlist",
  "description": "Add a song to a playlist."
 },
 {
  "name": "remove_song_from_playlist",
  "description": "Remove a song from a playlist."
 },
 {
  "name": "show_downloaded_songs",
  "description": "Get a list of downloaded songs."
 },
 {
  "name": "download_song",
  "description": "Download a song."
 },
 {
  "name": "remove_downloaded_song",
  "description": "Remove a song from downloads."
 },
 {
  "name": "show_following_artists",
  "description": "Get a list of artists the user is following."
 },
 {
  "name": "follow_artist",
  "description": "Follow an artist."
 },
 {
  "name": "unfollow_artist",
  "description": "Unfollow an artist."
 },
 {
  "name": "show_song_reviews",
  "description": "Get a list of reviews for a song."
 },
 {
  "name": "review_song",
  "description": "Rate or review a song."
 },
 {
  "name": "show_song_review",
  "description": "Show a song review."
 },
 {
  "name": "delete_song_review",
  "description": "Delete a song review."
 },
 {
  "name": "update_song_review",
  "description": "Update a song review."
 },
 {
  "name": "show_album_reviews",
  "description": "Get a list of reviews for an album."
 },
 {
  "name": "review_album",
  "description": "Rate or review an album."
 },
 {
  "name": "show_album_review",
  "description": "Show an album review."
 },
 {
  "name": "delete_album_review",
  "description": "Delete an album review."
 },
 {
  "name": "update_album_review",
  "description": "Update an album review."
 },
 {
  "name": "show_playlist_reviews",
  "description": "Show a list of reviews for your playlist or others' public playlist."
 },
 {
  "name": "review_playlist",
  "description": "Rate or review a playlist."
 },
 {
  "name": "show_playlist_review",
  "description": "Show a playlist review."
 },
 {
  "name": "delete_playlist_review",
  "description": "Delete a playlist review."
 },
 {
  "name": "update_playlist_review",
  "description": "Update a playlist review."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of users payment cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_current_song",
  "description": "Show details of the current song on the queue."
 },
 {
  "name": "play_music",
  "description": "Play music based on various criteria. You can pass, at most, any one of queue_position, song_id, album_id or playlist_id. If one of song_id, album_id or playlist_id is passed, that song, album or playlist will be added to the queue and played. Otherwise, the queue will remain unchanged. If queue_position is passed, the song at that position in the queue will be played. If none is passed, the current song in the queue will be played."
 },
 {
  "name": "pause_music",
  "description": "Pause the currently playing song."
 },
 {
  "name": "previous_song",
  "description": "Go to the previous song in the song queue."
 },
 {
  "name": "next_song",
  "description": "Go to the next song in the song queue."
 },
 {
  "name": "move_song_in_queue",
  "description": "Move a song in the queue to a new position."
 },
 {
  "name": "seek_song",
  "description": "Seek the current song to the given number of seconds."
 },
 {
  "name": "loop_song",
  "description": "Set whether to loop the current song."
 },
 {
  "name": "shuffle_song_queue",
  "description": "Shuffle songs in the music player queue."
 },
 {
  "name": "show_song_queue",
  "description": "Get the music player song queue. Songs are played in the order of the queue in a cycle."
 },
 {
  "name": "add_to_queue",
  "description": "Add a song, album or playlist to the music player song queue."
 },
 {
  "name": "clear_song_queue",
  "description": "Clear the music player song queue."
 },
 {
  "name": "remove_song_from_queue",
  "description": "Remove a song at the given position from the music player song queue."
 },
 {
  "name": "show_volume",
  "description": "Get the volume level of the music player."
 },
 {
  "name": "set_volume",
  "description": "Set the volume level of the music player."
 },
 {
  "name": "show_recommendations",
  "description": "Get personalized song recommendations for the user."
 },
 {
  "name": "show_premium_plans",
  "description": "Show information about premium plans available."
 },
 {
  "name": "show_premium_subscriptions",
  "description": "Show your premium subscription history."
 },
 {
  "name": "subscribe_premium",
  "description": "Subscribe to premium membership."
 },
 {
  "name": "download_premium_subscription_receipt",
  "description": "Download the receipt for a premium subscription."
 }
]
```


### Environment Interaction 2
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='login'))
```

```
{
 "app_name": "spotify",
 "api_name": "login",
 "path": "/auth/token",
 "method": "POST",
 "description": "Login to your account.",
 "parameters": [
  {
   "name": "username",
   "type": "string",
   "required": true,
   "description": "Your account email.",
   "default": null,
   "constraints": []
  },
  {
   "name": "password",
   "type": "string",
   "required": true,
   "description": "Your account password.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "access_token": "string",
   "token_type": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
# Get Spotify password from supervisor
print(apis.supervisor.show_account_passwords())
```

```
[
 {
  "account_name": "amazon",
  "password": "oIhoOb9"
 },
 {
  "account_name": "file_system",
  "password": "4k9jcny"
 },
 {
  "account_name": "gmail",
  "password": "#x}}5n5"
 },
 {
  "account_name": "phone",
  "password": "X53y6aW"
 },
 {
  "account_name": "simple_note",
  "password": "eizVxAh"
 },
 {
  "account_name": "splitwise",
  "password": "F{Q8_pw"
 },
 {
  "account_name": "spotify",
  "password": "3a-m^o6"
 },
 {
  "account_name": "todoist",
  "password": "+&R$o4K"
 },
 {
  "account_name": "venmo",
  "password": "rl2A-Xl"
 }
]
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
# Login to Spotify with user's email and password
login_result = apis.spotify.login(username='carbrown@gmail.com', password='3a-m^o6')
print(login_result)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2NhcmJyb3duQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.kf2xG5M8F_mduPWJbWrURnNy6or8nSA7bzIo2UbELCk",
 "token_type": "Bearer"
}
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
# Get current song and downloaded songs
current_song = apis.spotify.show_current_song()
downloaded_songs = apis.spotify.show_downloaded_songs()
print("Current song:", current_song)
print("Downloaded songs:", downloaded_songs)
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    current_song = apis.spotify.show_current_song()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 401:
{"message":"You are either not authorized to access this spotify API endpoint or your access token is missing, invalid or expired."}
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_current_song'))
```

```
{
 "app_name": "spotify",
 "api_name": "show_current_song",
 "path": "/music_player/current_song",
 "method": "GET",
 "description": "Show details of the current song on the queue.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "song_id": 1,
   "title": "string",
   "album_id": 1,
   "album_title": "string",
   "duration": 1,
   "artists": [
    {
     "id": 1,
     "name": "string"
    }
   ],
   "played_seconds": 1,
   "is_playing": true
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
access_token = login_result['access_token']
current_song = apis.spotify.show_current_song(access_token=access_token)
downloaded_songs = apis.spotify.show_downloaded_songs(access_token=access_token)
print("Current song:", current_song)
print("Downloaded songs:", downloaded_songs)
```

```
Current song: {'song_id': 322, 'title': 'Lost in the Labyrinth of Love', 'album_id': None, 'duration': 281, 'artists': [{'id': 36, 'name': 'Noah Bennett'}], 'played_seconds': 0, 'is_playing': True, 'is_looping': False}
Downloaded songs: [{'song_id': 55, 'title': 'Tangled Lies', 'album_id': 11, 'duration': 186, 'artists': [{'id': 5, 'name': 'Ava Morgan'}], 'downloaded_at': '2023-05-18T12:00:00'}, {'song_id': 66, 'title': 'Phantom Pain', 'album_id': 13, 'duration': 223, 'artists': [{'id': 31, 'name': 'Hazel Winter'}, {'id': 5, 'name': 'Ava Morgan'}], 'downloaded_at': '2023-05-18T12:00:00'}, {'song_id': 13, 'title': 'Beneath the Veil of Illusion', 'album_id': 3, 'duration': 220, 'artists': [{'id': 16, 'name': 'Apollo Serenade'}, {'id': 2, 'name': 'Phoenix Rivers'}], 'downloaded_at': '2023-05-04T02:13:28'}, {'song_id': 8, 'title': 'Shadows of the Past', 'album_id': 2, 'duration': 271, 'artists': [{'id': 32, 'name': 'Lucas Grey'}], 'downloaded_at': '2023-03-10T16:05:49'}, {'song_id': 301, 'title': 'A Fading Reflection in Water', 'album_id': None, 'duration': 244, 'artists': [{'id': 32, 'name': 'Lucas Grey'}], 'downloaded_at': '2023-03-09T14:12:17'}]
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='next_song'))
```

```
{
 "app_name": "spotify",
 "api_name": "next_song",
 "path": "/music_player/next_song",
 "method": "POST",
 "description": "Go to the next song in the song queue.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string",
   "song_id": 1
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
# Loop to go to next song until we find a downloaded song
downloaded_ids = {song['song_id'] for song in downloaded_songs}
current_song_id = current_song['song_id']
max_iterations = 1000
found = False
for _ in range(max_iterations):
    if current_song_id in downloaded_ids:
        found = True
        break
    # Go to next song
    next_result = apis.spotify.next_song(access_token=access_token)
    print("Next song result:", next_result)
    # Get new current song
    current_song = apis.spotify.show_current_song(access_token=access_token)
    current_song_id = current_song['song_id']
    print("Now current song:", current_song)

if found:
    print("Found downloaded song:", current_song)
else:
    print("No downloaded song found in queue after max iterations")

# Complete the task
apis.supervisor.complete_task()
```

```
Next song result: {'message': 'Moved to the next song in the queue.', 'song_id': 40}
Now current song: {'song_id': 40, 'title': 'Burning Like a Distant Star', 'album_id': 8, 'duration': 277, 'artists': [{'id': 8, 'name': 'Aria Sterling'}], 'played_seconds': 0, 'is_playing': True, 'is_looping': False}
Next song result: {'message': 'Moved to the next song in the queue.', 'song_id': 71}
Now current song: {'song_id': 71, 'title': 'Eternal Fade', 'album_id': 15, 'duration': 267, 'artists': [{'id': 29, 'name': 'Lucas Diaz'}, {'id': 7, 'name': 'Orion Steele'}], 'played_seconds': 0, 'is_playing': True, 'is_looping': False}
Next song result: {'message': 'Moved to the next song in the queue.', 'song_id': 50}
Now current song: {'song_id': 50, 'title': 'Lonely Skies', 'album_id': 10, 'duration': 284, 'artists': [{'id': 8, 'name': 'Aria Sterling'}], 'played_seconds': 0, 'is_playing': True, 'is_looping': False}
Next song result: {'message': 'Moved to the next song in the queue.', 'song_id': 66}
Now current song: {'song_id': 66, 'title': 'Phantom Pain', 'album_id': 13, 'duration': 223, 'artists': [{'id': 31, 'name': 'Hazel Winter'}, {'id': 5, 'name': 'Ava Morgan'}], 'played_seconds': 0, 'is_playing': True, 'is_looping': False}
Found downloaded song: {'song_id': 66, 'title': 'Phantom Pain', 'album_id': 13, 'duration': 223, 'artists': [{'id': 31, 'name': 'Hazel Winter'}, {'id': 5, 'name': 'Ava Morgan'}], 'played_seconds': 0, 'is_playing': True, 'is_looping': False}
```

