
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
# Let's explore the phone and venmo APIs.
print(apis.api_docs.show_api_descriptions(app_name='phone'))
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


### Environment Interaction 3
----------------------------------------------------------------------------
```python
# Let's look at the phone contacts API and venmo friends API docs.
print(apis.api_docs.show_api_doc(app_name='phone', api_name='show_contact_relationships'))
print(apis.api_docs.show_api_doc(app_name='phone', api_name='search_contacts'))
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='search_friends'))
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='add_friend'))
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='remove_friend'))
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
{
 "app_name": "venmo",
 "api_name": "remove_friend",
 "path": "/friends/{user_email}",
 "method": "DELETE",
 "description": "Remove a friend from your friend list.",
 "parameters": [
  {
   "name": "user_email",
   "type": "string",
   "required": true,
   "description": "Email address of the friend to remove.",
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


### Environment Interaction 4
----------------------------------------------------------------------------
```python
# Let's get the supervisor account credentials and login docs for phone and venmo.
print(apis.api_docs.show_api_doc(app_name='supervisor', api_name='show_account_passwords'))
print(apis.api_docs.show_api_doc(app_name='phone', api_name='login'))
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='login'))
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


### Environment Interaction 5
----------------------------------------------------------------------------
```python
# Get the account passwords from supervisor.
print(apis.supervisor.show_account_passwords())
```

```
[
 {
  "account_name": "amazon",
  "password": "5ge[KtE"
 },
 {
  "account_name": "file_system",
  "password": "tXQIUXl"
 },
 {
  "account_name": "gmail",
  "password": "69#=*3m"
 },
 {
  "account_name": "phone",
  "password": "wvIIPNe"
 },
 {
  "account_name": "simple_note",
  "password": "]ic5XP5"
 },
 {
  "account_name": "splitwise",
  "password": "*Yzj$iQ"
 },
 {
  "account_name": "spotify",
  "password": "&vSsyZ1"
 },
 {
  "account_name": "todoist",
  "password": "]dI#3dt"
 },
 {
  "account_name": "venmo",
  "password": "UIK!=rI"
 }
]
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
# Login to phone app using phone number and password.
phone_login = apis.phone.login(username='3643463570', password='wvIIPNe')
print(phone_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwaG9uZSszNjQzNDYzNTcwIiwiZXhwIjoxNjg0NDEyMDk4fQ.ZFQUPodJE26UEOFv1hdB1TZ5KINEyfNCENr0jlIt5vQ",
 "token_type": "Bearer"
}
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
# Login to venmo app using email and password.
venmo_login = apis.venmo.login(username='anita.burch@gmail.com', password='UIK!=rI')
print(venmo_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2ZW5tbythbml0YS5idXJjaEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTI3NDF9._UndgIF_4PAEnQz7Yn55jPuCVCIe_qecNjfXeJ6DkWo",
 "token_type": "Bearer"
}
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Let's check the phone contacts API documentation to understand how to get all contacts.
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


### Environment Interaction 9
----------------------------------------------------------------------------
```python
# Let's check the venmo search_friends API documentation.
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


### Environment Interaction 10
----------------------------------------------------------------------------
```python
# Get all phone contacts with pagination.
phone_token = phone_login['access_token']
all_phone_contacts = []
page_index = 0
page_limit = 20
while True:
    contacts = apis.phone.search_contacts(access_token=phone_token, page_index=page_index, page_limit=page_limit)
    if not contacts:
        break
    all_phone_contacts.extend(contacts)
    if len(contacts) < page_limit:
        break
    page_index += 1
print(f"Total phone contacts: {len(all_phone_contacts)}")
print(all_phone_contacts)
```

