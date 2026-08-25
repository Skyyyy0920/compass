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
{'spotify.Song', 'spotify.MusicPlayer', 'spotify.SongLike'}
==
{'spotify.MusicPlayer'}

In left but not right:
['spotify.Song', 'spotify.SongLike']
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
[19, 26, 28, 82, 93, 103, 109, 126, 133, 135, 167, 184, 197, 204, 206, 229,
232, 242, 255, 258, 272, 299, 301]
==
[26, 28, 82, 93, 126, 184, 197, 232, 255, 258, 272, 299]

In left but not right:
[19, 103, 109, 133, 135, 167, 204, 206, 229, 242, 301]

Original values:
[19, 26, 255, 82, 109, 184, 272, 301, 93, 204, 167, 299, 242, 28, 197, 133,
126, 135, 232, 103, 258, 206, 229]
==
[258, 197, 232, 26, 82, 126, 184, 299, 93, 272, 255, 28]