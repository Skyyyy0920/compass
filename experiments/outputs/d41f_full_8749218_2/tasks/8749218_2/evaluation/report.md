©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 5
Num Failed Tests : 1
Num Total  Tests : 6
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Passed Requirement
assert answers match.
>> Passed Requirement
assert model changes match spotify.MusicPlayer.
>> Passed Requirement
obtain added, updated, removed spotify.MusicPlayer records using
models.changed_records,
and assert 0 have been added or removed.
>> Passed Requirement
assert the updated music player is in the playing state.
>> Passed Requirement
assert the order of song_ids in the queue of the updated music player
is not identical or reverse to the order of
private_data.recommendation_song_ids.
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Fails ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Failed Requirement
assert set of song_ids in the queue of the updated music player
is identical to private_data.recommendation_song_ids.
```python
with test(
    """
    assert set of song_ids in the queue of the updated music player
    is identical to private_data.recommendation_song_ids.
    """
):
    queue_song_ids = set_of(updated_music_player.queue_songs, "id")
    test.case(queue_song_ids, "==", set(private_data.recommendation_song_ids))
```
----------
AssertionError:
{32, 194, 259, 324, 5, 6, 7, 27, 43, 236, 212, 246, 88, 281, 251, 29, 222}
==
{11, 141, 143, 144, 276, 277, 152, 157, 31, 33, 36, 306, 180, 56, 318, 198, 73,
75, 78, 80, 211, 214, 96, 229, 110, 246, 247, 250, 252, 125}

In left but not right:
[32, 194, 259, 324, 5, 6, 7, 27, 43, 236, 212, 88, 281, 251, 29, 222]

In right but not left:
[11, 141, 143, 144, 276, 277, 152, 157, 31, 33, 36, 306, 180, 56, 318, 198, 73,
75, 78, 80, 211, 214, 96, 229, 110, 247, 250, 252, 125]