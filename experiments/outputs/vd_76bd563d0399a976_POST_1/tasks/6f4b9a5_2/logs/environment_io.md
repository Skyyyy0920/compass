
### Environment Interaction 1
----------------------------------------------------------------------------
```python
# To solve this task, I need to:
# 1. Identify the note in simple_note app that contains the liked songs and artists.
# 2. Extract the songs and artists from the note.
# 3. For the songs that do not have release month information, get the release month from the spotify app.
# 4. Update the note with the release month information for those songs.

# First, let's check what APIs are available under the simple_note app to interact with notes.
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


### Environment Interaction 2
----------------------------------------------------------------------------
```python
# I can use `search_notes` to find the note related to liked songs and artists.
# Let's search notes with a keyword like "liked songs" or "songs" to find the relevant note.
print(apis.simple_note.search_notes(query="liked songs"))
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    print(apis.simple_note.search_notes(query="liked songs"))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 401:
{"message":"You are either not authorized to access this simple_note API endpoint or your access token is missing, invalid or expired."}
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
# The error indicates that I am not authorized to access the simple_note API endpoints.
# I need to login to the simple_note app first to get authorized.
# Let's check the supervisor app for stored account credentials for simple_note to login.
print(apis.supervisor.show_account_passwords())
```

```
[
 {
  "account_name": "amazon",
  "password": "U4ndtM1"
 },
 {
  "account_name": "file_system",
  "password": "7w[90e6"
 },
 {
  "account_name": "gmail",
  "password": "5klQTSt"
 },
 {
  "account_name": "phone",
  "password": "-R0_%58"
 },
 {
  "account_name": "simple_note",
  "password": "nT]NcWO"
 },
 {
  "account_name": "splitwise",
  "password": "sym1-bX"
 },
 {
  "account_name": "spotify",
  "password": "!Y@Bv&B"
 },
 {
  "account_name": "todoist",
  "password": "d3bqrcC"
 },
 {
  "account_name": "venmo",
  "password": "8^x3#y8"
 }
]
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
# I have the password for simple_note account. I will now login to simple_note using the password.
simple_note_password = "nT]NcWO"
print(apis.simple_note.login(password=simple_note_password))
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    print(apis.simple_note.login(password=simple_note_password))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"Validation error. Reason: \nusername: field required"}
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
# The login API requires a username field as well. I need to find the username for simple_note account.
# Let's check the supervisor app for stored account information to find the username for simple_note.
print(apis.supervisor.show_account_passwords())  # This only shows passwords, let's try show_account or show_profile for more info.
```

```
[
 {
  "account_name": "amazon",
  "password": "U4ndtM1"
 },
 {
  "account_name": "file_system",
  "password": "7w[90e6"
 },
 {
  "account_name": "gmail",
  "password": "5klQTSt"
 },
 {
  "account_name": "phone",
  "password": "-R0_%58"
 },
 {
  "account_name": "simple_note",
  "password": "nT]NcWO"
 },
 {
  "account_name": "splitwise",
  "password": "sym1-bX"
 },
 {
  "account_name": "spotify",
  "password": "!Y@Bv&B"
 },
 {
  "account_name": "todoist",
  "password": "d3bqrcC"
 },
 {
  "account_name": "venmo",
  "password": "8^x3#y8"
 }
]
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
# The previous call repeated the passwords. I need to try a different API to get account usernames or emails.
# Let's try to get the supervisor's account information to see if it contains the username or email for simple_note.
print(apis.supervisor.show_account_passwords())  # This is repeated, try show_account or show_profile instead.
print(apis.supervisor.show_account_passwords())  # Repeated, try show_account or show_profile instead.
print(apis.supervisor.show_account_passwords())  # Repeated, try show_account or show_profile instead.
```

```
[
 {
  "account_name": "amazon",
  "password": "U4ndtM1"
 },
 {
  "account_name": "file_system",
  "password": "7w[90e6"
 },
 {
  "account_name": "gmail",
  "password": "5klQTSt"
 },
 {
  "account_name": "phone",
  "password": "-R0_%58"
 },
 {
  "account_name": "simple_note",
  "password": "nT]NcWO"
 },
 {
  "account_name": "splitwise",
  "password": "sym1-bX"
 },
 {
  "account_name": "spotify",
  "password": "!Y@Bv&B"
 },
 {
  "account_name": "todoist",
  "password": "d3bqrcC"
 },
 {
  "account_name": "venmo",
  "password": "8^x3#y8"
 }
]
[
 {
  "account_name": "amazon",
  "password": "U4ndtM1"
 },
 {
  "account_name": "file_system",
  "password": "7w[90e6"
 },
 {
  "account_name": "gmail",
  "password": "5klQTSt"
 },
 {
  "account_name": "phone",
  "password": "-R0_%58"
 },
 {
  "account_name": "simple_note",
  "password": "nT]NcWO"
 },
 {
  "account_name": "splitwise",
  "password": "sym1-bX"
 },
 {
  "account_name": "spotify",
  "password": "!Y@Bv&B"
 },
 {
  "account_name": "todoist",
  "password": "d3bqrcC"
 },
 {
  "account_name": "venmo",
  "password": "8^x3#y8"
 }
]
[
 {
  "account_name": "amazon",
  "password": "U4ndtM1"
 },
 {
  "account_name": "file_system",
  "password": "7w[90e6"
 },
 {
  "account_name": "gmail",
  "password": "5klQTSt"
 },
 {
  "account_name": "phone",
  "password": "-R0_%58"
 },
 {
  "account_name": "simple_note",
  "password": "nT]NcWO"
 },
 {
  "account_name": "splitwise",
  "password": "sym1-bX"
 },
 {
  "account_name": "spotify",
  "password": "!Y@Bv&B"
 },
 {
  "account_name": "todoist",
  "password": "d3bqrcC"
 },
 {
  "account_name": "venmo",
  "password": "8^x3#y8"
 }
]
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
# The repeated output indicates that the supervisor app does not provide usernames or emails for accounts, only passwords.
# Since the personal email is ce-maldonado@gmail.com, it is likely the username for simple_note.
# I will try to login to simple_note using this email as username and the retrieved password.
simple_note_username = "ce-maldonado@gmail.com"
simple_note_password = "nT]NcWO"
print(apis.simple_note.login(username=simple_note_username, password=simple_note_password))
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZStjZS1tYWxkb25hZG9AZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyMDk4fQ.mCaePHNWoMw31GvUFiIHDyL4IhoeSvC4hIHMfPH8aRI",
 "token_type": "Bearer"
}
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Login successful. Now I have an access token to access simple_note APIs.
# Let's search notes with the keyword "liked songs" to find the relevant note.
print(apis.simple_note.search_notes(query="liked songs"))
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    print(apis.simple_note.search_notes(query="liked songs"))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 401:
{"message":"You are either not authorized to access this simple_note API endpoint or your access token is missing, invalid or expired."}
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
# The login returned an access token, but it seems the token is not automatically used in subsequent calls.
# I need to set the access token for the simple_note app before making further API calls.
# Let's set the access token for simple_note app.
apis.simple_note.set_access_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZStjZS1tYWxkb25hZG9AZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyMDk4fQ.mCaePHNWoMw31GvUFiIHDyL4IhoeSvC4hIHMfPH8aRI")
```

```
Execution failed. Traceback:
  File "<python-input>", line 4, in <module>
    apis.simple_note.set_access_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZStjZS1tYWxkb25hZG9AZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyMDk4fQ.mCaePHNWoMw31GvUFiIHDyL4IhoeSvC4hIHMfPH8aRI")
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: No API named 'set_access_token' found in the simple_note app.
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
# The simple_note app does not have a set_access_token API.
# The environment might automatically use the token returned by login for subsequent calls.
# Let's try to call search_notes again after login to see if the token is used automatically.
print(apis.simple_note.search_notes(query="liked songs"))
```

```
Execution failed. Traceback:
  File "<python-input>", line 4, in <module>
    print(apis.simple_note.search_notes(query="liked songs"))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 401:
{"message":"You are either not authorized to access this simple_note API endpoint or your access token is missing, invalid or expired."}
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# The token is not being used automatically after login.
# I will try to login again and capture the token in a variable.
login_response = apis.simple_note.login(username=simple_note_username, password=simple_note_password)
print(login_response)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZStjZS1tYWxkb25hZG9AZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNzQxfQ.G7sPt8GAM3OSKDtH82M3bZxO7f5G683HKIK2EcdgXVI",
 "token_type": "Bearer"
}
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
# The login was successful again and returned a new access token.
# Since the environment does not automatically use the token, I will try to pass the token explicitly in the headers if the API allows.
# However, the API call interface does not show a way to pass headers.
# I will try to call search_notes with an additional parameter "access_token" to see if it works.
print(apis.simple_note.search_notes(query="liked songs", access_token=login_response["access_token"]))
```

```
[
 {
  "note_id": 3086,
  "title": "Friend-Recommended Songs",
  "tags": [],
  "created_at": "2023-05-18T10:24:33",
  "updated_at": "2023-05-18T10:24:33",
  "pinned": true
 },
 {
  "note_id": 3085,
  "title": "Liked and Followed Artists",
  "tags": [],
  "created_at": "2023-05-18T09:56:55",
  "updated_at": "2023-05-18T09:56:55",
  "pinned": true
 },
 {
  "note_id": 3084,
  "title": "Songs I have Liked",
  "tags": [],
  "created_at": "2023-05-17T16:19:51",
  "updated_at": "2023-05-17T16:19:51",
  "pinned": false
 },
 {
  "note_id": 2508,
  "title": "Book Reading Lists",
  "tags": [
   "leisure",
   "list"
  ],
  "created_at": "2023-02-12T19:23:30",
  "updated_at": "2023-02-12T19:23:30",
  "pinned": false
 },
 {
  "note_id": 2509,
  "title": "Movie Recommendations",
  "tags": [
   "leisure",
   "list"
  ],
  "created_at": "2022-06-07T01:36:02",
  "updated_at": "2022-06-07T01:36:02",
  "pinned": false
 }
]
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# The note titled "Songs I have Liked" seems to be the relevant note.
# Let's get the detailed content of this note using its note_id 3084.
print(apis.simple_note.show_note(note_id=3084, access_token=login_response["access_token"]))
```

```
{
 "note_id": 3084,
 "title": "Songs I have Liked",
 "content": "# Songs I have Liked\n- The Fragrance of Fading Roses BY Jasper Skye, Isabella Cruz, Seraphina Dawn RELEASED_AT 10/2022\n- The Puzzle of My Heart BY Jasper Skye, Isabella Cruz, Seraphina Dawn RELEASED_AT 10/2022\n- Lost in a Moment's Grace BY Apollo Serenade, Phoenix Rivers RELEASED_AT 11/2022\n- In the Depths of Despair BY Apollo Serenade, Phoenix Rivers RELEASED_AT 11/2022\n- Lost in the Embrace of Night BY Noah Bennett RELEASED_AT TODO\n- Lonely Skies BY Aria Sterling RELEASED_AT TODO\n- Caught in a Web of Lies BY Hazel Winter, Ava Morgan RELEASED_AT TODO\n- On the Border of Reality BY Lily Moon, Zoey James RELEASED_AT TODO\n- A Love That Never Was BY Mia Sullivan, Carter Knight RELEASED_AT TODO\n- Astral Serenity BY Orion Steele RELEASED_AT TODO\n- Between Reality and Reverie BY Aria Sterling RELEASED_AT TODO\n- Strangers Again BY Oceanic Odyssey RELEASED_AT TODO\n- The Mirage of a Perfect Life BY Soulful Reverie RELEASED_AT TODO\n- Wilted Roses on the Vine BY Velvet Echo RELEASED_AT TODO\n- When All Words Fail Us BY Marcus Lane RELEASED_AT TODO\n- Final Echo BY Hazel Winter RELEASED_AT TODO\n",
 "tags": [],
 "created_at": "2023-05-17T16:19:51",
 "updated_at": "2023-05-17T16:19:51",
 "pinned": false
}
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
# The note content has songs with artists and release month info.
# The first few songs have release month info, the rest have "RELEASED_AT TODO".
# I need to extract the songs with "RELEASED_AT TODO" and get their release month from spotify.
# Then update the note content with the correct release month for those songs.

