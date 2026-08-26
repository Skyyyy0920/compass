
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


### Environment Interaction 3
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


### Environment Interaction 4
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


### Environment Interaction 5
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


### Environment Interaction 6
----------------------------------------------------------------------------
```python
print(apis.supervisor.show_profile())
```

```
{
 "first_name": "Chris",
 "last_name": "Mccoy",
 "email": "chris.mcco@gmail.com",
 "phone_number": "5584932120",
 "birthday": "1983-01-02",
 "sex": "male"
}
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
print(apis.supervisor.show_account_passwords())
```

```
[
 {
  "account_name": "amazon",
  "password": "Wx^QHo8"
 },
 {
  "account_name": "file_system",
  "password": "m0[n5qo"
 },
 {
  "account_name": "gmail",
  "password": "-f1{_-l"
 },
 {
  "account_name": "phone",
  "password": "Bk}DNKG"
 },
 {
  "account_name": "simple_note",
  "password": "Zz4vl@x"
 },
 {
  "account_name": "splitwise",
  "password": "-*n{3zK"
 },
 {
  "account_name": "spotify",
  "password": "InHl^KB"
 },
 {
  "account_name": "todoist",
  "password": "RY^8!)h"
 },
 {
  "account_name": "venmo",
  "password": "+dXReKG"
 }
]
```


### Environment Interaction 8
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


### Environment Interaction 9
----------------------------------------------------------------------------
```python
phone_login = apis.phone.login(username='5584932120', password='Bk}DNKG')
print(phone_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwaG9uZSs1NTg0OTMyMTIwIiwiZXhwIjoxNjg0NDEyMDk4fQ.xO3VLGReZoxtTMB2ss9rlVfhiIZ2iby2yLB2ScxsgGc",
 "token_type": "Bearer"
}
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
phone_token = phone_login['access_token']
print(apis.phone.show_contact_relationships(access_token=phone_token))
```

```
["coworker", "father", "friend", "manager", "mother", "parent", "roommate"]
```


### Environment Interaction 11
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


### Environment Interaction 12
----------------------------------------------------------------------------
```python
coworkers = apis.phone.search_contacts(access_token=phone_token, relationship='coworker', page_limit=20)
friends = apis.phone.search_contacts(access_token=phone_token, relationship='friend', page_limit=20)
print("Coworkers:", coworkers)
print("Friends:", friends)
```

```
Coworkers: [{'contact_id': 38, 'first_name': 'Andrew', 'last_name': 'Brown', 'email': 'andrew_brow@gmail.com', 'phone_number': '8993579400', 'relationships': ['coworker'], 'birthday': '1987-12-14', 'home_address': '320 Wilson View Suite 812\nSeattle\nWashington\nUnited States\n65482', 'work_address': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 33, 'first_name': 'Chelsea', 'last_name': 'Burch', 'email': 'chelsea-burch@gmail.com', 'phone_number': '7763361246', 'relationships': ['coworker'], 'birthday': '1992-03-22', 'home_address': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'work_address': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 37, 'first_name': 'Eric', 'last_name': 'Bailey', 'email': 'eric.bailey@gmail.com', 'phone_number': '9272583586', 'relationships': ['manager', 'coworker'], 'birthday': '1961-06-16', 'home_address': '791 Alison Cove Suite 470\nSeattle\nWashington\nUnited States\n29793', 'work_address': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 36, 'first_name': 'Kyle', 'last_name': 'Moore', 'email': 'kyl_moor@gmail.com', 'phone_number': '6372953330', 'relationships': ['coworker'], 'birthday': '1961-11-20', 'home_address': '2027 Pacheco Shoals Suite 696\nSeattle\nWashington\nUnited States\n16258', 'work_address': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 35, 'first_name': 'Nicholas', 'last_name': 'Weber', 'email': 'nicholas.weber@gmail.com', 'phone_number': '9503658964', 'relationships': ['coworker'], 'birthday': '1986-10-19', 'home_address': '247 Salinas Pines Suite 668\nSeattle\nWashington\nUnited States\n11799', 'work_address': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 39, 'first_name': 'Patricia', 'last_name': 'Ritter', 'email': 'pa_ritter@gmail.com', 'phone_number': '2444880289', 'relationships': ['coworker'], 'birthday': '1960-09-12', 'home_address': '734 Amanda Manors Suite 691\nSeattle\nWashington\nUnited States\n88675', 'work_address': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 32, 'first_name': 'Susan', 'last_name': 'Burton', 'email': 'susanmiller@gmail.com', 'phone_number': '3296062648', 'relationships': ['coworker'], 'birthday': '1994-04-30', 'home_address': '816 Brittney Overpass Suite 48\nSeattle\nWashington\nUnited States\n44756', 'work_address': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 34, 'first_name': 'Valerie', 'last_name': 'Blackburn', 'email': 'va-blac@gmail.com', 'phone_number': '5822399497', 'relationships': ['coworker'], 'birthday': '1951-03-24', 'home_address': '8705 Jonathan Corners Suite 675\nSeattle\nWashington\nUnited States\n94623', 'work_address': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'created_at': '2022-06-15T04:09:48'}]
Friends: [{'contact_id': 42, 'first_name': 'Cheryl', 'last_name': 'Martinez', 'email': 'cheweber@gmail.com', 'phone_number': '3517418245', 'relationships': ['friend'], 'birthday': '1993-07-30', 'home_address': '897 Carter Spurs Suite 636\nSeattle\nWashington\nUnited States\n29431', 'work_address': '406 Lindsay Courts Suite 522\nSeattle\nWashington\nUnited States\n26281', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 43, 'first_name': 'Cody', 'last_name': 'Smith', 'email': 'cod.smith@gmail.com', 'phone_number': '7826309761', 'relationships': ['friend'], 'birthday': '1993-03-02', 'home_address': '8948 Owens Via Suite 628\nSeattle\nWashington\nUnited States\n75367', 'work_address': '7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 45, 'first_name': 'Cory', 'last_name': 'Wilson', 'email': 'corwils@gmail.com', 'phone_number': '5412564532', 'relationships': ['friend'], 'birthday': '1985-07-29', 'home_address': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'work_address': '406 Lindsay Courts Suite 522\nSeattle\nWashington\nUnited States\n26281', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 46, 'first_name': 'Grant', 'last_name': 'Martinez', 'email': 'gra-martinez@gmail.com', 'phone_number': '7056722825', 'relationships': ['friend'], 'birthday': '1990-04-24', 'home_address': '897 Carter Spurs Suite 636\nSeattle\nWashington\nUnited States\n29431', 'work_address': '7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 44, 'first_name': 'Travis', 'last_name': 'Wilson', 'email': 'tra_wils@gmail.com', 'phone_number': '7599900254', 'relationships': ['friend'], 'birthday': '1982-05-18', 'home_address': '31434 Mark Trail Suite 731\nSeattle\nWashington\nUnited States\n75765', 'work_address': '7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946', 'created_at': '2022-06-15T04:09:48'}, {'contact_id': 47, 'first_name': 'William', 'last_name': 'Martinez', 'email': 'william_mart@gmail.com', 'phone_number': '4429057162', 'relationships': ['friend'], 'birthday': '1996-05-06', 'home_address': '6990 Nunez Corners Suite 644\nSeattle\nWashington\nUnited States\n88977', 'work_address': '96967 Fox Loop Suite 397\nSeattle\nWashington\nUnited States\n86832', 'created_at': '2022-06-15T04:09:48'}]
```


