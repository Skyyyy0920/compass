©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 2
Num Failed Tests : 3
Num Total  Tests : 5
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Passed Requirement
assert answers match.
>> Passed Requirement
assert model changes match venmo.Friendship
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Fails ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Failed Requirement
obtain added, deleted friendships using models.changed_records
and assert friend_ids of the added ones match
private_data.to_befriend_venmo_user_ids (ignore_order)
```python
with test(
    """
    obtain added, deleted friendships using models.changed_records
    and assert friend_ids of the added ones match
private_data.to_befriend_venmo_user_ids (ignore_order)
    """
):
    added_friendships, _, deleted_friendships =
models.changed_records("venmo.Friendship")
    added_friend_ids = list_of(added_friendships, "friend_id")
```
----------
AssertionError:  [32, 33, 35, 45] == [15, 43, 60, 97]

In left but not right:
[32, 33, 35, 45]

In right but not left:
[15, 43, 60, 97]

Original values:
[35, 33, 32, 45] == [43, 97, 15, 60]
>> Failed Requirement
assert friend_ids of the deleted ones match
private_data.to_unfriend_venmo_user_ids (ignore_order)
```python
with test(
    """
    assert friend_ids of the deleted ones match
private_data.to_unfriend_venmo_user_ids (ignore_order)
    """
):
    deleted_friend_ids = list_of(deleted_friendships, "friend_id")
    test.case(
        deleted_friend_ids, "==", private_data.to_unfriend_venmo_user_ids,
ignore_order=True
```
----------
AssertionError:  [29, 58, 72, 86] == [9, 16, 28, 71, 85, 100]

In left but not right:
[29, 58, 72, 86]

In right but not left:
[9, 16, 28, 71, 85, 100]

Original values:
[58, 86, 29, 72] == [16, 85, 9, 71, 100, 28]
>> Failed Requirement
assert all main_user's friends on venmo match
private_data.all_friends_venmo_user_ids in the end state (ignore_order)
```python
with test(
    """
    assert all main_user's friends on venmo match
    private_data.all_friends_venmo_user_ids in the end state (ignore_order)
    """
):
    venmo_user = models.end.venmo.User.find_from(main_user)
    venmo_friend_ids = list_of(venmo_user.friends, "id")
```
----------
AssertionError:
[9, 16, 28, 32, 33, 35, 45, 71, 85, 100]
==
[15, 29, 43, 58, 60, 72, 86, 97]

In left but not right:
[9, 16, 28, 32, 33, 35, 45, 71, 85, 100]

In right but not left:
[15, 29, 43, 58, 60, 72, 86, 97]

Original values:
[16, 85, 9, 71, 100, 28, 35, 32, 33, 45]
==
[58, 72, 29, 86, 43, 97, 15, 60]