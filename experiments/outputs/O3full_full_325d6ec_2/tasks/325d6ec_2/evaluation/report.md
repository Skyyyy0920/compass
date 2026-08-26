──────────────────────────────── Overall Stats ────────────────────────────────
Num Passed Tests : 3
Num Failed Tests : 2
Num Total  Tests : 5
─────────────────────────────────── Passes ────────────────────────────────────
>> Passed Requirement
obtain added, updated, removed spotify.MusicPlayer records using
models.changed_records,
and assert 1 has been updated, and 0 have been added or removed.
>> Passed Requirement
assert music player's cursor is on the song with private_data.target_song_id.
>> Passed Requirement
assert updated music_player's changed_field_names is only {"cursor_position"}.
──────────────────────────────────── Fails ────────────────────────────────────
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
AssertionError:  'phantom pain' == 'null'
>> Failed Requirement
assert model changes match spotify.MusicPlayer.
```python
with test(
    """
    assert model changes match spotify.MusicPlayer.
    """
):
    test.case(models.changed_model_names(), "==", {"spotify.MusicPlayer"})
```
----------
AssertionError:
{'spotify.User', 'spotify.MusicPlayer', 'gmail.GlobalEmailThread',
'gmail.UserEmailThread', 'gmail.Email'}
==
{'spotify.MusicPlayer'}

In left but not right:
['spotify.User', 'gmail.GlobalEmailThread', 'gmail.UserEmailThread',
'gmail.Email']