```
Total phone contacts: 27
[
 {
  "contact_id": 727,
  "first_name": "Allison",
  "last_name": "Calhoun",
  "email": "allison-calhoun@gmail.com",
  "phone_number": "3767193416",
  "relationships": [
   "coworker"
  ],
  "birthday": "1960-05-20",
  "home_address": "7183 Mckinney Stravenue Suite 7\nSeattle\nWashington\nUnited States\n55442",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 748,
  "first_name": "Anthony",
  "last_name": "Harrison",
  "email": "an-harrison@gmail.com",
  "phone_number": "2466064078",
  "relationships": [
   "roommate"
  ],
  "birthday": "1990-06-09",
  "home_address": "247 Salinas Pines Suite 668\nSeattle\nWashington\nUnited States\n11799",
  "work_address": "96967 Fox Loop Suite 397\nSeattle\nWashington\nUnited States\n86832",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 736,
  "first_name": "Caitlin",
  "last_name": "Burch",
  "email": "caiburc@gmail.com",
  "phone_number": "5896230193",
  "relationships": [
   "parent",
   "mother"
  ],
  "birthday": "1962-09-05",
  "home_address": "4380 Sosa Orchard Suite 194\nSeattle\nWashington\nUnited States\n73131",
  "work_address": "80547 Cynthia Square Suite 842\nSeattle\nWashington\nUnited States\n78964",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 735,
  "first_name": "Christopher",
  "last_name": "Burch",
  "email": "ch-burch@gmail.com",
  "phone_number": "4275730168",
  "relationships": [
   "parent",
   "father"
  ],
  "birthday": "1961-03-17",
  "home_address": "4380 Sosa Orchard Suite 194\nSeattle\nWashington\nUnited States\n73131",
  "work_address": "5840 Craig Turnpike Suite 634\nSeattle\nWashington\nUnited States\n78487",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 738,
  "first_name": "Chelsea",
  "last_name": "Burch",
  "email": "chelsea-burch@gmail.com",
  "phone_number": "7763361246",
  "relationships": [
   "sibling",
   "sister"
  ],
  "birthday": "1992-03-22",
  "home_address": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "work_address": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 728,
  "first_name": "Cody",
  "last_name": "Smith",
  "email": "cod.smith@gmail.com",
  "phone_number": "7826309761",
  "relationships": [
   "coworker"
  ],
  "birthday": "1993-03-02",
  "home_address": "8948 Owens Via Suite 628\nSeattle\nWashington\nUnited States\n75367",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 745,
  "first_name": "Cory",
  "last_name": "Wilson",
  "email": "corwils@gmail.com",
  "phone_number": "5412564532",
  "relationships": [
   "friend"
  ],
  "birthday": "1985-07-29",
  "home_address": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "work_address": "406 Lindsay Courts Suite 522\nSeattle\nWashington\nUnited States\n26281",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 747,
  "first_name": "Debra",
  "last_name": "Ritter",
  "email": "de_ritt@gmail.com",
  "phone_number": "3375602296",
  "relationships": [
   "friend"
  ],
  "birthday": "1994-11-30",
  "home_address": "5309 Rios Cliff Suite 287\nSeattle\nWashington\nUnited States\n84348",
  "work_address": "162 Smith Lake Suite 664\nSeattle\nWashington\nUnited States\n18461",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 739,
  "first_name": "Denise",
  "last_name": "Maldonado",
  "email": "deniseburch@gmail.com",
  "phone_number": "6279200672",
  "relationships": [
   "sibling",
   "sister"
  ],
  "birthday": "1994-08-14",
  "home_address": "727 Cannon Falls Suite 933\nSeattle\nWashington\nUnited States\n74687",
  "work_address": "265 Carpenter Loop Suite 064\nSeattle\nWashington\nUnited States\n44564",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 730,
  "first_name": "Grant",
  "last_name": "Martinez",
  "email": "gra-martinez@gmail.com",
  "phone_number": "7056722825",
  "relationships": [
   "coworker"
  ],
  "birthday": "1990-04-24",
  "home_address": "897 Carter Spurs Suite 636\nSeattle\nWashington\nUnited States\n29431",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 725,
  "first_name": "Jamie",
  "last_name": "Solomon",
  "email": "jamie-solomon@gmail.com",
  "phone_number": "8456546003",
  "relationships": [
   "manager",
   "coworker"
  ],
  "birthday": "1960-09-19",
  "home_address": "2317 Powell Stream Suite 570\nSeattle\nWashington\nUnited States\n32418",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 741,
  "first_name": "Jennifer",
  "last_name": "Powell",
  "email": "jepowell@gmail.com",
  "phone_number": "4288705164",
  "relationships": [
   "friend"
  ],
  "birthday": "1989-09-21",
  "home_address": "34495 Michael Burg Suite 805\nSeattle\nWashington\nUnited States\n38887",
  "work_address": "3850 Timothy Squares Suite 942\nSeattle\nWashington\nUnited States\n54179",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 740,
  "first_name": "Jordan",
  "last_name": "Harrison",
  "email": "jo-harr@gmail.com",
  "phone_number": "2254213734",
  "relationships": [
   "friend"
  ],
  "birthday": "1988-04-06",
  "home_address": "4912 Morales Divide Suite 845\nSeattle\nWashington\nUnited States\n24529",
  "work_address": "8875 Amy Extensions Suite 797\nSeattle\nWashington\nUnited States\n49596",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 734,
  "first_name": "Kayla",
  "last_name": "Burton",
  "email": "ka_burt@gmail.com",
  "phone_number": "4835398522",
  "relationships": [
   "coworker"
  ],
  "birthday": "1962-11-10",
  "home_address": "395 Tamara Place Suite 807\nSeattle\nWashington\nUnited States\n42274",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 744,
  "first_name": "Katie",
  "last_name": "Simpson",
  "email": "kat_simp@gmail.com",
  "phone_number": "6727300099",
  "relationships": [
   "friend"
  ],
  "birthday": "1965-01-15",
  "home_address": "808 Richard Crescent Suite 750\nSeattle\nWashington\nUnited States\n18427",
  "work_address": "97051 Keith Spur Suite 381\nSeattle\nWashington\nUnited States\n29218",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 746,
  "first_name": "Kathryn",
  "last_name": "Maldonado",
  "email": "kathrynmaldonado@gmail.com",
  "phone_number": "2473084266",
  "relationships": [
   "friend"
  ],
  "birthday": "1989-07-29",
  "home_address": "4912 Morales Divide Suite 845\nSeattle\nWashington\nUnited States\n24529",
  "work_address": "265 Carpenter Loop Suite 064\nSeattle\nWashington\nUnited States\n44564",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 742,
  "first_name": "Kevin",
  "last_name": "Blackburn",
  "email": "kevin.blac@gmail.com",
  "phone_number": "3654328626",
  "relationships": [
   "friend"
  ],
  "birthday": "1987-07-06",
  "home_address": "5183 Cabrera Trail Suite 457\nSeattle\nWashington\nUnited States\n66233",
  "work_address": "162 Smith Lake Suite 664\nSeattle\nWashington\nUnited States\n18461",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 726,
  "first_name": "Kristin",
  "last_name": "White",
  "email": "kri-powe@gmail.com",
  "phone_number": "6017026518",
  "relationships": [
   "coworker"
  ],
  "birthday": "1987-05-31",
  "home_address": "0031 Jeremy Cliff Suite 552\nSeattle\nWashington\nUnited States\n72731",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 749,
  "first_name": "Melissa",
  "last_name": "Bailey",
  "email": "mel.bailey@gmail.com",
  "phone_number": "3383946795",
  "relationships": [
   "roommate"
  ],
  "birthday": "1986-08-02",
  "home_address": "247 Salinas Pines Suite 668\nSeattle\nWashington\nUnited States\n11799",
  "work_address": "774 Samuel Cape Suite 202\nSeattle\nWashington\nUnited States\n16844",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 737,
  "first_name": "Michael",
  "last_name": "Burch",
  "email": "mi.burch@gmail.com",
  "phone_number": "8095050664",
  "relationships": [
   "sibling",
   "brother"
  ],
  "birthday": "1989-09-20",
  "home_address": "07161 Wilkerson Haven Suite 848\nSeattle\nWashington\nUnited States\n49511",
  "work_address": "162 Smith Lake Suite 664\nSeattle\nWashington\nUnited States\n18461",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 750,
  "first_name": "Nicholas",
  "last_name": "Weber",
  "email": "nicholas.weber@gmail.com",
  "phone_number": "9503658964",
  "relationships": [
   "roommate"
  ],
  "birthday": "1986-10-19",
  "home_address": "247 Salinas Pines Suite 668\nSeattle\nWashington\nUnited States\n11799",
  "work_address": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 732,
  "first_name": "Sabrina",
  "last_name": "Brown",
  "email": "sab-brown@gmail.com",
  "phone_number": "6639773608",
  "relationships": [
   "coworker"
  ],
  "birthday": "1954-02-03",
  "home_address": "77032 Jason Viaduct Suite 482\nSeattle\nWashington\nUnited States\n89837",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 733,
  "first_name": "Sandra",
  "last_name": "Martinez",
  "email": "saritt@gmail.com",
  "phone_number": "9012831674",
  "relationships": [
   "coworker"
  ],
  "birthday": "1998-11-17",
  "home_address": "6990 Nunez Corners Suite 644\nSeattle\nWashington\nUnited States\n88977",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 731,
  "first_name": "Stacy",
  "last_name": "Maldonado",
  "email": "st-maldonado@gmail.com",
  "phone_number": "9053203579",
  "relationships": [
   "coworker"
  ],
  "birthday": "1961-11-23",
  "home_address": "78543 Brian Canyon Suite 452\nSeattle\nWashington\nUnited States\n94342",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 724,
  "first_name": "Stephen",
  "last_name": "Mccoy",
  "email": "stmcco@gmail.com",
  "phone_number": "5707454150",
  "relationships": [
   "coworker"
  ],
  "birthday": "1956-03-22",
  "home_address": "3928 Justin Bridge Suite 149\nSeattle\nWashington\nUnited States\n59253",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 743,
  "first_name": "Tammy",
  "last_name": "Weaver",
  "email": "ta.weav@gmail.com",
  "phone_number": "2738013302",
  "relationships": [
   "friend"
  ],
  "birthday": "1987-10-28",
  "home_address": "775 Curry Plains Suite 496\nSeattle\nWashington\nUnited States\n19221",
  "work_address": "406 Lindsay Courts Suite 522\nSeattle\nWashington\nUnited States\n26281",
  "created_at": "2022-11-26T13:04:16"
 },
 {
  "contact_id": 729,
  "first_name": "Travis",
  "last_name": "Wilson",
  "email": "tra_wils@gmail.com",
  "phone_number": "7599900254",
  "relationships": [
   "coworker"
  ],
  "birthday": "1982-05-18",
  "home_address": "31434 Mark Trail Suite 731\nSeattle\nWashington\nUnited States\n75765",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2022-11-26T13:04:16"
 }
]
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Get all current venmo friends with pagination.
venmo_token = venmo_login['access_token']
all_venmo_friends = []
page_index = 0
page_limit = 20
while True:
    friends = apis.venmo.search_friends(access_token=venmo_token, page_index=page_index, page_limit=page_limit)
    if not friends:
        break
    all_venmo_friends.extend(friends)
    if len(friends) < page_limit:
        break
    page_index += 1
print(f"Total venmo friends: {len(all_venmo_friends)}")
print(all_venmo_friends)
```