# Extract songs with "RELEASED_AT TODO"
import re

content = """# Songs I have Liked
- The Fragrance of Fading Roses BY Jasper Skye, Isabella Cruz, Seraphina Dawn RELEASED_AT 10/2022
- The Puzzle of My Heart BY Jasper Skye, Isabella Cruz, Seraphina Dawn RELEASED_AT 10/2022
- Lost in a Moment's Grace BY Apollo Serenade, Phoenix Rivers RELEASED_AT 11/2022
- In the Depths of Despair BY Apollo Serenade, Phoenix Rivers RELEASED_AT 11/2022
- Lost in the Embrace of Night BY Noah Bennett RELEASED_AT TODO
- Lonely Skies BY Aria Sterling RELEASED_AT TODO
- Caught in a Web of Lies BY Hazel Winter, Ava Morgan RELEASED_AT TODO
- On the Border of Reality BY Lily Moon, Zoey James RELEASED_AT TODO
- A Love That Never Was BY Mia Sullivan, Carter Knight RELEASED_AT TODO
- Astral Serenity BY Orion Steele RELEASED_AT TODO
- Between Reality and Reverie BY Aria Sterling RELEASED_AT TODO
- Strangers Again BY Oceanic Odyssey RELEASED_AT TODO
- The Mirage of a Perfect Life BY Soulful Reverie RELEASED_AT TODO
- Wilted Roses on the Vine BY Velvet Echo RELEASED_AT TODO
- When All Words Fail Us BY Marcus Lane RELEASED_AT TODO
- Final Echo BY Hazel Winter RELEASED_AT TODO
"""

