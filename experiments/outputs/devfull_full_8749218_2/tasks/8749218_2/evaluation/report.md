©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 4
Num Failed Tests : 2
Num Total  Tests : 6
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Passed Requirement
assert answers match.
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
{'spotify.Playlist', 'spotify.MusicPlayer', 'spotify.PlaylistSong'}
==
{'spotify.MusicPlayer'}

In left but not right:
['spotify.Playlist', 'spotify.PlaylistSong']
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
{128, 129, 257, 137, 267, 12, 142, 17, 145, 275, 148, 21, 149, 276, 278, 284,
33, 162, 36, 164, 166, 294, 173, 49, 178, 51, 311, 185, 313, 59, 318, 321, 66,
67, 194, 196, 199, 201, 207, 208, 210, 211, 88, 92, 109, 240, 113, 118, 119,
123}
==
{11, 141, 143, 144, 276, 277, 152, 157, 31, 33, 36, 306, 180, 56, 318, 198, 73,
75, 78, 80, 211, 214, 96, 229, 110, 246, 247, 250, 252, 125}

In left but not right:
[128, 129, 257, 137, 267, 12, 142, 17, 145, 275, 148, 21, 149, 278, 284, 162,
164, 166, 294, 173, 49, 178, 51, 311, 185, 313, 59, 321, 66, 67, 194, 196, 199,
201, 207, 208, 210, 88, 92, 109, 240, 113, 118, 119, 123]

In right but not left:
[11, 141, 143, 144, 277, 152, 157, 31, 306, 180, 56, 198, 73, 75, 78, 80, 214,
96, 229, 110, 246, 247, 250, 252, 125]