```
Total venmo friends: 10
[
 {
  "first_name": "Tammy",
  "last_name": "Weaver",
  "email": "ta.weav@gmail.com",
  "registered_at": "2023-01-24T08:24:07",
  "friends_since": "2023-05-11T07:36:04"
 },
 {
  "first_name": "Cory",
  "last_name": "Wilson",
  "email": "corwils@gmail.com",
  "registered_at": "2022-08-29T18:50:33",
  "friends_since": "2023-05-02T17:47:10"
 },
 {
  "first_name": "Jennifer",
  "last_name": "Powell",
  "email": "jepowell@gmail.com",
  "registered_at": "2023-01-10T09:03:33",
  "friends_since": "2023-05-06T19:58:10"
 },
 {
  "first_name": "Kathryn",
  "last_name": "Maldonado",
  "email": "kathrynmaldonado@gmail.com",
  "registered_at": "2022-10-08T10:30:22",
  "friends_since": "2023-04-29T02:45:18"
 },
 {
  "first_name": "Anthony",
  "last_name": "Harrison",
  "email": "an-harrison@gmail.com",
  "registered_at": "2022-12-23T16:09:19",
  "friends_since": "2023-05-12T12:42:41"
 },
 {
  "first_name": "Stacy",
  "last_name": "Maldonado",
  "email": "st-maldonado@gmail.com",
  "registered_at": "2022-08-19T16:12:47",
  "friends_since": "2023-05-03T06:26:43"
 },
 {
  "first_name": "Jamie",
  "last_name": "Solomon",
  "email": "jamie-solomon@gmail.com",
  "registered_at": "2023-01-17T09:00:50",
  "friends_since": "2023-05-02T03:34:23"
 },
 {
  "first_name": "Travis",
  "last_name": "Wilson",
  "email": "tra_wils@gmail.com",
  "registered_at": "2022-04-28T16:40:41",
  "friends_since": "2023-05-08T06:24:57"
 },
 {
  "first_name": "Kayla",
  "last_name": "Burton",
  "email": "ka_burt@gmail.com",
  "registered_at": "2022-07-14T13:15:05",
  "friends_since": "2023-05-06T17:22:29"
 },
 {
  "first_name": "Kristin",
  "last_name": "White",
  "email": "kri-powe@gmail.com",
  "registered_at": "2022-12-17T11:05:29",
  "friends_since": "2023-05-01T08:25:52"
 }
]
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
# Print all phone contacts to see their emails
print(f"Total phone contacts: {len(contacts)}")
for c in contacts:
    print(c)
```

