
### Environment Interaction 1
----------------------------------------------------------------------------
```python
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
print(apis.api_docs.show_api_descriptions(app_name='file_system'))
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
print(apis.api_docs.show_api_doc(app_name='file_system', api_name='show_directory'))
print(apis.api_docs.show_api_doc(app_name='simple_note', api_name='create_note'))
```

```
{
 "app_name": "file_system",
 "api_name": "show_directory",
 "path": "/directory",
 "method": "GET",
 "description": "Show a list of files and/or sub-directories, optionally recursively, in a directory.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from file_system app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "directory_path",
   "type": "string",
   "required": false,
   "description": "Path of the directory. Path can be absolute, starting with '/', or relative to the user's home directory, starting with '~/'.",
   "default": "/",
   "constraints": [
    "length >= 1"
   ]
  },
  {
   "name": "substring",
   "type": "string",
   "required": false,
   "description": "If passed, only files and sub-directories containing the given substring (ignoring case) will be shown.",
   "default": null,
   "constraints": []
  },
  {
   "name": "entry_type",
   "type": "string",
   "required": false,
   "description": "Whether to show all files and sub-directories, only files, or only sub-directories.",
   "default": "all",
   "constraints": [
    "value in ['all', 'files', 'directories']"
   ]
  },
  {
   "name": "recursive",
   "type": "boolean",
   "required": false,
   "description": "Whether to show files recursively.",
   "default": true,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   "string"
  ],
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "simple_note",
 "api_name": "create_note",
 "path": "/notes",
 "method": "POST",
 "description": "Create a new note.",
 "parameters": [
  {
   "name": "title",
   "type": "string",
   "required": true,
   "description": "Title of the note",
   "default": null,
   "constraints": [
    "length >= 1"
   ]
  },
  {
   "name": "content",
   "type": "string",
   "required": true,
   "description": "Content of the note",
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
   "name": "tags",
   "type": "list[string]",
   "required": false,
   "description": "Tags for the note.",
   "default": null,
   "constraints": []
  },
  {
   "name": "pinned",
   "type": "boolean",
   "required": false,
   "description": "Pinned status of the note.",
   "default": false,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string",
   "note_id": 1
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
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


### Environment Interaction 5
----------------------------------------------------------------------------
```python
passwords = apis.supervisor.show_account_passwords()
print(passwords)
```

```
[
 {
  "account_name": "amazon",
  "password": "QZy$N{l"
 },
 {
  "account_name": "file_system",
  "password": "z0pNZdK"
 },
 {
  "account_name": "gmail",
  "password": "(viQguu"
 },
 {
  "account_name": "phone",
  "password": "FiMwOzk"
 },
 {
  "account_name": "simple_note",
  "password": "=(4c-k0"
 },
 {
  "account_name": "splitwise",
  "password": "YJk6NuL"
 },
 {
  "account_name": "spotify",
  "password": "Bme[V91"
 },
 {
  "account_name": "todoist",
  "password": "MQ!CSVZ"
 },
 {
  "account_name": "venmo",
  "password": "J*(xh*P"
 }
]
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='file_system', api_name='login'))
print(apis.api_docs.show_api_doc(app_name='simple_note', api_name='login'))
```

```
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


### Environment Interaction 7
----------------------------------------------------------------------------
```python
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


### Environment Interaction 8
----------------------------------------------------------------------------
```python
print(apis.supervisor.show_profile())
```

```
{
 "first_name": "Adam",
 "last_name": "Blackburn",
 "email": "ad.blackburn@gmail.com",
 "phone_number": "8944155247",
 "birthday": "1979-11-13",
 "sex": "male"
}
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
file_system_login = apis.file_system.login(username='ad.blackburn@gmail.com', password='z0pNZdK')
print(file_system_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmaWxlX3N5c3RlbSthZC5ibGFja2J1cm5AZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyMDk4fQ.s7U9wjne6ShDPsxno0m7C8e9uI-dV_SirrlM-PON2Do",
 "token_type": "Bearer"
}
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
simple_note_login = apis.simple_note.login(username='ad.blackburn@gmail.com', password='=(4c-k0')
print(simple_note_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wbGVfbm90ZSthZC5ibGFja2J1cm5AZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNzQxfQ.5Shu7r2-iRUkHDNctqPsPH3ePgLvm7ZpfL321aSJHGQ",
 "token_type": "Bearer"
}
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
fs_token = file_system_login['access_token']
sn_token = simple_note_login['access_token']

