©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 1
Num Failed Tests : 4
Num Total  Tests : 5
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Passed Requirement
assert model changes match venmo.Friendship
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Fails ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Failed Requirement
assert answers match.
```python
with test(
    """
    assert answers match.
    """
):
    test.answer(predicted_answer, ground_truth_answer)
```
----------
AssertionError:
'venmo friends reset to match phone contacts: added 14 friends, removed 0.'
==
'null'
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
AssertionError:
[10, 16, 20, 23, 42, 46, 55, 68, 69, 88, 89, 91, 92, 95]
==
[10, 20, 23, 55, 68]

In left but not right:
[16, 42, 46, 69, 88, 89, 91, 92, 95]

Original values:
[88, 16, 10, 89, 20, 69, 23, 42, 92, 91, 68, 46, 55, 95]
==
[10, 68, 55, 20, 23]
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
AssertionError:  [] == [40, 52, 56, 66, 78]

In right but not left:
[40, 52, 56, 66, 78]

Original values:
[] == [40, 66, 56, 52, 78]
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
[10, 16, 20, 23, 31, 35, 36, 40, 42, 43, 46, 52, 55, 56, 66, 68, 69, 78, 88,
89, 91, 92, 95, 106]
==
[10, 20, 23, 31, 35, 36, 43, 55, 68, 106]

In left but not right:
[16, 40, 42, 46, 52, 56, 66, 69, 78, 88, 89, 91, 92, 95]

Original values:
[35, 31, 36, 106, 43, 40, 66, 56, 52, 78, 92, 46, 68, 88, 23, 42, 91, 20, 55,
16, 95, 69, 10, 89]
==
[35, 31, 36, 106, 43, 10, 68, 55, 20, 23]