### Environment Interaction 13
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


### Environment Interaction 14
----------------------------------------------------------------------------
```python
venmo_login = apis.venmo.login(username='chris.mcco@gmail.com', password='+dXReKG')
print(venmo_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2ZW5tbytjaHJpcy5tY2NvQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjc0MX0.Db27qY_vLx_qwJUtvxWG9fT2ELdJ1uWKptdNAm0HWGM",
 "token_type": "Bearer"
}
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='search_users'))
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
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='search_friends'))
```

```
{
 "app_name": "venmo",
 "api_name": "search_friends",
 "path": "/friends",
 "method": "GET",
 "description": "Search your or others' friends by name or email address.",
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
   "description": "Search friends by name or email address.",
   "default": "",
   "constraints": []
  },
  {
   "name": "user_email",
   "type": "string",
   "required": false,
   "description": "Email address of the user whose friends you want to see. If not passed, your friends will be returned.",
   "default": null,
   "constraints": [
    "value is email address"
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
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
venmo_token = venmo_login['access_token']
# Get all current venmo friends
all_friends = []
page = 0
while True:
    result = apis.venmo.search_friends(access_token=venmo_token, page_index=page, page_limit=20)
    if not result:
        break
    all_friends.extend(result)
    if len(result) < 20:
        break
    page += 1
print("Current venmo friends count:", len(all_friends))
print(all_friends)
```

```
Current venmo friends count: 9
[
 {
  "first_name": "Travis",
  "last_name": "Wilson",
  "email": "tra_wils@gmail.com",
  "registered_at": "2022-04-28T16:40:41",
  "friends_since": "2023-05-18T12:00:00"
 },
 {
  "first_name": "Cory",
  "last_name": "Wilson",
  "email": "corwils@gmail.com",
  "registered_at": "2022-08-29T18:50:33",
  "friends_since": "2023-05-18T12:00:00"
 },
 {
  "first_name": "Grant",
  "last_name": "Martinez",
  "email": "gra-martinez@gmail.com",
  "registered_at": "2022-11-17T11:34:25",
  "friends_since": "2023-05-18T12:00:00"
 },
 {
  "first_name": "Jose",
  "last_name": "Harrison",
  "email": "joseharr@gmail.com",
  "registered_at": "2022-12-14T14:46:35",
  "friends_since": "2023-05-18T12:00:00"
 },
 {
  "first_name": "Paul",
  "last_name": "Miller",
  "email": "paul_mill@gmail.com",
  "registered_at": "2022-06-26T10:55:47",
  "friends_since": "2023-05-18T12:00:00"
 },
 {
  "first_name": "Kyle",
  "last_name": "Moore",
  "email": "kyl_moor@gmail.com",
  "registered_at": "2022-11-01T15:16:37",
  "friends_since": "2023-05-18T12:00:00"
 },
 {
  "first_name": "Patricia",
  "last_name": "Ritter",
  "email": "pa_ritter@gmail.com",
  "registered_at": "2022-06-22T15:44:06",
  "friends_since": "2023-05-18T12:00:00"
 },
 {
  "first_name": "Valerie",
  "last_name": "Blackburn",
  "email": "va-blac@gmail.com",
  "registered_at": "2022-05-26T12:45:26",
  "friends_since": "2023-05-18T12:00:00"
 },
 {
  "first_name": "Susan",
  "last_name": "Burton",
  "email": "susanmiller@gmail.com",
  "registered_at": "2022-11-07T08:59:24",
  "friends_since": "2023-05-18T12:00:00"
 }
]
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='add_friend'))
```