# List files in the notes directory
files = apis.file_system.show_directory(access_token=fs_token, directory_path='~/documents/personal/notes/', entry_type='files')
print(files)
```

```
[
 "/home/adam/documents/personal/notes/Book_Reading_Lists.md",
 "/home/adam/documents/personal/notes/Food_Recipes.md",
 "/home/adam/documents/personal/notes/Funny_Quotes_Collection.md",
 "/home/adam/documents/personal/notes/Gift_Ideas_for_Various_Occasions.md",
 "/home/adam/documents/personal/notes/Grocery_List.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-04-30.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-01.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-02.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-03.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-04.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-05.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-06.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-07.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-08.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-09.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-10.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-11.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-12.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-13.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-14.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-15.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-16.md",
 "/home/adam/documents/personal/notes/Habit_Tracking_Log_for_2023-05-17.md",
 "/home/adam/documents/personal/notes/Inspirational_Quotes_Collection.md",
 "/home/adam/documents/personal/notes/Movie_Quotes_Collection.md",
 "/home/adam/documents/personal/notes/Movie_Recommendations.md",
 "/home/adam/documents/personal/notes/My_Bucket_List_([x]_=_done,_[_]_=_not_done)).md",
 "/home/adam/documents/personal/notes/Weekly_Workout_Plan.md"
]
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
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


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# Let's check the content of one file to understand the format
file_info = apis.file_system.show_file(access_token=fs_token, file_path=files[0])
print(file_info)
```

```
{
 "file_id": 25851,
 "path": "/home/adam/documents/personal/notes/Book_Reading_Lists.md",
 "content": "# Book Reading Lists\n\nThe Catcher in the Rye\n - authors: J.D. Salinger\n - genre: Coming-of-Age\n\nEducated\n - authors: Tara Westover\n - genre: Memoir\n\nThe Rise and Fall of the Third Reich\n - authors: William L. Shirer\n - genre: History\n\nThe Hobbit\n - authors: J.R.R. Tolkien\n - genre: Fantasy\n\n1984\n - authors: George Orwell\n - genre: Dystopian\n\nThe Girl on the Train\n - authors: Paula Hawkins\n - genre: Psychological Thriller\n\nThe Guns of August\n - authors: Barbara W. Tuchman\n - genre: History\n\nStart with Why\n - authors: Simon Sinek\n - genre: Business\n\n1491: New Revelations of the Americas Before Columbus\n - authors: Charles C. Mann\n - genre: History\n\nThinking, Fast and Slow\n - authors: Daniel Kahneman\n - genre: Psychology\n\nA People's History of the United States\n - authors: Howard Zinn\n - genre: History\n\nMilk and Honey\n - authors: Rupi Kaur\n - genre: Poetry\n\nThe Kite Runner\n - authors: Khaled Hosseini\n - genre: Historical Fiction\n\nThe Lord of the Rings: The Fellowship of the Ring\n - authors: J.R.R. Tolkien\n - genre: Epic Fantasy\n\nYou Are a Badass\n - authors: Jen Sincero\n - genre: Self-Help\n\nPride and Prejudice\n - authors: Jane Austen\n - genre: Romance\n\nGone Girl\n - authors: Gillian Flynn\n - genre: Mystery\n\nThe Da Vinci Code\n - authors: Dan Brown\n - genre: Thriller\n\nThe Great Gatsby\n - authors: F. Scott Fitzgerald\n - genre: Literary Fiction\n\nFahrenheit 451\n - authors: Ray Bradbury\n - genre: Science Fiction\n\nThe 7 Habits of Highly Effective People\n - authors: Stephen R. Covey\n - genre: Self-Help\n\nInfluence: The Psychology of Persuasion\n - authors: Robert B. Cialdini\n - genre: Psychology\n\nHarry Potter and the Sorcerer's Stone\n - authors: J.K. Rowling\n - genre: Young Adult\n\nGrit: The Power of Passion and Perseverance\n - authors: Angela Duckworth\n - genre: Psychology\n\nAtomic Habits\n - authors: James Clear\n - genre: Self-Help\n\nBecoming\n - authors: Michelle Obama\n - genre: Memoir\n\nQuiet: The Power of Introverts in a World That Can't Stop Talking\n - authors: Susan Cain\n - genre: Psychology\n\nLittle Women\n - authors: Louisa May Alcott\n - genre: Classic\n\nThe Hunger Games\n - authors: Suzanne Collins\n - genre: Science Fiction\n\nTo Kill a Mockingbird\n - authors: Harper Lee\n - genre: Classic",
 "created_at": "2022-12-16T12:22:12",
 "updated_at": "2022-12-16T12:22:12"
}
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
import os