```
Total phone contacts: 7
{
 "contact_id": 750,
 "first_name": "Nicholas",
 "last_name": "Weber",
 "email": "nicholas.weber@gmail.com",
 "phone_number": "9503658964",
 "relationships": [
  "roommate"
 ],
 "birthday": "1986-10-19",
 "home_address": "247 Salinas Pines Suite 668\nSeattle\nWashington\nUnited States\n11799",
 "work_address": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
 "created_at": "2022-11-26T13:04:16"
}
{
 "contact_id": 732,
 "first_name": "Sabrina",
 "last_name": "Brown",
 "email": "sab-brown@gmail.com",
 "phone_number": "6639773608",
 "relationships": [
  "coworker"
 ],
 "birthday": "1954-02-03",
 "home_address": "77032 Jason Viaduct Suite 482\nSeattle\nWashington\nUnited States\n89837",
 "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
 "created_at": "2022-11-26T13:04:16"
}
{
 "contact_id": 733,
 "first_name": "Sandra",
 "last_name": "Martinez",
 "email": "saritt@gmail.com",
 "phone_number": "9012831674",
 "relationships": [
  "coworker"
 ],
 "birthday": "1998-11-17",
 "home_address": "6990 Nunez Corners Suite 644\nSeattle\nWashington\nUnited States\n88977",
 "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
 "created_at": "2022-11-26T13:04:16"
}
{
 "contact_id": 731,
 "first_name": "Stacy",
 "last_name": "Maldonado",
 "email": "st-maldonado@gmail.com",
 "phone_number": "9053203579",
 "relationships": [
  "coworker"
 ],
 "birthday": "1961-11-23",
 "home_address": "78543 Brian Canyon Suite 452\nSeattle\nWashington\nUnited States\n94342",
 "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
 "created_at": "2022-11-26T13:04:16"
}
{
 "contact_id": 724,
 "first_name": "Stephen",
 "last_name": "Mccoy",
 "email": "stmcco@gmail.com",
 "phone_number": "5707454150",
 "relationships": [
  "coworker"
 ],
 "birthday": "1956-03-22",
 "home_address": "3928 Justin Bridge Suite 149\nSeattle\nWashington\nUnited States\n59253",
 "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
 "created_at": "2022-11-26T13:04:16"
}
{
 "contact_id": 743,
 "first_name": "Tammy",
 "last_name": "Weaver",
 "email": "ta.weav@gmail.com",
 "phone_number": "2738013302",
 "relationships": [
  "friend"
 ],
 "birthday": "1987-10-28",
 "home_address": "775 Curry Plains Suite 496\nSeattle\nWashington\nUnited States\n19221",
 "work_address": "406 Lindsay Courts Suite 522\nSeattle\nWashington\nUnited States\n26281",
 "created_at": "2022-11-26T13:04:16"
}
{
 "contact_id": 729,
 "first_name": "Travis",
 "last_name": "Wilson",
 "email": "tra_wils@gmail.com",
 "phone_number": "7599900254",
 "relationships": [
  "coworker"
 ],
 "birthday": "1982-05-18",
 "home_address": "31434 Mark Trail Suite 731\nSeattle\nWashington\nUnited States\n75765",
 "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
 "created_at": "2022-11-26T13:04:16"
}
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# Search for each phone contact on venmo to see if they exist
venmo_token = venmo_login['access_token']
phone_emails = [c['email'] for c in contacts]
print("Phone contact emails:", phone_emails)

for email in phone_emails:
    result = apis.venmo.search_friends(access_token=venmo_token, user_email=email)
    print(f"Search for {email}: {result}")
```

