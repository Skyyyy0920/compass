
### Environment Interaction 1
----------------------------------------------------------------------------
```python
<｜DSML｜python>
print(apis.api_docs.show_app_descriptions())
</｜DSML｜python>
```

```
Execution failed. Traceback:
Syntax error in line:
<｜DSML｜python>
Message: invalid character '｜' (U+FF5C)
```


### Environment Interaction 2
----------------------------------------------------------------------------
```python
<｜DSML｜python>
print(apis.api_docs.show_app_descriptions())
</｜DSML｜python>
```

```
Execution failed. Traceback:
Syntax error in line:
<｜DSML｜python>
Message: invalid character '｜' (U+FF5C)
```


### Environment Interaction 3
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


### Environment Interaction 7
----------------------------------------------------------------------------
```python
print(apis.supervisor.show_profile())
print(apis.supervisor.show_account_passwords())
```

```
{
 "first_name": "Jordan",
 "last_name": "Harrison",
 "email": "jo-harr@gmail.com",
 "phone_number": "2254213734",
 "birthday": "1988-04-06",
 "sex": "male"
}
[
 {
  "account_name": "amazon",
  "password": "hq(Y-=i"
 },
 {
  "account_name": "file_system",
  "password": "n#5vSNx"
 },
 {
  "account_name": "gmail",
  "password": "S4kyt)a"
 },
 {
  "account_name": "phone",
  "password": "Ee%AVVI"
 },
 {
  "account_name": "simple_note",
  "password": "%i(z@6X"
 },
 {
  "account_name": "splitwise",
  "password": "j9@8ww6"
 },
 {
  "account_name": "spotify",
  "password": "&{Ef&tC"
 },
 {
  "account_name": "todoist",
  "password": "YAeG+q9"
 },
 {
  "account_name": "venmo",
  "password": "ZEgU=ep"
 }
]
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='phone', api_name='show_contact_relationships'))
print(apis.api_docs.show_api_doc(app_name='phone', api_name='search_contacts'))
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
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='phone', api_name='login'))
print(apis.api_docs.show_api_doc(app_name='venmo', api_name='login'))
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


### Environment Interaction 10
----------------------------------------------------------------------------
```python
# Login to phone and venmo
phone_login = apis.phone.login(username='2254213734', password='Ee%AVVI')
venmo_login = apis.venmo.login(username='jo-harr@gmail.com', password='ZEgU=ep')
print(phone_login)
print(venmo_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwaG9uZSsyMjU0MjEzNzM0IiwiZXhwIjoxNjg0NDEyMDk4fQ.xDB7pMF6Krp9DLl8Iso5JL0Kc0SLV78Gpi7X42sF_v0",
 "token_type": "Bearer"
}
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2ZW5tbytqby1oYXJyQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjc0MX0.jCDXE7B3S-9Y2n1Q_cumB4OaPL8QtvGpz2uBEBNwnuQ",
 "token_type": "Bearer"
}
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Get phone relationships and contacts
phone_token = phone_login['access_token']
print(apis.phone.show_contact_relationships(access_token=phone_token))
print(apis.phone.search_contacts(access_token=phone_token, page_limit=20))
```

```
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
[
 {
  "contact_id": 264,
  "first_name": "Adam",
  "last_name": "Blackburn",
  "email": "ad.blackburn@gmail.com",
  "phone_number": "8944155247",
  "relationships": [
   "coworker"
  ],
  "birthday": "1979-11-13",
  "home_address": "478 Daniel Bridge Suite 056\nSeattle\nWashington\nUnited States\n65695",
  "work_address": "8875 Amy Extensions Suite 797\nSeattle\nWashington\nUnited States\n49596",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 272,
  "first_name": "Anthony",
  "last_name": "Harrison",
  "email": "an-harrison@gmail.com",
  "phone_number": "2466064078",
  "relationships": [
   "sibling",
   "brother"
  ],
  "birthday": "1990-06-09",
  "home_address": "247 Salinas Pines Suite 668\nSeattle\nWashington\nUnited States\n11799",
  "work_address": "96967 Fox Loop Suite 397\nSeattle\nWashington\nUnited States\n86832",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 262,
  "first_name": "Angela",
  "last_name": "Riddle",
  "email": "angriddle@gmail.com",
  "phone_number": "6925139040",
  "relationships": [
   "coworker"
  ],
  "birthday": "1959-02-19",
  "home_address": "127 Juan Fort Suite 361\nSeattle\nWashington\nUnited States\n39139",
  "work_address": "8875 Amy Extensions Suite 797\nSeattle\nWashington\nUnited States\n49596",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 275,
  "first_name": "Anita",
  "last_name": "Burch",
  "email": "anita.burch@gmail.com",
  "phone_number": "3643463570",
  "relationships": [
   "friend"
  ],
  "birthday": "1997-03-10",
  "home_address": "247 Salinas Pines Suite 668\nSeattle\nWashington\nUnited States\n11799",
  "work_address": "7844 Joshua Shore Suite 460\nSeattle\nWashington\nUnited States\n46946",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 266,
  "first_name": "Ashlee",
  "last_name": "Martinez",
  "email": "ashlee_martinez@gmail.com",
  "phone_number": "3506492550",
  "relationships": [
   "coworker"
  ],
  "birthday": "1960-10-16",
  "home_address": "7775 Weiss Grove Suite 543\nSeattle\nWashington\nUnited States\n21777",
  "work_address": "8875 Amy Extensions Suite 797\nSeattle\nWashington\nUnited States\n49596",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 270,
  "first_name": "Christina",
  "last_name": "Harrison",
  "email": "chrharrison@gmail.com",
  "phone_number": "7487401121",
  "relationships": [
   "parent",
   "mother"
  ],
  "birthday": "1957-09-17",
  "home_address": "5918 Johnson Land Suite 815\nSeattle\nWashington\nUnited States\n18995",
  "work_address": "80547 Cynthia Square Suite 842\nSeattle\nWashington\nUnited States\n78964",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 267,
  "first_name": "Connor",
  "last_name": "Brown",
  "email": "connorbrow@gmail.com",
  "phone_number": "5734599766",
  "relationships": [
   "coworker"
  ],
  "birthday": "1984-11-29",
  "home_address": "34495 Michael Burg Suite 805\nSeattle\nWashington\nUnited States\n38887",
  "work_address": "8875 Amy Extensions Suite 797\nSeattle\nWashington\nUnited States\n49596",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 268,
  "first_name": "Glenn",
  "last_name": "Burton",
  "email": "glenn.burton@gmail.com",
  "phone_number": "8638518861",
  "relationships": [
   "coworker"
  ],
  "birthday": "1993-08-13",
  "home_address": "816 Brittney Overpass Suite 48\nSeattle\nWashington\nUnited States\n44756",
  "work_address": "8875 Amy Extensions Suite 797\nSeattle\nWashington\nUnited States\n49596",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 280,
  "first_name": "Jason",
  "last_name": "Simpson",
  "email": "jasonsimp@gmail.com",
  "phone_number": "5516882990",
  "relationships": [
   "friend"
  ],
  "birthday": "1991-04-05",
  "home_address": "775 Curry Plains Suite 496\nSeattle\nWashington\nUnited States\n19221",
  "work_address": "5840 Craig Turnpike Suite 634\nSeattle\nWashington\nUnited States\n78487",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 265,
  "first_name": "Jeffrey",
  "last_name": "Smith",
  "email": "jefsmith@gmail.com",
  "phone_number": "3272301258",
  "relationships": [
   "coworker"
  ],
  "birthday": "1989-03-30",
  "home_address": "9648 Jones Meadow Suite 841\nSeattle\nWashington\nUnited States\n56694",
  "work_address": "8875 Amy Extensions Suite 797\nSeattle\nWashington\nUnited States\n49596",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 277,
  "first_name": "Jeremy",
  "last_name": "Calhoun",
  "email": "jer.calhoun@gmail.com",
  "phone_number": "2786837088",
  "relationships": [
   "friend"
  ],
  "birthday": "1990-11-24",
  "home_address": "478 Daniel Bridge Suite 056\nSeattle\nWashington\nUnited States\n65695",
  "work_address": "97051 Keith Spur Suite 381\nSeattle\nWashington\nUnited States\n29218",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 271,
  "first_name": "Jose",
  "last_name": "Harrison",
  "email": "joseharr@gmail.com",
  "phone_number": "2474975253",
  "relationships": [
   "sibling",
   "brother"
  ],
  "birthday": "1985-12-15",
  "home_address": "172 Matthew Knolls Suite 730\nSeattle\nWashington\nUnited States\n65644",
  "work_address": "774 Samuel Cape Suite 202\nSeattle\nWashington\nUnited States\n16844",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 278,
  "first_name": "Joseph",
  "last_name": "Weber",
  "email": "joseph.webe@gmail.com",
  "phone_number": "2233697879",
  "relationships": [
   "friend"
  ],
  "birthday": "1996-09-29",
  "home_address": "28073 William Corners Suite 495\nSeattle\nWashington\nUnited States\n36752",
  "work_address": "96967 Fox Loop Suite 397\nSeattle\nWashington\nUnited States\n86832",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 283,
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
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 276,
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
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 281,
  "first_name": "Marcus",
  "last_name": "Smith",
  "email": "ma_smith@gmail.com",
  "phone_number": "7196131136",
  "relationships": [
   "friend"
  ],
  "birthday": "1986-02-21",
  "home_address": "3516 Kevin Village Suite 778\nSeattle\nWashington\nUnited States\n86248",
  "work_address": "96967 Fox Loop Suite 397\nSeattle\nWashington\nUnited States\n86832",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 274,
  "first_name": "Miranda",
  "last_name": "Weber",
  "email": "mir-powe@gmail.com",
  "phone_number": "4885870260",
  "relationships": [
   "friend"
  ],
  "birthday": "1995-09-18",
  "home_address": "28073 William Corners Suite 495\nSeattle\nWashington\nUnited States\n36752",
  "work_address": "97051 Keith Spur Suite 381\nSeattle\nWashington\nUnited States\n29218",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 273,
  "first_name": "Morgan",
  "last_name": "Burton",
  "email": "morgan-harrison@gmail.com",
  "phone_number": "8903665635",
  "relationships": [
   "sibling",
   "sister"
  ],
  "birthday": "1992-08-11",
  "home_address": "5754 Kaylee Trace Suite 282\nSeattle\nWashington\nUnited States\n18299",
  "work_address": "406 Lindsay Courts Suite 522\nSeattle\nWashington\nUnited States\n26281",
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 285,
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
  "created_at": "2021-10-21T07:40:51"
 },
 {
  "contact_id": 269,
  "first_name": "Ronald",
  "last_name": "Harrison",
  "email": "ron.harrison@gmail.com",
  "phone_number": "3546176171",
  "relationships": [
   "parent",
   "father"
  ],
  "birthday": "1957-12-21",
  "home_address": "5918 Johnson Land Suite 815\nSeattle\nWashington\nUnited States\n18995",
  "work_address": "97051 Keith Spur Suite 381\nSeattle\nWashington\nUnited States\n29218",
  "created_at": "2021-10-21T07:40:51"
 }
]
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
# Let's explore the venmo API to understand how to search users, create payment requests, and make payments.
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


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# Let's check the API docs for search_users, create_payment_request, and create_transaction.
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


