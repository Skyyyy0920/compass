──────────────────────────────── Overall Stats ────────────────────────────────
Num Passed Tests : 4
Num Failed Tests : 1
Num Total  Tests : 5
─────────────────────────────────── Passes ────────────────────────────────────
>> Passed Requirement
assert answers match.
>> Passed Requirement
assert model changes match spotify.MusicPlayer.
>> Passed Requirement
obtain added, updated, removed spotify.MusicPlayer records using
models.changed_records,
and assert 1 has been updated, and 0 have been added or removed.
>> Passed Requirement
assert music player is in playing state.
──────────────────────────────────── Fails ────────────────────────────────────
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
[14, 71, 76, 111, 121, 139, 153, 157, 178, 180, 290]
==
[14, 71, 76, 111, 121, 139, 153, 157, 158, 178, 180, 290]

In right but not left:
[158]

Original values:
[290, 153, 139, 178, 180, 121, 76, 111, 157, 71, 14]
==
[71, 158, 157, 76, 14, 153, 111, 139, 121, 290, 178, 180]