```
Phone contact emails: ['nicholas.weber@gmail.com', 'sab-brown@gmail.com', 'saritt@gmail.com', 'st-maldonado@gmail.com', 'stmcco@gmail.com', 'ta.weav@gmail.com', 'tra_wils@gmail.com']
Search for nicholas.weber@gmail.com: [{'first_name': 'Chelsea', 'last_name': 'Burch', 'email': 'chelsea-burch@gmail.com', 'registered_at': '2023-01-29T10:18:37', 'friends_since': '2022-08-05T05:23:13'}, {'first_name': 'Valerie', 'last_name': 'Blackburn', 'email': 'va-blac@gmail.com', 'registered_at': '2022-05-26T12:45:26', 'friends_since': '2023-02-11T17:10:26'}, {'first_name': 'Eric', 'last_name': 'Bailey', 'email': 'eric.bailey@gmail.com', 'registered_at': '2022-08-29T12:35:03', 'friends_since': '2022-12-24T18:04:05'}, {'first_name': 'Patricia', 'last_name': 'Ritter', 'email': 'pa_ritter@gmail.com', 'registered_at': '2022-06-22T15:44:06', 'friends_since': '2023-02-20T04:09:07'}, {'first_name': 'Kyle', 'last_name': 'Moore', 'email': 'kyl_moor@gmail.com', 'registered_at': '2022-11-01T15:16:37', 'friends_since': '2023-03-01T11:02:24'}]
Search for sab-brown@gmail.com: [{'first_name': 'Richard', 'last_name': 'Riddle', 'email': 'ric.riddle@gmail.com', 'registered_at': '2022-05-29T10:21:21', 'friends_since': '2023-02-15T09:17:58'}, {'first_name': 'Cody', 'last_name': 'Smith', 'email': 'cod.smith@gmail.com', 'registered_at': '2023-01-05T14:36:26', 'friends_since': '2023-05-14T18:31:30'}, {'first_name': 'Grant', 'last_name': 'Martinez', 'email': 'gra-martinez@gmail.com', 'registered_at': '2022-11-17T11:34:25', 'friends_since': '2023-04-14T19:50:43'}, {'first_name': 'Stacy', 'last_name': 'Maldonado', 'email': 'st-maldonado@gmail.com', 'registered_at': '2022-08-19T16:12:47', 'friends_since': '2023-04-13T13:19:19'}, {'first_name': 'Travis', 'last_name': 'Wilson', 'email': 'tra_wils@gmail.com', 'registered_at': '2022-04-28T16:40:41', 'friends_since': '2023-02-21T05:25:18'}]
Search for saritt@gmail.com: [{'first_name': 'Martin', 'last_name': 'Blackburn', 'email': 'mar_blac@gmail.com', 'registered_at': '2022-06-04T16:12:50', 'friends_since': '2023-05-13T13:19:49'}, {'first_name': 'Connor', 'last_name': 'Brown', 'email': 'connorbrow@gmail.com', 'registered_at': '2023-01-31T08:47:45', 'friends_since': '2023-02-14T22:12:27'}, {'first_name': 'Grant', 'last_name': 'Martinez', 'email': 'gra-martinez@gmail.com', 'registered_at': '2022-11-17T11:34:25', 'friends_since': '2023-02-19T12:58:31'}, {'first_name': 'Travis', 'last_name': 'Wilson', 'email': 'tra_wils@gmail.com', 'registered_at': '2022-04-28T16:40:41', 'friends_since': '2023-05-03T08:58:49'}, {'first_name': 'Sabrina', 'last_name': 'Brown', 'email': 'sab-brown@gmail.com', 'registered_at': '2023-02-07T10:07:44', 'friends_since': '2023-05-05T08:19:48'}]
Search for st-maldonado@gmail.com: [{'first_name': 'Joyce', 'last_name': 'Weaver', 'email': 'joyce-weav@gmail.com', 'registered_at': '2022-07-23T10:43:03', 'friends_since': '2022-08-20T05:22:12'}, {'first_name': 'Sandra', 'last_name': 'Martinez', 'email': 'saritt@gmail.com', 'registered_at': '2022-12-05T18:00:27', 'friends_since': '2023-02-04T22:06:09'}, {'first_name': 'Jamie', 'last_name': 'Solomon', 'email': 'jamie-solomon@gmail.com', 'registered_at': '2023-01-17T09:00:50', 'friends_since': '2023-03-09T15:53:01'}, {'first_name': 'Jonathan', 'last_name': 'Ball', 'email': 'jo.ball@gmail.com', 'registered_at': '2022-08-26T16:01:41', 'friends_since': '2022-09-20T09:23:09'}, {'first_name': 'Jeffery', 'last_name': 'Simpson', 'email': 'je.simpson@gmail.com', 'registered_at': '2022-12-11T14:33:33', 'friends_since': '2022-10-14T21:50:38'}]
Search for stmcco@gmail.com: [{'first_name': 'Kayla', 'last_name': 'Burton', 'email': 'ka_burt@gmail.com', 'registered_at': '2022-07-14T13:15:05', 'friends_since': '2023-02-08T17:27:28'}, {'first_name': 'Isaac', 'last_name': 'Miller', 'email': 'ismill@gmail.com', 'registered_at': '2022-10-23T10:39:38', 'friends_since': '2023-04-07T23:01:22'}, {'first_name': 'Anita', 'last_name': 'Burch', 'email': 'anita.burch@gmail.com', 'registered_at': '2022-03-30T10:20:20', 'friends_since': '2023-05-17T18:23:05'}, {'first_name': 'Mason', 'last_name': 'Smith', 'email': 'masmith@gmail.com', 'registered_at': '2023-02-13T16:08:22', 'friends_since': '2023-01-30T17:39:51'}, {'first_name': 'Grant', 'last_name': 'Martinez', 'email': 'gra-martinez@gmail.com', 'registered_at': '2022-11-17T11:34:25', 'friends_since': '2023-02-13T11:08:44'}]
Search for ta.weav@gmail.com: [{'first_name': 'Jordan', 'last_name': 'Harrison', 'email': 'jo-harr@gmail.com', 'registered_at': '2022-04-10T14:26:20', 'friends_since': '2023-05-17T20:10:44'}, {'first_name': 'Morgan', 'last_name': 'Burton', 'email': 'morgan-harrison@gmail.com', 'registered_at': '2022-05-17T16:56:09', 'friends_since': '2023-02-22T23:57:40'}, {'first_name': 'Kathryn', 'last_name': 'Maldonado', 'email': 'kathrynmaldonado@gmail.com', 'registered_at': '2022-10-08T10:30:22', 'friends_since': '2023-02-24T13:04:23'}, {'first_name': 'Richard', 'last_name': 'Riddle', 'email': 'ric.riddle@gmail.com', 'registered_at': '2022-05-29T10:21:21', 'friends_since': '2023-03-17T03:44:13'}, {'first_name': 'Michael', 'last_name': 'Burch', 'email': 'mi.burch@gmail.com', 'registered_at': '2022-04-05T14:42:46', 'friends_since': '2023-03-31T14:14:52'}]
Search for tra_wils@gmail.com: [{'first_name': 'Kevin', 'last_name': 'Blackburn', 'email': 'kevin.blac@gmail.com', 'registered_at': '2022-05-15T18:48:46', 'friends_since': '2022-09-11T21:28:42'}, {'first_name': 'Jamie', 'last_name': 'Solomon', 'email': 'jamie-solomon@gmail.com', 'registered_at': '2023-01-17T09:00:50', 'friends_since': '2022-10-13T19:29:45'}, {'first_name': 'Cody', 'last_name': 'Smith', 'email': 'cod.smith@gmail.com', 'registered_at': '2023-01-05T14:36:26', 'friends_since': '2022-09-26T15:56:19'}, {'first_name': 'Kayla', 'last_name': 'Burton', 'email': 'ka_burt@gmail.com', 'registered_at': '2022-07-14T13:15:05', 'friends_since': '2022-11-24T15:52:14'}, {'first_name': 'Stephen', 'last_name': 'Mccoy', 'email': 'stmcco@gmail.com', 'registered_at': '2023-01-24T12:51:50', 'friends_since': '2022-11-25T16:58:08'}]
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
# Let's check the phone's search_friends API to understand what "friends" means in the phone context.
print(apis.api_docs.show_api_doc(app_name='phone', api_name='search_friends'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    print(apis.api_docs.show_api_doc(app_name='phone', api_name='search_friends'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name search_friends found for the phone app. Check the api and app name again."}
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
# Fetch all phone contacts (paginate) and also get the list of relationships
phone_token = phone_login['access_token']
all_contacts = []
page_index = 0
page_limit = 20
while True:
    page = apis.phone.search_contacts(access_token=phone_token, page_index=page_index, page_limit=page_limit)
    if not page:
        break
    all_contacts.extend(page)
    if len(page) < page_limit:
        break
    page_index += 1
print(f"Total phone contacts fetched: {len(all_contacts)}")
# Print relationships
print(apis.phone.show_contact_relationships(access_token=phone_token))
```

