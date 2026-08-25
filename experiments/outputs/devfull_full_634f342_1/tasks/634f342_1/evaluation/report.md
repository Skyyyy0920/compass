©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 1
Num Failed Tests : 6
Num Total  Tests : 7
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Passed Requirement
assert answers match.
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Fails ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
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
AssertionError:  7 == 1
>> Failed Requirement
assert the added playlist's title is public_data.playlist_title.
```python
with test(
    """
    assert the added playlist's title is public_data.playlist_title.
    """
):
    added_playlist = added_playlists[0]
    test.case(added_playlist.title, "==", public_data.playlist_title)
```
----------
AssertionError:  'Intergalactic Anthems: Sci-Fi Songs' == 'Archived Songs'
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
{128, 257, 130, 131, 4, 261, 15, 276, 21, 278, 280, 29, 159, 287, 162, 35, 39,
298, 43, 172, 303, 308, 182, 311, 185, 187, 318, 191, 65, 197, 74, 207, 210,
211, 223, 224, 226, 105, 250, 251, 124, 127}
==
{128, 257, 162, 131, 261, 74, 43, 172, 207, 308, 311, 280, 29, 127}

In left but not right:
[130, 4, 15, 276, 21, 278, 159, 287, 35, 39, 298, 303, 182, 185, 187, 318, 191,
65, 197, 210, 211, 223, 224, 226, 105, 250, 251, 124]
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
{445: [43, 124, 128, 159, 162, 211], 448: [35, 39, 127, 131, 207, 276, 287,
303], 447: [4, 15, 21, 65, 172, 187, 191, 197], 443: [39, 74, 105, 182, 185,
210, 223, 280, 298], 446: [207, 226, 257, 308, 318], 444: [29, 130, 224, 250,
251, 261, 278, 311]}
==
{443: [74, 280], 444: [29, 261, 311], 445: [43, 128, 162], 446: [207, 257,
308], 448: [127, 131, 207], 447: [172]}

Original values:
defaultdict(<class 'list'>, {445: [159, 124, 162, 128, 211, 43], 448: [276, 39,
287, 303, 131, 207, 35, 127], 447: [197, 15, 187, 65, 191, 21, 172, 4], 443:
[74, 39, 223, 298, 210, 185, 105, 182, 280], 446: [207, 308, 226, 318, 257],
444: [278, 251, 311, 130, 261, 29, 250, 224]})
==
Munch({443: [74, 280], 444: [261, 311, 29], 445: [43, 162, 128], 446: [207,
308, 257], 448: [207, 131, 127], 447: [172]})