```
{
 "app_name": "venmo",
 "api_name": "add_friend",
 "path": "/friends/{user_email}",
 "method": "POST",
 "description": "Add a friend to your friend list.",
 "parameters": [
  {
   "name": "user_email",
   "type": "string",
   "required": true,
   "description": "Email address of the friend to add.",
   "default": null,
   "constraints": [
    "value is email address"
   ]
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from venmo app login.",
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


### Environment Interaction 19
----------------------------------------------------------------------------
```python
# Get list of all coworkers and friends from phone contacts
coworkers = apis.phone.search_contacts(access_token=phone_token, relationship='coworker', page_limit=20)
friends = apis.phone.search_contacts(access_token=phone_token, relationship='friend', page_limit=20)

# Combine all contacts to add
contacts_to_add = coworkers + friends
print("Total contacts to consider:", len(contacts_to_add))

# Get current venmo friends emails
current_friend_emails = {f['email'] for f in all_friends}
print("Current friend emails:", current_friend_emails)

# Determine which contacts are not yet friends
to_add = [c for c in contacts_to_add if c['email'] not in current_friend_emails]
print("Contacts to add:", [(c['first_name'], c['last_name'], c['email']) for c in to_add])
```

```
Total contacts to consider: 14
Current friend emails: {'joseharr@gmail.com', 'gra-martinez@gmail.com', 'paul_mill@gmail.com', 'pa_ritter@gmail.com', 'susanmiller@gmail.com', 'kyl_moor@gmail.com', 'corwils@gmail.com', 'tra_wils@gmail.com', 'va-blac@gmail.com'}
Contacts to add: [('Andrew', 'Brown', 'andrew_brow@gmail.com'), ('Chelsea', 'Burch', 'chelsea-burch@gmail.com'), ('Eric', 'Bailey', 'eric.bailey@gmail.com'), ('Nicholas', 'Weber', 'nicholas.weber@gmail.com'), ('Cheryl', 'Martinez', 'cheweber@gmail.com'), ('Cody', 'Smith', 'cod.smith@gmail.com'), ('William', 'Martinez', 'william_mart@gmail.com')]
```


### Environment Interaction 20
----------------------------------------------------------------------------
```python
# Search for each contact to add on venmo to confirm they exist
for contact in to_add:
    email = contact['email']
    result = apis.venmo.search_users(access_token=venmo_token, query=email, page_limit=20)
    print(f"Search for {email}: {result}")
