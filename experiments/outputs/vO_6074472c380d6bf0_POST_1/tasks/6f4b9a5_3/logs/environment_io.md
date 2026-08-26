
### Environment Interaction 1
----------------------------------------------------------------------------
```python
# Let's first see the available apps and their descriptions.
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
# Let's explore the simple_note app APIs.
print(apis.api_docs.show_api_descriptions(app_name='simple_note'))
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
  "name": "search_notes",
  "description": "Search your notes. This will not show contents of the notes. Pinned notes will be shown first by default, except when dont_reorder_pinned is true."
 },
 {
  "name": "create_note",
  "description": "Create a new note."
 },
 {
  "name": "show_note",
  "description": "Show detailed information of a note, including its content."
 },
 {
  "name": "delete_note",
  "description": "Delete a note."
 },
 {
  "name": "update_note",
  "description": "Update a note's title, content, tags, and/or pinned status."
 },
 {
  "name": "add_content_to_note",
  "description": "Append or prepend content to a note."
 }
]
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
# Let's check the supervisor app for account credentials.
print(apis.api_docs.show_api_descriptions(app_name='supervisor'))
```

```
[
 {
  "name": "show_active_task",
  "description": "Show the currently active task assigned to you by the supervisor."
 },
 {
  "name": "complete_task",
  "description": "Mark the currently active task as complete with the given answer."
 },
 {
  "name": "show_profile",
  "description": "Show your supervisor's profile information."
 },
 {
  "name": "show_addresses",
  "description": "Show your supervisor's addresses."
 },
 {
  "name": "show_payment_cards",
  "description": "Show your supervisor's payment_cards."
 },
 {
  "name": "show_account_passwords",
  "description": "Show your supervisor's app account passwords."
 }
]
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
# Let's get the account passwords from supervisor.
print(apis.supervisor.show_account_passwords())
```

```
[
 {
  "account_name": "amazon",
  "password": "[l0#5Yw"
 },
 {
  "account_name": "file_system",
  "password": "V]^dE[b"
 },
 {
  "account_name": "gmail",
  "password": "YUUXyJY"
 },
 {
  "account_name": "phone",
  "password": "]wpD$Y6"
 },
 {
  "account_name": "simple_note",
  "password": "sTv9L0p"
 },
 {
  "account_name": "splitwise",
  "password": "_fmm=r1"
 },
 {
  "account_name": "spotify",
  "password": "=ql86Wp"
 },
 {
  "account_name": "todoist",
  "password": "cO0f)9V"
 },
 {
  "account_name": "venmo",
  "password": "+REx^]2"
 }
]
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
# Let's see the login API specification for simple_note.
print(apis.api_docs.show_api_doc(app_name='simple_note', api_name='login'))
```

```
{
 "app_name": "simple_note",
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
# Login to simple_note with the supervisor's email and password.
print(apis.simple_note.login(username='alexwhite@gmail.com', password='sTv9L0p'))
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZSthbGV4d2hpdGVAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyMDk4fQ.VMhraCsVPjQJj_BspbHcmYtryXaeQ8QSyrJBz1oWxuU",
 "token_type": "Bearer"
}
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
# Now let's search for notes in simple_note.
print(apis.simple_note.search_notes())
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    print(apis.simple_note.search_notes())
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 401:
{"message":"You are either not authorized to access this simple_note API endpoint or your access token is missing, invalid or expired."}
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Let's check the search_notes API specification.
print(apis.api_docs.show_api_doc(app_name='simple_note', api_name='search_notes'))
```

```
{
 "app_name": "simple_note",
 "api_name": "search_notes",
 "path": "/notes",
 "method": "GET",
 "description": "Search your notes. This will not show contents of the notes. Pinned notes will be shown first by default, except when dont_reorder_pinned is true.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from simple_note app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "query",
   "type": "string",
   "required": false,
   "description": "Search query for the notes.",
   "default": "",
   "constraints": []
  },
  {
   "name": "tags",
   "type": "list[string]",
   "required": false,
   "description": "Tags to filter the notes by. Notes not having any of these tags will be filtered out.",
   "default": null,
   "constraints": []
  },
  {
   "name": "pinned",
   "type": "boolean",
   "required": false,
   "description": "Filter notes by pinned status.",
   "default": null,
   "constraints": []
  },
  {
   "name": "dont_reorder_pinned",
   "type": "boolean",
   "required": false,
   "description": "If true, pinned notes will not be reordered to be shown at the top.",
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
   "description": "The attribute to sort the notes by prefixed with +/- to reflect ascending/descending. Valid attributes: created_at and updated_at. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page. If both query and sort_by are not given, null, or empty, sort_by will default to -updated_at.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   {
    "note_id": 1,
    "title": "string",
    "tags": [
     "string"
    ],
    "created_at": "2019-01-01T00:00:00",
    "updated_at": "2019-01-01T00:00:00",
    "pinned": true
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
# Let's store the access token and search for notes.
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZSthbGV4d2hpdGVAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyMDk4fQ.VMhraCsVPjQJj_BspbHcmYtryXaeQ8QSyrJBz1oWxuU"
print(apis.simple_note.search_notes(access_token=access_token))
```

```
[
 {
  "note_id": 3086,
  "title": "Songs to Try Out",
  "tags": [],
  "created_at": "2023-05-18T11:40:17",
  "updated_at": "2023-05-18T11:40:17",
  "pinned": true
 },
 {
  "note_id": 3085,
  "title": "Followed Artists on Spotify",
  "tags": [],
  "created_at": "2023-05-18T11:10:51",
  "updated_at": "2023-05-18T11:10:51",
  "pinned": true
 },
 {
  "note_id": 3069,
  "title": "Habit Tracking Log for 2023-05-17",
  "tags": [
   "habit-tracker"
  ],
  "created_at": "2023-05-17T20:48:03",
  "updated_at": "2023-05-17T20:48:03",
  "pinned": true
 },
 {
  "note_id": 3070,
  "title": "Habit Tracking Log for 2023-05-16",
  "tags": [
   "habit-tracker"
  ],
  "created_at": "2023-05-16T20:55:25",
  "updated_at": "2023-05-16T20:55:25",
  "pinned": true
 },
 {
  "note_id": 3084,
  "title": "Spotify Liked Songs",
  "tags": [],
  "created_at": "2023-05-17T12:13:03",
  "updated_at": "2023-05-17T12:13:03",
  "pinned": false
 }
]
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
# Let's look at the "Spotify Liked Songs" note.
print(apis.simple_note.show_note(access_token=access_token, note_id=3084))
```

