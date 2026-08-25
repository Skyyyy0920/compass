©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 1
Num Failed Tests : 6
Num Total  Tests : 7
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Passed Requirement
assert model changes match spotify.Playlist, spotify.PlaylistSong.
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
AssertionError:  2 == 1
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
AssertionError:  'Archived Playlist Songs (AI Archive)' == 'Archived Playlist
Songs'
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
AssertionError:  set() == {320, 324, 4, 69, 295, 265, 298, 299, 245, 22, 278,
219, 92}

In right but not left:
[320, 324, 4, 69, 295, 265, 298, 299, 245, 22, 278, 219, 92]
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
{320, 4, 324, 295, 299, 245, 22, 92}
==
{320, 324, 4, 69, 295, 265, 298, 299, 245, 22, 278, 219, 92}

In right but not left:
[69, 265, 298, 278, 219]
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
{515: [245], 516: [92, 299, 320], 514: [22, 324], 517: [4], 513: [295]}
==
{513: [295], 514: [22, 324], 519: [22, 265, 298], 515: [245], 516: [92, 299,
320], 517: [4], 518: [69, 219, 278]}

Original values:
defaultdict(<class 'list'>, {515: [245], 516: [320, 92, 299], 514: [22, 324],
517: [4], 513: [295]})
==
Munch({513: [295], 514: [324, 22], 519: [22, 298, 265], 515: [245], 516: [320,
92, 299], 517: [4], 518: [278, 69, 219]})