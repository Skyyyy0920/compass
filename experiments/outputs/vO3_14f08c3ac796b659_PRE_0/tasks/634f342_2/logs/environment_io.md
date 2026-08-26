
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
# Let's explore the Spotify and file_system APIs.
print(apis.api_docs.show_api_descriptions(app_name='spotify'))
print(apis.api_docs.show_api_descriptions(app_name='file_system'))
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
  "name": "show_directory",
  "description": "Show a list of files and/or sub-directories, optionally recursively, in a directory."
 },
 {
  "name": "create_directory",
  "description": "Create a directory if it does not exist, optionally recursively."
 },
 {
  "name": "delete_directory",
  "description": "Delete a directory with its sub-directories and files."
 },
 {
  "name": "directory_exists",
  "description": "Check if a directory exists."
 },
 {
  "name": "show_file",
  "description": "Show a file's content and other details, if it exists."
 },
 {
  "name": "create_file",
  "description": "Create a new file with the given content."
 },
 {
  "name": "delete_file",
  "description": "Delete a file."
 },
 {
  "name": "update_file",
  "description": "Update a file's content."
 },
 {
  "name": "file_exists",
  "description": "Check if a file exists."
 },
 {
  "name": "copy_file",
  "description": "Copy a file to another location."
 },
 {
  "name": "move_file",
  "description": "Move a file to another location."
 },
 {
  "name": "copy_directory",
  "description": "Copy a directory to another location."
 },
 {
  "name": "move_directory",
  "description": "Move a directory to another location."
 },
 {
  "name": "compress_directory",
  "description": "Compress a directory."
 },
 {
  "name": "decompress_file",
  "description": "Decompress a compressed file."
 }
]
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
# Let's get the full list of file_system APIs
print(apis.api_docs.show_api_descriptions(app_name='file_system'))
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
  "name": "show_directory",
  "description": "Show a list of files and/or sub-directories, optionally recursively, in a directory."
 },
 {
  "name": "create_directory",
  "description": "Create a directory if it does not exist, optionally recursively."
 },
 {
  "name": "delete_directory",
  "description": "Delete a directory with its sub-directories and files."
 },
 {
  "name": "directory_exists",
  "description": "Check if a directory exists."
 },
 {
  "name": "show_file",
  "description": "Show a file's content and other details, if it exists."
 },
 {
  "name": "create_file",
  "description": "Create a new file with the given content."
 },
 {
  "name": "delete_file",
  "description": "Delete a file."
 },
 {
  "name": "update_file",
  "description": "Update a file's content."
 },
 {
  "name": "file_exists",
  "description": "Check if a file exists."
 },
 {
  "name": "copy_file",
  "description": "Copy a file to another location."
 },
 {
  "name": "move_file",
  "description": "Move a file to another location."
 },
 {
  "name": "copy_directory",
  "description": "Copy a directory to another location."
 },
 {
  "name": "move_directory",
  "description": "Move a directory to another location."
 },
 {
  "name": "compress_directory",
  "description": "Compress a directory."
 },
 {
  "name": "decompress_file",
  "description": "Decompress a compressed file."
 }
]
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
# Let's get the account passwords from supervisor to access Spotify and file system.
print(apis.supervisor.show_account_passwords())
```

```
[
 {
  "account_name": "amazon",
  "password": "5%NF!wN"
 },
 {
  "account_name": "file_system",
  "password": "*AbZz@R"
 },
 {
  "account_name": "gmail",
  "password": "De8X_n3"
 },
 {
  "account_name": "phone",
  "password": "edM$BZ4"
 },
 {
  "account_name": "simple_note",
  "password": "1YXp{5h"
 },
 {
  "account_name": "splitwise",
  "password": "5n{C#t1"
 },
 {
  "account_name": "spotify",
  "password": "MG}]ZZ9"
 },
 {
  "account_name": "todoist",
  "password": "3g5B!BE"
 },
 {
  "account_name": "venmo",
  "password": "O=SUPrZ"
 }
]
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
# Let's check the supervisor APIs for account info and login details.
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


### Environment Interaction 6
----------------------------------------------------------------------------
```python
# Let's get the API docs for Spotify login and file_system login and show_file.
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='login'))
print(apis.api_docs.show_api_doc(app_name='file_system', api_name='login'))
print(apis.api_docs.show_api_doc(app_name='file_system', api_name='show_file'))
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
{
 "app_name": "file_system",
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
{
 "app_name": "file_system",
 "api_name": "show_file",
 "path": "/file",
 "method": "GET",
 "description": "Show a file's content and other details, if it exists.",
 "parameters": [
  {
   "name": "file_path",
   "type": "string",
   "required": true,
   "description": "Path of the file. Path can be absolute, starting with '/', or relative to the user's home directory, starting with '~/'.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from file_system app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "file_id": 1,
   "path": "string",
   "content": "string",
   "created_at": "2019-01-01T00:00:00",
   "updated_at": "2019-01-01T00:00:00"
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
# Let's get the supervisor's profile to find the email for login.
print(apis.supervisor.show_profile())
```

```
{
 "first_name": "Vickie",
 "last_name": "Powell",
 "email": "vicpowe@gmail.com",
 "phone_number": "8924356613",
 "birthday": "1959-01-26",
 "sex": "female"
}
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Let's get the API docs for Spotify login and file_system login to confirm parameters.
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='login'))
print(apis.api_docs.show_api_doc(app_name='file_system', api_name='login'))
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
{
 "app_name": "file_system",
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


### Environment Interaction 9
----------------------------------------------------------------------------
```python
# Log in to Spotify and file_system using the supervisor's email and passwords.
spotify_login = apis.spotify.login(username='vicpowe@gmail.com', password='MG}]ZZ9')
print(spotify_login)

