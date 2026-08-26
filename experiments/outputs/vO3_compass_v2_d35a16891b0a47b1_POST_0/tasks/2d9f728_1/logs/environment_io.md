
### Environment Interaction 1
----------------------------------------------------------------------------
```python
<｜DSML｜print(apis.api_docs.show_app_descriptions())
```

```
Execution failed. Traceback:
Syntax error in line:
<｜DSML｜print(apis.api_docs.show_app_descriptions())
Message: invalid character '｜' (U+FF5C)
```


### Environment Interaction 2
----------------------------------------------------------------------------
```python
<｜DSML｜print(apis.api_docs.show_app_descriptions())
```

```
Execution failed. Traceback:
Syntax error in line:
<｜DSML｜print(apis.api_docs.show_app_descriptions())
Message: invalid character '｜' (U+FF5C)
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
<｜DSML｜print(apis.api_docs.show_app_descriptions())
```

```
Execution failed. Traceback:
Syntax error in line:
<｜DSML｜print(apis.api_docs.show_app_descriptions())
Message: invalid character '｜' (U+FF5C)
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
<｜DSML｜print(apis.api_docs.show_app_descriptions())
```

```
Execution failed. Traceback:
Syntax error in line:
<｜DSML｜print(apis.api_docs.show_app_descriptions())
Message: invalid character '｜' (U+FF5C)
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
<｜DSML｜print(apis.api_docs.show_app_descriptions())
```

```
Execution failed. Traceback:
Syntax error in line:
<｜DSML｜print(apis.api_docs.show_app_descriptions())
Message: invalid character '｜' (U+FF5C)
```


### Environment Interaction 6
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


