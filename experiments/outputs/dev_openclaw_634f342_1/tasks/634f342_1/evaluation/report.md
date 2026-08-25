©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 1
Num Failed Tests : 6
Num Total  Tests : 7
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Passed Requirement
assert the added playlist's title is public_data.playlist_title.
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
AssertionError:  '<<not_given>>' == 'null'
>> Failed Requirement
assert model changes match spotify.Playlist, spotify.PlaylistSong.
```python
with test(
    """
    assert model changes match spotify.Playlist, spotify.PlaylistSong.
    """
):
    test.case(
        models.changed_model_names(),
        "==",
```
----------
AssertionError:
{'spotify.PlaylistSong', 'spotify.Playlist', 'spotify.PlaylistReview',
'spotify.PlaylistLike'}
==
{'spotify.PlaylistSong', 'spotify.Playlist'}

In left but not right:
['spotify.PlaylistReview', 'spotify.PlaylistLike']
>> Failed Requirement
obtain added, updated, deleted spotify.Playlist records using
models.changed_records,
and assert 1 has been added, 0 have been updated or deleted.
```python
with test(
    """
    obtain added, updated, deleted spotify.Playlist records using
models.changed_records,
    and assert 1 has been added, 0 have been updated or deleted.
    """
):
    added_playlists, updated_playlists, deleted_playlists =
models.changed_records(
        "spotify.Playlist"
```
----------
AssertionError:  1 == 0
>> Failed Requirement
obtain added, deleted spotify.PlaylistSong records using
models.changed_records,
and assert set of added song ids match to set of
private_data.to_archive_song_ids.
```python
with test(
    """
    obtain added, deleted spotify.PlaylistSong records using
models.changed_records,
    and assert set of added song ids match to set of
private_data.to_archive_song_ids.
    """
):
    added_playlist_songs, _, deleted_playlist_songs = models.changed_records(
        "spotify.PlaylistSong"
```
----------
AssertionError:
set()
==
{128, 257, 162, 131, 261, 74, 43, 172, 207, 308, 311, 280, 29, 127}

In right but not left:
[128, 257, 162, 131, 261, 74, 43, 172, 207, 308, 311, 280, 29, 127]
>> Failed Requirement
assert set of deleted song ids also match to set of
private_data.to_archive_song_ids.
```python
with test(
    """
    assert set of deleted song ids also match to set of
private_data.to_archive_song_ids.
    """
):
    deleted_song_ids = set_of(deleted_playlist_songs, "song_id")
    test.case(deleted_song_ids, "==", set(private_data.to_archive_song_ids))
```
----------
AssertionError:
{39, 105, 298, 74, 210, 182, 280, 185, 223}
==
{128, 257, 162, 131, 261, 74, 43, 172, 207, 308, 311, 280, 29, 127}

In left but not right:
[39, 105, 298, 210, 182, 185, 223]

In right but not left:
[128, 257, 162, 131, 261, 43, 172, 207, 308, 311, 29, 127]
>> Failed Requirement
assert playlist_id_to_song_ids of deleted_playlist_songs match
private_data.to_archive_playlist_id_to_song_ids (ignore_order)
```python
with test(
    """
    assert playlist_id_to_song_ids of deleted_playlist_songs match
    private_data.to_archive_playlist_id_to_song_ids (ignore_order)
    """
):
    playlist_id_to_song_ids = dict_list_of(deleted_playlist_songs,
"playlist_id", "song_id")
    test.case(
```
----------
AssertionError:
{443: [39, 74, 105, 182, 185, 210, 223, 280, 298]}
==
{443: [74, 280], 444: [29, 261, 311], 445: [43, 128, 162], 446: [207, 257,
308], 448: [127, 131, 207], 447: [172]}

Original values:
defaultdict(<class 'list'>, {443: [298, 185, 280, 74, 105, 182, 210, 39, 223]})
==
Munch({443: [74, 280], 444: [261, 311, 29], 445: [43, 162, 128], 446: [207,
308, 257], 448: [207, 131, 127], 447: [172]})