### Environment Interaction 14
----------------------------------------------------------------------------
```python
# Let's search for the roommates on Venmo to confirm their emails.
venmo_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2ZW5tbzpqby1oYXJyQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjc0MX0.jCDXE7B3S-9Y2n1Q_cumB4OaPL8QtvGpz2uBEBNwnuQ'
# Search for Kathryn Maldonado
print(apis.venmo.search_users(access_token=email_token, query='kathrynmaldonado@gmail.com', page_limit=5))
# Search for Nancy Ritter
print(apis.venmo.search_users(access_token=email_token, query='nan_ritt@gmail.com', page_limit=5))
```

```
Execution failed. Traceback:
  File "<python-input>", line 4, in <module>
    print(apis.venmo.search_users(access_token=email_token, query='kathrynmaldonado@gmail.com', page_limit=5))
                                               ^^^^^^^^^^^
NameError: name 'email_token' is not defined
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
# Use the venmo access token from history
venmo_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2ZW5tbzpqby1oYXJyQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjc0MX0.jCDXE7B3S-9Y2n1Q_cumB4OaPL8QtvGpz2uBEBNwnuQ'
# Search for Kathryn Maldonado
print(apis
```

```
Execution failed. Traceback:
Syntax error in line:
print(apis
Message: '(' was never closed
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
# Use the venmo access token from history
venmo_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2ZW5tbzpqby1oYXJyQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjc0MX0.jCDXE7B3S-9Y2n1Q_cumB4OaPL8QtvGpz2uBEBNwnuQ'
# Search for Kathryn Maldonado
print(apis.venmo.search_users(access_token=venmo_token, query='kathrynmaldonado@gmail.com', page_limit=5))
# Search for Nancy Ritter
print(apis.venmo.search_users(access_token=venmo_token, query='nan_ritt@gmail.com', page_limit=5))
```

```
Execution failed. Traceback:
  File "<python-input>", line 4, in <module>
    print(apis.venmo.search_users(access_token=venmo_token, query='kathrynmaldonado@gmail.com', page_limit=5))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 401:
{"message":"You are either not authorized to access this venmo API endpoint or your access token is missing, invalid or expired."}
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
# The token may have expired. Let's re-login to venmo.
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


### Environment Interaction 18
----------------------------------------------------------------------------
```python
# Re-login to venmo with supervisor's credentials
venmo_login = apis.venmo.login(username='jo-harr@gmail.com', password='ZEgU=ep')
print(venmo_login)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2ZW5tbytqby1oYXJyQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjczMX0.OddbFaNPbHiD2GDbVTbdj0NASlfzIH_f7ZKFDml-aGs",
 "token_type": "Bearer"
}
```

