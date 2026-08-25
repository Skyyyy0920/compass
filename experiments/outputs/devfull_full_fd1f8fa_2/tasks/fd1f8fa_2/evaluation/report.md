©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 3
Num Failed Tests : 2
Num Total  Tests : 5
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Passed Requirement
assert answers match.
>> Passed Requirement
obtain added, updated, removed spotify.MusicPlayer records using
models.changed_records,
and assert 1 has been updated, and 0 have been added or removed.
>> Passed Requirement
assert music player is in playing state.
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Fails ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
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
{'spotify.UserLibrarySong', 'spotify.MusicPlayer'}
==
{'spotify.MusicPlayer'}

In left but not right:
['spotify.UserLibrarySong']
>> Failed Requirement
assert song_ids in the end state of the music player's queue match
private_data.expected_queue_song_ids, ignoring order.
```python
with test(
    """
    assert song_ids in the end state of the music player's queue match
    private_data.expected_queue_song_ids, ignoring order.
    """
):
    music_player = updated_music_players[0]
    queue_song_ids = list_of(music_player.queue_songs, "id")
```
----------
AssertionError:
[1, 5, 15, 16, 43, 45, 49, 60, 65, 84, 97, 102, 104, 136, 164, 176, 195, 206,
214, 232, 242, 272, 283, 295]
==
[1, 5, 15, 60, 102, 104, 136, 176, 206, 214, 283, 295]

In left but not right:
[16, 43, 45, 49, 65, 84, 97, 164, 195, 232, 242, 272]

Original values:
[49, 195, 43, 164, 295, 60, 242, 97, 1, 176, 15, 136, 84, 5, 16, 283, 206, 232,
104, 65, 45, 102, 214, 272]
==
[60, 1, 104, 15, 176, 5, 295, 136, 214, 102, 283, 206]