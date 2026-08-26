
### Environment Interaction 1
----------------------------------------------------------------------------
```python
# First, let's see the available apps and their descriptions.
print(apis.api_docs.show_app_descriptions())
```

```
[
 {
  "name": "api_docs",
  "description": "An app to search and explore API documentation."
 },
 {
  "name": "supervisor",
  "description": "An app to access supervisor's personal information, account credentials, addresses, payment cards, and manage the assigned task."
 },
 {
  "name": "amazon",
  "description": "An online shopping app to buy products and manage orders, returns, etc."
 },
 {
  "name": "phone",
  "description": "An app to find and manage contact information for friends, family members, etc., send and receive messages, and manage alarms."
 },
 {
  "name": "file_system",
  "description": "A file system app to create and manage files and folders."
 },
 {
  "name": "spotify",
  "description": "A music streaming app to stream songs and manage song, album and playlist libraries."
 },
 {
  "name": "venmo",
  "description": "A social payment app to send, receive and request money to and from others."
 },
 {
  "name": "gmail",
  "description": "An email app to draft, send, receive, and manage emails."
 },
 {
  "name": "splitwise",
  "description": "A bill splitting app to track and split expenses with people."
 },
 {
  "name": "simple_note",
  "description": "A note-taking app to create and manage notes"
 },
 {
  "name": "todoist",
  "description": "A task management app to manage todo lists and collaborate on them with others."
 }
]
```


