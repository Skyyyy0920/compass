©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 1
Num Failed Tests : 4
Num Total  Tests : 5
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Passed Requirement
assert answers match.
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Fails ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Failed Requirement
assert model changes match venmo.Friendship
```python
with test(
    """
    assert model changes match venmo.Friendship
    """
):
    changed_model_names = models.changed_model_names()
    test.case(changed_model_names, "==", {"venmo.Friendship"})
```
----------
AssertionError:  set() == {'venmo.Friendship'}

In right but not left:
['venmo.Friendship']
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
AssertionError:  [] == [83, 90, 92, 95]

In right but not left:
[83, 90, 92, 95]

Original values:
[] == [90, 95, 92, 83]
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
AssertionError:  [] == [10, 34, 72, 103, 104]

In right but not left:
[10, 34, 72, 103, 104]

Original values:
[] == [72, 103, 34, 104, 10]
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
AssertionError:  [10, 34, 72, 91, 96, 101, 103, 104] == [83, 90, 91, 92, 95,
96, 101]

In left but not right:
[10, 34, 72, 103, 104]

In right but not left:
[83, 90, 92, 95]

Original values:
[96, 101, 91, 72, 103, 34, 104, 10] == [96, 101, 91, 90, 95, 92, 83]