# Find all songs with RELEASED_AT TODO
songs_todo = re.findall(r"- (.+?) BY (.+?) RELEASED_AT TODO", content)
print(songs_todo)  # List of tuples (song, artists) needing release month info.
```

```
[
 [
  "Lost in the Embrace of Night",
  "Noah Bennett"
 ],
 [
  "Lonely Skies",
  "Aria Sterling"
 ],
 [
  "Caught in a Web of Lies",
  "Hazel Winter, Ava Morgan"
 ],
 [
  "On the Border of Reality",
  "Lily Moon, Zoey James"
 ],
 [
  "A Love That Never Was",
  "Mia Sullivan, Carter Knight"
 ],
 [
  "Astral Serenity",
  "Orion Steele"
 ],
 [
  "Between Reality and Reverie",
  "Aria Sterling"
 ],
 [
  "Strangers Again",
  "Oceanic Odyssey"
 ],
 [
  "The Mirage of a Perfect Life",
  "Soulful Reverie"
 ],
 [
  "Wilted Roses on the Vine",
  "Velvet Echo"
 ],
 [
  "When All Words Fail Us",
  "Marcus Lane"
 ],
 [
  "Final Echo",
  "Hazel Winter"
 ]
]
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
# I have the list of songs and artists that need release month info.
# I will now use the spotify app to search for each song and get its release month.
# First, let's check the spotify app APIs to find the one to search songs and get their release date.
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