```

```
Search for andrew_brow@gmail.com: [{'first_name': 'Andrew', 'last_name': 'Brown', 'email': 'andrew_brow@gmail.com', 'registered_at': '2023-01-05T13:40:41', 'friends_since': None}, {'first_name': 'Stephen', 'last_name': 'Mccoy', 'email': 'stmcco@gmail.com', 'registered_at': '2023-01-24T12:51:50', 'friends_since': None}, {'first_name': 'Laura', 'last_name': 'Mccoy', 'email': 'la-mcco@gmail.com', 'registered_at': '2023-02-12T14:30:46', 'friends_since': None}, {'first_name': 'Jonathan', 'last_name': 'Ball', 'email': 'jo.ball@gmail.com', 'registered_at': '2022-08-26T16:01:41', 'friends_since': None}, {'first_name': 'Leslie', 'last_name': 'Ball', 'email': 'les_ball@gmail.com', 'registered_at': '2023-02-08T08:46:59', 'friends_since': None}, {'first_name': 'Bradley', 'last_name': 'Ball', 'email': 'bradley_ball@gmail.com', 'registered_at': '2022-04-27T18:22:21', 'friends_since': None}, {'first_name': 'Katherine', 'last_name': 'Smith', 'email': 'ka_ball@gmail.com', 'registered_at': '2022-04-25T18:24:54', 'friends_since': None}, {'first_name': 'Thomas', 'last_name': 'Solomon', 'email': 'thomas.solomon@gmail.com', 'registered_at': '2022-05-09T14:11:52', 'friends_since': None}, {'first_name': 'Jamie', 'last_name': 'Solomon', 'email': 'jamie-solomon@gmail.com', 'registered_at': '2023-01-17T09:00:50', 'friends_since': None}, {'first_name': 'James', 'last_name': 'Solomon', 'email': 'ja-solomon@gmail.com', 'registered_at': '2022-10-02T15:33:08', 'friends_since': None}, {'first_name': 'Troy', 'last_name': 'Solomon', 'email': 'tr_solo@gmail.com', 'registered_at': '2022-04-05T09:14:55', 'friends_since': None}, {'first_name': 'Ronald', 'last_name': 'Harrison', 'email': 'ron.harrison@gmail.com', 'registered_at': '2022-07-28T16:36:46', 'friends_since': None}, {'first_name': 'Christina', 'last_name': 'Harrison', 'email': 'chrharrison@gmail.com', 'registered_at': '2022-10-01T16:49:36', 'friends_since': None}, {'first_name': 'Jose', 'last_name': 'Harrison', 'email': 'joseharr@gmail.com', 'registered_at': '2022-12-14T14:46:35', 'friends_since': '2022-12-14T14:46:35'}, {'first_name': 'Jordan', 'last_name': 'Harrison', 'email': 'jo-harr@gmail.com', 'registered_at': '2022-04-10T14:26:20', 'friends_since': None}, {'first_name': 'Anthony', 'last_name': 'Harrison', 'email': 'an-harrison@gmail.com', 'registered_at': '2022-12-23T16:09:19', 'friends_since': None}, {'first_name': 'Morgan', 'last_name': 'Burton', 'email': 'morgan-harrison@gmail.com', 'registered_at': '2022-05-17T16:56:09', 'friends_since': None}, {'first_name': 'Richard', 'last_name': 'Riddle', 'email': 'ric.riddle@gmail.com', 'registered_at': '2022-05-29T10:21:21', 'friends_since': None}, {'first_name': 'Angela', 'last_name': 'Riddle', 'email': 'angriddle@gmail.com', 'registered_at': '2022-05-22T13:02:38', 'friends_since': None}, {'first_name': 'Alexander', 'last_name': 'Riddle', 'email': 'alexander-ridd@gmail.com', 'registered_at': '2022-11-11T17:28:44', 'friends_since': None}]
Search for chelsea-burch@gmail.com: [{'first_name': 'Chelsea', 'last_name': 'Burch', 'email': 'chelsea-burch@gmail.com', 'registered_at': '2023-01-29T10:18:37', 'friends_since': None}, {'first_name': 'Stephen', 'last_name': 'Mccoy', 'email': 'stmcco@gmail.com', 'registered_at': '2023-01-24T12:51:50', 'friends_since': None}, {'first_name': 'Laura', 'last_name': 'Mccoy', 'email': 'la-mcco@gmail.com', 'registered_at': '2023-02-12T14:30:46', 'friends_since': None}, {'first_name': 'Jonathan', 'last_name': 'Ball', 'email': 'jo.ball@gmail.com', 'registered_at': '2022-08-26T16:01:41', 'friends_since': None}, {'first_name': 'Leslie', 'last_name': 'Ball', 'email': 'les_ball@gmail.com', 'registered_at': '2023-02-08T08:46:59', 'friends_since': None}, {'first_name': 'Bradley', 'last_name': 'Ball', 'email': 'bradley_ball@gmail.com', 'registered_at': '2022-04-27T18:22:21', 'friends_since': None}, {'first_name': 'Katherine', 'last_name': 'Smith', 'email': 'ka_ball@gmail.com', 'registered_at': '2022-04-25T18:24:54', 'friends_since': None}, {'first_name': 'Thomas', 'last_name': 'Solomon', 'email': 'thomas.solomon@gmail.com', 'registered_at': '2022-05-09T14:11:52', 'friends_since': None}, {'first_name': 'Jamie', 'last_name': 'Solomon', 'email': 'jamie-solomon@gmail.com', 'registered_at': '2023-01-17T09:00:50', 'friends_since': None}, {'first_name': 'James', 'last_name': 'Solomon', 'email': 'ja-solomon@gmail.com', 'registered_at': '2022-10-02T15:33:08', 'friends_since': None}, {'first_name': 'Troy', 'last_name': 'Solomon', 'email': 'tr_solo@gmail.com', 'registered_at': '2022-04-05T09:14:55', 'friends_since': None}, {'first_name': 'Ronald', 'last_name': 'Harrison', 'email': 'ron.harrison@gmail.com', 'registered_at': '2022-07-28T16:36:46', 'friends_since': None}, {'first_name': 'Christina', 'last_name': 'Harrison', 'email': 'chrharrison@gmail.com', 'registered_at': '2022-10-01T16:49:36', 'friends_since': None}, {'first_name': 'Jose', 'last_name': 'Harrison', 'email': 'joseharr@gmail.com', 'registered_at': '2022-12-14T14:46:35', 'friends_since': '2022-12-14T14:46:35'}, {'first_name': 'Jordan', 'last_name': 'Harrison', 'email': 'jo-harr@gmail.com', 'registered_at': '2022-04-10T14:26:20', 'friends_since': None}, {'first_name': 'Anthony', 'last_name': 'Harrison', 'email': 'an-harrison@gmail.com', 'registered_at': '2022-12-23T16:09:19', 'friends_since': None}, {'first_name': 'Morgan', 'last_name': 'Burton', 'email': 'morgan-harrison@gmail.com', 'registered_at': '2022-05-17T16:56:09', 'friends_since': None}, {'first_name': 'Richard', 'last_name': 'Riddle', 'email': 'ric.riddle@gmail.com', 'registered_at': '2022-05-29T10:21:21', 'friends_since': None}, {'first_name': 'Angela', 'last_name': 'Riddle', 'email': 'angriddle@gmail.com', 'registered_at': '2022-05-22T13:02:38', 'friends_since': None}, {'first_name': 'Alexander', 'last_name': 'Riddle', 'email': 'alexander-ridd@gmail.com', 'registered_at': '2022-11-11T17:28:44', 'friends_since': None}]
Search for eric.bailey@gmail.com: [{'first_name': 'Eric', 'last_name': 'Bailey', 'email': 'eric.bailey@gmail.com', 'registered_at': '2022-08-29T12:35:03', 'friends_since': None}, {'first_name': 'Stephen', 'last_name': 'Mccoy', 'email': 'stmcco@gmail.com', 'registered_at': '2023-01-24T12:51:50', 'friends_since': None}, {'first_name': 'Laura', 'last_name': 'Mccoy', 'email': 'la-mcco@gmail.com', 'registered_at': '2023-02-12T14:30:46', 'friends_since': None}, {'first_name': 'Jonathan', 'last_name': 'Ball', 'email': 'jo.ball@gmail.com', 'registered_at': '2022-08-26T16:01:41', 'friends_since': None}, {'first_name': 'Leslie', 'last_name': 'Ball', 'email': 'les_ball@gmail.com', 'registered_at': '2023-02-08T08:46:59', 'friends_since': None}, {'first_name': 'Bradley', 'last_name': 'Ball', 'email': 'bradley_ball@gmail.com', 'registered_at': '2022-04-27T18:22:21', 'friends_since': None}, {'first_name': 'Katherine', 'last_name': 'Smith', 'email': 'ka_ball@gmail.com', 'registered_at': '2022-04-25T18:24:54', 'friends_since': None}, {'first_name': 'Thomas', 'last_name': 'Solomon', 'email': 'thomas.solomon@gmail.com', 'registered_at': '2022-05-09T14:11:52', 'friends_since': None}, {'first_name': 'Jamie', 'last_name': 'Solomon', 'email': 'jamie-solomon@gmail.com', 'registered_at': '2023-01-17T09:00:50', 'friends_since': None}, {'first_name': 'James', 'last_name': 'Solomon', 'email': 'ja-solomon@gmail.com', 'registered_at': '2022-10-02T15:33:08', 'friends_since': None}, {'first_name': 'Troy', 'last_name': 'Solomon', 'email': 'tr_solo@gmail.com', 'registered_at': '2022-04-05T09:14:55', 'friends_since': None}, {'first_name': 'Ronald', 'last_name': 'Harrison', 'email': 'ron.harrison@gmail.com', 'registered_at': '2022-07-28T16:36:46', 'friends_since': None}, {'first_name': 'Christina', 'last_name': 'Harrison', 'email': 'chrharrison@gmail.com', 'registered_at': '2022-10-01T16:49:36', 'friends_since': None}, {'first_name': 'Jose', 'last_name': 'Harrison', 'email': 'joseharr@gmail.com', 'registered_at': '2022-12-14T14:46:35', 'friends_since': '2022-12-14T14:46:35'}, {'first_name': 'Jordan', 'last_name': 'Harrison', 'email': 'jo-harr@gmail.com', 'registered_at': '2022-04-10T14:26:20', 'friends_since': None}, {'first_name': 'Anthony', 'last_name': 'Harrison', 'email': 'an-harrison@gmail.com', 'registered_at': '2022-12-23T16:09:19', 'friends_since': None}, {'first_name': 'Morgan', 'last_name': 'Burton', 'email': 'morgan-harrison@gmail.com', 'registered_at': '2022-05-17T16:56:09', 'friends_since': None}, {'first_name': 'Richard', 'last_name': 'Riddle', 'email': 'ric.riddle@gmail.com', 'registered_at': '2022-05-29T10:21:21', 'friends_since': None}, {'first_name': 'Angela', 'last_name': 'Riddle', 'email': 'angriddle@gmail.com', 'registered_at': '2022-05-22T13:02:38', 'friends_since': None}, {'first_name': 'Alexander', 'last_name': 'Riddle', 'email': 'alexander-ridd@gmail.com', 'registered_at': '2022-11-11T17:28:44', 'friends_since': None}]
Search for nicholas.weber@gmail.com: [{'first_name': 'Nicholas', 'last_name': 'Weber', 'email': 'nicholas.weber@gmail.com', 'registered_at': '2022-03-24T17:16:25', 'friends_since': None}, {'first_name': 'Stephen', 'last_name': 'Mccoy', 'email': 'stmcco@gmail.com', 'registered_at': '2023-01-24T12:51:50', 'friends_since': None}, {'first_name': 'Laura', 'last_name': 'Mccoy', 'email': 'la-mcco@gmail.com', 'registered_at': '2023-02-12T14:30:46', 'friends_since': None}, {'first_name': 'Jonathan', 'last_name': 'Ball', 'email': 'jo.ball@gmail.com', 'registered_at': '2022-08-26T16:01:41', 'friends_since': None}, {'first_name': 'Leslie', 'last_name': 'Ball', 'email': 'les_ball@gmail.com', 'registered_at': '2023-02-08T08:46:59', 'friends_since': None}, {'first_name': 'Bradley', 'last_name': 'Ball', 'email': 'bradley_ball@gmail.com', 'registered_at': '2022-04-27T18:22:21', 'friends_since': None}, {'first_name': 'Katherine', 'last_name': 'Smith', 'email': 'ka_ball@gmail.com', 'registered_at': '2022-04-25T18:24:54', 'friends_since': None}, {'first_name': 'Thomas', 'last_name': 'Solomon', 'email': 'thomas.solomon@gmail.com', 'registered_at': '2022-05-09T14:11:52', 'friends_since': None}, {'first_name': 'Jamie', 'last_name': 'Solomon', 'email': 'jamie-solomon@gmail.com', 'registered_at': '2023-01-17T09:00:50', 'friends_since': None}, {'first_name': 'James', 'last_name': 'Solomon', 'email': 'ja-solomon@gmail.com', 'registered_at': '2022-10-02T15:33:08', 'friends_since': None}, {'first_name': 'Troy', 'last_name': 'Solomon', 'email': 'tr_solo@gmail.com', 'registered_at': '2022-04-05T09:14:55', 'friends_since': None}, {'first_name': 'Ronald', 'last_name': 'Harrison', 'email': 'ron.harrison@gmail.com', 'registered_at': '2022-07-28T16:36:46', 'friends_since': None}, {'first_name': 'Christina', 'last_name': 'Harrison', 'email': 'chrharrison@gmail.com', 'registered_at': '2022-10-01T16:49:36', 'friends_since': None}, {'first_name': 'Jose', 'last_name': 'Harrison', 'email': 'joseharr@gmail.com', 'registered_at': '2022-12-14T14:46:35', 'friends_since': '2022-12-14T14:46:35'}, {'first_name': 'Jordan', 'last_name': 'Harrison', 'email': 'jo-harr@gmail.com', 'registered_at': '2022-04-10T14:26:20', 'friends_since': None}, {'first_name': 'Anthony', 'last_name': 'Harrison', 'email': 'an-harrison@gmail.com', 'registered_at': '2022-12-23T16:09:19', 'friends_since': None}, {'first_name': 'Morgan', 'last_name': 'Burton', 'email': 'morgan-harrison@gmail.com', 'registered_at': '2022-05-17T16:56:09', 'friends_since': None}, {'first_name': 'Richard', 'last_name': 'Riddle', 'email': 'ric.riddle@gmail.com', 'registered_at': '2022-05-29T10:21:21', 'friends_since': None}, {'first_name': 'Angela', 'last_name': 'Riddle', 'email': 'angriddle@gmail.com', 'registered_at': '2022-05-22T13:02:38', 'friends_since': None}, {'first_name': 'Alexander', 'last_name': 'Riddle', 'email': 'alexander-ridd@gmail.com', 'registered_at': '2022-11-11T17:28:44', 'friends_since': None}]
Search for cheweber@gmail.com: [{'first_name': 'Cheryl', 'last_name': 'Martinez', 'email': 'cheweber@gmail.com', 'registered_at': '2022-03-22T18:57:46', 'friends_since': None}, {'first_name': 'Stephen', 'last_name': 'Mccoy', 'email': 'stmcco@gmail.com', 'registered_at': '2023-01-24T12:51:50', 'friends_since': None}, {'first_name': 'Laura', 'last_name': 'Mccoy', 'email': 'la-mcco@gmail.com', 'registered_at': '2023-02-12T14:30:46', 'friends_since': None}, {'first_name': 'Jonathan', 'last_name': 'Ball', 'email': 'jo.ball@gmail.com', 'registered_at': '2022-08-26T16:01:41', 'friends_since': None}, {'first_name': 'Leslie', 'last_name': 'Ball', 'email': 'les_ball@gmail.com', 'registered_at': '2023-02-08T08:46:59', 'friends_since': None}, {'first_name': 'Bradley', 'last_name': 'Ball', 'email': 'bradley_ball@gmail.com', 'registered_at': '2022-04-27T18:22:21', 'friends_since': None}, {'first_name': 'Katherine', 'last_name': 'Smith', 'email': 'ka_ball@gmail.com', 'registered_at': '2022-04-25T18:24:54', 'friends_since': None}, {'first_name': 'Thomas', 'last_name': 'Solomon', 'email': 'thomas.solomon@gmail.com', 'registered_at': '2022-05-09T14:11:52', 'friends_since': None}, {'first_name': 'Jamie', 'last_name': 'Solomon', 'email': 'jamie-solomon@gmail.com', 'registered_at': '2023-01-17T09:00:50', 'friends_since': None}, {'first_name': 'James', 'last_name': 'Solomon', 'email': 'ja-solomon@gmail.com', 'registered_at': '2022-10-02T15:33:08', 'friends_since': None}, {'first_name': 'Troy', 'last_name': 'Solomon', 'email': 'tr_solo@gmail.com', 'registered_at': '2022-04-05T09:14:55', 'friends_since': None}, {'first_name': 'Ronald', 'last_name': 'Harrison', 'email': 'ron.harrison@gmail.com', 'registered_at': '2022-07-28T16:36:46', 'friends_since': None}, {'first_name': 'Christina', 'last_name': 'Harrison', 'email': 'chrharrison@gmail.com', 'registered_at': '2022-10-01T16:49:36', 'friends_since': None}, {'first_name': 'Jose', 'last_name': 'Harrison', 'email': 'joseharr@gmail.com', 'registered_at': '2022-12-14T14:46:35', 'friends_since': '2022-12-14T14:46:35'}, {'first_name': 'Jordan', 'last_name': 'Harrison', 'email': 'jo-harr@gmail.com', 'registered_at': '2022-04-10T14:26:20', 'friends_since': None}, {'first_name': 'Anthony', 'last_name': 'Harrison', 'email': 'an-harrison@gmail.com', 'registered_at': '2022-12-23T16:09:19', 'friends_since': None}, {'first_name': 'Morgan', 'last_name': 'Burton', 'email': 'morgan-harrison@gmail.com', 'registered_at': '2022-05-17T16:56:09', 'friends_since': None}, {'first_name': 'Richard', 'last_name': 'Riddle', 'email': 'ric.riddle@gmail.com', 'registered_at': '2022-05-29T10:21:21', 'friends_since': None}, {'first_name': 'Angela', 'last_name': 'Riddle', 'email': 'angriddle@gmail.com', 'registered_at': '2022-05-22T13:02:38', 'friends_since': None}, {'first_name': 'Alexander', 'last_name': 'Riddle', 'email': 'alexander-ridd@gmail.com', 'registered_at': '2022-11-11T17:28:44', 'friends_since': None}]
Search for cod.smith@gmail.com: [{'first_name': 'Cody', 'last_name': 'Smith', 'email': 'cod.smith@gmail.com', 'registered_at': '2023-01-05T14:36:26', 'friends_since': None}, {'first_name': 'Stephen', 'last_name': 'Mccoy', 'email': 'stmcco@gmail.com', 'registered_at': '2023-01-24T12:51:50', 'friends_since': None}, {'first_name': 'Laura', 'last_name': 'Mccoy', 'email': 'la-mcco@gmail.com', 'registered_at': '2023-02-12T14:30:46', 'friends_since': None}, {'first_name': 'Jonathan', 'last_name': 'Ball', 'email': 'jo.ball@gmail.com', 'registered_at': '2022-08-26T16:01:41', 'friends_since': None}, {'first_name': 'Leslie', 'last_name': 'Ball', 'email': 'les_ball@gmail.com', 'registered_at': '2023-02-08T08:46:59', 'friends_since': None}, {'first_name': 'Bradley', 'last_name': 'Ball', 'email': 'bradley_ball@gmail.com', 'registered_at': '2022-04-27T18:22:21', 'friends_since': None}, {'first_name': 'Katherine', 'last_name': 'Smith', 'email': 'ka_ball@gmail.com', 'registered_at': '2022-04-25T18:24:54', 'friends_since': None}, {'first_name': 'Thomas', 'last_name': 'Solomon', 'email': 'thomas.solomon@gmail.com', 'registered_at': '2022-05-09T14:11:52', 'friends_since': None}, {'first_name': 'Jamie', 'last_name': 'Solomon', 'email': 'jamie-solomon@gmail.com', 'registered_at': '2023-01-17T09:00:50', 'friends_since': None}, {'first_name': 'James', 'last_name': 'Solomon', 'email': 'ja-solomon@gmail.com', 'registered_at': '2022-10-02T15:33:08', 'friends_since': None}, {'first_name': 'Troy', 'last_name': 'Solomon', 'email': 'tr_solo@gmail.com', 'registered_at': '2022-04-05T09:14:55', 'friends_since': None}, {'first_name': 'Ronald', 'last_name': 'Harrison', 'email': 'ron.harrison@gmail.com', 'registered_at': '2022-07-28T16:36:46', 'friends_since': None}, {'first_name': 'Christina', 'last_name': 'Harrison', 'email': 'chrharrison@gmail.com', 'registered_at': '2022-10-01T16:49:36', 'friends_since': None}, {'first_name': 'Jose', 'last_name': 'Harrison', 'email': 'joseharr@gmail.com', 'registered_at': '2022-12-14T14:46:35', 'friends_since': '2022-12-14T14:46:35'}, {'first_name': 'Jordan', 'last_name': 'Harrison', 'email': 'jo-harr@gmail.com', 'registered_at': '2022-04-10T14:26:20', 'friends_since': None}, {'first_name': 'Anthony', 'last_name': 'Harrison', 'email': 'an-harrison@gmail.com', 'registered_at': '2022-12-23T16:09:19', 'friends_since': None}, {'first_name': 'Morgan', 'last_name': 'Burton', 'email': 'morgan-harrison@gmail.com', 'registered_at': '2022-05-17T16:56:09', 'friends_since': None}, {'first_name': 'Richard', 'last_name': 'Riddle', 'email': 'ric.riddle@gmail.com', 'registered_at': '2022-05-29T10:21:21', 'friends_since': None}, {'first_name': 'Angela', 'last_name': 'Riddle', 'email': 'angriddle@gmail.com', 'registered_at': '2022-05-22T13:02:38', 'friends_since': None}, {'first_name': 'Alexander', 'last_name': 'Riddle', 'email': 'alexander-ridd@gmail.com', 'registered_at': '2022-11-11T17:28:44', 'friends_since': None}]
Search for william_mart@gmail.com: [{'first_name': 'William', 'last_name': 'Martinez', 'email': 'william_mart@gmail.com', 'registered_at': '2023-01-09T09:09:20', 'friends_since': None}, {'first_name': 'Stephen', 'last_name': 'Mccoy', 'email': 'stmcco@gmail.com', 'registered_at': '2023-01-24T12:51:50', 'friends_since': None}, {'first_name': 'Laura', 'last_name': 'Mccoy', 'email': 'la-mcco@gmail.com', 'registered_at': '2023-02-12T14:30:46', 'friends_since': None}, {'first_name': 'Jonathan', 'last_name': 'Ball', 'email': 'jo.ball@gmail.com', 'registered_at': '2022-08-26T16:01:41', 'friends_since': None}, {'first_name': 'Leslie', 'last_name': 'Ball', 'email': 'les_ball@gmail.com', 'registered_at': '2023-02-08T08:46:59', 'friends_since': None}, {'first_name': 'Bradley', 'last_name': 'Ball', 'email': 'bradley_ball@gmail.com', 'registered_at': '2022-04-27T18:22:21', 'friends_since': None}, {'first_name': 'Katherine', 'last_name': 'Smith', 'email': 'ka_ball@gmail.com', 'registered_at': '2022-04-25T18:24:54', 'friends_since': None}, {'first_name': 'Thomas', 'last_name': 'Solomon', 'email': 'thomas.solomon@gmail.com', 'registered_at': '2022-05-09T14:11:52', 'friends_since': None}, {'first_name': 'Jamie', 'last_name': 'Solomon', 'email': 'jamie-solomon@gmail.com', 'registered_at': '2023-01-17T09:00:50', 'friends_since': None}, {'first_name': 'James', 'last_name': 'Solomon', 'email': 'ja-solomon@gmail.com', 'registered_at': '2022-10-02T15:33:08', 'friends_since': None}, {'first_name': 'Troy', 'last_name': 'Solomon', 'email': 'tr_solo@gmail.com', 'registered_at': '2022-04-05T09:14:55', 'friends_since': None}, {'first_name': 'Ronald', 'last_name': 'Harrison', 'email': 'ron.harrison@gmail.com', 'registered_at': '2022-07-28T16:36:46', 'friends_since': None}, {'first_name': 'Christina', 'last_name': 'Harrison', 'email': 'chrharrison@gmail.com', 'registered_at': '2022-10-01T16:49:36', 'friends_since': None}, {'first_name': 'Jose', 'last_name': 'Harrison', 'email': 'joseharr@gmail.com', 'registered_at': '2022-12-14T14:46:35', 'friends_since': '2022-12-14T14:46:35'}, {'first_name': 'Jordan', 'last_name': 'Harrison', 'email': 'jo-harr@gmail.com', 'registered_at': '2022-04-10T14:26:20', 'friends_since': None}, {'first_name': 'Anthony', 'last_name': 'Harrison', 'email': 'an-harrison@gmail.com', 'registered_at': '2022-12-23T16:09:19', 'friends_since': None}, {'first_name': 'Morgan', 'last_name': 'Burton', 'email': 'morgan-harrison@gmail.com', 'registered_at': '2022-05-17T16:56:09', 'friends_since': None}, {'first_name': 'Richard', 'last_name': 'Riddle', 'email': 'ric.riddle@gmail.com', 'registered_at': '2022-05-29T10:21:21', 'friends_since': None}, {'first_name': 'Angela', 'last_name': 'Riddle', 'email': 'angriddle@gmail.com', 'registered_at': '2022-05-22T13:02:38', 'friends_since': None}, {'first_name': 'Alexander', 'last_name': 'Riddle', 'email': 'alexander-ridd@gmail.com', 'registered_at': '2022-11-11T17:28:44', 'friends_since': None}]
```


### Environment Interaction 21
----------------------------------------------------------------------------
```python
# Add each contact as a friend on venmo
for contact in to_add:
    email = contact['email']
    result = apis.venmo.add_friend(access_token=venmo_token, user_email=email)
    print(f"Adding {email}: {result}")