### Environment Interaction 9
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='supervisor', api_name='show_profile'))
```

```
{
 "app_name": "supervisor",
 "api_name": "show_profile",
 "path": "/profile",
 "method": "GET",
 "description": "Show your supervisor's profile information.",
 "parameters": [],
 "response_schemas": {
  "success": {
   "first_name": "string",
   "last_name": "string",
   "email": "user@example.com",
   "phone_number": "string",
   "birthday": "string",
   "sex": "male"
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
print(apis.supervisor.show_profile())
```

```
{
 "first_name": "Troy",
 "last_name": "Solomon",
 "email": "tr_solo@gmail.com",
 "phone_number": "7273731063",
 "birthday": "1990-02-02",
 "sex": "male"
}
```


### Environment Interaction 11
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


### Environment Interaction 12
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


### Environment Interaction 13
----------------------------------------------------------------------------
```python
print(apis.supervisor.show_account_passwords())
```

```
[
 {
  "account_name": "amazon",
  "password": "Dd^+uzP"
 },
 {
  "account_name": "file_system",
  "password": "QF^61f3"
 },
 {
  "account_name": "gmail",
  "password": "*WytI+J"
 },
 {
  "account_name": "phone",
  "password": "u&Xg}+5"
 },
 {
  "account_name": "simple_note",
  "password": "jXbJu50"
 },
 {
  "account_name": "splitwise",
  "password": "mi)AdQ3"
 },
 {
  "account_name": "spotify",
  "password": "Q3c_DvY"
 },
 {
  "account_name": "todoist",
  "password": "=Z$WBI0"
 },
 {
  "account_name": "venmo",
  "password": "z*@]t]Q"
 }
]
```


### Environment Interaction 14
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


### Environment Interaction 15
----------------------------------------------------------------------------
```python
phone_password = [p['password'] for p in apis.supervisor.show_account_passwords() if p['account_name']=='phone'][0]
print(phone_password)
```

```
u&Xg}+5
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
phone_login = apis.phone.login(username='7273731063', password=phone_password)
print(phone_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwaG9uZSs3MjczNzMxMDYzIiwiZXhwIjoxNjg0NDEyMDk4fQ.jo0TktWpkHfQr2HWWPdBNOb_RCVSYDCCCzau-mi9hTc",
 "token_type": "Bearer"
}
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
phone_token = phone_login['access_token']
print(apis.phone.show_contact_relationships(access_token=phone_token))
```

```
["brother", "coworker", "father", "friend", "manager", "mother", "parent", "roommate", "sibling"]
```


### Environment Interaction 18
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


### Environment Interaction 19
----------------------------------------------------------------------------
```python
roommates = apis.phone.search_contacts(access_token=phone_token, relationship='roommate', page_limit=20)
print(roommates)
```

```
[
 {
  "contact_id": 202,
  "first_name": "Jordan",
  "last_name": "Harrison",
  "email": "jo-harr@gmail.com",
  "phone_number": "2254213734",
  "relationships": [
   "roommate"
  ],
  "birthday": "1988-04-06",
  "home_address": "4912 Morales Divide Suite 845\nSeattle\nWashington\nUnited States\n24529",
  "work_address": "8875 Amy Extensions Suite 797\nSeattle\nWashington\nUnited States\n49596",
  "created_at": "2022-06-27T09:28:38"
 },
 {
  "contact_id": 203,
  "first_name": "Kathryn",
  "last_name": "Maldonado",
  "email": "kathrynmaldonado@gmail.com",
  "phone_number": "2473084266",
  "relationships": [
   "roommate"
  ],
  "birthday": "1989-07-29",
  "home_address": "4912 Morales Divide Suite 845\nSeattle\nWashington\nUnited States\n24529",
  "work_address": "265 Carpenter Loop Suite 064\nSeattle\nWashington\nUnited States\n44564",
  "created_at": "2022-06-27T09:28:38"
 },
 {
  "contact_id": 204,
  "first_name": "Nancy",
  "last_name": "Ritter",
  "email": "nan_ritt@gmail.com",
  "phone_number": "2307354647",
  "relationships": [
   "roommate"
  ],
  "birthday": "1990-08-14",
  "home_address": "4912 Morales Divide Suite 845\nSeattle\nWashington\nUnited States\n24529",
  "work_address": "96967 Fox Loop Suite 397\nSeattle\nWashington\nUnited States\n86832",
  "created_at": "2022-06-27T09:28:38"
 }
]
```


### Environment Interaction 20
----------------------------------------------------------------------------
```python
# Get venmo password from supervisor account passwords
passwords = apis.supervisor.show_account_passwords()
venmo_password = [p['password'] for p in passwords if p['account_name'] == 'venmo'][0]
print(venmo_password)
```

```
z*@]t]Q
```


### Environment Interaction 21
----------------------------------------------------------------------------
```python
# Login to venmo using email and password
venmo_login = apis.venmo.login(username='tr_solo@gmail.com', password=venmo_password)
print(venmo_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2ZW5tbyt0cl9zb2xvQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjc0MX0.CnnFJ-eY44bM2SuBZSiYPVEJ2y6ltC8EDHnTzUyB6mg",
 "token_type": "Bearer"
}
```


### Environment Interaction 22
----------------------------------------------------------------------------
```python
# Search for roommates on Venmo to get their user IDs
jordan = apis.venmo.search_users(query='Jordan Harrison', access_token=venmo_login['access_token'])
print(jordan)
```

```
[
 {
  "first_name": "Jordan",
  "last_name": "Harrison",
  "email": "jo-harr@gmail.com",
  "registered_at": "2022-04-10T14:26:20",
  "friends_since": null
 },
 {
  "first_name": "Ronald",
  "last_name": "Harrison",
  "email": "ron.harrison@gmail.com",
  "registered_at": "2022-07-28T16:36:46",
  "friends_since": null
 },
 {
  "first_name": "Anthony",
  "last_name": "Harrison",
  "email": "an-harrison@gmail.com",
  "registered_at": "2022-12-23T16:09:19",
  "friends_since": null
 },
 {
  "first_name": "Christina",
  "last_name": "Harrison",
  "email": "chrharrison@gmail.com",
  "registered_at": "2022-10-01T16:49:36",
  "friends_since": null
 },
 {
  "first_name": "Jose",
  "last_name": "Harrison",
  "email": "joseharr@gmail.com",
  "registered_at": "2022-12-14T14:46:35",
  "friends_since": "2022-12-14T14:46:35"
 }
]
```


### Environment Interaction 23
----------------------------------------------------------------------------
```python
# Let's check the API docs for search_users, create_payment_request, and create_transaction
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='search_users'))
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='create_payment_request'))
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='create_transaction'))
```

```
{
 "app_name": "venmo",
 "api_name": "search_users",
 "path": "/users",
 "method": "GET",
 "description": "Search Venmo users by name or email address.",
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
   "name": "query",
   "type": "string",
   "required": false,
   "description": "Search query string.",
   "default": "",
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
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "registered_at": "2019-01-01T00:00:00",
    "friends_since": "2019-01-01T00:00:00"
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "venmo",
 "api_name": "create_payment_request",
 "path": "/payment_requests",
 "method": "POST",
 "description": "Send a payment request.",
 "parameters": [
  {
   "name": "user_email",
   "type": "string",
   "required": true,
   "description": "Email address of the receiver user.",
   "default": null,
   "constraints": [
    "value is email address"
   ]
  },
  {
   "name": "amount",
   "type": "number",
   "required": true,
   "description": "Amount of the payment request.",
   "default": null,
   "constraints": [
    "value > 0.0"
   ]
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
   "name": "description",
   "type": "string",
   "required": false,
   "description": "Description of or note about the payment request.",
   "default": "",
   "constraints": []
  },
  {
   "name": "private",
   "type": "boolean",
   "required": false,
   "description": "The privacy of the transaction on approval of the payment request.",
   "default": false,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string",
   "payment_request_id": 1
  },
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "venmo",
 "api_name": "create_transaction",
 "path": "/transactions",
 "method": "POST",
 "description": "Send money to a user.",
 "parameters": [
  {
   "name": "receiver_email",
   "type": "string",
   "required": true,
   "description": "Email address of the receiver.",
   "default": null,
   "constraints": [
    "value is email address"
   ]
  },
  {
   "name": "amount",
   "type": "number",
   "required": true,
   "description": "Amount of the transaction.",
   "default": null,
   "constraints": [
    "value > 0.0"
   ]
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
   "name": "description",
   "type": "string",
   "required": false,
   "description": "Description of or note about the transaction.",
   "default": "",
   "constraints": []
  },
  {
   "name": "payment_card_id",
   "type": "integer",
   "required": false,
   "description": "ID of the payment card to use for the transaction. If not passed, Venmo balance will be used.",
   "default": null,
   "constraints": []
  },
  {
   "name": "private",
   "type": "boolean",
   "required": false,
   "description": "Whether the transaction is private or not.",
   "default": false,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string",
   "transaction_id": 1
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
# Create taxi payment requests to each roommate (Jordan, Kathryn, Nancy) for $15 each
taxi_amount = 60 / 4  # 15
print(taxi_amount)
# Request from Jordan
print(apis.venmo.create_payment_request(user_email='jo-harr@gmail.com', amount=taxi_amount, access_token=venmo_login['access_token'], description='For Taxi'))
# Request from Kathryn
print(apis.venmo.create_payment_request(user_email='kathrynmaldonado@gmail.com', amount=taxi_amount, access_token=venmo_login['access_token'], description='For Taxi'))
# Request from Nancy
print(apis.venmo.create_payment_request(user_email='nan_ritt@gmail.com', amount=taxi_amount, access_token=venmo_login['access_token'], description='For Taxi'))
```

```
15.0
{"message": "Payment request created.", "payment_request_id": 6097}
{"message": "Payment request created.", "payment_request_id": 6098}
{"message": "Payment request created.", "payment_request_id": 6099}
```

