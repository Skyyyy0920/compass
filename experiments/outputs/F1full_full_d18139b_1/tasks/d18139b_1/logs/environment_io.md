
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


### Environment Interaction 3
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='phone'))
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
  "name": "send_password_reset_code",
  "description": "Send password reset code to your phone number."
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
  "name": "show_contact_relationships",
  "description": "Get a list of all relationships available in your contact book."
 },
 {
  "name": "search_contacts",
  "description": "Search your contact book for relatives' information."
 },
 {
  "name": "add_contact",
  "description": "Add a new contact."
 },
 {
  "name": "delete_contact",
  "description": "Delete contact information."
 },
 {
  "name": "update_contact",
  "description": "Update contact information."
 },
 {
  "name": "show_text_message_window",
  "description": "Show text messages with a contact around a given date and time."
 },
 {
  "name": "search_text_messages",
  "description": "Show or search your text messages."
 },
 {
  "name": "show_text_message",
  "description": "Show text message details."
 },
 {
  "name": "delete_text_message",
  "description": "Delete a text message."
 },
 {
  "name": "send_text_message",
  "description": "Send a text message on the given phone number."
 },
 {
  "name": "show_alarms",
  "description": "Get a list of alarms."
 },
 {
  "name": "create_alarm",
  "description": "Create a new alarm."
 },
 {
  "name": "show_alarm",
  "description": "Show alarm details."
 },
 {
  "name": "delete_alarm",
  "description": "Delete an alarm."
 },
 {
  "name": "update_alarm",
  "description": "Update an alarm's settings."
 },
 {
  "name": "show_voice_message_window",
  "description": "Show voice messages with a contact around a given date and time."
 },
 {
  "name": "search_voice_messages",
  "description": "Show or search text voice_messages between the user and a contact."
 },
 {
  "name": "show_voice_message",
  "description": "Show voice message details."
 },
 {
  "name": "delete_voice_message",
  "description": "Delete a voice message."
 },
 {
  "name": "send_voice_message",
  "description": "Send a voice message on the given phone number."
 },
 {
  "name": "get_current_date_and_time",
  "description": "Show current date and time."
 }
]
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='venmo'))
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
  "description": "Show public profile information of a user, including your friendship status with them."
 },
 {
  "name": "search_users",
  "description": "Search Venmo users by name or email address."
 },
 {
  "name": "search_friends",
  "description": "Search your or others' friends by name or email address."
 },
 {
  "name": "add_friend",
  "description": "Add a friend to your friend list."
 },
 {
  "name": "remove_friend",
  "description": "Remove a friend from your friend list."
 },
 {
  "name": "show_venmo_balance",
  "description": "Show your Venmo balance."
 },
 {
  "name": "add_to_venmo_balance",
  "description": "Add money to your Venmo balance."
 },
 {
  "name": "withdraw_from_venmo_balance",
  "description": "Withdraw money from your Venmo balance."
 },
 {
  "name": "show_bank_transfer_history",
  "description": "Show histroy of money transfer from Venmo to payment card and vice versa."
 },
 {
  "name": "download_bank_transfer_receipt",
  "description": "Download the receipt of money transfer from Venmo to payment card or vice versa."
 },
 {
  "name": "show_transaction",
  "description": "Show transaction details."
 },
 {
  "name": "update_transaction",
  "description": "Update transaction information."
 },
 {
  "name": "show_transactions",
  "description": "Get a list of your transactions."
 },
 {
  "name": "create_transaction",
  "description": "Send money to a user."
 },
 {
  "name": "download_transaction_receipt",
  "description": "Download the receipt of a transaction (money sent from one user to another)."
 },
 {
  "name": "like_transaction",
  "description": "Like a transaction."
 },
 {
  "name": "unlike_transaction",
  "description": "Unlike a transaction."
 },
 {
  "name": "show_transaction_comments",
  "description": "Get a list of transaction comments."
 },
 {
  "name": "create_transaction_comment",
  "description": "Create a new transaction comment."
 },
 {
  "name": "show_transaction_comment",
  "description": "Show detailed information about a transaction comment."
 },
 {
  "name": "delete_transaction_comment",
  "description": "Delete a transaction comment."
 },
 {
  "name": "update_transaction_comment",
  "description": "Update a transaction comment."
 },
 {
  "name": "like_transaction_comment",
  "description": "Like a transaction comment."
 },
 {
  "name": "unlike_transaction_comment",
  "description": "Unlike a previously liked transaction comment."
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
  "name": "show_payment_cards",
  "description": "Get a list of users payment cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_received_payment_requests",
  "description": "Get a list of payment requests you have received from others."
 },
 {
  "name": "show_sent_payment_requests",
  "description": "Get a list of payment requests you have sent to others."
 },
 {
  "name": "create_payment_request",
  "description": "Send a payment request."
 },
 {
  "name": "delete_payment_request",
  "description": "Delete a payment request."
 },
 {
  "name": "update_payment_request",
  "description": "Update payment request information."
 },
 {
  "name": "approve_payment_request",
  "description": "Approve a payment request."
 },
 {
  "name": "deny_payment_request",
  "description": "Deny a payment request."
 },
 {
  "name": "remind_payment_request",
  "description": "Send a reminder to a user via notification about this payment request."
 },
 {
  "name": "show_social_feed",
  "description": "Show your social feed (transactions of your friends)."
 },
 {
  "name": "show_notifications",
  "description": "Get a list of your notifications."
 },
 {
  "name": "delete_notifications",
  "description": "Delete all of your notifications."
 },
 {
  "name": "mark_notifications",
  "description": "Mark all notifications as read or unread."
 },
 {
  "name": "show_notifications_count",
  "description": "Get the count of your notifications."
 },
 {
  "name": "delete_notification",
  "description": "Delete a notification."
 },
 {
  "name": "mark_notification",
  "description": "Mark a notification as read or unread."
 }
]
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
# Get current date and time to know the calendar month
print(apis.phone.get_current_date_and_time())
```

```
{"date": "Monday, June 19, 2023", "time": "12:31 PM"}
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
# Get venmo account password from supervisor
print(apis.supervisor.show_account_passwords())
```

```
[
 {
  "account_name": "amazon",
  "password": "EfWDm1a"
 },
 {
  "account_name": "file_system",
  "password": "mv-l]Ud"
 },
 {
  "account_name": "gmail",
  "password": "-Uf_)OB"
 },
 {
  "account_name": "phone",
  "password": "b4GXZH6"
 },
 {
  "account_name": "simple_note",
  "password": "g{WPN$i"
 },
 {
  "account_name": "splitwise",
  "password": "+xGGeSF"
 },
 {
  "account_name": "spotify",
  "password": "rvP5MvY"
 },
 {
  "account_name": "todoist",
  "password": "Ibi7M7b"
 },
 {
  "account_name": "venmo",
  "password": "uNK8[nt"
 }
]
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='login'))
```

```
{
 "app_name": "venmo",
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


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Login to venmo with the supervisor's email and venmo password
print(apis.venmo.login(username='joseharr@gmail.com', password='uNK8[nt'))
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2ZW5tbytqb3NlaGFyckBnbWFpbC5jb20iLCJleHAiOjE2ODcxNzg3NzJ9.7vW2oB7_WlT2-135iNZBuJn1oVMWT1vgpJ15IjmDB6U",
 "token_type": "Bearer"
}
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
print(apis.phone.show_contact_relationships())
```

```
Execution failed. Traceback:
  File "<python-input>", line 1, in <module>
    print(apis.phone.show_contact_relationships())
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 401:
{"message":"You are either not authorized to access this phone API endpoint or your access token is missing, invalid or expired."}
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='phone', api_name='login'))
```

```
{
 "app_name": "phone",
 "api_name": "login",
 "path": "/auth/token",
 "method": "POST",
 "description": "Login to your account.",
 "parameters": [
  {
   "name": "username",
   "type": "string",
   "required": true,
   "description": "Your account phone_number.",
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


### Environment Interaction 11
----------------------------------------------------------------------------
```python
print(apis.phone.login(username='2474975253', password='b4GXZH6'))
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwaG9uZSsyNDc0OTc1MjUzIiwiZXhwIjoxNjg3MTc5NDE1fQ.8Fgb2cFpfnjMV5XtUaNMJeJKxLKTph1y0zRa7eFig7M",
 "token_type": "Bearer"
}
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
print(apis.phone.show_contact_relationships())
```

```
Execution failed. Traceback:
  File "<python-input>", line 1, in <module>
    print(apis.phone.show_contact_relationships())
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 401:
{"message":"You are either not authorized to access this phone API endpoint or your access token is missing, invalid or expired."}
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='phone', api_name='show_contact_relationships'))
```

```
{
 "app_name": "phone",
 "api_name": "show_contact_relationships",
 "path": "/contact_relationships",
 "method": "GET",
 "description": "Get a list of all relationships available in your contact book.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from phone app login.",
   "default": null,
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
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
# Store the phone access token
phone_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwaG9uZSsyNDc0OTc1MjUzIiwiZXhwIjoxNjg3MTc5NDE1fQ.8Fgb2cFpfnjMV5XtUaNMJeJKxLKTph1y0zRa7eFig7M"
print(apis.phone.show_contact_relationships(access_token=phone_token))
```

```
[
 "brother",
 "coworker",
 "father",
 "friend",
 "mother",
 "parent",
 "roommate",
 "sibling",
 "sister",
 "subordinate"
]
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='phone', api_name='search_contacts'))
```

```
{
 "app_name": "phone",
 "api_name": "search_contacts",
 "path": "/contacts",
 "method": "GET",
 "description": "Search your contact book for relatives' information.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from phone app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "query",
   "type": "string",
   "required": false,
   "description": "Search query for the contacts list.",
   "default": "",
   "constraints": []
  },
  {
   "name": "relationship",
   "type": "string",
   "required": false,
   "description": "Relationship with the person in the contacts list to filter by.",
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
    "contact_id": 1,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "phone_number": "string",
    "relationships": [
     "string"
    ],
    "birthday": "string",
    "home_address": "string",
    "work_address": "string",
    "created_at": "2019-01-01T00:00:00"
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
# Search contacts with relationship "roommate"
print(apis.phone.search_contacts(access_token=phone_token, relationship='roommate'))
```

```
[
 {
  "contact_id": 259,
  "first_name": "Chris",
  "last_name": "Mccoy",
  "email": "chris.mcco@gmail.com",
  "phone_number": "5584932120",
  "relationships": [
   "roommate"
  ],
  "birthday": "1983-01-02",
  "home_address": "172 Matthew Knolls Suite 730\nSeattle\nWashington\nUnited States\n65644",
  "work_address": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "created_at": "2023-03-19T23:30:11"
 },
 {
  "contact_id": 260,
  "first_name": "Lindsey",
  "last_name": "Simpson",
  "email": "lindseysimpson@gmail.com",
  "phone_number": "3567801924",
  "relationships": [
   "roommate"
  ],
  "birthday": "1993-11-23",
  "home_address": "172 Matthew Knolls Suite 730\nSeattle\nWashington\nUnited States\n65644",
  "work_address": "406 Lindsay Courts Suite 522\nSeattle\nWashington\nUnited States\n26281",
  "created_at": "2023-03-19T23:30:11"
 },
 {
  "contact_id": 261,
  "first_name": "Paul",
  "last_name": "Miller",
  "email": "paul_mill@gmail.com",
  "phone_number": "3379617841",
  "relationships": [
   "roommate"
  ],
  "birthday": "1997-08-01",
  "home_address": "172 Matthew Knolls Suite 730\nSeattle\nWashington\nUnited States\n65644",
  "work_address": "265 Carpenter Loop Suite 064\nSeattle\nWashington\nUnited States\n44564",
  "created_at": "2023-03-19T23:30:11"
 }
]
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='show_received_payment_requests'))
```

```
{
 "app_name": "venmo",
 "api_name": "show_received_payment_requests",
 "path": "/received_payment_requests",
 "method": "GET",
 "description": "Get a list of payment requests you have received from others.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from venmo app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "status",
   "type": "string",
   "required": false,
   "description": "Filter payment requests by status. Will skip filtering if not passed.",
   "default": null,
   "constraints": [
    "value in ['pending', 'approved', 'denied']"
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
  }
 ],
 "response_schemas": {
  "success": [
   {
    "payment_request_id": 1,
    "amount": 0.0,
    "description": "string",
    "created_at": "2019-01-01T00:00:00",
    "updated_at": "2019-01-01T00:00:00",
    "approved_at": "2019-01-01T00:00:00",
    "denied_at": "2019-01-01T00:00:00",
    "private": true,
    "sender": {
     "name": "string",
     "email": "user@example.com"
    },
    "receiver": {
     "name": "string",
     "email": "user@example.com"
    }
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
venmo_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2ZW5tbytqb3NlaGFyckBnbWFpbC5jb20iLCJleHAiOjE2ODcxNzg3NzJ9.7vW2oB7_WlT2-135iNZBuJn1oVMWT1vgpJ15IjmDB6U"
print(apis.venmo.show_received_payment_requests(access_token=venmo_token, status='pending'))
```

```
[
 {
  "payment_request_id": 6152,
  "amount": 23.0,
  "description": "\ud83c\udf31 Vegan Cooking Ingredients \ud83c\udf45",
  "created_at": "2023-06-17T14:58:29",
  "updated_at": "2023-06-17T14:58:29",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6209,
  "amount": 14.0,
  "description": "\ud83d\udcda Study Group Snack Fund \ud83d\udcd6",
  "created_at": "2023-06-17T13:36:53",
  "updated_at": "2023-06-17T13:36:53",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Leslie Ball",
   "email": "les_ball@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6210,
  "amount": 70.0,
  "description": "Bungee Jumping",
  "created_at": "2023-06-17T13:36:53",
  "updated_at": "2023-06-17T13:36:53",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Melissa Bailey",
   "email": "mel.bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6201,
  "amount": 46.0,
  "description": "\ud83c\udfa7Podcast Mic \ud83c\udfa4",
  "created_at": "2023-06-13T15:49:07",
  "updated_at": "2023-06-13T15:49:07",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Edwin Wilson",
   "email": "ed_wilson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6131,
  "amount": 6.0,
  "description": "Dog Park \ud83d\udc36 Outing",
  "created_at": "2023-06-04T14:11:42",
  "updated_at": "2023-06-04T14:11:42",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 }
]
```


### Environment Interaction 19
----------------------------------------------------------------------------
```python
# Get all pending payment requests (page 0 with limit 20)
print(apis.venmo.show_received_payment_requests(access_token=venmo_token, status='pending', page_index=0, page_limit=20))
```

```
[
 {
  "payment_request_id": 6152,
  "amount": 23.0,
  "description": "\ud83c\udf31 Vegan Cooking Ingredients \ud83c\udf45",
  "created_at": "2023-06-17T14:58:29",
  "updated_at": "2023-06-17T14:58:29",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6209,
  "amount": 14.0,
  "description": "\ud83d\udcda Study Group Snack Fund \ud83d\udcd6",
  "created_at": "2023-06-17T13:36:53",
  "updated_at": "2023-06-17T13:36:53",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Leslie Ball",
   "email": "les_ball@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6210,
  "amount": 70.0,
  "description": "Bungee Jumping",
  "created_at": "2023-06-17T13:36:53",
  "updated_at": "2023-06-17T13:36:53",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Melissa Bailey",
   "email": "mel.bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6201,
  "amount": 46.0,
  "description": "\ud83c\udfa7Podcast Mic \ud83c\udfa4",
  "created_at": "2023-06-13T15:49:07",
  "updated_at": "2023-06-13T15:49:07",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Edwin Wilson",
   "email": "ed_wilson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6131,
  "amount": 6.0,
  "description": "Dog Park \ud83d\udc36 Outing",
  "created_at": "2023-06-04T14:11:42",
  "updated_at": "2023-06-04T14:11:42",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6182,
  "amount": 42.0,
  "description": "\ud83c\udfb8 Music Lessons",
  "created_at": "2023-06-03T15:06:40",
  "updated_at": "2023-06-03T15:06:40",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Robert Martinez",
   "email": "robertmartinez@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6128,
  "amount": 94.0,
  "description": "Fishing Gear",
  "created_at": "2023-06-03T08:35:40",
  "updated_at": "2023-06-03T08:35:40",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6129,
  "amount": 162.0,
  "description": "Photography Gear",
  "created_at": "2023-06-03T08:35:40",
  "updated_at": "2023-06-03T08:35:40",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6130,
  "amount": 53.0,
  "description": "Mixology Class",
  "created_at": "2023-06-03T08:35:40",
  "updated_at": "2023-06-03T08:35:40",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Lindsey Simpson",
   "email": "lindseysimpson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6126,
  "amount": 100.0,
  "description": "\ud83d\udc53New Specs",
  "created_at": "2023-06-02T18:50:18",
  "updated_at": "2023-06-02T18:50:18",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6124,
  "amount": 44.0,
  "description": "Art Gallery",
  "created_at": "2023-06-01T17:50:18",
  "updated_at": "2023-06-01T17:50:18",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6123,
  "amount": 105.0,
  "description": "Birthday Gift",
  "created_at": "2023-05-31T11:02:08",
  "updated_at": "2023-05-31T11:02:08",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6118,
  "amount": 35.0,
  "description": "Groceries",
  "created_at": "2023-05-28T17:17:04",
  "updated_at": "2023-05-28T17:17:04",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6168,
  "amount": 89.0,
  "description": "Cosplay \ud83e\uddb8 Gear",
  "created_at": "2023-05-27T15:24:15",
  "updated_at": "2023-05-27T15:24:15",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Gina Burch",
   "email": "gina-ritter@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6163,
  "amount": 10.0,
  "description": "\ud83d\ude80 Rocket League Tourney \ud83d\udca5\ud83c\udfae",
  "created_at": "2023-05-23T12:19:00",
  "updated_at": "2023-05-23T12:19:00",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Troy Solomon",
   "email": "tr_solo@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6103,
  "amount": 19.0,
  "description": "\ud83d\udef5 Food Delivery for Lazy Day \ud83c\udf55",
  "created_at": "2023-05-21T08:40:44",
  "updated_at": "2023-05-21T08:40:44",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6104,
  "amount": 12.0,
  "description": "\ud83c\udf70 Dessert Run \ud83c\udf68\ud83c\udf70",
  "created_at": "2023-05-21T08:40:44",
  "updated_at": "2023-05-21T08:40:44",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Lindsey Simpson",
   "email": "lindseysimpson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4372,
  "amount": 54.0,
  "description": "Date Night \ud83c\udf77",
  "created_at": "2023-05-16T13:22:03",
  "updated_at": "2023-05-16T13:22:03",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "William Martinez",
   "email": "william_mart@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 250,
  "amount": 7.0,
  "description": "\ud83e\uddfc Laundry Day \ud83e\uddfa\ud83d\udca6",
  "created_at": "2023-05-13T16:14:33",
  "updated_at": "2023-05-13T16:14:33",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Leslie Ball",
   "email": "les_ball@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 1869,
  "amount": 15.0,
  "description": "\ud83d\ude95Lyft Home",
  "created_at": "2023-05-07T20:10:14",
  "updated_at": "2023-05-07T20:10:14",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Michael Burch",
   "email": "mi.burch@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 }
]
```


### Environment Interaction 20
----------------------------------------------------------------------------
```python
# Check if there are more pending payment requests on page 1
print(apis.venmo.show_received_payment_requests(access_token=venmo_token, status='pending', page_index=1, page_limit=20))
```

```
[
 {
  "payment_request_id": 4718,
  "amount": 90.0,
  "description": "\ud83d\udc5f New Sneakers \ud83d\udc5f\ud83d\udd25",
  "created_at": "2023-05-05T23:53:47",
  "updated_at": "2023-05-05T23:53:47",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Sherry Smith",
   "email": "she_bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4612,
  "amount": 42.0,
  "description": "Dance Class",
  "created_at": "2023-05-04T16:11:19",
  "updated_at": "2023-05-04T16:11:19",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Melissa Bailey",
   "email": "mel.bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 3203,
  "amount": 55.0,
  "description": "Couples Massage \ud83d\udc86\ud83d\udc86",
  "created_at": "2023-05-03T00:33:55",
  "updated_at": "2023-05-03T00:33:55",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Tammy Weaver",
   "email": "ta.weav@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 5485,
  "amount": 14.0,
  "description": "\ud83d\udef5 Food Delivery for Lazy Day \ud83c\udf55",
  "created_at": "2023-05-02T00:07:07",
  "updated_at": "2023-05-02T00:07:07",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Gina Burch",
   "email": "gina-ritter@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 1873,
  "amount": 80.0,
  "description": "Electronics",
  "created_at": "2023-04-30T10:36:15",
  "updated_at": "2023-04-30T10:36:15",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Michael Burch",
   "email": "mi.burch@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4326,
  "amount": 35.0,
  "description": "\ud83d\udc7b Haunted House Adventure \ud83c\udf83",
  "created_at": "2023-04-27T13:05:43",
  "updated_at": "2023-04-27T13:05:43",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Robert Martinez",
   "email": "robertmartinez@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 3204,
  "amount": 87.0,
  "description": "Electronics",
  "created_at": "2023-04-19T18:11:20",
  "updated_at": "2023-04-19T18:11:20",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Tammy Weaver",
   "email": "ta.weav@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4611,
  "amount": 45.0,
  "description": "Record Store \ud83c\udfb6 Finds",
  "created_at": "2023-04-13T05:55:47",
  "updated_at": "2023-04-13T05:55:47",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Melissa Bailey",
   "email": "mel.bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 249,
  "amount": 91.0,
  "description": "Photography",
  "created_at": "2023-04-09T19:04:13",
  "updated_at": "2023-04-09T19:04:13",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Leslie Ball",
   "email": "les_ball@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 3200,
  "amount": 74.0,
  "description": "Fishing Gear",
  "created_at": "2023-04-01T05:16:42",
  "updated_at": "2023-04-01T05:16:42",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Tammy Weaver",
   "email": "ta.weav@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4723,
  "amount": 8.0,
  "description": "\ud83c\udf7f Netflix Subscription \ud83c\udfac\ud83d\udecb\ufe0f",
  "created_at": "2023-04-01T01:46:41",
  "updated_at": "2023-04-01T01:46:41",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Sherry Smith",
   "email": "she_bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 346,
  "amount": 282.0,
  "description": "Business Workshop",
  "created_at": "2023-03-28T13:48:38",
  "updated_at": "2023-03-28T13:48:38",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Katherine Smith",
   "email": "ka_ball@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 571,
  "amount": 61.0,
  "description": "Online courses",
  "created_at": "2023-03-20T03:03:03",
  "updated_at": "2023-03-20T03:03:03",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Troy Solomon",
   "email": "tr_solo@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 3457,
  "amount": 17.0,
  "description": "\ud83c\udfae Gaming Marathon Snacks \ud83c\udfb2",
  "created_at": "2023-03-07T10:10:05",
  "updated_at": "2023-03-07T10:10:05",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Lindsey Simpson",
   "email": "lindseysimpson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4715,
  "amount": 26.0,
  "description": "Fishing License",
  "created_at": "2023-03-02T11:02:56",
  "updated_at": "2023-03-02T11:02:56",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Sherry Smith",
   "email": "she_bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 5801,
  "amount": 34.0,
  "description": "\ud83d\udc1f Aquarium Visit \ud83e\udd91",
  "created_at": "2023-02-28T15:14:13",
  "updated_at": "2023-02-28T15:14:13",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Glenn Burton",
   "email": "glenn.burton@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 3455,
  "amount": 29.0,
  "description": "Skincare \ud83d\udc86\ud83c\udf3f",
  "created_at": "2023-02-27T05:16:56",
  "updated_at": "2023-02-27T05:16:56",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Lindsey Simpson",
   "email": "lindseysimpson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 251,
  "amount": 23.0,
  "description": "\ud83d\udc87Salon Day",
  "created_at": "2023-02-26T15:18:38",
  "updated_at": "2023-02-26T15:18:38",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Leslie Ball",
   "email": "les_ball@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 568,
  "amount": 29.0,
  "description": "Charity Run \ud83c\udfc3\ud83d\udc96",
  "created_at": "2023-02-24T07:10:01",
  "updated_at": "2023-02-24T07:10:01",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Troy Solomon",
   "email": "tr_solo@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 565,
  "amount": 15.0,
  "description": "\ud83d\udef5Scooter Ride",
  "created_at": "2023-02-22T02:33:47",
  "updated_at": "2023-02-22T02:33:47",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Troy Solomon",
   "email": "tr_solo@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 }
]
```


### Environment Interaction 21
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='approve_payment_request'))
```

```
{
 "app_name": "venmo",
 "api_name": "approve_payment_request",
 "path": "/payment_requests/{payment_request_id}/approve",
 "method": "POST",
 "description": "Approve a payment request.",
 "parameters": [
  {
   "name": "payment_request_id",
   "type": "integer",
   "required": true,
   "description": "ID of the payment request to approve.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from venmo app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "payment_card_id",
   "type": "integer",
   "required": false,
   "description": "ID of the payment card to use for approving the payment request. If not passed, Venmo balance will be used.",
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


### Environment Interaction 22
----------------------------------------------------------------------------
```python
# Check if there are more pending payment requests on page 2
print(apis.venmo.show_received_payment_requests(access_token=venmo_token, status='pending', page_index=2, page_limit=20))
```

```
[
 {
  "payment_request_id": 4615,
  "amount": 14.0,
  "description": "\ud83c\udfae Gaming Marathon Snacks \ud83c\udfb2",
  "created_at": "2023-02-19T14:45:42",
  "updated_at": "2023-02-19T14:45:42",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Melissa Bailey",
   "email": "mel.bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 149,
  "amount": 27.0,
  "description": "\ud83d\udcd6 Bookstore Haul \ud83d\udcda\u2764\ufe0f",
  "created_at": "2023-02-17T16:43:35",
  "updated_at": "2023-02-17T16:43:35",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 5482,
  "amount": 118.0,
  "description": "Hotel Stay",
  "created_at": "2023-02-08T13:43:34",
  "updated_at": "2023-02-08T13:43:34",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Gina Burch",
   "email": "gina-ritter@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4610,
  "amount": 38.0,
  "description": "\ud83c\udf79 Cocktail Mixing Class \ud83c\udf78",
  "created_at": "2023-01-31T23:23:23",
  "updated_at": "2023-01-31T23:23:23",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Melissa Bailey",
   "email": "mel.bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 5799,
  "amount": 20.0,
  "description": "\ud83d\udcf1 App Store Fun",
  "created_at": "2023-01-28T15:18:22",
  "updated_at": "2023-01-28T15:18:22",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Glenn Burton",
   "email": "glenn.burton@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4324,
  "amount": 46.0,
  "description": "New \ud83c\udfae Game Purchase",
  "created_at": "2023-01-24T09:04:05",
  "updated_at": "2023-01-24T09:04:05",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Robert Martinez",
   "email": "robertmartinez@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 573,
  "amount": 123.0,
  "description": "Makeup Class",
  "created_at": "2023-01-13T21:00:23",
  "updated_at": "2023-01-13T21:00:23",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Troy Solomon",
   "email": "tr_solo@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 567,
  "amount": 18.0,
  "description": "\ud83c\udf73 Breakfast Club \ud83e\udd5e\ud83c\udf73",
  "created_at": "2023-01-09T00:09:41",
  "updated_at": "2023-01-09T00:09:41",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Troy Solomon",
   "email": "tr_solo@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4722,
  "amount": 40.0,
  "description": "Yoga class zen",
  "created_at": "2023-01-02T14:06:37",
  "updated_at": "2023-01-02T14:06:37",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Sherry Smith",
   "email": "she_bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 5486,
  "amount": 5.0,
  "description": "Dog Park \ud83d\udc36 Outing",
  "created_at": "2022-12-31T00:53:08",
  "updated_at": "2022-12-31T00:53:08",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Gina Burch",
   "email": "gina-ritter@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 5484,
  "amount": 151.0,
  "description": "Musical Instruments",
  "created_at": "2022-12-29T00:29:48",
  "updated_at": "2022-12-29T00:29:48",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Gina Burch",
   "email": "gina-ritter@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 1872,
  "amount": 21.0,
  "description": "Fishing License",
  "created_at": "2022-12-23T05:23:11",
  "updated_at": "2022-12-23T05:23:11",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Michael Burch",
   "email": "mi.burch@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 146,
  "amount": 387.0,
  "description": "Flight Ticket",
  "created_at": "2022-12-21T21:31:59",
  "updated_at": "2022-12-21T21:31:59",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 147,
  "amount": 41.0,
  "description": "\ud83c\udfa7Podcast Mic \ud83c\udfa4",
  "created_at": "2022-12-19T13:53:38",
  "updated_at": "2022-12-19T13:53:38",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 3456,
  "amount": 62.0,
  "description": "Grocery \ud83d\uded2 Haul",
  "created_at": "2022-12-17T21:06:12",
  "updated_at": "2022-12-17T21:06:12",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Lindsey Simpson",
   "email": "lindseysimpson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4719,
  "amount": 33.0,
  "description": "\ud83d\udc8d Small Gift \ud83d\udc8d\ud83d\udc96",
  "created_at": "2022-12-16T08:51:12",
  "updated_at": "2022-12-16T08:51:12",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Sherry Smith",
   "email": "she_bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 }
]
```


### Environment Interaction 23
----------------------------------------------------------------------------
```python
# Approve the payment requests from roommates in June 2023
# Roommate emails: chris.mcco@gmail.com, lindseysimpson@gmail.com, paul_mill@gmail.com
# June 2023 requests from roommates: 6152, 6131, 6128, 6129, 6130, 6126, 6124

roommate_requests = [6152, 6131, 6128, 6129, 6130, 6126, 6124]

for req_id in roommate_requests:
    result = apis.venmo.approve_payment_request(payment_request_id=req_id, access_token=venmo_token)
    print(f"Approved request {req_id}: {result}")
```

```
Execution failed. Traceback:
  File "<python-input>", line 8, in <module>
    result = apis.venmo.approve_payment_request(payment_request_id=req_id, access_token=venmo_token)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"Insufficient money in the Venmo balance."}
```


### Environment Interaction 24
----------------------------------------------------------------------------
```python
# Check venmo balance and payment cards
print(apis.venmo.show_venmo_balance(access_token=venmo_token))
print(apis.venmo.show_payment_cards(access_token=venmo_token))
```

```
{"venmo_balance": 0.0}
[
 {
  "payment_card_id": 58,
  "card_name": "Visa",
  "owner_name": "Jose Harrison",
  "card_number": 4905421304266040,
  "expiry_year": 2022,
  "expiry_month": 9,
  "cvv_number": 156
 },
 {
  "payment_card_id": 59,
  "card_name": "American Express",
  "owner_name": "Jose Harrison",
  "card_number": 1976550218228021,
  "expiry_year": 2024,
  "expiry_month": 4,
  "cvv_number": 448
 },
 {
  "payment_card_id": 60,
  "card_name": "MasterCard",
  "owner_name": "Jose Harrison",
  "card_number": 3369882836923626,
  "expiry_year": 2024,
  "expiry_month": 2,
  "cvv_number": 960
 },
 {
  "payment_card_id": 61,
  "card_name": "Wells Fargo",
  "owner_name": "Jose Harrison",
  "card_number": 6839691458272611,
  "expiry_year": 2022,
  "expiry_month": 7,
  "cvv_number": 369
 }
]
```


### Environment Interaction 25
----------------------------------------------------------------------------
```python
# Use a valid payment card (card 59) to approve the requests
for req_id in roommate_requests:
    result = apis.venmo.approve_payment_request(payment_request_id=req_id, access_token=venmo_token, payment_card_id=59)
    print(f"Approved request {req_id}: {result}")
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    result = apis.venmo.approve_payment_request(payment_request_id=req_id, access_token=venmo_token, payment_card_id=59)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"This payment request has already been completed."}
```


### Environment Interaction 26
----------------------------------------------------------------------------
```python
# Check current status of received payment requests
print(apis.venmo.show_received_payment_requests(access_token=venmo_token, status='approved'))
```

```
[
 {
  "payment_request_id": 6153,
  "amount": 26.0,
  "description": "\ud83c\udf38 Springtime Flower Garden Project \ud83c\udf37",
  "created_at": "2023-06-18T17:55:33",
  "updated_at": "2023-06-18T17:55:33",
  "approved_at": "2023-06-19T07:19:30",
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6152,
  "amount": 23.0,
  "description": "\ud83c\udf31 Vegan Cooking Ingredients \ud83c\udf45",
  "created_at": "2023-06-17T14:58:29",
  "updated_at": "2023-06-17T14:58:29",
  "approved_at": "2023-06-19T12:31:14",
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6151,
  "amount": 49.0,
  "description": "\ud83c\udfab Theater Tickets",
  "created_at": "2023-06-16T13:55:17",
  "updated_at": "2023-06-16T13:55:17",
  "approved_at": "2023-06-16T14:25:04",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Lindsey Simpson",
   "email": "lindseysimpson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6207,
  "amount": 5.0,
  "description": "Guitar Strings",
  "created_at": "2023-06-16T10:29:19",
  "updated_at": "2023-06-16T10:29:19",
  "approved_at": "2023-06-17T05:50:57",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Edwin Wilson",
   "email": "ed_wilson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6149,
  "amount": 156.0,
  "description": "\ud83e\uddf3 Travel Fund \ud83c\udf0d\u2708\ufe0f",
  "created_at": "2023-06-14T14:01:51",
  "updated_at": "2023-06-14T14:01:51",
  "approved_at": "2023-06-16T05:47:34",
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 }
]
```


### Environment Interaction 27
----------------------------------------------------------------------------
```python
# Re-fetch pending requests to see current state after the error
print(apis.venmo.show_received_payment_requests(access_token=venmo_token, status='pending', page_index=0, page_limit=20))
```

```
[
 {
  "payment_request_id": 6209,
  "amount": 14.0,
  "description": "\ud83d\udcda Study Group Snack Fund \ud83d\udcd6",
  "created_at": "2023-06-17T13:36:53",
  "updated_at": "2023-06-17T13:36:53",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Leslie Ball",
   "email": "les_ball@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6210,
  "amount": 70.0,
  "description": "Bungee Jumping",
  "created_at": "2023-06-17T13:36:53",
  "updated_at": "2023-06-17T13:36:53",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Melissa Bailey",
   "email": "mel.bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6201,
  "amount": 46.0,
  "description": "\ud83c\udfa7Podcast Mic \ud83c\udfa4",
  "created_at": "2023-06-13T15:49:07",
  "updated_at": "2023-06-13T15:49:07",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Edwin Wilson",
   "email": "ed_wilson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6182,
  "amount": 42.0,
  "description": "\ud83c\udfb8 Music Lessons",
  "created_at": "2023-06-03T15:06:40",
  "updated_at": "2023-06-03T15:06:40",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Robert Martinez",
   "email": "robertmartinez@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6130,
  "amount": 53.0,
  "description": "Mixology Class",
  "created_at": "2023-06-03T08:35:40",
  "updated_at": "2023-06-03T08:35:40",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Lindsey Simpson",
   "email": "lindseysimpson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6126,
  "amount": 100.0,
  "description": "\ud83d\udc53New Specs",
  "created_at": "2023-06-02T18:50:18",
  "updated_at": "2023-06-02T18:50:18",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6124,
  "amount": 44.0,
  "description": "Art Gallery",
  "created_at": "2023-06-01T17:50:18",
  "updated_at": "2023-06-01T17:50:18",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6123,
  "amount": 105.0,
  "description": "Birthday Gift",
  "created_at": "2023-05-31T11:02:08",
  "updated_at": "2023-05-31T11:02:08",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6118,
  "amount": 35.0,
  "description": "Groceries",
  "created_at": "2023-05-28T17:17:04",
  "updated_at": "2023-05-28T17:17:04",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6168,
  "amount": 89.0,
  "description": "Cosplay \ud83e\uddb8 Gear",
  "created_at": "2023-05-27T15:24:15",
  "updated_at": "2023-05-27T15:24:15",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Gina Burch",
   "email": "gina-ritter@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6163,
  "amount": 10.0,
  "description": "\ud83d\ude80 Rocket League Tourney \ud83d\udca5\ud83c\udfae",
  "created_at": "2023-05-23T12:19:00",
  "updated_at": "2023-05-23T12:19:00",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Troy Solomon",
   "email": "tr_solo@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6103,
  "amount": 19.0,
  "description": "\ud83d\udef5 Food Delivery for Lazy Day \ud83c\udf55",
  "created_at": "2023-05-21T08:40:44",
  "updated_at": "2023-05-21T08:40:44",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6104,
  "amount": 12.0,
  "description": "\ud83c\udf70 Dessert Run \ud83c\udf68\ud83c\udf70",
  "created_at": "2023-05-21T08:40:44",
  "updated_at": "2023-05-21T08:40:44",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Lindsey Simpson",
   "email": "lindseysimpson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4372,
  "amount": 54.0,
  "description": "Date Night \ud83c\udf77",
  "created_at": "2023-05-16T13:22:03",
  "updated_at": "2023-05-16T13:22:03",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "William Martinez",
   "email": "william_mart@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 250,
  "amount": 7.0,
  "description": "\ud83e\uddfc Laundry Day \ud83e\uddfa\ud83d\udca6",
  "created_at": "2023-05-13T16:14:33",
  "updated_at": "2023-05-13T16:14:33",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Leslie Ball",
   "email": "les_ball@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 1869,
  "amount": 15.0,
  "description": "\ud83d\ude95Lyft Home",
  "created_at": "2023-05-07T20:10:14",
  "updated_at": "2023-05-07T20:10:14",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Michael Burch",
   "email": "mi.burch@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4718,
  "amount": 90.0,
  "description": "\ud83d\udc5f New Sneakers \ud83d\udc5f\ud83d\udd25",
  "created_at": "2023-05-05T23:53:47",
  "updated_at": "2023-05-05T23:53:47",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Sherry Smith",
   "email": "she_bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4612,
  "amount": 42.0,
  "description": "Dance Class",
  "created_at": "2023-05-04T16:11:19",
  "updated_at": "2023-05-04T16:11:19",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Melissa Bailey",
   "email": "mel.bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 3203,
  "amount": 55.0,
  "description": "Couples Massage \ud83d\udc86\ud83d\udc86",
  "created_at": "2023-05-03T00:33:55",
  "updated_at": "2023-05-03T00:33:55",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Tammy Weaver",
   "email": "ta.weav@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 5485,
  "amount": 14.0,
  "description": "\ud83d\udef5 Food Delivery for Lazy Day \ud83c\udf55",
  "created_at": "2023-05-02T00:07:07",
  "updated_at": "2023-05-02T00:07:07",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Gina Burch",
   "email": "gina-ritter@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 }
]
```


### Environment Interaction 28
----------------------------------------------------------------------------
```python
# Check all approved and denied requests to see what happened to 6131, 6128, 6129
print(apis.venmo.show_received_payment_requests(access_token=venmo_token, status='approved', page_index=0, page_limit=20))
```

```
[
 {
  "payment_request_id": 6153,
  "amount": 26.0,
  "description": "\ud83c\udf38 Springtime Flower Garden Project \ud83c\udf37",
  "created_at": "2023-06-18T17:55:33",
  "updated_at": "2023-06-18T17:55:33",
  "approved_at": "2023-06-19T07:19:30",
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6152,
  "amount": 23.0,
  "description": "\ud83c\udf31 Vegan Cooking Ingredients \ud83c\udf45",
  "created_at": "2023-06-17T14:58:29",
  "updated_at": "2023-06-17T14:58:29",
  "approved_at": "2023-06-19T12:31:14",
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6151,
  "amount": 49.0,
  "description": "\ud83c\udfab Theater Tickets",
  "created_at": "2023-06-16T13:55:17",
  "updated_at": "2023-06-16T13:55:17",
  "approved_at": "2023-06-16T14:25:04",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Lindsey Simpson",
   "email": "lindseysimpson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6207,
  "amount": 5.0,
  "description": "Guitar Strings",
  "created_at": "2023-06-16T10:29:19",
  "updated_at": "2023-06-16T10:29:19",
  "approved_at": "2023-06-17T05:50:57",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Edwin Wilson",
   "email": "ed_wilson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6149,
  "amount": 156.0,
  "description": "\ud83e\uddf3 Travel Fund \ud83c\udf0d\u2708\ufe0f",
  "created_at": "2023-06-14T14:01:51",
  "updated_at": "2023-06-14T14:01:51",
  "approved_at": "2023-06-16T05:47:34",
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6192,
  "amount": 33.0,
  "description": "Pizza & \ud83c\udfa5 Netflix",
  "created_at": "2023-06-09T13:59:06",
  "updated_at": "2023-06-09T13:59:06",
  "approved_at": "2023-06-10T03:36:15",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Melissa Bailey",
   "email": "mel.bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6193,
  "amount": 46.0,
  "description": "Brunchin' \ud83e\udd42",
  "created_at": "2023-06-09T13:59:06",
  "updated_at": "2023-06-09T13:59:06",
  "approved_at": "2023-06-12T00:23:18",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Gina Burch",
   "email": "gina-ritter@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6131,
  "amount": 6.0,
  "description": "Dog Park \ud83d\udc36 Outing",
  "created_at": "2023-06-04T14:11:42",
  "updated_at": "2023-06-04T14:11:42",
  "approved_at": "2023-06-19T12:31:14",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6128,
  "amount": 94.0,
  "description": "Fishing Gear",
  "created_at": "2023-06-03T08:35:40",
  "updated_at": "2023-06-03T08:35:40",
  "approved_at": "2023-06-19T12:31:14",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6129,
  "amount": 162.0,
  "description": "Photography Gear",
  "created_at": "2023-06-03T08:35:40",
  "updated_at": "2023-06-03T08:35:40",
  "approved_at": "2023-06-19T12:31:14",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6127,
  "amount": 42.0,
  "description": "Theme Park",
  "created_at": "2023-06-02T18:50:18",
  "updated_at": "2023-06-02T18:50:18",
  "approved_at": "2023-06-04T02:08:08",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6121,
  "amount": 40.0,
  "description": "Gym \ud83d\udcaa\ud83c\udffc Supplements",
  "created_at": "2023-05-31T11:02:08",
  "updated_at": "2023-05-31T11:02:08",
  "approved_at": "2023-05-31T14:40:18",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6107,
  "amount": 86.0,
  "description": "Tutoring",
  "created_at": "2023-05-23T08:02:43",
  "updated_at": "2023-05-23T08:02:43",
  "approved_at": "2023-05-24T17:18:42",
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6159,
  "amount": 161.0,
  "description": "Art Supplies",
  "created_at": "2023-05-20T17:49:34",
  "updated_at": "2023-05-20T17:49:34",
  "approved_at": "2023-05-21T07:46:22",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Leslie Ball",
   "email": "les_ball@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6101,
  "amount": 16.0,
  "description": "Movie Ticket",
  "created_at": "2023-05-20T12:53:24",
  "updated_at": "2023-05-20T12:53:24",
  "approved_at": "2023-05-21T14:30:59",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6098,
  "amount": 51.0,
  "description": "Camping Fees",
  "created_at": "2023-05-18T16:24:26",
  "updated_at": "2023-05-18T16:24:26",
  "approved_at": "2023-05-18T16:44:20",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6155,
  "amount": 52.0,
  "description": "Sushi night \ud83c\udf63",
  "created_at": "2023-05-18T12:15:34",
  "updated_at": "2023-05-18T12:15:34",
  "approved_at": "2023-05-19T23:22:10",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Troy Solomon",
   "email": "tr_solo@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 3198,
  "amount": 13.0,
  "description": "\ud83c\udf7a Craft Beers \ud83c\udf7b\ud83d\udc4c",
  "created_at": "2023-05-17T15:16:40",
  "updated_at": "2023-05-17T15:16:40",
  "approved_at": "2023-05-18T04:33:46",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Tammy Weaver",
   "email": "ta.weav@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 5483,
  "amount": 28.0,
  "description": "Books",
  "created_at": "2023-05-12T05:43:05",
  "updated_at": "2023-05-12T05:43:05",
  "approved_at": "2023-05-12T13:18:22",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Gina Burch",
   "email": "gina-ritter@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4328,
  "amount": 21.0,
  "description": "\ud83d\udcd6 Bookstore Haul \ud83d\udcda\u2764\ufe0f",
  "created_at": "2023-05-12T02:01:07",
  "updated_at": "2023-05-12T02:01:07",
  "approved_at": "2023-05-13T01:44:49",
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Robert Martinez",
   "email": "robertmartinez@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 }
]
```


### Environment Interaction 29
----------------------------------------------------------------------------
```python
# Approve the remaining pending requests from roommates in June 2023
# 6130 (Lindsey), 6126 (Chris), 6124 (Paul)
pending_roommate_requests = [6130, 6126, 6124]

for req_id in pending_roommate_requests:
    result = apis.venmo.approve_payment_request(payment_request_id=req_id, access_token=venmo_token, payment_card_id=59)
    print(f"Approved request {req_id}: {result}")
```

```
Approved request 6130: {'message': 'Payment request approved.'}
Approved request 6126: {'message': 'Payment request approved.'}
Approved request 6124: {'message': 'Payment request approved.'}
```


### Environment Interaction 30
----------------------------------------------------------------------------
```python
# Verify all pending requests from roommates in June 2023 are approved
# Fetch all pending requests again to confirm
pending = apis.venmo.show_received_payment_requests(access_token=venmo_token, status='pending', page_index=0, page_limit=20)
print(pending)
```

```
[
 {
  "payment_request_id": 6209,
  "amount": 14.0,
  "description": "\ud83d\udcda Study Group Snack Fund \ud83d\udcd6",
  "created_at": "2023-06-17T13:36:53",
  "updated_at": "2023-06-17T13:36:53",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Leslie Ball",
   "email": "les_ball@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6210,
  "amount": 70.0,
  "description": "Bungee Jumping",
  "created_at": "2023-06-17T13:36:53",
  "updated_at": "2023-06-17T13:36:53",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Melissa Bailey",
   "email": "mel.bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6201,
  "amount": 46.0,
  "description": "\ud83c\udfa7Podcast Mic \ud83c\udfa4",
  "created_at": "2023-06-13T15:49:07",
  "updated_at": "2023-06-13T15:49:07",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Edwin Wilson",
   "email": "ed_wilson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6182,
  "amount": 42.0,
  "description": "\ud83c\udfb8 Music Lessons",
  "created_at": "2023-06-03T15:06:40",
  "updated_at": "2023-06-03T15:06:40",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Robert Martinez",
   "email": "robertmartinez@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6123,
  "amount": 105.0,
  "description": "Birthday Gift",
  "created_at": "2023-05-31T11:02:08",
  "updated_at": "2023-05-31T11:02:08",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6118,
  "amount": 35.0,
  "description": "Groceries",
  "created_at": "2023-05-28T17:17:04",
  "updated_at": "2023-05-28T17:17:04",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6168,
  "amount": 89.0,
  "description": "Cosplay \ud83e\uddb8 Gear",
  "created_at": "2023-05-27T15:24:15",
  "updated_at": "2023-05-27T15:24:15",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Gina Burch",
   "email": "gina-ritter@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6163,
  "amount": 10.0,
  "description": "\ud83d\ude80 Rocket League Tourney \ud83d\udca5\ud83c\udfae",
  "created_at": "2023-05-23T12:19:00",
  "updated_at": "2023-05-23T12:19:00",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Troy Solomon",
   "email": "tr_solo@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6103,
  "amount": 19.0,
  "description": "\ud83d\udef5 Food Delivery for Lazy Day \ud83c\udf55",
  "created_at": "2023-05-21T08:40:44",
  "updated_at": "2023-05-21T08:40:44",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Paul Miller",
   "email": "paul_mill@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 6104,
  "amount": 12.0,
  "description": "\ud83c\udf70 Dessert Run \ud83c\udf68\ud83c\udf70",
  "created_at": "2023-05-21T08:40:44",
  "updated_at": "2023-05-21T08:40:44",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Lindsey Simpson",
   "email": "lindseysimpson@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4372,
  "amount": 54.0,
  "description": "Date Night \ud83c\udf77",
  "created_at": "2023-05-16T13:22:03",
  "updated_at": "2023-05-16T13:22:03",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "William Martinez",
   "email": "william_mart@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 250,
  "amount": 7.0,
  "description": "\ud83e\uddfc Laundry Day \ud83e\uddfa\ud83d\udca6",
  "created_at": "2023-05-13T16:14:33",
  "updated_at": "2023-05-13T16:14:33",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Leslie Ball",
   "email": "les_ball@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 1869,
  "amount": 15.0,
  "description": "\ud83d\ude95Lyft Home",
  "created_at": "2023-05-07T20:10:14",
  "updated_at": "2023-05-07T20:10:14",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Michael Burch",
   "email": "mi.burch@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4718,
  "amount": 90.0,
  "description": "\ud83d\udc5f New Sneakers \ud83d\udc5f\ud83d\udd25",
  "created_at": "2023-05-05T23:53:47",
  "updated_at": "2023-05-05T23:53:47",
  "approved_at": null,
  "denied_at": null,
  "private": true,
  "sender": {
   "name": "Sherry Smith",
   "email": "she_bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4612,
  "amount": 42.0,
  "description": "Dance Class",
  "created_at": "2023-05-04T16:11:19",
  "updated_at": "2023-05-04T16:11:19",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Melissa Bailey",
   "email": "mel.bailey@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 3203,
  "amount": 55.0,
  "description": "Couples Massage \ud83d\udc86\ud83d\udc86",
  "created_at": "2023-05-03T00:33:55",
  "updated_at": "2023-05-03T00:33:55",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Tammy Weaver",
   "email": "ta.weav@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 5485,
  "amount": 14.0,
  "description": "\ud83d\udef5 Food Delivery for Lazy Day \ud83c\udf55",
  "created_at": "2023-05-02T00:07:07",
  "updated_at": "2023-05-02T00:07:07",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Gina Burch",
   "email": "gina-ritter@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 1873,
  "amount": 80.0,
  "description": "Electronics",
  "created_at": "2023-04-30T10:36:15",
  "updated_at": "2023-04-30T10:36:15",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Michael Burch",
   "email": "mi.burch@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 4326,
  "amount": 35.0,
  "description": "\ud83d\udc7b Haunted House Adventure \ud83c\udf83",
  "created_at": "2023-04-27T13:05:43",
  "updated_at": "2023-04-27T13:05:43",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Robert Martinez",
   "email": "robertmartinez@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 },
 {
  "payment_request_id": 3204,
  "amount": 87.0,
  "description": "Electronics",
  "created_at": "2023-04-19T18:11:20",
  "updated_at": "2023-04-19T18:11:20",
  "approved_at": null,
  "denied_at": null,
  "private": false,
  "sender": {
   "name": "Tammy Weaver",
   "email": "ta.weav@gmail.com"
  },
  "receiver": {
   "name": "Jose Harrison",
   "email": "joseharr@gmail.com"
  }
 }
]
```


### Environment Interaction 31
----------------------------------------------------------------------------
```python
apis.supervisor.complete_task()
```

```
Execution successful.
```