```

```
Adding andrew_brow@gmail.com: {'message': 'Added to your friend list.'}
Adding chelsea-burch@gmail.com: {'message': 'Added to your friend list.'}
Adding eric.bailey@gmail.com: {'message': 'Added to your friend list.'}
Adding nicholas.weber@gmail.com: {'message': 'Added to your friend list.'}
Adding cheweber@gmail.com: {'message': 'Added to your friend list.'}
Adding cod.smith@gmail.com: {'message': 'Added to your friend list.'}
Adding william_mart@gmail.com: {'message': 'Added to your friend list.'}
```


### Environment Interaction 22
----------------------------------------------------------------------------
```python
# Verify all contacts are now friends
all_friends_after = []
page = 0
while True:
    result = apis.venmo.search_friends(access_token=venmo_token, page_index=page, page_limit=20)
    if not result:
        break
    all_friends_after.extend(result)
    if len(result) < 20:
        break
    page += 1

friend_emails_after = {f['email'] for f in all_friends_after}
print("Total friends now:", len(all_friends_after))
print("All contacts added:", all(c['email'] in friend_emails_after for c in contacts_to_add))
```

```
Total friends now: 16
All contacts added: True
```


### Environment Interaction 23
----------------------------------------------------------------------------
```python
apis.supervisor.complete_task()
```

```
Execution successful.
```