# Get list of files
files = apis.file_system.show_directory(access_token=fs_token, directory_path='~/documents/personal/notes/', entry_type='files')

for file_path in files:
    # Get file content
    file_info = apis.file_system.show_file(access_token=fs_token, file_path=file_path)
    content = file_info['content']
    
    # Extract filename without extension
    filename = file_path.split('/')[-1]  # e.g., "Book_Reading_Lists.md"
    # Remove .md extension
    if filename.endswith('.md'):
        filename = filename[:-3]
    # Replace underscores with spaces
    title = filename.replace('_', ' ')
    
    # Create note in Simple Note
    result = apis.simple_note.create_note(access_token=sn_token, title=title, content=content)
    print(f"Created note: {title} -> {result}")
```

```
Created note: Book Reading Lists -> {'message': 'Note created.', 'note_id': 3084}
Created note: Food Recipes -> {'message': 'Note created.', 'note_id': 3085}
Created note: Funny Quotes Collection -> {'message': 'Note created.', 'note_id': 3086}
Created note: Gift Ideas for Various Occasions -> {'message': 'Note created.', 'note_id': 3087}
Created note: Grocery List -> {'message': 'Note created.', 'note_id': 3088}
Created note: Habit Tracking Log for 2023-04-30 -> {'message': 'Note created.', 'note_id': 3089}
Created note: Habit Tracking Log for 2023-05-01 -> {'message': 'Note created.', 'note_id': 3090}
Created note: Habit Tracking Log for 2023-05-02 -> {'message': 'Note created.', 'note_id': 3091}
Created note: Habit Tracking Log for 2023-05-03 -> {'message': 'Note created.', 'note_id': 3092}
Created note: Habit Tracking Log for 2023-05-04 -> {'message': 'Note created.', 'note_id': 3093}
Created note: Habit Tracking Log for 2023-05-05 -> {'message': 'Note created.', 'note_id': 3094}
Created note: Habit Tracking Log for 2023-05-06 -> {'message': 'Note created.', 'note_id': 3095}
Created note: Habit Tracking Log for 2023-05-07 -> {'message': 'Note created.', 'note_id': 3096}
Created note: Habit Tracking Log for 2023-05-08 -> {'message': 'Note created.', 'note_id': 3097}
Created note: Habit Tracking Log for 2023-05-09 -> {'message': 'Note created.', 'note_id': 3098}
Created note: Habit Tracking Log for 2023-05-10 -> {'message': 'Note created.', 'note_id': 3099}
Created note: Habit Tracking Log for 2023-05-11 -> {'message': 'Note created.', 'note_id': 3100}
Created note: Habit Tracking Log for 2023-05-12 -> {'message': 'Note created.', 'note_id': 3101}
Created note: Habit Tracking Log for 2023-05-13 -> {'message': 'Note created.', 'note_id': 3102}
Created note: Habit Tracking Log for 2023-05-14 -> {'message': 'Note created.', 'note_id': 3103}
Created note: Habit Tracking Log for 2023-05-15 -> {'message': 'Note created.', 'note_id': 3104}
Created note: Habit Tracking Log for 2023-05-16 -> {'message': 'Note created.', 'note_id': 3105}
Created note: Habit Tracking Log for 2023-05-17 -> {'message': 'Note created.', 'note_id': 3106}
Created note: Inspirational Quotes Collection -> {'message': 'Note created.', 'note_id': 3107}
Created note: Movie Quotes Collection -> {'message': 'Note created.', 'note_id': 3108}
Created note: Movie Recommendations -> {'message': 'Note created.', 'note_id': 3109}
Created note: My Bucket List ([x] = done, [ ] = not done)) -> {'message': 'Note created.', 'note_id': 3110}
Created note: Weekly Workout Plan -> {'message': 'Note created.', 'note_id': 3111}
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
apis.supervisor.complete_task()
```

```
Execution successful.
```