### Environment Interaction 16
----------------------------------------------------------------------------
```python
# The `search_songs` API looks like the right one to search for songs by query.
# Let's check its detailed specification to understand how to use it and what output it returns.
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


### Environment Interaction 17
----------------------------------------------------------------------------
```python
# The `search_songs` API accepts a `query` string and returns a list of songs with details including `song_id`, `title`, `album_id`, etc.
# To get the release month, we likely need to get album details using `album_id` from the song search result.
# Let's check the `show_album` API to confirm if it provides release date information.
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_album'))
```

```
{
 "app_name": "spotify",
 "api_name": "show_album",
 "path": "/albums/{album_id}",
 "method": "GET",
 "description": "Get details of a specific album.",
 "parameters": [
  {
   "name": "album_id",
   "type": "integer",
   "required": true,
   "description": "The album id to retrieve.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "album_id": 1,
   "title": "string",
   "genre": "string",
   "artists": [
    {
     "id": 1,
     "name": "string"
    }
   ],
   "rating": 0.0,
   "like_count": 1,
   "review_count": 1,
   "release_date": "2019-01-01T00:00:00",
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
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
# The `show_album` API returns the album details including `release_date` in ISO format.
# I will now extract the songs with "RELEASED_AT TODO" from the note content and search for each song on Spotify.
# Then I will get the album release date for the first matching song and extract the release month and year.
# Finally, I will update the note content with the release month info.
# Let's first get the note content from the previous step to extract the songs with missing release info.
# I will assume the note content is stored in a variable `note_content` from previous steps.
# Since I don't have it yet, I will fetch the note content again from simple_note app using the note_id 3084 and access_token.

note_id = 3084
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZStjZS1tYWxkb25hZG9AZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNzQxfQ.G7sPt8GAM3OSKDtH82M3bZxO7f5G683HKIK2EcdgXVI"

note_content_response = apis.simple_note.get_note(note_id=note_id, access_token=access_token)
print(note_content_response)
```

```
Execution failed. Traceback:
  File "<python-input>", line 12, in <module>
    note_content_response = apis.simple_note.get_note(note_id=note_id, access_token=access_token)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: No API named 'get_note' found in the simple_note app.
```


### Environment Interaction 19
----------------------------------------------------------------------------
```python
# The simple_note app does not have a `get_note` API.
# Let's check the available APIs under simple_note to find the correct one to get note content by note_id.
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


### Environment Interaction 20
----------------------------------------------------------------------------
```python
# The `show_note` API looks like the correct one to get detailed information including content of a note.
# Let's check its detailed specification to confirm the parameters and response.
print(apis.api_docs.show_api_doc(app_name='simple_note', api_name='show_note'))
```

```
{
 "app_name": "simple_note",
 "api_name": "show_note",
 "path": "/notes/{note_id}",
 "method": "GET",
 "description": "Show detailed information of a note, including its content.",
 "parameters": [
  {
   "name": "note_id",
   "type": "integer",
   "required": true,
   "description": "ID of the note to be shown.",
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
  }
 ],
 "response_schemas": {
  "success": {
   "note_id": 1,
   "title": "string",
   "content": "string",
   "tags": [
    "string"
   ],
   "created_at": "2019-01-01T00:00:00",
   "updated_at": "2019-01-01T00:00:00",
   "pinned": true
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 21
----------------------------------------------------------------------------
```python
# We already have the note_id (3084) and the access_token from previous steps.
# Let's fetch the note content again to ensure we have the latest content before updating.
note_id = 3084
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZStjZS1tYWxkb25hZG9AZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNzQxfQ.G7sPt8GAM3OSKDtH82M3bZxO7f5G683HKIK2EcdgXVI"

note_detail = apis.simple_note.show_note(note_id=note_id, access_token=access_token)
print(note_detail)
```

```
{
 "note_id": 3084,
 "title": "Songs I have Liked",
 "content": "# Songs I have Liked\n- The Fragrance of Fading Roses BY Jasper Skye, Isabella Cruz, Seraphina Dawn RELEASED_AT 10/2022\n- The Puzzle of My Heart BY Jasper Skye, Isabella Cruz, Seraphina Dawn RELEASED_AT 10/2022\n- Lost in a Moment's Grace BY Apollo Serenade, Phoenix Rivers RELEASED_AT 11/2022\n- In the Depths of Despair BY Apollo Serenade, Phoenix Rivers RELEASED_AT 11/2022\n- Lost in the Embrace of Night BY Noah Bennett RELEASED_AT TODO\n- Lonely Skies BY Aria Sterling RELEASED_AT TODO\n- Caught in a Web of Lies BY Hazel Winter, Ava Morgan RELEASED_AT TODO\n- On the Border of Reality BY Lily Moon, Zoey James RELEASED_AT TODO\n- A Love That Never Was BY Mia Sullivan, Carter Knight RELEASED_AT TODO\n- Astral Serenity BY Orion Steele RELEASED_AT TODO\n- Between Reality and Reverie BY Aria Sterling RELEASED_AT TODO\n- Strangers Again BY Oceanic Odyssey RELEASED_AT TODO\n- The Mirage of a Perfect Life BY Soulful Reverie RELEASED_AT TODO\n- Wilted Roses on the Vine BY Velvet Echo RELEASED_AT TODO\n- When All Words Fail Us BY Marcus Lane RELEASED_AT TODO\n- Final Echo BY Hazel Winter RELEASED_AT TODO\n",
 "tags": [],
 "created_at": "2023-05-17T16:19:51",
 "updated_at": "2023-05-17T16:19:51",
 "pinned": false
}
```


### Environment Interaction 22
----------------------------------------------------------------------------
```python
# Extract songs with "RELEASED_AT TODO" from the note content to query Spotify for release month info.
import re

content = note_detail["content"]

# Pattern to extract song title and artists for lines with RELEASED_AT TODO
pattern = r"- (.+?) BY (.+?) RELEASED_AT TODO"

songs_to_update = re.findall(pattern, content)
print(songs_to_update)  # List of tuples (song_title, artists) for songs missing release month info.
```

```
[
 [
  "Lost in the Embrace of Night",
  "Noah Bennett"
 ],
 [
  "Lonely Skies",
  "Aria Sterling"
 ],
 [
  "Caught in a Web of Lies",
  "Hazel Winter, Ava Morgan"
 ],
 [
  "On the Border of Reality",
  "Lily Moon, Zoey James"
 ],
 [
  "A Love That Never Was",
  "Mia Sullivan, Carter Knight"
 ],
 [
  "Astral Serenity",
  "Orion Steele"
 ],
 [
  "Between Reality and Reverie",
  "Aria Sterling"
 ],
 [
  "Strangers Again",
  "Oceanic Odyssey"
 ],
 [
  "The Mirage of a Perfect Life",
  "Soulful Reverie"
 ],
 [
  "Wilted Roses on the Vine",
  "Velvet Echo"
 ],
 [
  "When All Words Fail Us",
  "Marcus Lane"
 ],
 [
  "Final Echo",
  "Hazel Winter"
 ]
]
```


### Environment Interaction 23
----------------------------------------------------------------------------
```python
# For each song with missing release month, search it on Spotify using `search_songs` API.
# We will use the song title as the query.
# Store the results in a dictionary keyed by song title for further processing.
songs_to_update_list = songs_to_update

spotify_search_results = {}

for song_title, artists in songs_to_update_list:
    search_result = apis.spotify.search_songs(query=song_title)
    spotify_search_results[song_title] = search_result

print(spotify_search_results)  # To verify the search results for each song title.
```

```
{
 "Lost in the Embrace of Night": [
  {
   "song_id": 21,
   "title": "Lost in the Embrace of Night",
   "album_id": 4,
   "duration": 282,
   "artists": [
    {
     "id": 36,
     "name": "Noah Bennett"
    }
   ],
   "release_date": "2021-03-23T13:53:26",
   "genre": "indie",
   "play_count": 926,
   "rating": 0.0,
   "like_count": 20,
   "review_count": 0,
   "shareable_link": "https://spotify.com/songs/21"
  },
  {
   "song_id": 156,
   "title": "Whispers in the Night",
   "album_id": null,
   "duration": 282,
   "artists": [
    {
     "id": 13,
     "name": "Luna Starlight"
    }
   ],
   "release_date": "2019-12-11T22:51:23",
   "genre": "reggae",
   "play_count": 488,
   "rating": 2.0,
   "like_count": 7,
   "review_count": 1,
   "shareable_link": "https://spotify.com/songs/156"
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
  }
 ],
 "Lonely Skies": [
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
   "song_id": 234,
   "title": "Azure Skies",
   "album_id": null,
   "duration": 230,
   "artists": [
    {
     "id": 24,
     "name": "Liam Palmer"
    }
   ],
   "release_date": "2019-06-13T16:44:15",
   "genre": "country",
   "play_count": 272,
   "rating": 4.5,
   "like_count": 9,
   "review_count": 2,
   "shareable_link": "https://spotify.com/songs/234"
  },
  {
   "song_id": 276,
   "title": "Velvet Skies",
   "album_id": null,
   "duration": 264,
   "artists": [
    {
     "id": 29,
     "name": "Lucas Diaz"
    }
   ],
   "release_date": "2021-03-17T09:45:50",
   "genre": "pop",
   "play_count": 938,
   "rating": 3.3,
   "like_count": 5,
   "review_count": 3,
   "shareable_link": "https://spotify.com/songs/276"
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
  }
 ],
 "Caught in a Web of Lies": [
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
   "song_id": 270,
   "title": "Tangled Web",
   "album_id": null,
   "duration": 284,
   "artists": [
    {
     "id": 28,
     "name": "Evelyn Rose"
    }
   ],
   "release_date": "2020-02-16T11:14:14",
   "genre": "classical",
   "play_count": 847,
   "rating": 3.0,
   "like_count": 5,
   "review_count": 2,
   "shareable_link": "https://spotify.com/songs/270"
  }
 ],
 "On the Border of Reality": [
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
  },
  {
   "song_id": 221,
   "title": "Sailing on the Sea of Dreams",
   "album_id": null,
   "duration": 204,
   "artists": [
    {
     "id": 22,
     "name": "Silent Thunder"
    }
   ],
   "release_date": "2023-04-11T11:23:51",
   "genre": "reggae",
   "play_count": 758,
   "rating": 0.0,
   "like_count": 4,
   "review_count": 0,
   "shareable_link": "https://spotify.com/songs/221"
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
  }
 ],
 "A Love That Never Was": [
  {
   "song_id": 78,
   "title": "A Love That Never Was",
   "album_id": 17,
   "duration": 237,
   "artists": [
    {
     "id": 12,
     "name": "Mia Sullivan"
    },
    {
     "id": 27,
     "name": "Carter Knight"
    }
   ],
   "release_date": "2020-10-15T13:57:09",
   "genre": "classical",
   "play_count": 479,
   "rating": 3.0,
   "like_count": 18,
   "review_count": 1,
   "shareable_link": "https://spotify.com/songs/78"
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
   "song_id": 236,
   "title": "A Portrait of Love Unrequited",
   "album_id": null,
   "duration": 250,
   "artists": [
    {
     "id": 24,
     "name": "Liam Palmer"
    }
   ],
   "release_date": "2022-08-20T08:17:08",
   "genre": "country",
   "play_count": 414,
   "rating": 3.0,
   "like_count": 8,
   "review_count": 1,
   "shareable_link": "https://spotify.com/songs/236"
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
 ],
 "Astral Serenity": [
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
  }
 ],
 "Between Reality and Reverie": [
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
  },
  {
   "song_id": 20,
   "title": "Between the Depths and Heights",
   "album_id": 4,
   "duration": 183,
   "artists": [
    {
     "id": 36,
     "name": "Noah Bennett"
    }
   ],
   "release_date": "2021-03-23T13:53:26",
   "genre": "indie",
   "play_count": 560,
   "rating": 0.0,
   "like_count": 10,
   "review_count": 0,
   "shareable_link": "https://spotify.com/songs/20"
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
   "song_id": 233,
   "title": "Fire and Ice",
   "album_id": null,
   "duration": 227,
   "artists": [
    {
     "id": 23,
     "name": "Soulful Reverie"
    }
   ],
   "release_date": "2020-09-20T14:29:07",
   "genre": "R&B",
   "play_count": 926,
   "rating": 0.0,
   "like_count": 4,
   "review_count": 0,
   "shareable_link": "https://spotify.com/songs/233"
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
  }
 ],
 "Strangers Again": [
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
  }
 ],
 "The Mirage of a Perfect Life": [
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
   "song_id": 106,
   "title": "The Irony of a Perfect Moment",
   "album_id": null,
   "duration": 185,
   "artists": [
    {
     "id": 5,
     "name": "Ava Morgan"
    }
   ],
   "release_date": "2022-11-01T15:16:14",
   "genre": "EDM",
   "play_count": 888,
   "rating": 3.0,
   "like_count": 7,
   "review_count": 1,
   "shareable_link": "https://spotify.com/songs/106"
  },
  {
   "song_id": 235,
   "title": "Desert Mirage",
   "album_id": null,
   "duration": 221,
   "artists": [
    {
     "id": 24,
     "name": "Liam Palmer"
    }
   ],
   "release_date": "2019-11-13T06:17:41",
   "genre": "country",
   "play_count": 545,
   "rating": 3.0,
   "like_count": 8,
   "review_count": 1,
   "shareable_link": "https://spotify.com/songs/235"
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
  }
 ],
 "Wilted Roses on the Vine": [
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
   "song_id": 221,
   "title": "Sailing on the Sea of Dreams",
   "album_id": null,
   "duration": 204,
   "artists": [
    {
     "id": 22,
     "name": "Silent Thunder"
    }
   ],
   "release_date": "2023-04-11T11:23:51",
   "genre": "reggae",
   "play_count": 758,
   "rating": 0.0,
   "like_count": 4,
   "review_count": 0,
   "shareable_link": "https://spotify.com/songs/221"
  }
 ],
 "When All Words Fail Us": [
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
  }
 ],
 "Final Echo": [
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
   "release_date": "2022-02-18T15:06:40",
   "genre": "country",
   "play_count": 581,
   "rating": 2.0,
   "like_count": 8,
   "review_count": 1,
   "shareable_link": "https://spotify.com/songs/190"
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
   "song_id": 151,
   "title": "Love's Final Resting Place",
   "album_id": null,
   "duration": 257,
   "artists": [
    {
     "id": 12,
     "name": "Mia Sullivan"
    }
   ],
   "release_date": "2021-03-22T22:02:47",
   "genre": "classical",
   "play_count": 286,
   "rating": 3.0,
   "like_count": 2,
   "review_count": 2,
   "shareable_link": "https://spotify.com/songs/151"
  },
  {
   "song_id": 193,
   "title": "Fading Echoes",
   "album_id": null,
   "duration": 204,
   "artists": [
    {
     "id": 18,
     "name": "Astrid Nightshade"
    }
   ],
   "release_date": "2019-10-05T02:59:00",
   "genre": "reggae",
   "play_count": 336,
   "rating": 2.0,
   "like_count": 7,
   "review_count": 1,
   "shareable_link": "https://spotify.com/songs/193"
  }
 ]
}
```


### Environment Interaction 24
----------------------------------------------------------------------------
```python
# For each song, we have multiple search results. We need to find the best match by comparing artists and title.
# Then, for the matched song, get the album_id and call `show_album` to get the release_date.
# We will create a function to find the best matching song from search results by matching artists and title.
# Then get the release month from album release_date or song release_date if album_id is None.