```
Total phone contacts fetched: 27
[
 "brother",
 "coworker",
 "father",
 "friend",
 "manager",
 "mother",
 "parent",
 "roommate",
 "sibling",
 "sister"
]
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
# Print all phone contacts with their relationships
for c in all_contacts:
    print(f"{c['first_name']} {c['last_name']} - {c['email']} - relationships: {c['relationships']}")
```

```
Allison Calhoun - allison-calhoun@gmail.com - relationships: ['coworker']
Anthony Harrison - an-harrison@gmail.com - relationships: ['roommate']
Caitlin Burch - caiburc@gmail.com - relationships: ['parent', 'mother']
Christopher Burch - ch-burch@gmail.com - relationships: ['parent', 'father']
Chelsea Burch - chelsea-burch@gmail.com - relationships: ['sibling', 'sister']
Cody Smith - cod.smith@gmail.com - relationships: ['coworker']
Cory Wilson - corwils@gmail.com - relationships: ['friend']
Debra Ritter - de_ritt@gmail.com - relationships: ['friend']
Denise Maldonado - deniseburch@gmail.com - relationships: ['sibling', 'sister']
Grant Martinez - gra-martinez@gmail.com - relationships: ['coworker']
Jamie Solomon - jamie-solomon@gmail.com - relationships: ['manager', 'coworker']
Jennifer Powell - jepowell@gmail.com - relationships: ['friend']
Jordan Harrison - jo-harr@gmail.com - relationships: ['friend']
Kayla Burton - ka_burt@gmail.com - relationships: ['coworker']
Katie Simpson - kat_simp@gmail.com - relationships: ['friend']
Kathryn Maldonado - kathrynmaldonado@gmail.com - relationships: ['friend']
Kevin Blackburn - kevin.blac@gmail.com - relationships: ['friend']
Kristin White - kri-powe@gmail.com - relationships: ['coworker']
Melissa Bailey - mel.bailey@gmail.com - relationships: ['roommate']
Michael Burch - mi.burch@gmail.com - relationships: ['sibling', 'brother']
Nicholas Weber - nicholas.weber@gmail.com - relationships: ['roommate']
Sabrina Brown - sab-brown@gmail.com - relationships: ['coworker']
Sandra Martinez - saritt@gmail.com - relationships: ['coworker']
Stacy Maldonado - st-maldonado@gmail.com - relationships: ['coworker']
Stephen Mccoy - stmcco@gmail.com - relationships: ['coworker']
Tammy Weaver - ta.weav@gmail.com - relationships: ['friend']
Travis Wilson - tra_wils@gmail.com - relationships: ['coworker']
```