fs_login = apis.file_system.login(username='vicpowe@gmail.com', password='*AbZz@R')
print(fs_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K3ZpY3Bvd2VAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyMDk4fQ.idhGRJkHzxyYhU-Y-BETJurmIMNgnRedLoX32Gwu6Y4",
 "token_type": "Bearer"
}
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmaWxlX3N5c3RlbSt2aWNwb3dlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjc0MX0.YSnnbTAEq7NGdW5tWQtW_ljyt7Sn2m4p0HER_AHBvsc",
 "token_type": "Bearer"
}
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
# Let's get the file_system show_file API doc to confirm parameters.
print(apis.api_docs.show_api_doc(app_name='file_system', api_name='show_file'))
```

```
{
 "app_name": "file_system",
 "api_name": "show_file",
 "path": "/file",
 "method": "GET",
 "description": "Show a file's content and other details, if it exists.",
 "parameters": [
  {
   "name": "file_path",
   "type": "string",
   "required": true,
   "description": "Path of the file. Path can be absolute, starting with '/', or relative to the user's home directory, starting with '~/'.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from file_system app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "file_id": 1,
   "path": "string",
   "content": "string",
   "created_at": "2019-01-01T00:00:00",
   "updated_at": "2019-01-01T00:00:00"
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Read the songs_to_archive.txt file from the file system.
fs_token = fs_login['access_token']
file_data = apis.file_system.show_file(file_path='~/documents/personal/songs_to_archive.txt', access_token=fs_token)
print(file_data)
```

```
{
 "file_id": 25851,
 "path": "/home/vickie/documents/personal/songs_to_archive.txt",
 "content": "# Songs to Archive\n- The Intangible Essence of You by Seraphina Dawn\n- The Paradox of Our Love by Oceanic Odyssey\n- Love's Last Lonely Mile by Velvet Echo\n- Caught in a Storm of Emotions by Ethan Wallace\n- When Dreams Begin to Crumble by Oceanic Odyssey\n- Gone Astray by Aria Sterling\n- Love's Aftermath by Mia Sullivan\n- Journey to the Celestial Realm by Dylan Stone\n- In the Chambers of My Mind by Jasper Skye\n- Lost in the Echoes of Time by Ethan Wallace\n- Wandering the Streets Alone by Felix Blackwood\n- The Illusion of Forever by Liam Palmer\n- Nostalgia's Hold by Marigold Muse\n- Symphony of the Twilight Forest by Aria Sterling\n- Crimson Skies of Longing by Phoenix Rivers\n- A Broken Heart's Lament by Lucas Diaz\n- Weeping Sky by Luna Starlight\n- Fading Like a Distant Star by Hazel Winter\n",
 "created_at": "2023-05-17T10:35:03",
 "updated_at": "2023-05-17T10:35:03"
}
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
# Let's explore the Spotify API docs for playlists and songs.
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


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# Let's get the API docs for playlist library and related functions.
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_playlist_library'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_playlist'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='add_song_to_playlist'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='remove_song_from_playlist'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='create_playlist'))
```

```
{
 "app_name": "spotify",
 "api_name": "show_playlist_library",
 "path": "/library/playlists",
 "method": "GET",
 "description": "Get a list of playlists in the user's playlist library.",
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
   "name": "is_public",
   "type": "boolean",
   "required": false,
   "description": "Whether to show public playlists or private playlists.",
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
  }
 ],
 "response_schemas": {
  "success": [
   {
    "playlist_id": 1,
    "title": "string",
    "is_public": true,
    "rating": 0.0,
    "like_count": 1,
    "review_count": 1,
    "owner": {
     "name": "string",
     "email": "user@example.com"
    },
    "created_at": "2019-01-01T00:00:00",
    "song_ids": [
     1
    ]
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "spotify",
 "api_name": "show_playlist",
 "path": "/playlists/{playlist_id}",
 "method": "GET",
 "description": "Get detailed information about a specific playlist. You can view your own playlists or others' playlists if they are public.",
 "parameters": [
  {
   "name": "playlist_id",
   "type": "integer",
   "required": true,
   "description": "The playlist id to retrieve.",
   "default": null,
   "constraints": []
  },
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
   "playlist_id": 1,
   "title": "string",
   "is_public": true,
   "rating": 0.0,
   "like_count": 1,
   "review_count": 1,
   "owner": {
    "name": "string",
    "email": "user@example.com"
   },
   "created_at": "2019-01-01T00:00:00",
   "shareable_link": "string",
   "songs": [
    {
     "id": 1,
     "title": "string",
     "artist_ids": [
      1
     ]
    }
   ]
  },
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "spotify",
 "api_name": "add_song_to_playlist",
 "path": "/playlists/{playlist_id}/songs/{song_id}",
 "method": "POST",
 "description": "Add a song to a playlist.",
 "parameters": [
  {
   "name": "playlist_id",
   "type": "integer",
   "required": true,
   "description": "The playlist id to add the song to.",
   "default": null,
   "constraints": []
  },
  {
   "name": "song_id",
   "type": "integer",
   "required": true,
   "description": "The song id to add.",
   "default": null,
   "constraints": []
  },
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
   "message": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "spotify",
 "api_name": "remove_song_from_playlist",
 "path": "/playlists/{playlist_id}/songs/{song_id}",
 "method": "DELETE",
 "description": "Remove a song from a playlist.",
 "parameters": [
  {
   "name": "playlist_id",
   "type": "integer",
   "required": true,
   "description": "The playlist id to remove the song from.",
   "default": null,
   "constraints": []
  },
  {
   "name": "song_id",
   "type": "integer",
   "required": true,
   "description": "The song id to remove.",
   "default": null,
   "constraints": []
  },
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
   "message": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "spotify",
 "api_name": "create_playlist",
 "path": "/playlists",
 "method": "POST",
 "description": "Create a new playlist.",
 "parameters": [
  {
   "name": "title",
   "type": "string",
   "required": true,
   "description": "The title of the playlist.",
   "default": null,
   "constraints": [
    "length >= 1"
   ]
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "is_public",
   "type": "boolean",
   "required": false,
   "description": "Whether the playlist is public or not.",
   "default": false,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string",
   "playlist_id": 1
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
# Let's get the search_songs API doc to understand how to search for songs.
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


### Environment Interaction 15
----------------------------------------------------------------------------
```python
# Let's get the Spotify login API doc to ensure we can re-authenticate if needed.
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


### Environment Interaction 16
----------------------------------------------------------------------------
```python
# Let's re-login to Spotify and file_system to get fresh tokens, and read the archive file.
import json

# Login to Spotify
spotify_login = apis.spotify.login(username='vicpowe@gmail.com', password='MG}]ZZ9')
print(spotify_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K3ZpY3Bvd2VAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNzMxfQ.NXbP6lS_xcSVzFzM9QXI_u_Klg8tdXyb3vZsVVcntC0",
 "token_type": "Bearer"
}
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
# Login to file_system and read the songs_to_archive.txt file
fs_login = apis.file_system.login(username='vicpowe@gmail.com', password='*AbZz@R')
print(fs_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmaWxlX3N5c3RlbSt2aWNwb3dlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjE1N30.c3FIzYl4nkeBMMxbjdPmWjGrixCbgYTJAlA31zq5dsA",
 "token_type": "Bearer"
}
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
# Read the songs_to_archive.txt file from file_system
fs_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmaWxlX3N5c3RlbSt2aWNwb3dlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjE1N30.c3FIzYl4nkeBMMxbjdPmWjGrixCbgYTJAlA31zq5dsA'
file_data = apis.file_system.show_file(file_path='~/documents/personal/songs_to_archive.txt', access_token=fs_token)
print(file_data)
```

```
{
 "file_id": 25851,
 "path": "/home/vickie/documents/personal/songs_to_archive.txt",
 "content": "# Songs to Archive\n- The Intangible Essence of You by Seraphina Dawn\n- The Paradox of Our Love by Oceanic Odyssey\n- Love's Last Lonely Mile by Velvet Echo\n- Caught in a Storm of Emotions by Ethan Wallace\n- When Dreams Begin to Crumble by Oceanic Odyssey\n- Gone Astray by Aria Sterling\n- Love's Aftermath by Mia Sullivan\n- Journey to the Celestial Realm by Dylan Stone\n- In the Chambers of My Mind by Jasper Skye\n- Lost in the Echoes of Time by Ethan Wallace\n- Wandering the Streets Alone by Felix Blackwood\n- The Illusion of Forever by Liam Palmer\n- Nostalgia's Hold by Marigold Muse\n- Symphony of the Twilight Forest by Aria Sterling\n- Crimson Skies of Longing by Phoenix Rivers\n- A Broken Heart's Lament by Lucas Diaz\n- Weeping Sky by Luna Starlight\n- Fading Like a Distant Star by Hazel Winter\n",
 "created_at": "2023-05-17T10:35:03",
 "updated_at": "2023-05-17T10:35:03"
}
```


### Environment Interaction 19
----------------------------------------------------------------------------
```python
# Parse the file content to extract song titles and artists
import re

content = file_data['content']
songs_to_archive = []
for line in content.split('\n'):
    line = line.strip()
    if line.startswith('- '):
        # Remove the "- " prefix
        song_str = line[2:]
        # Split by " by " to get title and artist
        if ' by ' in song_str:
            title, artist = song_str.split(' by ', 1)
            songs_to_archive.append({'title': title.strip(), 'artist': artist.strip()})
print(songs_to_archive)
```

```
[
 {
  "title": "The Intangible Essence of You",
  "artist": "Seraphina Dawn"
 },
 {
  "title": "The Paradox of Our Love",
  "artist": "Oceanic Odyssey"
 },
 {
  "title": "Love's Last Lonely Mile",
  "artist": "Velvet Echo"
 },
 {
  "title": "Caught in a Storm of Emotions",
  "artist": "Ethan Wallace"
 },
 {
  "title": "When Dreams Begin to Crumble",
  "artist": "Oceanic Odyssey"
 },
 {
  "title": "Gone Astray",
  "artist": "Aria Sterling"
 },
 {
  "title": "Love's Aftermath",
  "artist": "Mia Sullivan"
 },
 {
  "title": "Journey to the Celestial Realm",
  "artist": "Dylan Stone"
 },
 {
  "title": "In the Chambers of My Mind",
  "artist": "Jasper Skye"
 },
 {
  "title": "Lost in the Echoes of Time",
  "artist": "Ethan Wallace"
 },
 {
  "title": "Wandering the Streets Alone",
  "artist": "Felix Blackwood"
 },
 {
  "title": "The Illusion of Forever",
  "artist": "Liam Palmer"
 },
 {
  "title": "Nostalgia's Hold",
  "artist": "Marigold Muse"
 },
 {
  "title": "Symphony of the Twilight Forest",
  "artist": "Aria Sterling"
 },
 {
  "title": "Crimson Skies of Longing",
  "artist": "Phoenix Rivers"
 },
 {
  "title": "A Broken Heart's Lament",
  "artist": "Lucas Diaz"
 },
 {
  "title": "Weeping Sky",
  "artist": "Luna Starlight"
 },
 {
  "title": "Fading Like a Distant Star",
  "artist": "Hazel Winter"
 }
]
```


### Environment Interaction 20
----------------------------------------------------------------------------
```python
# Store the Spotify access token and get all playlists
spotify_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K3ZpY3Bvd2VAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNzMxfQ.NXbP6lS_xcSVzFzM9QXI_u_Klg8tdXyb3vZsVVcntC0'

# Get all playlists (paginate through all pages)
all_playlists = []
page_index = 0
while True:
    playlists_page = apis.spotify.show_playlist_library(access_token=spotify_token, page_index=page_index, page_limit=20)
    print(f"Page {page_index}: {playlists_page}")
    if not playlists_page or len(playlists_page) == 0:
        break
    all_playlists.extend(playlists_page)
    if len(playlists_page) < 20:
        break
    page_index += 1

print(f"\nTotal playlists found: {len(all_playlists)}")
```

```
Page 0: [{'playlist_id': 160, 'title': 'Coffeehouse Chronicles', 'is_public': True, 'rating': 0.0, 'like_count': 2, 'review_count': 0, 'owner': {'name': 'Vickie Powell', 'email': 'vicpowe@gmail.com'}, 'created_at': '2023-04-28T00:13:35', 'song_ids': [58, 91, 106, 117, 148, 185, 202, 216, 223, 246]}, {'playlist_id': 161, 'title': 'Cubicle Chronicles: Office Vibes', 'is_public': False, 'rating': 0.0, 'like_count': 0, 'review_count': 0, 'owner': {'name': 'Vickie Powell', 'email': 'vicpowe@gmail.com'}, 'created_at': '2023-04-05T10:12:01', 'song_ids': [7, 58, 100, 128, 167, 201, 208, 215, 219, 277]}, {'playlist_id': 162, 'title': 'Vocal Virtuosity: A Cappella Excellence', 'is_public': True, 'rating': 4.0, 'like_count': 1, 'review_count': 1, 'owner': {'name': 'Vickie Powell', 'email': 'vicpowe@gmail.com'}, 'created_at': '2023-03-21T22:44:01', 'song_ids': [41, 114, 153, 188, 210]}, {'playlist_id': 163, 'title': 'Midnight Melodies: Late Night Jams', 'is_public': True, 'rating': 0.0, 'like_count': 0, 'review_count': 0, 'owner': {'name': 'Vickie Powell', 'email': 'vicpowe@gmail.com'}, 'created_at': '2023-03-29T12:30:34', 'song_ids': [90, 96, 118, 171, 208, 271, 300, 312]}, {'playlist_id': 164, 'title': 'Countryside Chronicles: Folk Favorites', 'is_public': False, 'rating': 0.0, 'like_count': 0, 'review_count': 0, 'owner': {'name': 'Vickie Powell', 'email': 'vicpowe@gmail.com'}, 'created_at': '2023-03-18T11:10:53', 'song_ids': [7, 10, 17, 23, 80, 100, 203, 207, 212, 238]}, {'playlist_id': 165, 'title': 'The Rom-Com Mixtape', 'is_public': True, 'rating': 5.0, 'like_count': 0, 'review_count': 1, 'owner': {'name': 'Vickie Powell', 'email': 'vicpowe@gmail.com'}, 'created_at': '2023-03-17T00:52:56', 'song_ids': [29, 46, 65, 88, 99, 104, 120]}, {'playlist_id': 166, 'title': 'Underground Explorations: Alt & Experimental', 'is_public': True, 'rating': 0.0, 'like_count': 2, 'review_count': 0, 'owner': {'name': 'Vickie Powell', 'email': 'vicpowe@gmail.com'}, 'created_at': '2023-03-30T15:10:02', 'song_ids': [2, 75, 89, 160, 278, 291]}, {'playlist_id': 167, 'title': 'Woodstock Reimagined: Festival Vibes', 'is_public': False, 'rating': 0.0, 'like_count': 1, 'review_count': 0, 'owner': {'name': 'Vickie Powell', 'email': 'vicpowe@gmail.com'}, 'created_at': '2023-03-03T08:08:05', 'song_ids': [41, 46, 106, 110, 116, 130, 199, 268]}]

Total playlists found: 8
```


### Environment Interaction 21
----------------------------------------------------------------------------
```python
# Let's check the search_songs API doc to understand how to search for songs
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


### Environment Interaction 22
----------------------------------------------------------------------------
```python
# Let's create the "Old Songs" playlist first
# We have the Spotify access token from earlier
spotify_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K3ZpY3Bvd2VAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNzMxfQ.NXbP6lS_xcSVzFzM9QXI_u8sldb7vzVcntC0"

# Create the playlist
result = apis.spotify.create_playlist(title="Old Songs", access_token=spotify_access_token)
print(result)
```

```
Execution failed. Traceback:
  File "<python-input>", line 6, in <module>
    result = apis.spotify.create_playlist(title="Old Songs", access_token=spotify_access_token)
                                                                          ^^^^^^^^^^^^^^^^^^^^
NameError: name 'spotify_access_token' is not defined
```


### Environment Interaction 23
----------------------------------------------------------------------------
```python
# Let me check the login API doc to get a fresh token
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


### Environment Interaction 24
----------------------------------------------------------------------------
```python
# Login to Spotify to get a fresh access token
login_result = apis.spotify.login(username="vicpowe@gmail.com", password="MG}]ZZ9")
print(login_result)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K3ZpY3Bvd2VAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNjA0fQ.EFEWQeqXh4QJgo0f_iFg9lxoLhhj06sYrWqYoalbHVM",
 "token_type": "Bearer"
}
```


### Environment Interaction 25
----------------------------------------------------------------------------
```python
# Create the "Old Songs" playlist
create_result = apis.spotify.create_playlist(title="Old Songs", access_token=login_result["access_token"])
print(create_result)
```

```
{"message": "Playlist created.", "playlist_id": 654}
```


### Environment Interaction 26
----------------------------------------------------------------------------
```python
# Get all playlists to see their song IDs
playlists = apis.spotify.show_playlist_library(access_token=login_result["access_token"], page_limit=20)
print(playlists)
```

```
[
 {
  "playlist_id": 160,
  "title": "Coffeehouse Chronicles",
  "is_public": true,
  "rating": 0.0,
  "like_count": 2,
  "review_count": 0,
  "owner": {
   "name": "Vickie Powell",
   "email": "vicpowe@gmail.com"
  },
  "created_at": "2023-04-28T00:13:35",
  "song_ids": [
   58,
   91,
   106,
   117,
   148,
   185,
   202,
   216,
   223,
   246
  ]
 },
 {
  "playlist_id": 161,
  "title": "Cubicle Chronicles: Office Vibes",
  "is_public": false,
  "rating": 0.0,
  "like_count": 0,
  "review_count": 0,
  "owner": {
   "name": "Vickie Powell",
   "email": "vicpowe@gmail.com"
  },
  "created_at": "2023-04-05T10:12:01",
  "song_ids": [
   7,
   58,
   100,
   128,
   167,
   201,
   208,
   215,
   219,
   277
  ]
 },
 {
  "playlist_id": 162,
  "title": "Vocal Virtuosity: A Cappella Excellence",
  "is_public": true,
  "rating": 4.0,
  "like_count": 1,
  "review_count": 1,
  "owner": {
   "name": "Vickie Powell",
   "email": "vicpowe@gmail.com"
  },
  "created_at": "2023-03-21T22:44:01",
  "song_ids": [
   41,
   114,
   153,
   188,
   210
  ]
 },
 {
  "playlist_id": 163,
  "title": "Midnight Melodies: Late Night Jams",
  "is_public": true,
  "rating": 0.0,
  "like_count": 0,
  "review_count": 0,
  "owner": {
   "name": "Vickie Powell",
   "email": "vicpowe@gmail.com"
  },
  "created_at": "2023-03-29T12:30:34",
  "song_ids": [
   90,
   96,
   118,
   171,
   208,
   271,
   300,
   312
  ]
 },
 {
  "playlist_id": 164,
  "title": "Countryside Chronicles: Folk Favorites",
  "is_public": false,
  "rating": 0.0,
  "like_count": 0,
  "review_count": 0,
  "owner": {
   "name": "Vickie Powell",
   "email": "vicpowe@gmail.com"
  },
  "created_at": "2023-03-18T11:10:53",
  "song_ids": [
   7,
   10,
   17,
   23,
   80,
   100,
   203,
   207,
   212,
   238
  ]
 },
 {
  "playlist_id": 165,
  "title": "The Rom-Com Mixtape",
  "is_public": true,
  "rating": 5.0,
  "like_count": 0,
  "review_count": 1,
  "owner": {
   "name": "Vickie Powell",
   "email": "vicpowe@gmail.com"
  },
  "created_at": "2023-03-17T00:52:56",
  "song_ids": [
   29,
   46,
   65,
   88,
   99,
   104,
   120
  ]
 },
 {
  "playlist_id": 166,
  "title": "Underground Explorations: Alt & Experimental",
  "is_public": true,
  "rating": 0.0,
  "like_count": 2,
  "review_count": 0,
  "owner": {
   "name": "Vickie Powell",
   "email": "vicpowe@gmail.com"
  },
  "created_at": "2023-03-30T15:10:02",
  "song_ids": [
   2,
   75,
   89,
   160,
   278,
   291
  ]
 },
 {
  "playlist_id": 167,
  "title": "Woodstock Reimagined: Festival Vibes",
  "is_public": false,
  "rating": 0.0,
  "like_count": 1,
  "review_count": 0,
  "owner": {
   "name": "Vickie Powell",
   "email": "vicpowe@gmail.com"
  },
  "created_at": "2023-03-03T08:08:05",
  "song_ids": [
   41,
   46,
   106,
   110,
   116,
   130,
   199,
   268
  ]
 },
 {
  "playlist_id": 654,
  "title": "Old Songs",
  "is_public": false,
  "rating": 0.0,
  "like_count": 0,
  "review_count": 0,
  "owner": {
   "name": "Vickie Powell",
   "email": "vicpowe@gmail.com"
  },
  "created_at": "2023-05-18T12:00:00",
  "song_ids": []
 }
]
```


### Environment Interaction 27
----------------------------------------------------------------------------
```python
# Let's search for the first song to understand the search results
search_result = apis.spotify.search_songs(query="The Intangible Essence of You Seraphina Dawn", access_token=login_result["access_token"], page_limit=20)
print(search_result)
```

```
[
 {
  "song_id": 117,
  "title": "The Intangible Essence of You",
  "album_id": null,
  "duration": 281,
  "artists": [
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2020-06-06T20:34:42",
  "genre": "EDM",
  "play_count": 483,
  "rating": 4.5,
  "like_count": 7,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/117"
 },
 {
  "song_id": 298,
  "title": "When Dawn Breaks Without You",
  "album_id": null,
  "duration": 248,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   }
  ],
  "release_date": "2021-05-21T19:35:41",
  "genre": "R&B",
  "play_count": 718,
  "rating": 0.0,
  "like_count": 8,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/298"
 },
 {
  "song_id": 111,
  "title": "Lonesome Road",
  "album_id": null,
  "duration": 277,
  "artists": [
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-06-30T23:28:04",
  "genre": "EDM",
  "play_count": 658,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/111"
 },
 {
  "song_id": 112,
  "title": "Silent Tears",
  "album_id": null,
  "duration": 189,
  "artists": [
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2020-01-17T15:57:44",
  "genre": "EDM",
  "play_count": 356,
  "rating": 2.0,
  "like_count": 2,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/112"
 },
 {
  "song_id": 116,
  "title": "Paper Planes",
  "album_id": null,
  "duration": 232,
  "artists": [
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2021-03-06T18:06:01",
  "genre": "EDM",
  "play_count": 565,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/116"
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
  "song_id": 113,
  "title": "Chasing Echoes in the Dark",
  "album_id": null,
  "duration": 263,
  "artists": [
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2020-12-31T12:44:37",
  "genre": "EDM",
  "play_count": 949,
  "rating": 0.0,
  "like_count": 5,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/113"
 },
 {
  "song_id": 114,
  "title": "When All Hope Seems Lost",
  "album_id": null,
  "duration": 253,
  "artists": [
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "release_date": "2022-04-20T12:58:02",
  "genre": "EDM",
  "play_count": 868,
  "rating": 5.0,
  "like_count": 5,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/114"
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
  "song_id": 10,
  "title": "The Curse of Loving You",
  "album_id": 2,
  "duration": 211,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   }
  ],
  "release_date": "2022-05-21T21:55:36",
  "genre": "R&B",
  "play_count": 386,
  "rating": 0.0,
  "like_count": 20,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/10"
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
  "song_id": 186,
  "title": "The Edge of Eternity",
  "album_id": null,
  "duration": 300,
  "artists": [
   {
    "id": 17,
    "name": "Dylan Stone"
   }
  ],
  "release_date": "2021-04-27T11:35:55",
  "genre": "country",
  "play_count": 269,
  "rating": 5.0,
  "like_count": 8,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/186"
 },
 {
  "song_id": 238,
  "title": "The Illusion of Forever",
  "album_id": null,
  "duration": 185,
  "artists": [
   {
    "id": 24,
    "name": "Liam Palmer"
   }
  ],
  "release_date": "2023-01-04T13:07:48",
  "genre": "country",
  "play_count": 716,
  "rating": 0.0,
  "like_count": 5,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/238"
 }
]
```


### Environment Interaction 28
----------------------------------------------------------------------------
```python
# Let's search for the second song
search_result2 = apis.spotify.search_songs(query="The Paradox of Our Love Oceanic Odyssey", access_token=login_result["access_token"], page_limit=20)
print(search_result2)
```

```
[
 {
  "song_id": 216,
  "title": "The Paradox of Our Love",
  "album_id": null,
  "duration": 215,
  "artists": [
   {
    "id": 21,
    "name": "Oceanic Odyssey"
   }
  ],
  "release_date": "2021-09-15T07:24:22",
  "genre": "classical",
  "play_count": 595,
  "rating": 4.5,
  "like_count": 8,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/216"
 },
 {
  "song_id": 219,
  "title": "Strangers Again",
  "album_id": null,
  "duration": 292,
  "artists": [
   {
    "id": 21,
    "name": "Oceanic Odyssey"
   }
  ],
  "release_date": "2022-06-18T11:40:31",
  "genre": "classical",
  "play_count": 557,
  "rating": 0.0,
  "like_count": 9,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/219"
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
  "song_id": 214,
  "title": "The Sweet Pain of Reminiscence",
  "album_id": null,
  "duration": 253,
  "artists": [
   {
    "id": 21,
    "name": "Oceanic Odyssey"
   }
  ],
  "release_date": "2020-07-31T14:41:55",
  "genre": "classical",
  "play_count": 325,
  "rating": 0.0,
  "like_count": 0,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/214"
 },
 {
  "song_id": 218,
  "title": "Lost in the Tumult of Emotions",
  "album_id": null,
  "duration": 249,
  "artists": [
   {
    "id": 21,
    "name": "Oceanic Odyssey"
   }
  ],
  "release_date": "2021-10-25T15:03:50",
  "genre": "classical",
  "play_count": 282,
  "rating": 0.0,
  "like_count": 10,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/218"
 },
 {
  "song_id": 220,
  "title": "The Threads of a Frayed Bond",
  "album_id": null,
  "duration": 217,
  "artists": [
   {
    "id": 21,
    "name": "Oceanic Odyssey"
   }
  ],
  "release_date": "2022-12-25T14:08:13",
  "genre": "classical",
  "play_count": 133,
  "rating": 3.5,
  "like_count": 8,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/220"
 },
 {
  "song_id": 212,
  "title": "A Labyrinth of Empty Streets",
  "album_id": null,
  "duration": 211,
  "artists": [
   {
    "id": 21,
    "name": "Oceanic Odyssey"
   }
  ],
  "release_date": "2022-05-07T16:06:08",
  "genre": "classical",
  "play_count": 634,
  "rating": 3.5,
  "like_count": 6,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/212"
 },
 {
  "song_id": 217,
  "title": "Torn Between Two Worlds",
  "album_id": null,
  "duration": 224,
  "artists": [
   {
    "id": 21,
    "name": "Oceanic Odyssey"
   }
  ],
  "release_date": "2021-12-29T21:30:48",
  "genre": "classical",
  "play_count": 734,
  "rating": 2.0,
  "like_count": 6,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/217"
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
  "song_id": 154,
  "title": "The Ghosts of Our Past",
  "album_id": null,
  "duration": 204,
  "artists": [
   {
    "id": 12,
    "name": "Mia Sullivan"
   }
  ],
  "release_date": "2022-11-17T07:32:44",
  "genre": "classical",
  "play_count": 637,
  "rating": 0.0,
  "like_count": 9,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/154"
 },
 {
  "song_id": 195,
  "title": "Rhapsody of the Ocean's Embrace",
  "album_id": null,
  "duration": 298,
  "artists": [
   {
    "id": 18,
    "name": "Astrid Nightshade"
   }
  ],
  "release_date": "2022-08-20T02:38:15",
  "genre": "reggae",
  "play_count": 826,
  "rating": 3.0,
  "like_count": 5,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/195"
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
  "song_id": 260,
  "title": "The Mystery of Your Love",
  "album_id": null,
  "duration": 300,
  "artists": [
   {
    "id": 27,
    "name": "Carter Knight"
   }
  ],
  "release_date": "2019-04-09T18:34:47",
  "genre": "classical",
  "play_count": 593,
  "rating": 2.0,
  "like_count": 7,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/260"
 },
 {
  "song_id": 271,
  "title": "The Hidden Language of Love",
  "album_id": null,
  "duration": 219,
  "artists": [
   {
    "id": 28,
    "name": "Evelyn Rose"
   }
  ],
  "release_date": "2022-11-04T16:43:50",
  "genre": "classical",
  "play_count": 156,
  "rating": 3.3,
  "like_count": 5,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/271"
 },
 {
  "song_id": 10,
  "title": "The Curse of Loving You",
  "album_id": 2,
  "duration": 211,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   }
  ],
  "release_date": "2022-05-21T21:55:36",
  "genre": "R&B",
  "play_count": 386,
  "rating": 0.0,
  "like_count": 20,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/10"
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
 }
]
```


### Environment Interaction 29
----------------------------------------------------------------------------
```python
# Let's define the list of songs to archive and search for the third song
songs_to_archive = [
    ("The Intangible Essence of You", "Seraphina Dawn"),
    ("The Paradox of Our Love", "Oceanic Odyssey"),
    ("Love's Last Lonely Mile", "Velvet Echo"),
    ("Caught in a Storm of Emotions", "Ethan Wallace"),
    ("When Dreams Begin to Crumble", "Oceanic Odyssey"),
    ("Gone Astray", "Aria Sterling"),
    ("Love's Aftermath", "Mia Sullivan"),
    ("Journey to the Celestial Realm", "Dylan Stone"),
    ("In the Chambers of My Mind", "Jasper Skye"),
    ("Lost in the Echoes of Time", "Ethan Wallace"),
    ("Wandering the Streets Alone", "Felix Blackwood"),
    ("The Illusion of Forever", "Liam Palmer"),
    ("Nostalgia's Hold", "Marigold Muse"),
    ("Symphony of the Twilight Forest", "Aria Sterling"),
    ("Crimson Skies of Longing", "Phoenix Rivers"),
    ("A Broken Heart's Lament", "Lucas Diaz"),
    ("Weeping Sky", "Luna Starlight"),
    ("Fading Like a Distant Star", "Hazel Winter")
]

# Search for the third song
search3 = apis.spotify.search_songs(query="Love's Last Lonely Mile Velvet Echo", access_token=login_result["access_token"], page_limit=20)
print(search3)
```

```
[
 {
  "song_id": 246,
  "title": "Love's Last Lonely Mile",
  "album_id": null,
  "duration": 190,
  "artists": [
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2022-03-01T04:56:55",
  "genre": "R&B",
  "play_count": 600,
  "rating": 4.0,
  "like_count": 7,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/246"
 },
 {
  "song_id": 244,
  "title": "Cosmic Drift",
  "album_id": null,
  "duration": 267,
  "artists": [
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2021-12-03T18:25:07",
  "genre": "R&B",
  "play_count": 389,
  "rating": 0.0,
  "like_count": 8,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/244"
 },
 {
  "song_id": 250,
  "title": "Invisible Chains",
  "album_id": null,
  "duration": 215,
  "artists": [
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2021-08-03T07:15:22",
  "genre": "R&B",
  "play_count": 554,
  "rating": 0.0,
  "like_count": 6,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/250"
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
  "release_date": "2022-11-11T09:54:16",
  "genre": "jazz",
  "play_count": 316,
  "rating": 3.0,
  "like_count": 14,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/50"
 },
 {
  "song_id": 243,
  "title": "Bittersweet Memories Remain",
  "album_id": null,
  "duration": 244,
  "artists": [
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2020-09-25T17:44:47",
  "genre": "R&B",
  "play_count": 883,
  "rating": 3.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/243"
 },
 {
  "song_id": 28,
  "title": "Invisible Lines",
  "album_id": 5,
  "duration": 199,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   },
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2022-07-15T17:46:36",
  "genre": "R&B",
  "play_count": 110,
  "rating": 4.0,
  "like_count": 12,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/28"
 },
 {
  "song_id": 247,
  "title": "A Symphony of Dreams",
  "album_id": null,
  "duration": 241,
  "artists": [
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2021-11-01T00:42:15",
  "genre": "R&B",
  "play_count": 374,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/247"
 },
 {
  "song_id": 23,
  "title": "Solitude's Melancholy",
  "album_id": 5,
  "duration": 287,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   },
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2022-07-15T17:46:36",
  "genre": "R&B",
  "play_count": 386,
  "rating": 3.0,
  "like_count": 11,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/23"
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
  "song_id": 245,
  "title": "Beneath the Surface of Love",
  "album_id": null,
  "duration": 206,
  "artists": [
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2019-12-30T06:19:02",
  "genre": "R&B",
  "play_count": 264,
  "rating": 3.0,
  "like_count": 3,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/245"
 },
 {
  "song_id": 248,
  "title": "Chasing the Mirage of Happiness",
  "album_id": null,
  "duration": 288,
  "artists": [
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2020-03-07T11:14:12",
  "genre": "R&B",
  "play_count": 324,
  "rating": 0.0,
  "like_count": 4,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/248"
 },
 {
  "song_id": 242,
  "title": "Cracks in the Facade of Love",
  "album_id": null,
  "duration": 285,
  "artists": [
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2020-07-07T06:33:27",
  "genre": "R&B",
  "play_count": 637,
  "rating": 0.0,
  "like_count": 7,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/242"
 },
 {
  "song_id": 249,
  "title": "Dancing on the Edge of Madness",
  "album_id": null,
  "duration": 192,
  "artists": [
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2021-03-09T19:50:11",
  "genre": "R&B",
  "play_count": 271,
  "rating": 4.0,
  "like_count": 5,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/249"
 },
 {
  "song_id": 24,
  "title": "The Unseen Scars of Love",
  "album_id": 5,
  "duration": 281,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   },
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2022-07-15T17:46:36",
  "genre": "R&B",
  "play_count": 630,
  "rating": 5.0,
  "like_count": 13,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/24"
 },
 {
  "song_id": 25,
  "title": "A Symphony of Broken Hearts",
  "album_id": 5,
  "duration": 260,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   },
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2022-07-15T17:46:36",
  "genre": "R&B",
  "play_count": 577,
  "rating": 0.0,
  "like_count": 9,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/25"
 },
 {
  "song_id": 27,
  "title": "When Angels Weep for Us",
  "album_id": 5,
  "duration": 230,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   },
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2022-07-15T17:46:36",
  "genre": "R&B",
  "play_count": 472,
  "rating": 0.0,
  "like_count": 14,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/27"
 },
 {
  "song_id": 26,
  "title": "In the Light of Dying Stars",
  "album_id": 5,
  "duration": 206,
  "artists": [
   {
    "id": 32,
    "name": "Lucas Grey"
   },
   {
    "id": 25,
    "name": "Velvet Echo"
   }
  ],
  "release_date": "2022-07-15T17:46:36",
  "genre": "R&B",
  "play_count": 445,
  "rating": 3.0,
  "like_count": 11,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/26"
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
  "song_id": 153,
  "title": "Love's Aftermath",
  "album_id": null,
  "duration": 265,
  "artists": [
   {
    "id": 12,
    "name": "Mia Sullivan"
   }
  ],
  "release_date": "2022-08-08T12:27:39",
  "genre": "classical",
  "play_count": 758,
  "rating": 3.0,
  "like_count": 8,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/153"
 },
 {
  "song_id": 204,
  "title": "Love's Lure",
  "album_id": null,
  "duration": 282,
  "artists": [
   {
    "id": 19,
    "name": "Ethan Wallace"
   }
  ],
  "release_date": "2020-08-27T12:07:30",
  "genre": "indie",
  "play_count": 694,
  "rating": 3.0,
  "like_count": 8,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/204"
 }
]
```


### Environment Interaction 30
----------------------------------------------------------------------------
```python
# Search for the fourth song
search4 = apis.spotify.search_songs(query="Caught in a Storm of Emotions Ethan Wallace", access_token=login_result["access_token"], page_limit=20)
print(search4)
```

```
[
 {
  "song_id": 201,
  "title": "Caught in a Storm of Emotions",
  "album_id": null,
  "duration": 195,
  "artists": [
   {
    "id": 19,
    "name": "Ethan Wallace"
   }
  ],
  "release_date": "2020-07-04T02:59:14",
  "genre": "indie",
  "play_count": 762,
  "rating": 4.0,
  "like_count": 7,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/201"
 },
 {
  "song_id": 203,
  "title": "Lost in the Echoes of Time",
  "album_id": null,
  "duration": 245,
  "artists": [
   {
    "id": 19,
    "name": "Ethan Wallace"
   }
  ],
  "release_date": "2022-03-27T07:06:38",
  "genre": "indie",
  "play_count": 692,
  "rating": 2.0,
  "like_count": 9,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/203"
 },
 {
  "song_id": 205,
  "title": "Cursed Fate",
  "album_id": null,
  "duration": 250,
  "artists": [
   {
    "id": 19,
    "name": "Ethan Wallace"
   }
  ],
  "release_date": "2020-12-27T23:40:50",
  "genre": "indie",
  "play_count": 355,
  "rating": 0.0,
  "like_count": 2,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/205"
 },
 {
  "song_id": 202,
  "title": "Summer's End",
  "album_id": null,
  "duration": 277,
  "artists": [
   {
    "id": 19,
    "name": "Ethan Wallace"
   }
  ],
  "release_date": "2022-04-03T03:07:10",
  "genre": "indie",
  "play_count": 356,
  "rating": 3.3,
  "like_count": 10,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/202"
 },
 {
  "song_id": 204,
  "title": "Love's Lure",
  "album_id": null,
  "duration": 282,
  "artists": [
   {
    "id": 19,
    "name": "Ethan Wallace"
   }
  ],
  "release_date": "2020-08-27T12:07:30",
  "genre": "indie",
  "play_count": 694,
  "rating": 3.0,
  "like_count": 8,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/204"
 },
 {
  "song_id": 206,
  "title": "Escaping the Chains of Fate",
  "album_id": null,
  "duration": 285,
  "artists": [
   {
    "id": 19,
    "name": "Ethan Wallace"
   }
  ],
  "release_date": "2022-03-11T03:58:50",
  "genre": "indie",
  "play_count": 175,
  "rating": 3.0,
  "like_count": 8,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/206"
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
  "song_id": 31,
  "title": "Waves of Yesterday",
  "album_id": 6,
  "duration": 229,
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
  "play_count": 125,
  "rating": 2.0,
  "like_count": 15,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/31"
 },
 {
  "song_id": 218,
  "title": "Lost in the Tumult of Emotions",
  "album_id": null,
  "duration": 249,
  "artists": [
   {
    "id": 21,
    "name": "Oceanic Odyssey"
   }
  ],
  "release_date": "2021-10-25T15:03:50",
  "genre": "classical",
  "play_count": 282,
  "rating": 0.0,
  "like_count": 10,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/218"
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
  "song_id": 30,
  "title": "Eternal Flame",
  "album_id": 6,
  "duration": 258,
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
  "play_count": 395,
  "rating": 0.0,
  "like_count": 10,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/30"
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
 },
 {
  "song_id": 279,
  "title": "The Silence After the Storm",
  "album_id": null,
  "duration": 193,
  "artists": [
   {
    "id": 29,
    "name": "Lucas Diaz"
   }
  ],
  "release_date": "2021-10-01T13:54:32",
  "genre": "pop",
  "play_count": 543,
  "rating": 3.0,
  "like_count": 4,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/279"
 },
 {
  "song_id": 134,
  "title": "Lost in a Sea of Echoes",
  "album_id": null,
  "duration": 224,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "release_date": "2021-05-28T14:23:11",
  "genre": "rock",
  "play_count": 385,
  "rating": 0.0,
  "like_count": 7,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/134"
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
  "song_id": 321,
  "title": "Drowning in a Sea of Regret",
  "album_id": null,
  "duration": 209,
  "artists": [
   {
    "id": 36,
    "name": "Noah Bennett"
   }
  ],
  "release_date": "2021-09-06T10:21:37",
  "genre": "indie",
  "play_count": 838,
  "rating": 0.0,
  "like_count": 2,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/321"
 },
 {
  "song_id": 317,
  "title": "Trapped in a Daydream",
  "album_id": null,
  "duration": 225,
  "artists": [
   {
    "id": 35,
    "name": "Nova Harmony"
   }
  ],
  "release_date": "2021-04-27T06:17:23",
  "genre": "indie",
  "play_count": 731,
  "rating": 2.0,
  "like_count": 8,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/317"
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
 }
]
```


### Environment Interaction 31
----------------------------------------------------------------------------
```python
# Search for the next song: Gone Astray by Aria Sterling
search5 = apis.spotify.search_songs(query="Gone Astray Aria Sterling", access_token=login_result["access_token"], page_limit=20)
print(search5)
```

```
[
 {
  "song_id": 41,
  "title": "Gone Astray",
  "album_id": 8,
  "duration": 281,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2021-06-10T10:41:47",
  "genre": "jazz",
  "play_count": 629,
  "rating": 0.0,
  "like_count": 15,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/41"
 },
 {
  "song_id": 45,
  "title": "Eclipsed",
  "album_id": 9,
  "duration": 267,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2022-09-27T00:38:12",
  "genre": "jazz",
  "play_count": 713,
  "rating": 0.0,
  "like_count": 14,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/45"
 },
 {
  "song_id": 37,
  "title": "Endless Roads",
  "album_id": 8,
  "duration": 268,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2021-06-10T10:41:47",
  "genre": "jazz",
  "play_count": 379,
  "rating": 3.0,
  "like_count": 9,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/37"
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
  "release_date": "2022-11-11T09:54:16",
  "genre": "jazz",
  "play_count": 316,
  "rating": 3.0,
  "like_count": 14,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/50"
 },
 {
  "song_id": 52,
  "title": "Bleeding Sun",
  "album_id": 10,
  "duration": 225,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2022-11-11T09:54:16",
  "genre": "jazz",
  "play_count": 648,
  "rating": 0.0,
  "like_count": 18,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/52"
 },
 {
  "song_id": 53,
  "title": "Unearthed Secrets",
  "album_id": 10,
  "duration": 231,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2022-11-11T09:54:16",
  "genre": "jazz",
  "play_count": 648,
  "rating": 2.0,
  "like_count": 9,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/53"
 },
 {
  "song_id": 124,
  "title": "Drowning Sorrows",
  "album_id": null,
  "duration": 241,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2022-07-16T12:24:44",
  "genre": "jazz",
  "play_count": 316,
  "rating": 3.0,
  "like_count": 2,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/124"
 },
 {
  "song_id": 127,
  "title": "Mystic Rhythms",
  "album_id": null,
  "duration": 219,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2020-04-13T07:10:31",
  "genre": "jazz",
  "play_count": 463,
  "rating": 0.0,
  "like_count": 2,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/127"
 },
 {
  "song_id": 128,
  "title": "Silent Sorrow",
  "album_id": null,
  "duration": 297,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2020-03-08T02:26:07",
  "genre": "jazz",
  "play_count": 842,
  "rating": 4.3,
  "like_count": 6,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/128"
 },
 {
  "song_id": 129,
  "title": "Moonlit Sighs",
  "album_id": null,
  "duration": 271,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2021-01-29T03:27:42",
  "genre": "jazz",
  "play_count": 778,
  "rating": 0.0,
  "like_count": 9,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/129"
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
  "song_id": 38,
  "title": "Destiny's Game",
  "album_id": 8,
  "duration": 256,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2021-06-10T10:41:47",
  "genre": "jazz",
  "play_count": 178,
  "rating": 2.0,
  "like_count": 6,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/38"
 },
 {
  "song_id": 43,
  "title": "Whispers of Destiny",
  "album_id": 8,
  "duration": 298,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2021-06-10T10:41:47",
  "genre": "jazz",
  "play_count": 433,
  "rating": 2.5,
  "like_count": 18,
  "review_count": 2,
  "shareable_link": "https://spotify.com/songs/43"
 },
 {
  "song_id": 47,
  "title": "Time's Hold",
  "album_id": 10,
  "duration": 269,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2022-11-11T09:54:16",
  "genre": "jazz",
  "play_count": 279,
  "rating": 0.0,
  "like_count": 17,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/47"
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
  "release_date": "2022-11-11T09:54:16",
  "genre": "jazz",
  "play_count": 314,
  "rating": 3.0,
  "like_count": 16,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/48"
 },
 {
  "song_id": 125,
  "title": "Heart's Abyss",
  "album_id": null,
  "duration": 189,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2023-01-12T06:12:23",
  "genre": "jazz",
  "play_count": 681,
  "rating": 3.0,
  "like_count": 8,
  "review_count": 3,
  "shareable_link": "https://spotify.com/songs/125"
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
  "song_id": 51,
  "title": "The Silence Between Us",
  "album_id": 10,
  "duration": 272,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2022-11-11T09:54:16",
  "genre": "jazz",
  "play_count": 991,
  "rating": 0.0,
  "like_count": 16,
  "review_count": 0,
  "shareable_link": "https://spotify.com/songs/51"
 },
 {
  "song_id": 123,
  "title": "Between Reality and Reverie",
  "album_id": null,
  "duration": 208,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "release_date": "2020-03-16T09:11:14",
  "genre": "jazz",
  "play_count": 826,
  "rating": 5.0,
  "like_count": 5,
  "review_count": 1,
  "shareable_link": "https://spotify.com/songs/123"
 }
]
```