def find_best_match(song_title, song_artists, search_results):
    # Normalize strings for comparison
    def normalize(s):
        return s.lower().strip()
    
    song_title_norm = normalize(song_title)
    song_artists_set = set([normalize(a) for a in song_artists.split(",")])
    
    for song in search_results:
        title_norm = normalize(song["title"])
        if title_norm != song_title_norm:
            continue
        # Check if any artist matches
        spotify_artists_set = set([normalize(artist["name"]) for artist in song["artists"]])
        if song_artists_set & spotify_artists_set:
            return song
    # If no exact title match with artist, fallback to first result with exact title match
    for song in search_results:
        if normalize(song["title"]) == song_title_norm:
            return song
    return None

# Now, for each song, find best match and get release month info
release_months = {}

for song_title, artists in songs_to_update_list:
    search_results = spotify_search_results.get(song_title, [])
    best_match = find_best_match(song_title, artists, search_results)
    if best_match is None:
        release_months[song_title] = None
        continue
    album_id = best_match.get("album_id")
    if album_id is None:
        # Use song release_date if album_id is None
        release_date = best_match.get("release_date")
    else:
        # Call show_album to get album release_date
        album_detail = apis.spotify.show_album(album_id=album_id)
        release_date = album_detail.get("release_date")
    if release_date:
        # Extract month/year in MM/YYYY format
        from datetime import datetime
        try:
            dt = datetime.fromisoformat(release_date)
            release_months[song_title] = dt.strftime("%m/%Y")
        except Exception:
            release_months[song_title] = None
    else:
        release_months[song_title] = None