```
{
 "note_id": 3084,
 "title": "Spotify Liked Songs",
 "content": "# Spotify Liked Songs\n- When Angels Weep for Us BY Lucas Grey, Velvet Echo RELEASED_AT 07/2022\n- Unspoken Words BY Aria Sterling RELEASED_AT 06/2021\n- Time's Hold BY Aria Sterling RELEASED_AT 11/2022\n- Bleeding Sun BY Aria Sterling RELEASED_AT 11/2022\n- Distant Love BY Ava Morgan RELEASED_AT 12/2022\n- Silver Lining BY Ava Morgan RELEASED_AT TODO\n- Walking Through the Valley of Shadows BY Lily Moon, Zoey James RELEASED_AT TODO\n- Where Shadows Come to Life BY Olivia Roberts RELEASED_AT TODO\n- Eternal Melancholy BY Olivia Roberts RELEASED_AT TODO\n- Crimson Veil BY Phoenix Rivers RELEASED_AT TODO\n- Elusive Joy BY Orion Steele RELEASED_AT TODO\n- Ephemeral Beauty BY Eliana Harper RELEASED_AT TODO\n- Stardust Serenade BY Violet Cascade RELEASED_AT TODO\n- Veiled Behind a Mask of Joy BY Liam Palmer RELEASED_AT TODO\n- In the Wake of Unspoken Promises BY Isabella Cruz RELEASED_AT TODO\n- Wading Through the Ashes of Love BY Marcus Lane RELEASED_AT TODO\n- Fading Like a Distant Star BY Hazel Winter RELEASED_AT TODO\n- Wilted Grace BY Felix Blackwood RELEASED_AT TODO\n",
 "tags": [],
 "created_at": "2023-05-17T12:13:03",
 "updated_at": "2023-05-17T12:13:03",
 "pinned": false
}
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Let's explore the Spotify app APIs.
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


### Environment Interaction 12
----------------------------------------------------------------------------
```python
# Let's login to Spotify.
print(apis.spotify.login(username='alexwhite@gmail.com', password='=ql86Wp'))
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2FsZXh3aGl0ZUBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTI3NDF9.3qp0wHC-52erJSa156gnuidJtPtERlDZWGt8QFflbuY",
 "token_type": "Bearer"
}
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# Let's check the Spotify search_songs API documentation.
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='search_songs'))
```

```
{
 "app_name": "spotify",
 "api_name": "search_songs",
 "path": "/songs",
 "method": "GET",
 "description": "Search for songs with a query.",
 "parameters": [
  {
   "name": "query",
   "type": "string",
   "required": false,
   "description": "The search query string.",
   "default": "",
   "constraints": []
  },
  {
   "name": "artist_id",
   "type": "integer",
   "required": false,
   "description": "The artist id to filter the search results by.",
   "default": null,
   "constraints": []
  },
  {
   "name": "album_id",
   "type": "integer",
   "required": false,
   "description": "The album id to filter the search results by.",
   "default": null,
   "constraints": []
  },
  {
   "name": "genre",
   "type": "string",
   "required": false,
   "description": "The genre to filter the albums by.",
   "default": null,
   "constraints": []
  },
  {
   "name": "min_release_date",
   "type": "string",
   "required": false,
   "description": "The minimum release date for search results in YYYY-MM-DD format.",
   "default": "1500-01-01",
   "constraints": []
  },
  {
   "name": "max_release_date",
   "type": "string",
   "required": false,
   "description": "The maximum release date for search results in YYYY-MM-DD format.",
   "default": "3000-01-01",
   "constraints": []
  },
  {
   "name": "min_duration",
   "type": "integer",
   "required": false,
   "description": "The minimum duration in seconds for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "max_duration",
   "type": "integer",
   "required": false,
   "description": "The maximum duration in seconds for search results.",
   "default": 9223372036854775807,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "min_rating",
   "type": "number",
   "required": false,
   "description": "The minimum rating for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "max_rating",
   "type": "number",
   "required": false,
   "description": "The maximum rating for search results.",
   "default": 5,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "min_like_count",
   "type": "integer",
   "required": false,
   "description": "The minimum like count for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "max_like_count",
   "type": "integer",
   "required": false,
   "description": "The maximum like count for search results.",
   "default": 9223372036854775807,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "min_play_count",
   "type": "integer",
   "required": false,
   "description": "The minimum play count for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "max_play_count",
   "type": "integer",
   "required": false,
   "description": "The maximum play count for search results.",
   "default": 9223372036854775807,
   "constraints": [
    "value >= 0.0"
   ]
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
   "description": "The attribute to sort the songs by prefixed with +/- to reflect ascending/descending. Valid attributes: rating, like_count and play_count. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page.",
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
    "release_date": "2019-01-01T00:00:00",
    "genre": "string",
    "play_count": 0.0,
    "rating": 0.0,
    "like_count": 1,
    "review_count": 1,
    "shareable_link": "string"
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
# Let's search for the first song with TODO: "Silver Lining" by "Ava Morgan"
print(apis.spotify.search_songs(query='Silver Lining Ava Morgan'))
```

```
[
 {
  "song_id": 57,
  "title": "Silver Lining",
  "album_id": 11,
  "duration": 287,
  "artists": [
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2022-12-11T06:22:44",
  "genre": "EDM",
  "play_count": 421,
  "rating": 0.0,
  "like_count": 15,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/57"
 },
 {
  "song_id": 54,
  "title": "Heartstrings Symphony",
  "album_id": 11,
  "duration": 232,
  "artists": [
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2022-12-11T06:22:44",
  "genre": "EDM",
  "play_count": 845,
  "rating": 0.0,
  "like_count": 12,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/54"
 },
 {
  "song_id": 55,
  "title": "Tangled Lies",
  "album_id": 11,
  "duration": 186,
  "artists": [
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2022-12-11T06:22:44",
  "genre": "EDM",
  "play_count": 437,
  "rating": 0.0,
  "like_count": 20,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/55"
 },
 {
  "song_id": 56,
  "title": "Distant Love",
  "album_id": 11,
  "duration": 202,
  "artists": [
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2022-12-11T06:22:44",
  "genre": "EDM",
  "play_count": 334,
  "rating": 0.0,
  "like_count": 17,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/56"
 },
 {
  "song_id": 107,
  "title": "Quiet Despair",
  "album_id": null,
  "duration": 191,
  "artists": [
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2021-05-21T07:02:49",
  "genre": "EDM",
  "play_count": 466,
  "rating": 3.5,
  "like_count": 7,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/107"
 }
]
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
# Let's check the simple_note API for updating notes.
print(apis.api_docs.show_api_descriptions(app_name='simple_note'))
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
  "name": "search_notes",
  "description": "Search your notes. This will not show contents of the notes. Pinned notes will be shown first by default, except when dont_reorder_pinned is true."
 },
 {
  "name": "create_note",
  "description": "Create a new note."
 },
 {
  "name": "show_note",
  "description": "Show detailed information of a note, including its content."
 },
 {
  "name": "delete_note",
  "description": "Delete a note."
 },
 {
  "name": "update_note",
  "description": "Update a note's title, content, tags, and/or pinned status."
 },
 {
  "name": "add_content_to_note",
  "description": "Append or prepend content to a note."
 }
]
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
# Let's check the update_note API documentation.
print(apis.api_docs.show_api_doc(app_name='simple_note', api_name='update_note'))
```

```
{
 "app_name": "simple_note",
 "api_name": "update_note",
 "path": "/notes/{note_id}",
 "method": "PATCH",
 "description": "Update a note's title, content, tags, and/or pinned status.",
 "parameters": [
  {
   "name": "note_id",
   "type": "integer",
   "required": true,
   "description": "ID of the note to update.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from simple_note app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "title",
   "type": "string",
   "required": false,
   "description": "Updated title of the note.",
   "default": null,
   "constraints": [
    "length >= 1"
   ]
  },
  {
   "name": "content",
   "type": "string",
   "required": false,
   "description": "Updated content of the note.",
   "default": null,
   "constraints": []
  },
  {
   "name": "tags",
   "type": "list[string]",
   "required": false,
   "description": "Updated tags for the note.",
   "default": null,
   "constraints": []
  },
  {
   "name": "pinned",
   "type": "boolean",
   "required": false,
   "description": "Updated pinned status of the note.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
# Let's retrieve the full content of note 3084 to see the exact format.
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZSthbGV4d2hpdGVAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyMDk4fQ.VMhraCsVPjQJj_BspbHcmYtryXaeQ8QSyrJBz1oWxuU'
print(apis.simple_note.show_note(note_id=3084, access_token=access_token))
```

```
{
 "note_id": 3084,
 "title": "Spotify Liked Songs",
 "content": "# Spotify Liked Songs\n- When Angels Weep for Us BY Lucas Grey, Velvet Echo RELEASED_AT 07/2022\n- Unspoken Words BY Aria Sterling RELEASED_AT 06/2021\n- Time's Hold BY Aria Sterling RELEASED_AT 11/2022\n- Bleeding Sun BY Aria Sterling RELEASED_AT 11/2022\n- Distant Love BY Ava Morgan RELEASED_AT 12/2022\n- Silver Lining BY Ava Morgan RELEASED_AT TODO\n- Walking Through the Valley of Shadows BY Lily Moon, Zoey James RELEASED_AT TODO\n- Where Shadows Come to Life BY Olivia Roberts RELEASED_AT TODO\n- Eternal Melancholy BY Olivia Roberts RELEASED_AT TODO\n- Crimson Veil BY Phoenix Rivers RELEASED_AT TODO\n- Elusive Joy BY Orion Steele RELEASED_AT TODO\n- Ephemeral Beauty BY Eliana Harper RELEASED_AT TODO\n- Stardust Serenade BY Violet Cascade RELEASED_AT TODO\n- Veiled Behind a Mask of Joy BY Liam Palmer RELEASED_AT TODO\n- In the Wake of Unspoken Promises BY Isabella Cruz RELEASED_AT TODO\n- Wading Through the Ashes of Love BY Marcus Lane RELEASED_AT TODO\n- Fading Like a Distant Star BY Hazel Winter RELEASED_AT TODO\n- Wilted Grace BY Felix Blackwood RELEASED_AT TODO\n",
 "tags": [],
 "created_at": "2023-05-17T12:13:03",
 "updated_at": "2023-05-17T12:13:03",
 "pinned": false
}
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
# Let's check the search_songs API documentation to understand parameters and response.
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='search_songs'))
```

```
{
 "app_name": "spotify",
 "api_name": "search_songs",
 "path": "/songs",
 "method": "GET",
 "description": "Search for songs with a query.",
 "parameters": [
  {
   "name": "query",
   "type": "string",
   "required": false,
   "description": "The search query string.",
   "default": "",
   "constraints": []
  },
  {
   "name": "artist_id",
   "type": "integer",
   "required": false,
   "description": "The artist id to filter the search results by.",
   "default": null,
   "constraints": []
  },
  {
   "name": "album_id",
   "type": "integer",
   "required": false,
   "description": "The album id to filter the search results by.",
   "default": null,
   "constraints": []
  },
  {
   "name": "genre",
   "type": "string",
   "required": false,
   "description": "The genre to filter the albums by.",
   "default": null,
   "constraints": []
  },
  {
   "name": "min_release_date",
   "type": "string",
   "required": false,
   "description": "The minimum release date for search results in YYYY-MM-DD format.",
   "default": "1500-01-01",
   "constraints": []
  },
  {
   "name": "max_release_date",
   "type": "string",
   "required": false,
   "description": "The maximum release date for search results in YYYY-MM-DD format.",
   "default": "3000-01-01",
   "constraints": []
  },
  {
   "name": "min_duration",
   "type": "integer",
   "required": false,
   "description": "The minimum duration in seconds for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "max_duration",
   "type": "integer",
   "required": false,
   "description": "The maximum duration in seconds for search results.",
   "default": 9223372036854775807,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "min_rating",
   "type": "number",
   "required": false,
   "description": "The minimum rating for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "max_rating",
   "type": "number",
   "required": false,
   "description": "The maximum rating for search results.",
   "default": 5,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "min_like_count",
   "type": "integer",
   "required": false,
   "description": "The minimum like count for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "max_like_count",
   "type": "integer",
   "required": false,
   "description": "The maximum like count for search results.",
   "default": 9223372036854775807,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "min_play_count",
   "type": "integer",
   "required": false,
   "description": "The minimum play count for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "max_play_count",
   "type": "integer",
   "required": false,
   "description": "The maximum play count for search results.",
   "default": 9223372036854775807,
   "constraints": [
    "value >= 0.0"
   ]
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
   "description": "The attribute to sort the songs by prefixed with +/- to reflect ascending/descending. Valid attributes: rating, like_count and play_count. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page.",
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
    "release_date": "2019-01-01T00:00:00",
    "genre": "string",
    "play_count": 0.0,
    "rating": 0.0,
    "like_count": 1,
    "review_count": 1,
    "shareable_link": "string"
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 19
----------------------------------------------------------------------------
```python
# Let's search for the next song "Walking Through the Valley of Shadows" by Lily Moon, Zoey James
spotify_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2FsZXh3aGl0ZUBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTI3NDF9.3qp0wHC-52erJSa156gnuidJtPtERlDZWGtZSQFflbuY'
print(apis.spotify.search_songs(query="Walking Through the Valley of Shadows Lily Moon Zoey James", access_token=spotify_token, page_limit=20))
```

```
[
 {
  "song_id": 75,
  "title": "Walking Through the Valley of Shadows",
  "album_id": 16,
  "duration": 195,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   },
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2022-08-02T08:03:50",
  "genre": "rock",
  "play_count": 806,
  "rating": 2.0,
  "like_count": 22,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/75"
 },
 {
  "song_id": 76,
  "title": "Whispers of the Heart",
  "album_id": 16,
  "duration": 270,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   },
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2022-08-02T08:03:50",
  "genre": "rock",
  "play_count": 330,
  "rating": 3.0,
  "like_count": 14,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/76"
 },
 {
  "song_id": 74,
  "title": "On the Border of Reality",
  "album_id": 16,
  "duration": 296,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   },
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2022-08-02T08:03:50",
  "genre": "rock",
  "play_count": 846,
  "rating": 4.0,
  "like_count": 14,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/74"
 },
 {
  "song_id": 69,
  "title": "Whispers of a Forgotten Love",
  "album_id": 14,
  "duration": 285,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   },
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2022-02-21T17:34:33",
  "genre": "rock",
  "play_count": 645,
  "rating": 4.0,
  "like_count": 17,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/69"
 },
 {
  "song_id": 67,
  "title": "The Echoes of a Silent Heart",
  "album_id": 14,
  "duration": 240,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   },
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2022-02-21T17:34:33",
  "genre": "rock",
  "play_count": 916,
  "rating": 0.0,
  "like_count": 9,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/67"
 },
 {
  "song_id": 68,
  "title": "Lost in the Wilderness of Love",
  "album_id": 14,
  "duration": 280,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   },
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2022-02-21T17:34:33",
  "genre": "rock",
  "play_count": 156,
  "rating": 3.0,
  "like_count": 13,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/68"
 },
 {
  "song_id": 309,
  "title": "Final Act",
  "album_id": null,
  "duration": 230,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   }
  ],
  "release_date": "2019-07-02T06:55:50",
  "genre": "rock",
  "play_count": 520,
  "rating": 2.0,
  "like_count": 8,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/309"
 },
 {
  "song_id": 311,
  "title": "Infinite Dreams",
  "album_id": null,
  "duration": 258,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   }
  ],
  "release_date": "2020-07-26T22:25:50",
  "genre": "rock",
  "play_count": 990,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/311"
 },
 {
  "song_id": 312,
  "title": "Eternal Tears",
  "album_id": null,
  "duration": 266,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   }
  ],
  "release_date": "2018-12-06T10:52:08",
  "genre": "rock",
  "play_count": 562,
  "rating": 2.0,
  "like_count": 7,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/312"
 },
 {
  "song_id": 313,
  "title": "Mystical Dreamscape",
  "album_id": null,
  "duration": 228,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   }
  ],
  "release_date": "2022-05-03T19:16:31",
  "genre": "rock",
  "play_count": 864,
  "rating": 3.7,
  "like_count": 3,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/313"
 },
 {
  "song_id": 310,
  "title": "Harmony of the Distant Stars",
  "album_id": null,
  "duration": 289,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   }
  ],
  "release_date": "2020-10-02T21:17:12",
  "genre": "rock",
  "play_count": 715,
  "rating": 2.0,
  "like_count": 6,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/310"
 },
 {
  "song_id": 58,
  "title": "Cursed Love",
  "album_id": 12,
  "duration": 214,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2021-10-02T22:00:08",
  "genre": "rock",
  "play_count": 602,
  "rating": 4.0,
  "like_count": 12,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/58"
 },
 {
  "song_id": 61,
  "title": "Ocean Eyes",
  "album_id": 12,
  "duration": 271,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2021-10-02T22:00:08",
  "genre": "rock",
  "play_count": 820,
  "rating": 0.0,
  "like_count": 17,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/61"
 },
 {
  "song_id": 60,
  "title": "The Haunting Echo of Goodbye",
  "album_id": 12,
  "duration": 224,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2021-10-02T22:00:08",
  "genre": "rock",
  "play_count": 792,
  "rating": 5.0,
  "like_count": 15,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/60"
 },
 {
  "song_id": 133,
  "title": "The Fleeting Joy of Youth",
  "album_id": null,
  "duration": 275,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2020-01-24T22:11:18",
  "genre": "rock",
  "play_count": 184,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/133"
 },
 {
  "song_id": 59,
  "title": "Love's Decline",
  "album_id": 12,
  "duration": 212,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2021-10-02T22:00:08",
  "genre": "rock",
  "play_count": 893,
  "rating": 5.0,
  "like_count": 14,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/59"
 },
 {
  "song_id": 62,
  "title": "Crimson Sunset Sonata",
  "album_id": 12,
  "duration": 255,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2021-10-02T22:00:08",
  "genre": "rock",
  "play_count": 387,
  "rating": 0.0,
  "like_count": 11,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/62"
 },
 {
  "song_id": 135,
  "title": "In the Silence of Your Absence",
  "album_id": null,
  "duration": 208,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2020-06-30T22:15:00",
  "genre": "rock",
  "play_count": 346,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/135"
 },
 {
  "song_id": 137,
  "title": "A Symphony of Fading Hopes",
  "album_id": null,
  "duration": 211,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2019-12-29T12:57:50",
  "genre": "rock",
  "play_count": 915,
  "rating": 5.0,
  "like_count": 6,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/137"
 },
 {
  "song_id": 136,
  "title": "Finding Solace in the Abyss",
  "album_id": null,
  "duration": 280,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2023-03-05T20:24:38",
  "genre": "rock",
  "play_count": 711,
  "rating": 5.0,
  "like_count": 10,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/136"
 }
]
```


### Environment Interaction 20
----------------------------------------------------------------------------
```python
# Found release date for Walking Through the Valley of Shadows: 08/2022
# Now search for "Where Shadows Come to Life" by Olivia Roberts
print(apis.spotify.search_songs(query="Where Shadows Come to Life Olivia Roberts", access_token=spotify_token, page_limit=20))
```

```
[
 {
  "song_id": 83,
  "title": "Where Shadows Come to Life",
  "album_id": null,
  "duration": 268,
  "artists": [
   {
    "id": 1,
    "name": "Olivia Roberts"
   }
  ],
  "release_date": "2023-01-16T22:55:35",
  "genre": "R&B",
  "play_count": 345,
  "rating": 2.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/83"
 },
 {
  "song_id": 86,
  "title": "Shattered",
  "album_id": null,
  "duration": 250,
  "artists": [
   {
    "id": 1,
    "name": "Olivia Roberts"
   }
  ],
  "release_date": "2019-10-04T09:19:25",
  "genre": "R&B",
  "play_count": 411,
  "rating": 3.0,
  "like_count": 9,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/86"
 },
 {
  "song_id": 84,
  "title": "Wilted Petals",
  "album_id": null,
  "duration": 217,
  "artists": [
   {
    "id": 1,
    "name": "Olivia Roberts"
   }
  ],
  "release_date": "2022-06-06T20:06:41",
  "genre": "R&B",
  "play_count": 236,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/84"
 },
 {
  "song_id": 85,
  "title": "Hidden Agony",
  "album_id": null,
  "duration": 183,
  "artists": [
   {
    "id": 1,
    "name": "Olivia Roberts"
   }
  ],
  "release_date": "2020-09-24T17:23:06",
  "genre": "R&B",
  "play_count": 403,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/85"
 },
 {
  "song_id": 87,
  "title": "Eternal Melancholy",
  "album_id": null,
  "duration": 249,
  "artists": [
   {
    "id": 1,
    "name": "Olivia Roberts"
   }
  ],
  "release_date": "2023-04-26T13:01:16",
  "genre": "R&B",
  "play_count": 257,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/87"
 },
 {
  "song_id": 168,
  "title": "Where Echoes Go to Die",
  "album_id": null,
  "duration": 236,
  "artists": [
   {
    "id": 14,
    "name": "Grace Harrison"
   }
  ],
  "release_date": "2022-06-01T13:34:28",
  "genre": "classical",
  "play_count": 678,
  "rating": 3.0,
  "like_count": 6,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/168"
 },
 {
  "song_id": 230,
  "title": "The Mirage of a Perfect Life",
  "album_id": null,
  "duration": 206,
  "artists": [
   {
    "id": 23,
    "name": "Soulful Reverie"
   }
  ],
  "release_date": "2020-11-06T10:00:03",
  "genre": "R&B",
  "play_count": 660,
  "rating": 3.0,
  "like_count": 9,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/230"
 },
 {
  "song_id": 222,
  "title": "A Place Where Love Once Lived",
  "album_id": null,
  "duration": 222,
  "artists": [
   {
    "id": 22,
    "name": "Silent Thunder"
   }
  ],
  "release_date": "2020-04-16T05:32:09",
  "genre": "reggae",
  "play_count": 424,
  "rating": 3.5,
  "like_count": 4,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/222"
 },
 {
  "song_id": 132,
  "title": "Shadow Dance",
  "album_id": null,
  "duration": 210,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2021-11-27T17:35:00",
  "genre": "jazz",
  "play_count": 688,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/132"
 },
 {
  "song_id": 39,
  "title": "A Pathway to Nowhere",
  "album_id": 8,
  "duration": 207,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2021-06-10T10:41:47",
  "genre": "jazz",
  "play_count": 594,
  "rating": 0.0,
  "like_count": 14,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/39"
 },
 {
  "song_id": 197,
  "title": "Surrendering to the Night",
  "album_id": null,
  "duration": 181,
  "artists": [
   {
    "id": 18,
    "name": "Astrid Nightshade"
   }
  ],
  "release_date": "2023-02-28T01:35:27",
  "genre": "reggae",
  "play_count": 344,
  "rating": 3.3,
  "like_count": 5,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/197"
 },
 {
  "song_id": 225,
  "title": "Shadows in the Twilight",
  "album_id": null,
  "duration": 244,
  "artists": [
   {
    "id": 22,
    "name": "Silent Thunder"
   }
  ],
  "release_date": "2020-12-30T23:31:49",
  "genre": "reggae",
  "play_count": 854,
  "rating": 2.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/225"
 },
 {
  "song_id": 304,
  "title": "Shadows in the Moonlight",
  "album_id": null,
  "duration": 298,
  "artists": [
   {
    "id": 33,
    "name": "Felix Blackwood"
   }
  ],
  "release_date": "2021-10-20T20:58:16",
  "genre": "classical",
  "play_count": 877,
  "rating": 2.0,
  "like_count": 5,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/304"
 },
 {
  "song_id": 318,
  "title": "Mystic Voyage to Avalon",
  "album_id": null,
  "duration": 203,
  "artists": [
   {
    "id": 35,
    "name": "Nova Harmony"
   }
  ],
  "release_date": "2020-08-05T01:56:10",
  "genre": "indie",
  "play_count": 858,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/318"
 },
 {
  "song_id": 8,
  "title": "Shadows of the Past",
  "album_id": 2,
  "duration": 271,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   }
  ],
  "release_date": "2022-05-21T21:55:36",
  "genre": "R&B",
  "play_count": 905,
  "rating": 0.0,
  "like_count": 12,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/8"
 },
 {
  "song_id": 188,
  "title": "Journey to the Celestial Realm",
  "album_id": null,
  "duration": 291,
  "artists": [
   {
    "id": 17,
    "name": "Dylan Stone"
   }
  ],
  "release_date": "2020-03-17T20:46:13",
  "genre": "country",
  "play_count": 387,
  "rating": 2.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/188"
 },
 {
  "song_id": 215,
  "title": "When Dreams Begin to Crumble",
  "album_id": null,
  "duration": 244,
  "artists": [
   {
    "id": 21,
    "name": "Oceanic Odyssey"
   }
  ],
  "release_date": "2021-09-06T11:58:43",
  "genre": "classical",
  "play_count": 104,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/215"
 },
 {
  "song_id": 261,
  "title": "The Shadows That Haunt Us",
  "album_id": null,
  "duration": 237,
  "artists": [
   {
    "id": 27,
    "name": "Carter Knight"
   }
  ],
  "release_date": "2019-07-31T14:00:27",
  "genre": "classical",
  "play_count": 846,
  "rating": 3.0,
  "like_count": 4,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/261"
 },
 {
  "song_id": 302,
  "title": "An Ode to Forgotten Dreams",
  "album_id": null,
  "duration": 204,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   }
  ],
  "release_date": "2023-01-16T15:16:03",
  "genre": "R&B",
  "play_count": 619,
  "rating": 5.0,
  "like_count": 3,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/302"
 },
 {
  "song_id": 75,
  "title": "Walking Through the Valley of Shadows",
  "album_id": 16,
  "duration": 195,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   },
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2022-08-02T08:03:50",
  "genre": "rock",
  "play_count": 806,
  "rating": 2.0,
  "like_count": 22,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/75"
 }
]
```


### Environment Interaction 21
----------------------------------------------------------------------------
```python
# Found: Where Shadows Come to Life -> 01/2023, Eternal Melancholy -> 04/2023
# Now search for "Crimson Veil" by Phoenix Rivers
print(apis.spotify.search_songs(query="Crimson Veil Phoenix Rivers", access_token=spotify_token, page_limit=20))
```

```
[
 {
  "song_id": 92,
  "title": "Crimson Veil",
  "album_id": null,
  "duration": 189,
  "artists": [
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2020-01-27T12:52:34",
  "genre": "R&B",
  "play_count": 972,
  "rating": 0.0,
  "like_count": 8,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/92"
 },
 {
  "song_id": 88,
  "title": "Crimson Skies of Longing",
  "album_id": null,
  "duration": 252,
  "artists": [
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2022-11-09T13:55:43",
  "genre": "R&B",
  "play_count": 995,
  "rating": 3.0,
  "like_count": 12,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/88"
 },
 {
  "song_id": 13,
  "title": "Beneath the Veil of Illusion",
  "album_id": 3,
  "duration": 220,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   },
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2022-11-08T06:55:52",
  "genre": "R&B",
  "play_count": 852,
  "rating": 3.0,
  "like_count": 13,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/13"
 },
 {
  "song_id": 89,
  "title": "Glass Castles",
  "album_id": null,
  "duration": 224,
  "artists": [
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2021-12-29T04:54:03",
  "genre": "R&B",
  "play_count": 415,
  "rating": 2.0,
  "like_count": 9,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/89"
 },
 {
  "song_id": 91,
  "title": "Black Diamond",
  "album_id": null,
  "duration": 212,
  "artists": [
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2019-08-26T21:33:04",
  "genre": "R&B",
  "play_count": 489,
  "rating": 0.0,
  "like_count": 7,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/91"
 },
 {
  "song_id": 209,
  "title": "Through the Veil of Tears",
  "album_id": null,
  "duration": 252,
  "artists": [
   {
    "id": 20,
    "name": "Emily Rivers"
   }
  ],
  "release_date": "2023-05-16T09:25:10",
  "genre": "country",
  "play_count": 672,
  "rating": 4.0,
  "like_count": 4,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/209"
 },
 {
  "song_id": 90,
  "title": "Whispers of Tomorrow",
  "album_id": null,
  "duration": 289,
  "artists": [
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2023-05-13T03:18:48",
  "genre": "R&B",
  "play_count": 188,
  "rating": 3.5,
  "like_count": 6,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/90"
 },
 {
  "song_id": 12,
  "title": "Haunted Memories",
  "album_id": 3,
  "duration": 295,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   },
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2022-11-08T06:55:52",
  "genre": "R&B",
  "play_count": 965,
  "rating": 0.0,
  "like_count": 10,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/12"
 },
 {
  "song_id": 14,
  "title": "Memories Etched in Melancholy",
  "album_id": 3,
  "duration": 196,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   },
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2022-11-08T06:55:52",
  "genre": "R&B",
  "play_count": 527,
  "rating": 4.0,
  "like_count": 10,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/14"
 },
 {
  "song_id": 15,
  "title": "In the Depths of Despair",
  "album_id": 3,
  "duration": 210,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   },
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2022-11-08T06:55:52",
  "genre": "R&B",
  "play_count": 293,
  "rating": 5.0,
  "like_count": 11,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/15"
 },
 {
  "song_id": 11,
  "title": "Lost in a Moment's Grace",
  "album_id": 3,
  "duration": 196,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   },
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2022-11-08T06:55:52",
  "genre": "R&B",
  "play_count": 428,
  "rating": 0.0,
  "like_count": 11,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/11"
 },
 {
  "song_id": 62,
  "title": "Crimson Sunset Sonata",
  "album_id": 12,
  "duration": 255,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2021-10-02T22:00:08",
  "genre": "rock",
  "play_count": 387,
  "rating": 0.0,
  "like_count": 11,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/62"
 },
 {
  "song_id": 163,
  "title": "Veiled Sorrow",
  "album_id": null,
  "duration": 225,
  "artists": [
   {
    "id": 14,
    "name": "Grace Harrison"
   }
  ],
  "release_date": "2018-07-18T14:37:57",
  "genre": "classical",
  "play_count": 144,
  "rating": 0.0,
  "like_count": 10,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/163"
 },
 {
  "song_id": 17,
  "title": "Dancing Through the Veil of Dreams",
  "album_id": 4,
  "duration": 238,
  "artists": [
   {
    "id": 36,
    "name": "Noah Bennett"
   }
  ],
  "release_date": "2021-03-23T13:53:26",
  "genre": "indie",
  "play_count": 762,
  "rating": 5.0,
  "like_count": 18,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/17"
 },
 {
  "song_id": 237,
  "title": "Veiled Behind a Mask of Joy",
  "album_id": null,
  "duration": 248,
  "artists": [
   {
    "id": 24,
    "name": "Liam Palmer"
   }
  ],
  "release_date": "2022-10-21T16:18:29",
  "genre": "country",
  "play_count": 125,
  "rating": 2.0,
  "like_count": 6,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/237"
 },
 {
  "song_id": 94,
  "title": "Bridges Burned and Rivers Crossed",
  "album_id": null,
  "duration": 250,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   }
  ],
  "release_date": "2018-11-23T10:11:42",
  "genre": "EDM",
  "play_count": 206,
  "rating": 3.5,
  "like_count": 4,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/94"
 },
 {
  "song_id": 207,
  "title": "A Tale of Unspoken Longing",
  "album_id": null,
  "duration": 206,
  "artists": [
   {
    "id": 20,
    "name": "Emily Rivers"
   }
  ],
  "release_date": "2022-02-27T22:43:23",
  "genre": "country",
  "play_count": 907,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/207"
 },
 {
  "song_id": 208,
  "title": "Fading Hopes in the Night",
  "album_id": null,
  "duration": 258,
  "artists": [
   {
    "id": 20,
    "name": "Emily Rivers"
   }
  ],
  "release_date": "2020-06-15T10:01:00",
  "genre": "country",
  "play_count": 789,
  "rating": 5.0,
  "like_count": 5,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/208"
 },
 {
  "song_id": 210,
  "title": "The Fragile Web of Destiny",
  "album_id": null,
  "duration": 184,
  "artists": [
   {
    "id": 20,
    "name": "Emily Rivers"
   }
  ],
  "release_date": "2021-08-19T11:50:53",
  "genre": "country",
  "play_count": 907,
  "rating": 4.2,
  "like_count": 8,
  "review_count": 4,
  "shareable_link": "https://spotify.com/songs/210"
 },
 {
  "song_id": 211,
  "title": "Caught in the Tangle of Time",
  "album_id": null,
  "duration": 300,
  "artists": [
   {
    "id": 20,
    "name": "Emily Rivers"
   }
  ],
  "release_date": "2019-01-03T13:57:10",
  "genre": "country",
  "play_count": 844,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/211"
 }
]
```


### Environment Interaction 22
----------------------------------------------------------------------------
```python
# Found: Crimson Veil -> 01/2020, and also Veiled Behind a Mask of Joy -> 10/2022
# Now search for "Elusive Joy" by Orion Steele
print(apis.spotify.search_songs(query="Elusive Joy Orion Steele", access_token=spotify_token, page_limit=20))
```

```
[
 {
  "song_id": 120,
  "title": "Elusive Joy",
  "album_id": null,
  "duration": 237,
  "artists": [
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "release_date": "2021-03-03T16:40:10",
  "genre": "pop",
  "play_count": 328,
  "rating": 3.0,
  "like_count": 8,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/120"
 },
 {
  "song_id": 118,
  "title": "Lost Hopes",
  "album_id": null,
  "duration": 240,
  "artists": [
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "release_date": "2022-05-24T04:31:08",
  "genre": "pop",
  "play_count": 660,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/118"
 },
 {
  "song_id": 119,
  "title": "Urban Jungle",
  "album_id": null,
  "duration": 287,
  "artists": [
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "release_date": "2021-07-17T15:17:27",
  "genre": "pop",
  "play_count": 568,
  "rating": 3.0,
  "like_count": 6,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/119"
 },
 {
  "song_id": 121,
  "title": "Astral Serenity",
  "album_id": null,
  "duration": 200,
  "artists": [
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "release_date": "2019-12-15T09:11:57",
  "genre": "pop",
  "play_count": 321,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/121"
 },
 {
  "song_id": 122,
  "title": "Lost Souls",
  "album_id": null,
  "duration": 206,
  "artists": [
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "release_date": "2018-12-06T11:52:44",
  "genre": "pop",
  "play_count": 281,
  "rating": 3.0,
  "like_count": 7,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/122"
 },
 {
  "song_id": 71,
  "title": "Eternal Fade",
  "album_id": 15,
  "duration": 267,
  "artists": [
   {
    "id": 29,
    "name": "Lucas Diaz"
   },
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "release_date": "2022-08-17T08:43:21",
  "genre": "pop",
  "play_count": 313,
  "rating": 0.0,
  "like_count": 14,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/71"
 },
 {
  "song_id": 73,
  "title": "When Silence Becomes Deafening",
  "album_id": 15,
  "duration": 237,
  "artists": [
   {
    "id": 29,
    "name": "Lucas Diaz"
   },
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "release_date": "2022-08-17T08:43:21",
  "genre": "pop",
  "play_count": 482,
  "rating": 3.5,
  "like_count": 16,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/73"
 },
 {
  "song_id": 70,
  "title": "Serenade of the Forgotten Stars",
  "album_id": 15,
  "duration": 265,
  "artists": [
   {
    "id": 29,
    "name": "Lucas Diaz"
   },
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "release_date": "2022-08-17T08:43:21",
  "genre": "pop",
  "play_count": 201,
  "rating": 3.0,
  "like_count": 11,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/70"
 },
 {
  "song_id": 72,
  "title": "Wandering Through Time's Embrace",
  "album_id": 15,
  "duration": 186,
  "artists": [
   {
    "id": 29,
    "name": "Lucas Diaz"
   },
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "release_date": "2022-08-17T08:43:21",
  "genre": "pop",
  "play_count": 151,
  "rating": 3.0,
  "like_count": 14,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/72"
 },
 {
  "song_id": 157,
  "title": "Chasing the Elusive Horizon",
  "album_id": null,
  "duration": 201,
  "artists": [
   {
    "id": 13,
    "name": "Luna Starlight"
   }
  ],
  "release_date": "2023-02-02T00:27:34",
  "genre": "reggae",
  "play_count": 308,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/157"
 },
 {
  "song_id": 133,
  "title": "The Fleeting Joy of Youth",
  "album_id": null,
  "duration": 275,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2020-01-24T22:11:18",
  "genre": "rock",
  "play_count": 184,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/133"
 },
 {
  "song_id": 237,
  "title": "Veiled Behind a Mask of Joy",
  "album_id": null,
  "duration": 248,
  "artists": [
   {
    "id": 24,
    "name": "Liam Palmer"
   }
  ],
  "release_date": "2022-10-21T16:18:29",
  "genre": "country",
  "play_count": 125,
  "rating": 2.0,
  "like_count": 6,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/237"
 },
 {
  "song_id": 1,
  "title": "Painting Shadows on the Wall",
  "album_id": 1,
  "duration": 217,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 638,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/1"
 },
 {
  "song_id": 2,
  "title": "Lost in the Mists of Time",
  "album_id": 1,
  "duration": 224,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 205,
  "rating": 0.0,
  "like_count": 11,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/2"
 },
 {
  "song_id": 3,
  "title": "The Fragrance of Fading Roses",
  "album_id": 1,
  "duration": 270,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 463,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/3"
 },
 {
  "song_id": 4,
  "title": "The Puzzle of My Heart",
  "album_id": 1,
  "duration": 181,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 667,
  "rating": 0.0,
  "like_count": 14,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/4"
 },
 {
  "song_id": 5,
  "title": "Chasing the Ghosts of Yesterday",
  "album_id": 1,
  "duration": 255,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 466,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/5"
 },
 {
  "song_id": 6,
  "title": "Reflections in a Pool of Regret",
  "album_id": 1,
  "duration": 271,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 265,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/6"
 },
 {
  "song_id": 7,
  "title": "Memories Stitched in Time",
  "album_id": 1,
  "duration": 279,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 443,
  "rating": 0.0,
  "like_count": 18,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/7"
 },
 {
  "song_id": 8,
  "title": "Shadows of the Past",
  "album_id": 2,
  "duration": 271,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   }
  ],
  "release_date": "2022-05-21T21:55:36",
  "genre": "R&B",
  "play_count": 905,
  "rating": 0.0,
  "like_count": 12,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/8"
 }
]
```


### Environment Interaction 23
----------------------------------------------------------------------------
```python
# Found: Elusive Joy -> 03/2021, Veiled Behind a Mask of Joy -> 10/2022
# Now search for "Ephemeral Beauty" by Eliana Harper
print(apis.spotify.search_songs(query="Ephemeral Beauty Eliana Harper", access_token=spotify_token, page_limit=20))
```

```
[
 {
  "song_id": 149,
  "title": "Ephemeral Beauty",
  "album_id": null,
  "duration": 234,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "release_date": "2020-01-24T17:58:58",
  "genre": "hip-hop",
  "play_count": 701,
  "rating": 4.0,
  "like_count": 7,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/149"
 },
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
  "release_date": "2021-02-05T04:10:20",
  "genre": "hip-hop",
  "play_count": 809,
  "rating": 2.0,
  "like_count": 12,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/33"
 },
 {
  "song_id": 146,
  "title": "Drifting Through Eternal Skies",
  "album_id": null,
  "duration": 294,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "release_date": "2019-11-06T19:28:29",
  "genre": "hip-hop",
  "play_count": 277,
  "rating": 3.5,
  "like_count": 4,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/146"
 },
 {
  "song_id": 144,
  "title": "Longing for a Touch Unfelt",
  "album_id": null,
  "duration": 270,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "release_date": "2022-01-06T06:32:37",
  "genre": "hip-hop",
  "play_count": 220,
  "rating": 3.5,
  "like_count": 7,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/144"
 },
 {
  "song_id": 145,
  "title": "Melodies from a Distant Past",
  "album_id": null,
  "duration": 279,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "release_date": "2021-02-18T03:38:46",
  "genre": "hip-hop",
  "play_count": 507,
  "rating": 4.0,
  "like_count": 2,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/145"
 },
 {
  "song_id": 35,
  "title": "Dancing in the Rain of Tears",
  "album_id": 7,
  "duration": 244,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "release_date": "2021-02-05T04:10:20",
  "genre": "hip-hop",
  "play_count": 135,
  "rating": 4.0,
  "like_count": 11,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/35"
 },
 {
  "song_id": 36,
  "title": "A Whisper in the Midnight Air",
  "album_id": 7,
  "duration": 234,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "release_date": "2021-02-05T04:10:20",
  "genre": "hip-hop",
  "play_count": 974,
  "rating": 3.7,
  "like_count": 16,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/36"
 },
 {
  "song_id": 147,
  "title": "In the Arms of a Stranger",
  "album_id": null,
  "duration": 199,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "release_date": "2022-03-15T08:47:53",
  "genre": "hip-hop",
  "play_count": 365,
  "rating": 3.7,
  "like_count": 6,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/147"
 },
 {
  "song_id": 148,
  "title": "Dancing on the Precipice of Love",
  "album_id": null,
  "duration": 244,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "release_date": "2019-04-28T14:55:58",
  "genre": "hip-hop",
  "play_count": 476,
  "rating": 4.0,
  "like_count": 2,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/148"
 },
 {
  "song_id": 34,
  "title": "Under the Gaze of a Watchful Moon",
  "album_id": 7,
  "duration": 196,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "release_date": "2021-02-05T04:10:20",
  "genre": "hip-hop",
  "play_count": 357,
  "rating": 4.0,
  "like_count": 10,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/34"
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
  "release_date": "2019-02-18T10:59:51",
  "genre": "EDM",
  "play_count": 178,
  "rating": 3.0,
  "like_count": 5,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/93"
 },
 {
  "song_id": 167,
  "title": "The Tragic Beauty of Love",
  "album_id": null,
  "duration": 190,
  "artists": [
   {
    "id": 14,
    "name": "Grace Harrison"
   }
  ],
  "release_date": "2019-05-19T20:53:31",
  "genre": "classical",
  "play_count": 898,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/167"
 },
 {
  "song_id": 1,
  "title": "Painting Shadows on the Wall",
  "album_id": 1,
  "duration": 217,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 638,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/1"
 },
 {
  "song_id": 2,
  "title": "Lost in the Mists of Time",
  "album_id": 1,
  "duration": 224,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 205,
  "rating": 0.0,
  "like_count": 11,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/2"
 },
 {
  "song_id": 3,
  "title": "The Fragrance of Fading Roses",
  "album_id": 1,
  "duration": 270,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 463,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/3"
 },
 {
  "song_id": 4,
  "title": "The Puzzle of My Heart",
  "album_id": 1,
  "duration": 181,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 667,
  "rating": 0.0,
  "like_count": 14,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/4"
 },
 {
  "song_id": 5,
  "title": "Chasing the Ghosts of Yesterday",
  "album_id": 1,
  "duration": 255,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 466,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/5"
 },
 {
  "song_id": 6,
  "title": "Reflections in a Pool of Regret",
  "album_id": 1,
  "duration": 271,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 265,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/6"
 },
 {
  "song_id": 7,
  "title": "Memories Stitched in Time",
  "album_id": 1,
  "duration": 279,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 443,
  "rating": 0.0,
  "like_count": 18,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/7"
 },
 {
  "song_id": 8,
  "title": "Shadows of the Past",
  "album_id": 2,
  "duration": 271,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   }
  ],
  "release_date": "2022-05-21T21:55:36",
  "genre": "R&B",
  "play_count": 905,
  "rating": 0.0,
  "like_count": 12,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/8"
 }
]
```


### Environment Interaction 24
----------------------------------------------------------------------------
```python
# Found: Ephemeral Beauty -> 01/2020
# Now search for "Stardust Serenade" by Violet Cascade
print(apis.spotify.search_songs(query="Stardust Serenade Violet Cascade", access_token=spotify_token, page_limit=20))
```

```
[
 {
  "song_id": 175,
  "title": "Stardust Serenade",
  "album_id": null,
  "duration": 286,
  "artists": [
   {
    "id": 15,
    "name": "Violet Cascade"
   }
  ],
  "release_date": "2019-04-20T02:39:30",
  "genre": "reggae",
  "play_count": 363,
  "rating": 3.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/175"
 },
 {
  "song_id": 172,
  "title": "Neon Reverie",
  "album_id": null,
  "duration": 206,
  "artists": [
   {
    "id": 15,
    "name": "Violet Cascade"
   }
  ],
  "release_date": "2022-03-10T13:45:15",
  "genre": "reggae",
  "play_count": 315,
  "rating": 3.0,
  "like_count": 5,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/172"
 },
 {
  "song_id": 173,
  "title": "Beyond the Echo",
  "album_id": null,
  "duration": 233,
  "artists": [
   {
    "id": 15,
    "name": "Violet Cascade"
   }
  ],
  "release_date": "2020-07-24T00:00:14",
  "genre": "reggae",
  "play_count": 892,
  "rating": 0.0,
  "like_count": 3,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/173"
 },
 {
  "song_id": 171,
  "title": "End of the Line",
  "album_id": null,
  "duration": 211,
  "artists": [
   {
    "id": 15,
    "name": "Violet Cascade"
   }
  ],
  "release_date": "2022-10-11T03:35:30",
  "genre": "reggae",
  "play_count": 806,
  "rating": 4.0,
  "like_count": 7,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/171"
 },
 {
  "song_id": 170,
  "title": "The Silence that Speaks Volumes",
  "album_id": null,
  "duration": 286,
  "artists": [
   {
    "id": 15,
    "name": "Violet Cascade"
   }
  ],
  "release_date": "2021-05-01T15:55:35",
  "genre": "reggae",
  "play_count": 368,
  "rating": 0.0,
  "like_count": 3,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/170"
 },
 {
  "song_id": 174,
  "title": "The Fading Light of Memory",
  "album_id": null,
  "duration": 258,
  "artists": [
   {
    "id": 15,
    "name": "Violet Cascade"
   }
  ],
  "release_date": "2023-02-26T14:59:23",
  "genre": "reggae",
  "play_count": 768,
  "rating": 5.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/174"
 },
 {
  "song_id": 169,
  "title": "The Resonance of a Silent Cry",
  "album_id": null,
  "duration": 226,
  "artists": [
   {
    "id": 15,
    "name": "Violet Cascade"
   }
  ],
  "release_date": "2021-06-28T20:23:54",
  "genre": "reggae",
  "play_count": 429,
  "rating": 0.0,
  "like_count": 10,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/169"
 },
 {
  "song_id": 231,
  "title": "Rust and Stardust",
  "album_id": null,
  "duration": 278,
  "artists": [
   {
    "id": 23,
    "name": "Soulful Reverie"
   }
  ],
  "release_date": "2021-06-14T05:23:07",
  "genre": "R&B",
  "play_count": 901,
  "rating": 5.0,
  "like_count": 5,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/231"
 },
 {
  "song_id": 29,
  "title": "Violet Rain",
  "album_id": 6,
  "duration": 294,
  "artists": [
   {
    "id": 36,
    "name": "Noah Bennett"
   },
   {
    "id": 19,
    "name": "Ethan Wallace"
   },
   {
    "id": 35,
    "name": "Nova Harmony"
   }
  ],
  "release_date": "2021-04-02T04:32:45",
  "genre": "indie",
  "play_count": 265,
  "rating": 3.5,
  "like_count": 14,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/29"
 },
 {
  "song_id": 179,
  "title": "Reckless Love",
  "album_id": null,
  "duration": 219,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "release_date": "2021-12-15T18:27:57",
  "genre": "R&B",
  "play_count": 454,
  "rating": 2.5,
  "like_count": 9,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/179"
 },
 {
  "song_id": 181,
  "title": "Fading Stars",
  "album_id": null,
  "duration": 192,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "release_date": "2021-08-29T00:24:01",
  "genre": "R&B",
  "play_count": 381,
  "rating": 0.0,
  "like_count": 3,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/181"
 },
 {
  "song_id": 184,
  "title": "Enchanted Reverie",
  "album_id": null,
  "duration": 192,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "release_date": "2023-04-04T14:07:29",
  "genre": "R&B",
  "play_count": 336,
  "rating": 0.0,
  "like_count": 8,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/184"
 },
 {
  "song_id": 176,
  "title": "Echoes of Silence",
  "album_id": null,
  "duration": 267,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "release_date": "2022-06-10T21:32:34",
  "genre": "R&B",
  "play_count": 865,
  "rating": 0.0,
  "like_count": 7,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/176"
 },
 {
  "song_id": 12,
  "title": "Haunted Memories",
  "album_id": 3,
  "duration": 295,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   },
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2022-11-08T06:55:52",
  "genre": "R&B",
  "play_count": 965,
  "rating": 0.0,
  "like_count": 10,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/12"
 },
 {
  "song_id": 178,
  "title": "Sorrow's Silent Symphony",
  "album_id": null,
  "duration": 287,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "release_date": "2022-05-16T15:14:26",
  "genre": "R&B",
  "play_count": 975,
  "rating": 3.0,
  "like_count": 2,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/178"
 },
 {
  "song_id": 213,
  "title": "Serenade of the Silver Moon",
  "album_id": null,
  "duration": 232,
  "artists": [
   {
    "id": 21,
    "name": "Oceanic Odyssey"
   }
  ],
  "release_date": "2020-09-24T02:12:57",
  "genre": "classical",
  "play_count": 590,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/213"
 },
 {
  "song_id": 177,
  "title": "Through the Kaleidoscope of Tears",
  "album_id": null,
  "duration": 244,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "release_date": "2020-03-16T11:18:32",
  "genre": "R&B",
  "play_count": 475,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/177"
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
  "release_date": "2022-03-16T10:58:17",
  "genre": "R&B",
  "play_count": 314,
  "rating": 0.0,
  "like_count": 5,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/182"
 },
 {
  "song_id": 183,
  "title": "In the Tunnels of Despair",
  "album_id": null,
  "duration": 257,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "release_date": "2020-06-16T02:39:33",
  "genre": "R&B",
  "play_count": 378,
  "rating": 2.0,
  "like_count": 7,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/183"
 },
 {
  "song_id": 185,
  "title": "Mysteries of the Silent Sea",
  "album_id": null,
  "duration": 196,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "release_date": "2020-07-21T09:45:39",
  "genre": "R&B",
  "play_count": 990,
  "rating": 0.0,
  "like_count": 7,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/185"
 }
]
```


### Environment Interaction 25
----------------------------------------------------------------------------
```python
# Found: Stardust Serenade -> 04/2019
# Now search for "In the Wake of Unspoken Promises" by Isabella Cruz
print(apis.spotify.search_songs(query="In the Wake of Unspoken Promises Isabella Cruz", access_token=spotify_token, page_limit=20))
```

```
[
 {
  "song_id": 253,
  "title": "In the Wake of Unspoken Promises",
  "album_id": null,
  "duration": 285,
  "artists": [
   {
    "id": 26,
    "name": "Isabella Cruz"
   }
  ],
  "release_date": "2022-07-11T18:45:36",
  "genre": "EDM",
  "play_count": 548,
  "rating": 0.0,
  "like_count": 5,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/253"
 },
 {
  "song_id": 257,
  "title": "In the Theater of Broken Promises",
  "album_id": null,
  "duration": 194,
  "artists": [
   {
    "id": 26,
    "name": "Isabella Cruz"
   }
  ],
  "release_date": "2019-04-08T03:10:33",
  "genre": "EDM",
  "play_count": 992,
  "rating": 2.5,
  "like_count": 7,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/257"
 },
 {
  "song_id": 251,
  "title": "Trapped in the Snare of Love",
  "album_id": null,
  "duration": 268,
  "artists": [
   {
    "id": 26,
    "name": "Isabella Cruz"
   }
  ],
  "release_date": "2023-05-14T03:58:33",
  "genre": "EDM",
  "play_count": 352,
  "rating": 0.0,
  "like_count": 2,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/251"
 },
 {
  "song_id": 252,
  "title": "Dark Reverie",
  "album_id": null,
  "duration": 216,
  "artists": [
   {
    "id": 26,
    "name": "Isabella Cruz"
   }
  ],
  "release_date": "2022-03-27T22:45:27",
  "genre": "EDM",
  "play_count": 558,
  "rating": 3.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/252"
 },
 {
  "song_id": 254,
  "title": "Blind Trust",
  "album_id": null,
  "duration": 247,
  "artists": [
   {
    "id": 26,
    "name": "Isabella Cruz"
   }
  ],
  "release_date": "2022-07-01T07:30:02",
  "genre": "EDM",
  "play_count": 573,
  "rating": 0.0,
  "like_count": 5,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/254"
 },
 {
  "song_id": 258,
  "title": "Empty Rooms",
  "album_id": null,
  "duration": 233,
  "artists": [
   {
    "id": 26,
    "name": "Isabella Cruz"
   }
  ],
  "release_date": "2021-03-08T07:03:02",
  "genre": "EDM",
  "play_count": 561,
  "rating": 0.0,
  "like_count": 3,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/258"
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
  "release_date": "2022-01-08T16:12:50",
  "genre": "R&B",
  "play_count": 958,
  "rating": 5.0,
  "like_count": 7,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/299"
 },
 {
  "song_id": 2,
  "title": "Lost in the Mists of Time",
  "album_id": 1,
  "duration": 224,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 205,
  "rating": 0.0,
  "like_count": 11,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/2"
 },
 {
  "song_id": 255,
  "title": "Uncharted Waters of the Heart",
  "album_id": null,
  "duration": 253,
  "artists": [
   {
    "id": 26,
    "name": "Isabella Cruz"
   }
  ],
  "release_date": "2019-11-14T12:26:22",
  "genre": "EDM",
  "play_count": 732,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/255"
 },
 {
  "song_id": 256,
  "title": "When the Stars Align",
  "album_id": null,
  "duration": 196,
  "artists": [
   {
    "id": 26,
    "name": "Isabella Cruz"
   }
  ],
  "release_date": "2019-07-01T21:14:33",
  "genre": "EDM",
  "play_count": 631,
  "rating": 2.5,
  "like_count": 7,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/256"
 },
 {
  "song_id": 7,
  "title": "Memories Stitched in Time",
  "album_id": 1,
  "duration": 279,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 443,
  "rating": 0.0,
  "like_count": 18,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/7"
 },
 {
  "song_id": 6,
  "title": "Reflections in a Pool of Regret",
  "album_id": 1,
  "duration": 271,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 265,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/6"
 },
 {
  "song_id": 3,
  "title": "The Fragrance of Fading Roses",
  "album_id": 1,
  "duration": 270,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 463,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/3"
 },
 {
  "song_id": 4,
  "title": "The Puzzle of My Heart",
  "album_id": 1,
  "duration": 181,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 667,
  "rating": 0.0,
  "like_count": 14,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/4"
 },
 {
  "song_id": 5,
  "title": "Chasing the Ghosts of Yesterday",
  "album_id": 1,
  "duration": 255,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 466,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/5"
 },
 {
  "song_id": 1,
  "title": "Painting Shadows on the Wall",
  "album_id": 1,
  "duration": 217,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 638,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/1"
 },
 {
  "song_id": 42,
  "title": "Unspoken Words",
  "album_id": 8,
  "duration": 199,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2021-06-10T10:41:47",
  "genre": "jazz",
  "play_count": 349,
  "rating": 0.0,
  "like_count": 11,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/42"
 },
 {
  "song_id": 289,
  "title": "Wasted Promises",
  "album_id": null,
  "duration": 258,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   }
  ],
  "release_date": "2019-08-30T00:48:51",
  "genre": "EDM",
  "play_count": 211,
  "rating": 3.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/289"
 },
 {
  "song_id": 207,
  "title": "A Tale of Unspoken Longing",
  "album_id": null,
  "duration": 206,
  "artists": [
   {
    "id": 20,
    "name": "Emily Rivers"
   }
  ],
  "release_date": "2022-02-27T22:43:23",
  "genre": "country",
  "play_count": 907,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/207"
 },
 {
  "song_id": 161,
  "title": "In the Embrace of Midnight",
  "album_id": null,
  "duration": 232,
  "artists": [
   {
    "id": 13,
    "name": "Luna Starlight"
   }
  ],
  "release_date": "2022-12-22T20:20:13",
  "genre": "reggae",
  "play_count": 733,
  "rating": 3.0,
  "like_count": 5,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/161"
 }
]
```


### Environment Interaction 26
----------------------------------------------------------------------------
```python
# Found: In the Wake of Unspoken Promises -> 07/2022
# Now search for "Wading Through the Ashes of Love" by Marcus Lane
print(apis.spotify.search_songs(query="Wading Through the Ashes of Love Marcus Lane", access_token=spotify_token, page_limit=20))
```

```
[
 {
  "song_id": 285,
  "title": "Wading Through the Ashes of Love",
  "album_id": null,
  "duration": 195,
  "artists": [
   {
    "id": 30,
    "name": "Marcus Lane"
   }
  ],
  "release_date": "2020-09-25T08:36:54",
  "genre": "reggae",
  "play_count": 750,
  "rating": 0.0,
  "like_count": 7,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/285"
 },
 {
  "song_id": 283,
  "title": "Bitter Haze",
  "album_id": null,
  "duration": 191,
  "artists": [
   {
    "id": 30,
    "name": "Marcus Lane"
   }
  ],
  "release_date": "2020-07-07T14:12:42",
  "genre": "reggae",
  "play_count": 715,
  "rating": 0.0,
  "like_count": 9,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/283"
 },
 {
  "song_id": 286,
  "title": "Golden Lies",
  "album_id": null,
  "duration": 295,
  "artists": [
   {
    "id": 30,
    "name": "Marcus Lane"
   }
  ],
  "release_date": "2021-03-01T07:07:35",
  "genre": "reggae",
  "play_count": 210,
  "rating": 2.0,
  "like_count": 8,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/286"
 },
 {
  "song_id": 280,
  "title": "The Tragedy of Living Without",
  "album_id": null,
  "duration": 196,
  "artists": [
   {
    "id": 30,
    "name": "Marcus Lane"
   }
  ],
  "release_date": "2021-07-11T20:26:48",
  "genre": "reggae",
  "play_count": 835,
  "rating": 0.0,
  "like_count": 9,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/280"
 },
 {
  "song_id": 284,
  "title": "Under the Weight of Regret",
  "album_id": null,
  "duration": 203,
  "artists": [
   {
    "id": 30,
    "name": "Marcus Lane"
   }
  ],
  "release_date": "2019-09-19T06:44:30",
  "genre": "reggae",
  "play_count": 878,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/284"
 },
 {
  "song_id": 281,
  "title": "Serenity in the Rain",
  "album_id": null,
  "duration": 186,
  "artists": [
   {
    "id": 30,
    "name": "Marcus Lane"
   }
  ],
  "release_date": "2022-02-11T05:29:03",
  "genre": "reggae",
  "play_count": 279,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/281"
 },
 {
  "song_id": 282,
  "title": "When All Words Fail Us",
  "album_id": null,
  "duration": 293,
  "artists": [
   {
    "id": 30,
    "name": "Marcus Lane"
   }
  ],
  "release_date": "2020-07-12T08:05:18",
  "genre": "reggae",
  "play_count": 422,
  "rating": 0.0,
  "like_count": 9,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/282"
 },
 {
  "song_id": 32,
  "title": "Wading Through Rivers of Tears",
  "album_id": 6,
  "duration": 234,
  "artists": [
   {
    "id": 36,
    "name": "Noah Bennett"
   },
   {
    "id": 19,
    "name": "Ethan Wallace"
   },
   {
    "id": 35,
    "name": "Nova Harmony"
   }
  ],
  "release_date": "2021-04-02T04:32:45",
  "genre": "indie",
  "play_count": 448,
  "rating": 3.7,
  "like_count": 19,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/32"
 },
 {
  "song_id": 115,
  "title": "Ashes and Roses",
  "album_id": null,
  "duration": 259,
  "artists": [
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2019-12-18T18:15:33",
  "genre": "EDM",
  "play_count": 265,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/115"
 },
 {
  "song_id": 209,
  "title": "Through the Veil of Tears",
  "album_id": null,
  "duration": 252,
  "artists": [
   {
    "id": 20,
    "name": "Emily Rivers"
   }
  ],
  "release_date": "2023-05-16T09:25:10",
  "genre": "country",
  "play_count": 672,
  "rating": 4.0,
  "like_count": 4,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/209"
 },
 {
  "song_id": 17,
  "title": "Dancing Through the Veil of Dreams",
  "album_id": 4,
  "duration": 238,
  "artists": [
   {
    "id": 36,
    "name": "Noah Bennett"
   }
  ],
  "release_date": "2021-03-23T13:53:26",
  "genre": "indie",
  "play_count": 762,
  "rating": 5.0,
  "like_count": 18,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/17"
 },
 {
  "song_id": 177,
  "title": "Through the Kaleidoscope of Tears",
  "album_id": null,
  "duration": 244,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "release_date": "2020-03-16T11:18:32",
  "genre": "R&B",
  "play_count": 475,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/177"
 },
 {
  "song_id": 196,
  "title": "Falling Through the Cracks of Time",
  "album_id": null,
  "duration": 278,
  "artists": [
   {
    "id": 18,
    "name": "Astrid Nightshade"
   }
  ],
  "release_date": "2020-07-29T17:06:15",
  "genre": "reggae",
  "play_count": 949,
  "rating": 0.0,
  "like_count": 11,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/196"
 },
 {
  "song_id": 75,
  "title": "Walking Through the Valley of Shadows",
  "album_id": 16,
  "duration": 195,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   },
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2022-08-02T08:03:50",
  "genre": "rock",
  "play_count": 806,
  "rating": 2.0,
  "like_count": 22,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/75"
 },
 {
  "song_id": 63,
  "title": "Journey Through the Unknown",
  "album_id": 13,
  "duration": 290,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   },
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2021-03-02T14:08:32",
  "genre": "EDM",
  "play_count": 582,
  "rating": 5.0,
  "like_count": 2,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/63"
 },
 {
  "song_id": 146,
  "title": "Drifting Through Eternal Skies",
  "album_id": null,
  "duration": 294,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "release_date": "2019-11-06T19:28:29",
  "genre": "hip-hop",
  "play_count": 277,
  "rating": 3.5,
  "like_count": 4,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/146"
 },
 {
  "song_id": 152,
  "title": "The Enigma of Love",
  "album_id": null,
  "duration": 190,
  "artists": [
   {
    "id": 12,
    "name": "Mia Sullivan"
   }
  ],
  "release_date": "2022-05-12T02:37:23",
  "genre": "classical",
  "play_count": 367,
  "rating": 0.0,
  "like_count": 3,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/152"
 },
 {
  "song_id": 72,
  "title": "Wandering Through Time's Embrace",
  "album_id": 15,
  "duration": 186,
  "artists": [
   {
    "id": 29,
    "name": "Lucas Diaz"
   },
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "release_date": "2022-08-17T08:43:21",
  "genre": "pop",
  "play_count": 151,
  "rating": 3.0,
  "like_count": 14,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/72"
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
  "release_date": "2019-02-18T10:59:51",
  "genre": "EDM",
  "play_count": 178,
  "rating": 3.0,
  "like_count": 5,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/93"
 },
 {
  "song_id": 138,
  "title": "The Inescapable Gravity of Love",
  "album_id": null,
  "duration": 280,
  "artists": [
   {
    "id": 10,
    "name": "Zoe Mitchell"
   }
  ],
  "release_date": "2019-08-29T00:44:38",
  "genre": "classical",
  "play_count": 193,
  "rating": 5.0,
  "like_count": 6,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/138"
 }
]
```


### Environment Interaction 27
----------------------------------------------------------------------------
```python
# Found: Wading Through the Ashes of Love -> 09/2020
# Now search for "Fading Like a Distant Star" by Hazel Winter
print(apis.spotify.search_songs(query="Fading Like a Distant Star Hazel Winter", access_token=spotify_token, page_limit=20))
```

```
[
 {
  "song_id": 291,
  "title": "Fading Like a Distant Star",
  "album_id": null,
  "duration": 182,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   }
  ],
  "release_date": "2019-01-28T09:34:15",
  "genre": "EDM",
  "play_count": 785,
  "rating": 0.0,
  "like_count": 9,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/291"
 },
 {
  "song_id": 40,
  "title": "Burning Like a Distant Star",
  "album_id": 8,
  "duration": 277,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2021-06-10T10:41:47",
  "genre": "jazz",
  "play_count": 120,
  "rating": 0.0,
  "like_count": 10,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/40"
 },
 {
  "song_id": 293,
  "title": "Dancing in a Field of Thorns",
  "album_id": null,
  "duration": 291,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   }
  ],
  "release_date": "2020-07-01T11:06:04",
  "genre": "EDM",
  "play_count": 786,
  "rating": 0.0,
  "like_count": 3,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/293"
 },
 {
  "song_id": 310,
  "title": "Harmony of the Distant Stars",
  "album_id": null,
  "duration": 289,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   }
  ],
  "release_date": "2020-10-02T21:17:12",
  "genre": "rock",
  "play_count": 715,
  "rating": 2.0,
  "like_count": 6,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/310"
 },
 {
  "song_id": 287,
  "title": "Painted Skies",
  "album_id": null,
  "duration": 298,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   }
  ],
  "release_date": "2019-05-01T22:57:58",
  "genre": "EDM",
  "play_count": 661,
  "rating": 3.0,
  "like_count": 5,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/287"
 },
 {
  "song_id": 289,
  "title": "Wasted Promises",
  "album_id": null,
  "duration": 258,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   }
  ],
  "release_date": "2019-08-30T00:48:51",
  "genre": "EDM",
  "play_count": 211,
  "rating": 3.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/289"
 },
 {
  "song_id": 292,
  "title": "Final Echo",
  "album_id": null,
  "duration": 221,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   }
  ],
  "release_date": "2022-07-16T08:47:26",
  "genre": "EDM",
  "play_count": 171,
  "rating": 0.0,
  "like_count": 7,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/292"
 },
 {
  "song_id": 294,
  "title": "Eternal Reverie",
  "album_id": null,
  "duration": 292,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   }
  ],
  "release_date": "2019-11-13T06:15:54",
  "genre": "EDM",
  "play_count": 910,
  "rating": 5.0,
  "like_count": 3,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/294"
 },
 {
  "song_id": 181,
  "title": "Fading Stars",
  "album_id": null,
  "duration": 192,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "release_date": "2021-08-29T00:24:01",
  "genre": "R&B",
  "play_count": 381,
  "rating": 0.0,
  "like_count": 3,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/181"
 },
 {
  "song_id": 64,
  "title": "Caught in a Web of Lies",
  "album_id": 13,
  "duration": 280,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   },
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2021-03-02T14:08:32",
  "genre": "EDM",
  "play_count": 468,
  "rating": 0.0,
  "like_count": 11,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/64"
 },
 {
  "song_id": 288,
  "title": "Love's Mirage",
  "album_id": null,
  "duration": 273,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   }
  ],
  "release_date": "2022-08-08T12:36:10",
  "genre": "EDM",
  "play_count": 100,
  "rating": 4.0,
  "like_count": 9,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/288"
 },
 {
  "song_id": 65,
  "title": "Eternal Solitude",
  "album_id": 13,
  "duration": 206,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   },
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2021-03-02T14:08:32",
  "genre": "EDM",
  "play_count": 818,
  "rating": 2.0,
  "like_count": 13,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/65"
 },
 {
  "song_id": 66,
  "title": "Phantom Pain",
  "album_id": 13,
  "duration": 223,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   },
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2021-03-02T14:08:32",
  "genre": "EDM",
  "play_count": 975,
  "rating": 0.0,
  "like_count": 7,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/66"
 },
 {
  "song_id": 290,
  "title": "Whispers in the Wind",
  "album_id": null,
  "duration": 253,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   }
  ],
  "release_date": "2020-07-08T10:47:35",
  "genre": "EDM",
  "play_count": 438,
  "rating": 3.0,
  "like_count": 12,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/290"
 },
 {
  "song_id": 295,
  "title": "City of Fallen Angels",
  "album_id": null,
  "duration": 222,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   }
  ],
  "release_date": "2020-12-12T05:37:59",
  "genre": "EDM",
  "play_count": 591,
  "rating": 2.0,
  "like_count": 5,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/295"
 },
 {
  "song_id": 63,
  "title": "Journey Through the Unknown",
  "album_id": 13,
  "duration": 290,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   },
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2021-03-02T14:08:32",
  "genre": "EDM",
  "play_count": 582,
  "rating": 5.0,
  "like_count": 2,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/63"
 },
 {
  "song_id": 145,
  "title": "Melodies from a Distant Past",
  "album_id": null,
  "duration": 279,
  "artists": [
   {
    "id": 11,
    "name": "Eliana Harper"
   }
  ],
  "release_date": "2021-02-18T03:38:46",
  "genre": "hip-hop",
  "play_count": 507,
  "rating": 4.0,
  "like_count": 2,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/145"
 },
 {
  "song_id": 137,
  "title": "A Symphony of Fading Hopes",
  "album_id": null,
  "duration": 211,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2019-12-29T12:57:50",
  "genre": "rock",
  "play_count": 915,
  "rating": 5.0,
  "like_count": 6,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/137"
 },
 {
  "song_id": 109,
  "title": "The Weight of a Thousand Stars",
  "album_id": null,
  "duration": 225,
  "artists": [
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2021-08-24T17:46:53",
  "genre": "EDM",
  "play_count": 973,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/109"
 },
 {
  "song_id": 110,
  "title": "A Love Written in the Stars",
  "album_id": null,
  "duration": 268,
  "artists": [
   {
    "id": 5,
    "name": "Ava Morgan"
   }
  ],
  "release_date": "2019-06-20T09:41:43",
  "genre": "EDM",
  "play_count": 531,
  "rating": 3.0,
  "like_count": 6,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/110"
 }
]
```


### Environment Interaction 28
----------------------------------------------------------------------------
```python
# Found: Fading Like a Distant Star -> 01/2019
# Now search for "Wilted Grace" by Felix Blackwood
print(apis.spotify.search_songs(query="Wilted Grace Felix Blackwood", access_token=spotify_token, page_limit=20))
```

```
[
 {
  "song_id": 306,
  "title": "Wilted Grace",
  "album_id": null,
  "duration": 275,
  "artists": [
   {
    "id": 33,
    "name": "Felix Blackwood"
   }
  ],
  "release_date": "2022-01-05T00:57:31",
  "genre": "classical",
  "play_count": 326,
  "rating": 0.0,
  "like_count": 7,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/306"
 },
 {
  "song_id": 307,
  "title": "Fractured",
  "album_id": null,
  "duration": 297,
  "artists": [
   {
    "id": 33,
    "name": "Felix Blackwood"
   }
  ],
  "release_date": "2023-05-06T12:09:43",
  "genre": "classical",
  "play_count": 866,
  "rating": 4.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/307"
 },
 {
  "song_id": 305,
  "title": "Electric Pulse",
  "album_id": null,
  "duration": 191,
  "artists": [
   {
    "id": 33,
    "name": "Felix Blackwood"
   }
  ],
  "release_date": "2021-07-21T10:11:55",
  "genre": "classical",
  "play_count": 233,
  "rating": 4.0,
  "like_count": 6,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/305"
 },
 {
  "song_id": 80,
  "title": "Wandering the Streets Alone",
  "album_id": 18,
  "duration": 189,
  "artists": [
   {
    "id": 33,
    "name": "Felix Blackwood"
   }
  ],
  "release_date": "2022-07-06T10:24:33",
  "genre": "classical",
  "play_count": 863,
  "rating": 0.0,
  "like_count": 14,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/80"
 },
 {
  "song_id": 304,
  "title": "Shadows in the Moonlight",
  "album_id": null,
  "duration": 298,
  "artists": [
   {
    "id": 33,
    "name": "Felix Blackwood"
   }
  ],
  "release_date": "2021-10-20T20:58:16",
  "genre": "classical",
  "play_count": 877,
  "rating": 2.0,
  "like_count": 5,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/304"
 },
 {
  "song_id": 81,
  "title": "Echoes of the Whispering Wind",
  "album_id": 18,
  "duration": 217,
  "artists": [
   {
    "id": 33,
    "name": "Felix Blackwood"
   }
  ],
  "release_date": "2022-07-06T10:24:33",
  "genre": "classical",
  "play_count": 645,
  "rating": 2.0,
  "like_count": 17,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/81"
 },
 {
  "song_id": 308,
  "title": "The Melancholy of Wasted Years",
  "album_id": null,
  "duration": 268,
  "artists": [
   {
    "id": 33,
    "name": "Felix Blackwood"
   }
  ],
  "release_date": "2023-01-21T14:09:13",
  "genre": "classical",
  "play_count": 907,
  "rating": 3.2,
  "like_count": 5,
  "review_count": 4,
  "shareable_link": "https://spotify.com/songs/308"
 },
 {
  "song_id": 82,
  "title": "Lost in the Twilight of Hope",
  "album_id": 18,
  "duration": 193,
  "artists": [
   {
    "id": 33,
    "name": "Felix Blackwood"
   }
  ],
  "release_date": "2022-07-06T10:24:33",
  "genre": "classical",
  "play_count": 750,
  "rating": 4.3,
  "like_count": 24,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/82"
 },
 {
  "song_id": 84,
  "title": "Wilted Petals",
  "album_id": null,
  "duration": 217,
  "artists": [
   {
    "id": 1,
    "name": "Olivia Roberts"
   }
  ],
  "release_date": "2022-06-06T20:06:41",
  "genre": "R&B",
  "play_count": 236,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/84"
 },
 {
  "song_id": 241,
  "title": "Wilted Roses on the Vine",
  "album_id": null,
  "duration": 187,
  "artists": [
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2020-02-03T16:32:19",
  "genre": "R&B",
  "play_count": 713,
  "rating": 2.0,
  "like_count": 7,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/241"
 },
 {
  "song_id": 163,
  "title": "Veiled Sorrow",
  "album_id": null,
  "duration": 225,
  "artists": [
   {
    "id": 14,
    "name": "Grace Harrison"
   }
  ],
  "release_date": "2018-07-18T14:37:57",
  "genre": "classical",
  "play_count": 144,
  "rating": 0.0,
  "like_count": 10,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/163"
 },
 {
  "song_id": 165,
  "title": "Hearts on Fire",
  "album_id": null,
  "duration": 183,
  "artists": [
   {
    "id": 14,
    "name": "Grace Harrison"
   }
  ],
  "release_date": "2022-12-18T10:15:09",
  "genre": "classical",
  "play_count": 419,
  "rating": 3.0,
  "like_count": 6,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/165"
 },
 {
  "song_id": 164,
  "title": "Waiting for the Morning Light",
  "album_id": null,
  "duration": 204,
  "artists": [
   {
    "id": 14,
    "name": "Grace Harrison"
   }
  ],
  "release_date": "2021-04-10T19:52:27",
  "genre": "classical",
  "play_count": 915,
  "rating": 3.5,
  "like_count": 2,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/164"
 },
 {
  "song_id": 166,
  "title": "In the Embrace of Solitude",
  "album_id": null,
  "duration": 204,
  "artists": [
   {
    "id": 14,
    "name": "Grace Harrison"
   }
  ],
  "release_date": "2019-06-21T13:36:29",
  "genre": "classical",
  "play_count": 971,
  "rating": 2.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/166"
 },
 {
  "song_id": 167,
  "title": "The Tragic Beauty of Love",
  "album_id": null,
  "duration": 190,
  "artists": [
   {
    "id": 14,
    "name": "Grace Harrison"
   }
  ],
  "release_date": "2019-05-19T20:53:31",
  "genre": "classical",
  "play_count": 898,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/167"
 },
 {
  "song_id": 168,
  "title": "Where Echoes Go to Die",
  "album_id": null,
  "duration": 236,
  "artists": [
   {
    "id": 14,
    "name": "Grace Harrison"
   }
  ],
  "release_date": "2022-06-01T13:34:28",
  "genre": "classical",
  "play_count": 678,
  "rating": 3.0,
  "like_count": 6,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/168"
 },
 {
  "song_id": 162,
  "title": "Caught in the Afterglow of Love",
  "album_id": null,
  "duration": 228,
  "artists": [
   {
    "id": 14,
    "name": "Grace Harrison"
   }
  ],
  "release_date": "2019-02-02T02:47:19",
  "genre": "classical",
  "play_count": 967,
  "rating": 4.0,
  "like_count": 11,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/162"
 },
 {
  "song_id": 11,
  "title": "Lost in a Moment's Grace",
  "album_id": 3,
  "duration": 196,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   },
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "release_date": "2022-11-08T06:55:52",
  "genre": "R&B",
  "play_count": 428,
  "rating": 0.0,
  "like_count": 11,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/11"
 },
 {
  "song_id": 1,
  "title": "Painting Shadows on the Wall",
  "album_id": 1,
  "duration": 217,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 638,
  "rating": 0.0,
  "like_count": 13,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/1"
 },
 {
  "song_id": 2,
  "title": "Lost in the Mists of Time",
  "album_id": 1,
  "duration": 224,
  "artists": [
   {
    "id": 3,
    "name": "Jasper Skye"
   },
   {
    "id": 26,
    "name": "Isabella Cruz"
   },
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-10-29T01:54:53",
  "genre": "EDM",
  "play_count": 205,
  "rating": 0.0,
  "like_count": 11,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/2"
 }
]
```


### Environment Interaction 29
----------------------------------------------------------------------------
```python
# Found: Wilted Grace -> 01/2022
# Now let's get the current content of the note to see the exact format
print(apis.simple_note.show_note(note_id=3084, access_token=simple_note_token))
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    print(apis.simple_note.show_note(note_id=3084, access_token=simple_note_token))
                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'simple_note_token' is not defined
```


### Environment Interaction 30
----------------------------------------------------------------------------
```python
# Let's first get the active task to confirm what we need to do
print(apis.supervisor.show_active_task())
```

```
{
 "instruction": "I keep a log of all my liked songs and respective artists in a note in simple_note. I want to add release month information for them as well. I have added it for the first few songs. Add it for the rest.",
 "status": null,
 "answer": "<<NOT_GIVEN>>"
}
```


### Environment Interaction 31
----------------------------------------------------------------------------
```python
# Let's get the simple_note access token from supervisor and view the note
# First, let's check the supervisor's account passwords to get the simple_note token
print(apis.supervisor.show_account_passwords())
```

```
[
 {
  "account_name": "amazon",
  "password": "[l0#5Yw"
 },
 {
  "account_name": "file_system",
  "password": "V]^dE[b"
 },
 {
  "account_name": "gmail",
  "password": "YUUXyJY"
 },
 {
  "account_name": "phone",
  "password": "]wpD$Y6"
 },
 {
  "account_name": "simple_note",
  "password": "sTv9L0p"
 },
 {
  "account_name": "splitwise",
  "password": "_fmm=r1"
 },
 {
  "account_name": "spotify",
  "password": "=ql86Wp"
 },
 {
  "account_name": "todoist",
  "password": "cO0f)9V"
 },
 {
  "account_name": "venmo",
  "password": "+REx^]2"
 }
]
```


### Environment Interaction 32
----------------------------------------------------------------------------
```python
# Let me check the simple_note login API documentation
print(apis.api_docs.show_api_doc(app_name='simple_note', api_name='login'))
```

```
{
 "app_name": "simple_note",
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


### Environment Interaction 33
----------------------------------------------------------------------------
```python
# Login to simple_note to get the access token
login_response = apis.simple_note.login(username='alexwhite@gmail.com', password='sTv9L0p')
print(login_response)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZSthbGV4d2hpdGVAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNzMxfQ.lVZpRVk0oUlWxftYVcd62cNL_83O7pPOd77sy0ZKmYo",
 "token_type": "Bearer"
}
```


### Environment Interaction 34
----------------------------------------------------------------------------
```python
# View the note content to see the exact format
note = apis.simple_note.show_note(note_id=3084, access_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZSthbGV4d2hpdGVAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNzMxfQ.lVZpRVk0oUlWxftYVcd62cNL_83O7pPOd77sy0ZKmYo')
print(note)
```

```
{
 "note_id": 3084,
 "title": "Spotify Liked Songs",
 "content": "# Spotify Liked Songs\n- When Angels Weep for Us BY Lucas Grey, Velvet Echo RELEASED_AT 07/2022\n- Unspoken Words BY Aria Sterling RELEASED_AT 06/2021\n- Time's Hold BY Aria Sterling RELEASED_AT 11/2022\n- Bleeding Sun BY Aria Sterling RELEASED_AT 11/2022\n- Distant Love BY Ava Morgan RELEASED_AT 12/2022\n- Silver Lining BY Ava Morgan RELEASED_AT TODO\n- Walking Through the Valley of Shadows BY Lily Moon, Zoey James RELEASED_AT TODO\n- Where Shadows Come to Life BY Olivia Roberts RELEASED_AT TODO\n- Eternal Melancholy BY Olivia Roberts RELEASED_AT TODO\n- Crimson Veil BY Phoenix Rivers RELEASED_AT TODO\n- Elusive Joy BY Orion Steele RELEASED_AT TODO\n- Ephemeral Beauty BY Eliana Harper RELEASED_AT TODO\n- Stardust Serenade BY Violet Cascade RELEASED_AT TODO\n- Veiled Behind a Mask of Joy BY Liam Palmer RELEASED_AT TODO\n- In the Wake of Unspoken Promises BY Isabella Cruz RELEASED_AT TODO\n- Wading Through the Ashes of Love BY Marcus Lane RELEASED_AT TODO\n- Fading Like a Distant Star BY Hazel Winter RELEASED_AT TODO\n- Wilted Grace BY Felix Blackwood RELEASED_AT TODO\n",
 "tags": [],
 "created_at": "2023-05-17T12:13:03",
 "updated_at": "2023-05-17T12:13:03",
 "pinned": false
}
```


### Environment Interaction 35
----------------------------------------------------------------------------
```python
# Update the note with release month info for the remaining songs
# Map song titles to release month/year (MM/YYYY)
release_dates = {
    "Silver Lining": "12/2022",
    "Walking Through the Valley of Shadows": "08/2022",
    "Where Shadows Come to Life": "01/2023",
    "Eternal Melancholy": "04/2023",
    "Crimson Veil": "01/2020",
    "Elusive Joy": "03/2021",
    "Ephemeral Beauty": "01/2020",
    "Stardust Serenade": "04/2019",
    "Veiled Behind a Mask of Joy": "10/2022",
    "In the Wake of Unspoken Promises": "07/2022",
    "Wading Through the Ashes of Love": "09/2020",
    "Fading Like a Distant Star": "01/2019",
    "Wilted Grace": "01/2022"
}

# Get the current note content
note_content = note['content']

# Replace each "RELEASED_AT TODO" with the correct month/year
for song_title, month_year in release_dates.items():
    # Find the line containing the song title and replace the TODO
    # We'll do a simple string replacement: "RELEASED_AT TODO" -> "RELEASED_AT {month_year}"
    # But we need to ensure we only replace for the correct song. Since each line is unique, we can replace the TODO on the line that contains the song title.
    # We'll split lines and process each line.
    pass

# Let's do it properly: split into lines, for each line, if it contains a song title from our dict, replace "TODO" with the month/year.
lines = note['content'].split('\n')
new_lines = []
for line in lines:
    # Check if any song title is in the line
    for title, month_year in release_dates.items():
        if title in line and 'RELEASED_AT TODO' in line:
            line = line.replace('RELEASED_AT TODO', f'RELEASED_AT {month_year}')
            break
    new_lines.append(line)

new_content = '\n'.join(new_lines)
print(new_content)
```

```
# Spotify Liked Songs
- When Angels Weep for Us BY Lucas Grey, Velvet Echo RELEASED_AT 07/2022
- Unspoken Words BY Aria Sterling RELEASED_AT 06/2021
- Time's Hold BY Aria Sterling RELEASED_AT 11/2022
- Bleeding Sun BY Aria Sterling RELEASED_AT 11/2022
- Distant Love BY Ava Morgan RELEASED_AT 12/2022
- Silver Lining BY Ava Morgan RELEASED_AT 12/2022
- Walking Through the Valley of Shadows BY Lily Moon, Zoey James RELEASED_AT 08/2022
- Where Shadows Come to Life BY Olivia Roberts RELEASED_AT 01/2023
- Eternal Melancholy BY Olivia Roberts RELEASED_AT 04/2023
- Crimson Veil BY Phoenix Rivers RELEASED_AT 01/2020
- Elusive Joy BY Orion Steele RELEASED_AT 03/2021
- Ephemeral Beauty BY Eliana Harper RELEASED_AT 01/2020
- Stardust Serenade BY Violet Cascade RELEASED_AT 04/2019
- Veiled Behind a Mask of Joy BY Liam Palmer RELEASED_AT 10/2022
- In the Wake of Unspoken Promises BY Isabella Cruz RELEASED_AT 07/2022
- Wading Through the Ashes of Love BY Marcus Lane RELEASED_AT 09/2020
- Fading Like a Distant Star BY Hazel Winter RELEASED_AT 01/2019
- Wilted Grace BY Felix Blackwood RELEASED_AT 01/2022
```


### Environment Interaction 36
----------------------------------------------------------------------------
```python
# Update the note with the new content
update_response = apis.simple_note.update_note(
    note_id=3084,
    access_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZSthbGV4d2hpdGVAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNzMxfQ.lVZpRVk0oUlWxftYVcd62cNL_83O7pPOd77sy0ZKmYo',
    content=new_content
)
print(update_response)
```

```
{"message": "Note updated."}
```


### Environment Interaction 37
----------------------------------------------------------------------------
```python
# Verify the note was updated correctly
note = apis.simple_note.show_note(note_id=3084, access_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZSthbGV4d2hpdGVAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNzMxfQ.lVZpRVk0oUlWxftYVcd62cNL_83O7pPOd77sy0ZKmYo')
print(note['content'])
```

```
# Spotify Liked Songs
- When Angels Weep for Us BY Lucas Grey, Velvet Echo RELEASED_AT 07/2022
- Unspoken Words BY Aria Sterling RELEASED_AT 06/2021
- Time's Hold BY Aria Sterling RELEASED_AT 11/2022
- Bleeding Sun BY Aria Sterling RELEASED_AT 11/2022
- Distant Love BY Ava Morgan RELEASED_AT 12/2022
- Silver Lining BY Ava Morgan RELEASED_AT 12/2022
- Walking Through the Valley of Shadows BY Lily Moon, Zoey James RELEASED_AT 08/2022
- Where Shadows Come to Life BY Olivia Roberts RELEASED_AT 01/2023
- Eternal Melancholy BY Olivia Roberts RELEASED_AT 04/2023
- Crimson Veil BY Phoenix Rivers RELEASED_AT 01/2020
- Elusive Joy BY Orion Steele RELEASED_AT 03/2021
- Ephemeral Beauty BY Eliana Harper RELEASED_AT 01/2020
- Stardust Serenade BY Violet Cascade RELEASED_AT 04/2019
- Veiled Behind a Mask of Joy BY Liam Palmer RELEASED_AT 10/2022
- In the Wake of Unspoken Promises BY Isabella Cruz RELEASED_AT 07/2022
- Wading Through the Ashes of Love BY Marcus Lane RELEASED_AT 09/2020
- Fading Like a Distant Star BY Hazel Winter RELEASED_AT 01/2019
- Wilted Grace BY Felix Blackwood RELEASED_AT 01/2022
```


### Environment Interaction 38
----------------------------------------------------------------------------
```python
# Task completed - all release dates have been added to the note
apis.supervisor.complete_task()
```

```
Execution successful.
```