### Environment Interaction 2
----------------------------------------------------------------------------
```python
# Let's see the Spotify API descriptions.
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


### Environment Interaction 3
----------------------------------------------------------------------------
```python
# Let's get the Spotify account credentials from supervisor.
print(apis.api_docs.show_api_doc(app_name='supervisor', api_name='show_account_passwords'))
```

```
{
 "app_name": "supervisor",
 "api_name": "show_account_passwords",
 "path": "/account_passwords",
 "method": "GET",
 "description": "Show your supervisor's app account passwords.",
 "parameters": [],
 "response_schemas": {
  "success": [
   {
    "account_name": "string",
    "password": "string"
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
# Let's get the Spotify account credentials from supervisor.
print(apis.supervisor.show_account_passwords())
```

```
[
 {
  "account_name": "amazon",
  "password": "_@+7@Ei"
 },
 {
  "account_name": "file_system",
  "password": "M*}9H25"
 },
 {
  "account_name": "gmail",
  "password": "FgP]brO"
 },
 {
  "account_name": "phone",
  "password": "eF@$eFT"
 },
 {
  "account_name": "simple_note",
  "password": "tHH!E]U"
 },
 {
  "account_name": "splitwise",
  "password": "o1nzdVD"
 },
 {
  "account_name": "spotify",
  "password": "%oxCE]q"
 },
 {
  "account_name": "todoist",
  "password": "7(%[]a8"
 },
 {
  "account_name": "venmo",
  "password": "YUtGXre"
 }
]
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
# Let's see the login API spec for Spotify.
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


### Environment Interaction 6
----------------------------------------------------------------------------
```python
# Login to Spotify with the supervisor's email and password.
print(apis.spotify.login(username='as_moore@gmail.com', password='%oxCE]q'))
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2FzX21vb3JlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.Ry-dT0WNVUiSCQYSD3KUYzl-EGoNtS5NB0ssm2lBGNQ",
 "token_type": "Bearer"
}
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
# Let's check the relevant Spotify API docs for current song, queue, liked songs, and previous song.
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_current_song'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_song_queue'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_liked_songs'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='previous_song'))
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
{
 "app_name": "spotify",
 "api_name": "show_song_queue",
 "path": "/music_player/song_queue",
 "method": "GET",
 "description": "Get the music player song queue. Songs are played in the order of the queue in a cycle.",
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
  "success": [
   {
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
    "position": 1,
    "is_playing": true,
    "is_current": true
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "spotify",
 "api_name": "show_liked_songs",
 "path": "/liked_songs",
 "method": "GET",
 "description": "Get a list of songs you have liked.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "page_index",
   "type": "integer",
   "required": false,
   "description": "The index of the page to return.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "page_limit",
   "type": "integer",
   "required": false,
   "description": "The maximum number of results to return per page.",
   "default": 5,
   "constraints": [
    "value >= 1.0, <= 20.0"
   ]
  },
  {
   "name": "sort_by",
   "type": "string",
   "required": false,
   "description": "The attribute to sort the liked songs by prefixed with +/- to reflect ascending/descending. Valid attributes: liked_at, play_count and title.",
   "default": "-liked_at",
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   {
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
    "liked_at": "2019-01-01T00:00:00"
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "spotify",
 "api_name": "previous_song",
 "path": "/music_player/previous_song",
 "method": "POST",
 "description": "Go to the previous song in the song queue.",
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


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Let's get the current song and the liked songs.
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2FzX21vb3JlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.Ry-dT0WNVUiSCQYSD3KUYzl-EGoNtS5NB0ssm2lBGNQ'

# Get current song
current_song = apis.spotify.show_current_song(access_token=access_token)
print("Current song:", current_song)

# Get liked songs (first page)
liked_songs = apis.spotify.show_liked_songs(access_token=access_token, page_index=0, page_limit=20)
print("Liked songs page 0:", liked_songs)
```

```
Current song: {'song_id': 93, 'title': 'The Ephemeral Dance of Love', 'album_id': None, 'duration': 191, 'artists': [{'id': 3, 'name': 'Jasper Skye'}], 'played_seconds': 0, 'is_playing': True, 'is_looping': False}
Liked songs page 0: [{'song_id': 33, 'title': 'Unveiled', 'album_id': 7, 'duration': 238, 'artists': [{'id': 11, 'name': 'Eliana Harper'}], 'liked_at': '2023-05-18T12:00:00'}, {'song_id': 299, 'title': 'In the Wake of Goodbye', 'album_id': None, 'duration': 261, 'artists': [{'id': 32, 'name': 'Lucas Grey'}], 'liked_at': '2023-05-18T12:00:00'}, {'song_id': 117, 'title': 'The Intangible Essence of You', 'album_id': None, 'duration': 281, 'artists': [{'id': 6, 'name': 'Seraphina Dawn'}], 'liked_at': '2023-03-14T04:50:33'}, {'song_id': 68, 'title': 'Lost in the Wilderness of Love', 'album_id': 14, 'duration': 280, 'artists': [{'id': 34, 'name': 'Lily Moon'}, {'id': 9, 'name': 'Zoey James'}], 'liked_at': '2023-02-21T17:57:11'}, {'song_id': 82, 'title': 'Lost in the Twilight of Hope', 'album_id': 18, 'duration': 193, 'artists': [{'id': 33, 'name': 'Felix Blackwood'}], 'liked_at': '2022-12-30T00:14:35'}, {'song_id': 216, 'title': 'The Paradox of Our Love', 'album_id': None, 'duration': 215, 'artists': [{'id': 21, 'name': 'Oceanic Odyssey'}], 'liked_at': '2022-12-17T08:17:36'}, {'song_id': 291, 'title': 'Fading Like a Distant Star', 'album_id': None, 'duration': 182, 'artists': [{'id': 31, 'name': 'Hazel Winter'}], 'liked_at': '2022-11-23T00:41:12'}, {'song_id': 254, 'title': 'Blind Trust', 'album_id': None, 'duration': 247, 'artists': [{'id': 26, 'name': 'Isabella Cruz'}], 'liked_at': '2022-10-14T01:35:08'}, {'song_id': 122, 'title': 'Lost Souls', 'album_id': None, 'duration': 206, 'artists': [{'id': 7, 'name': 'Orion Steele'}], 'liked_at': '2022-09-21T15:56:27'}, {'song_id': 225, 'title': 'Shadows in the Twilight', 'album_id': None, 'duration': 244, 'artists': [{'id': 22, 'name': 'Silent Thunder'}], 'liked_at': '2022-09-16T18:53:44'}, {'song_id': 9, 'title': 'When Fate Becomes a Foe', 'album_id': 2, 'duration': 196, 'artists': [{'id': 32, 'name': 'Lucas Grey'}], 'liked_at': '2022-09-08T16:16:51'}, {'song_id': 90, 'title': 'Whispers of Tomorrow', 'album_id': None, 'duration': 289, 'artists': [{'id': 2, 'name': 'Phoenix Rivers'}], 'liked_at': '2022-09-08T03:36:15'}, {'song_id': 196, 'title': 'Falling Through the Cracks of Time', 'album_id': None, 'duration': 278, 'artists': [{'id': 18, 'name': 'Astrid Nightshade'}], 'liked_at': '2022-08-18T21:07:46'}, {'song_id': 23, 'title': "Solitude's Melancholy", 'album_id': 5, 'duration': 287, 'artists': [{'id': 32, 'name': 'Lucas Grey'}, {'id': 25, 'name': 'Velvet Echo'}], 'liked_at': '2022-08-03T17:43:55'}, {'song_id': 147, 'title': 'In the Arms of a Stranger', 'album_id': None, 'duration': 199, 'artists': [{'id': 11, 'name': 'Eliana Harper'}], 'liked_at': '2022-07-19T17:19:25'}, {'song_id': 193, 'title': 'Fading Echoes', 'album_id': None, 'duration': 204, 'artists': [{'id': 18, 'name': 'Astrid Nightshade'}], 'liked_at': '2022-07-18T07:42:13'}, {'song_id': 278, 'title': "A Broken Heart's Lament", 'album_id': None, 'duration': 215, 'artists': [{'id': 29, 'name': 'Lucas Diaz'}], 'liked_at': '2022-07-18T05:30:53'}, {'song_id': 27, 'title': 'When Angels Weep for Us', 'album_id': 5, 'duration': 230, 'artists': [{'id': 32, 'name': 'Lucas Grey'}, {'id': 25, 'name': 'Velvet Echo'}], 'liked_at': '2022-07-14T10:32:50'}, {'song_id': 45, 'title': 'Eclipsed', 'album_id': 9, 'duration': 267, 'artists': [{'id': 8, 'name': 'Aria Sterling'}], 'liked_at': '2022-07-06T20:55:04'}]
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
# Let's get the song queue to understand the order.
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2FzX21vb3JlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.Ry-dT0WNVUiSCQYSD3KUYzl-EGoNtS5NB0ssm2lBGNQ'
queue = apis.spotify.show_song_queue(access_token=access_token)
print(queue)
```

```
[
 {
  "song_id": 33,
  "title": "Unveiled",
  "album_id": 7,
  "duration": 238,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "position": 0,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 190,
  "title": "Final Goodbye",
  "album_id": null,
  "duration": 291,
  "artists": [
   {
    "id": 17,
    "name": "Dylan Stone"
   }
  ],
  "position": 1,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 277,
  "title": "Hidden Scars",
  "album_id": null,
  "duration": 297,
  "artists": [
   {
    "id": 29,
    "name": "Lucas Diaz"
   }
  ],
  "position": 2,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 182,
  "title": "Melodies of the Forgotten Past",
  "album_id": null,
  "duration": 282,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "position": 3,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 48,
  "title": "Cherry Blossom Tears",
  "album_id": 10,
  "duration": 286,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "position": 4,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 93,
  "title": "The Ephemeral Dance of Love",
  "album_id": null,
  "duration": 191,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   }
  ],
  "position": 5,
  "is_playing": true,
  "is_current": true
 },
 {
  "song_id": 98,
  "title": "Chasing Echoes in the Rain",
  "album_id": null,
  "duration": 261,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   }
  ],
  "position": 6,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 192,
  "title": "Chronicles of a Broken Heart",
  "album_id": null,
  "duration": 266,
  "artists": [
   {
    "id": 18,
    "name": "Astrid Nightshade"
   }
  ],
  "position": 7,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 50,
  "title": "Lonely Skies",
  "album_id": 10,
  "duration": 284,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "position": 8,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 299,
  "title": "In the Wake of Goodbye",
  "album_id": null,
  "duration": 261,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   }
  ],
  "position": 9,
  "is_playing": false,
  "is_current": false
 }
]
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
# Let's get all liked songs by fetching all pages.
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2FzX21vb3JlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.Ry-dT0WNVUiSCQYSD3KUYzl-EGoNtS5NB0ssm2lBGNQ'

all_liked_songs = []
page_index = 0
while True:
    page = apis.spotify.show_liked_songs(access_token=access_token, page_index=page_index, page_limit=20)
    if not page:
        break
    all_liked_songs.extend(page)
    if len(page) < 20:
        break
    page_index += 1

liked_song_ids = {song['song_id'] for song in all_liked_songs}
print(f"Total liked songs: {len(all_liked_songs)}")
print(f"Liked song IDs: {sorted(liked_song_ids)}")
```

```
Total liked songs: 19
Liked song IDs: [9, 23, 27, 33, 45, 68, 82, 90, 117, 122, 147, 193, 196, 216, 225, 254, 278, 291, 299]
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Let's go to the previous song and check if it's liked.
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2FzX21vb3JlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.Ry-dT0WNVUiSCQYSD3KUYzl-EGoNtS5NB0ssm2lBGNQ'
result = apis.spotify.previous_song(access_token=access_token)
print(result)
current = apis.spotify.show_current_song(access_token=access_token)
print(current)
```

```
{"message": "Moved to the previous song in the queue.", "song_id": 48}
{
 "song_id": 48,
 "title": "Cherry Blossom Tears",
 "album_id": 10,
 "duration": 286,
 "artists": [
  {
   "id": 8,
   "name": "Aria Sterling"
  }
 ],
 "played_seconds": 0,
 "is_playing": true,
 "is_looping": false
}
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
# Song 48 is not liked. Go to previous song.
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2FzX21vb3JlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.Ry-dT0WNVUiSCQYSD3KUYzl-EGoNtS5NB0ssm2lBGNQ'
result = apis.spotify.previous_song(access_token=access_token)
print(result)
current = apis.spotify.show_current_song(access_token=access_token)
print(current)
```

```
{"message": "Moved to the previous song in the queue.", "song_id": 182}
{
 "song_id": 182,
 "title": "Melodies of the Forgotten Past",
 "album_id": null,
 "duration": 282,
 "artists": [
  {
   "id": 16,
   "name": "Apollo Serenade"
  }
 ],
 "played_seconds": 0,
 "is_playing": true,
 "is_looping": false
}
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# Song 182 is not liked. Go to previous song.
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2FzX21vb3JlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.Ry-dT0WNVUiSCQYSD3KUYzl-EGoNtS5NB0ssm2lBGNQ'
result = apis.spotify.previous_song(access_token=access_token)
print(result)
current = apis.spotify.show_current_song(access_token=access_token)
print(current)
```

```
{"message": "Moved to the previous song in the queue.", "song_id": 277}
{
 "song_id": 277,
 "title": "Hidden Scars",
 "album_id": null,
 "duration": 297,
 "artists": [
  {
   "id": 29,
   "name": "Lucas Diaz"
  }
 ],
 "played_seconds": 0,
 "is_playing": true,
 "is_looping": false
}
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
# Song 277 is not liked. Go to previous song.
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2FzX21vb3JlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.Ry-dT0WNVUiSCQYSD3KUYzl-EGoNtS5NB0ssm2lBGNQ'
result = apis.spotify.previous_song(access_token=access_token)
print(result)
current = apis.spotify.show_current_song(access_token=access_token)
print(current)
```

```
{"message": "Moved to the previous song in the queue.", "song_id": 190}
{
 "song_id": 190,
 "title": "Final Goodbye",
 "album_id": null,
 "duration": 291,
 "artists": [
  {
   "id": 17,
   "name": "Dylan Stone"
  }
 ],
 "played_seconds": 0,
 "is_playing": true,
 "is_looping": false
}
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
# Song 190 is not liked. Go to previous song.
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2FzX21vb3JlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.Ry-dT0WNVUiSCQYSD3KUYzl-EGoNtS5NB0ssm2lBGNQ'
result = apis.spotify.previous_song(access_token=access_token)
print(result)
current = apis.spotify.show_current_song(access_token=access_token)
print(current)
```

```
{"message": "Moved to the previous song in the queue.", "song_id": 33}
{
 "song_id": 33,
 "title": "Unveiled",
 "album_id": 7,
 "duration": 238,
 "artists": [
  {
   "id": 11,
   "name": "Eliana Harper"
  }
 ],
 "played_seconds": 0,
 "is_playing": true,
 "is_looping": false
}
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
# We have reached song 33 "Unveiled" which is in the liked songs list. The task is complete.
apis.supervisor.complete_task()
```

```
Execution successful.
```