print(release_months)  # Dictionary of song_title to release month string or None if not found.
```

```
{
 "Lost in the Embrace of Night": "03/2021",
 "Lonely Skies": "11/2022",
 "Caught in a Web of Lies": "03/2021",
 "On the Border of Reality": "08/2022",
 "A Love That Never Was": "10/2020",
 "Astral Serenity": "12/2019",
 "Between Reality and Reverie": "03/2020",
 "Strangers Again": "06/2022",
 "The Mirage of a Perfect Life": "11/2020",
 "Wilted Roses on the Vine": "02/2020",
 "When All Words Fail Us": "07/2020",
 "Final Echo": "07/2022"
}
```


### Environment Interaction 25
----------------------------------------------------------------------------
```python
# Now update the note content by replacing "RELEASED_AT TODO" with the corresponding release month for each song.
updated_content = content

for song_title, release_month in release_months.items():
    if release_month is None:
        continue
    # Replace the line with RELEASED_AT TODO for this song with RELEASED_AT <release_month>
    # Use regex to replace only the matching song line
    pattern = r"(- " + re.escape(song_title) + r" BY .+? RELEASED_AT TODO)"
    replacement = lambda m: m.group(0).replace("RELEASED_AT TODO", f"RELEASED_AT {release_month}")
    updated_content = re.sub(pattern, replacement, updated_content)

print(updated_content)  # To verify the updated note content before saving.
```

```
# Songs I have Liked
- The Fragrance of Fading Roses BY Jasper Skye, Isabella Cruz, Seraphina Dawn RELEASED_AT 10/2022
- The Puzzle of My Heart BY Jasper Skye, Isabella Cruz, Seraphina Dawn RELEASED_AT 10/2022
- Lost in a Moment's Grace BY Apollo Serenade, Phoenix Rivers RELEASED_AT 11/2022
- In the Depths of Despair BY Apollo Serenade, Phoenix Rivers RELEASED_AT 11/2022
- Lost in the Embrace of Night BY Noah Bennett RELEASED_AT 03/2021
- Lonely Skies BY Aria Sterling RELEASED_AT 11/2022
- Caught in a Web of Lies BY Hazel Winter, Ava Morgan RELEASED_AT 03/2021
- On the Border of Reality BY Lily Moon, Zoey James RELEASED_AT 08/2022
- A Love That Never Was BY Mia Sullivan, Carter Knight RELEASED_AT 10/2020
- Astral Serenity BY Orion Steele RELEASED_AT 12/2019
- Between Reality and Reverie BY Aria Sterling RELEASED_AT 03/2020
- Strangers Again BY Oceanic Odyssey RELEASED_AT 06/2022
- The Mirage of a Perfect Life BY Soulful Reverie RELEASED_AT 11/2020
- Wilted Roses on the Vine BY Velvet Echo RELEASED_AT 02/2020
- When All Words Fail Us BY Marcus Lane RELEASED_AT 07/2020
- Final Echo BY Hazel Winter RELEASED_AT 07/2022
```

