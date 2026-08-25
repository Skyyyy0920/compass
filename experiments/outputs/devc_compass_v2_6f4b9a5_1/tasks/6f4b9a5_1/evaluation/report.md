©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 2
Num Failed Tests : 6
Num Total  Tests : 8
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Passed Requirement
assert answers match.
>> Passed Requirement
obtain added, updated, removed simple_note.Note records using
models.changed_records,
and assert 0 were added or removed.
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Fails ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Failed Requirement
assert model changes match simple_note.Note.
```python
with test(
    """
    assert model changes match simple_note.Note.
    """
):
    test.case(models.changed_model_names(), "==", {"simple_note.Note"})
```
----------
AssertionError:  set() == {'simple_note.Note'}

In right but not left:
['simple_note.Note']
>> Failed Requirement
assert exactly 1 simple_note.Note was updated.
```python
with test(
    """
    assert exactly 1 simple_note.Note was updated.
    """
):
    test.case(len(updated_notes), "==", 1)
    updated_note = updated_notes[0]
```
----------
AssertionError:  0 == 1
>> Failed Requirement
assert the updated note has ID private_data.note_id.
```python
with test(
    """
    assert the updated note has ID private_data.note_id.
    """
):
    test.case(updated_note.id, "==", private_data.note_id)
```
----------
>> Failed Requirement
parse the contents of the updated note to obtain song_name_to_artist_names,
song_name_to_release_month_str
and assert the song_name_to_artist_names match
private_data.song_name_to_artist_names (ignore order, normalize_text).
```python
with test(
    """
    parse the contents of the updated note to obtain song_name_to_artist_names,
song_name_to_release_month_str
    and assert the song_name_to_artist_names match
    private_data.song_name_to_artist_names (ignore order, normalize_text).
    """
):
    content_lines = updated_note.content.split("\n")
```
----------
>> Failed Requirement
assert the song_name_to_release_month_str match
private_data.song_name_to_release_month_str (ignore order, normalize_text).
```python
with test(
    """
    assert the song_name_to_release_month_str match
    private_data.song_name_to_release_month_str (ignore order, normalize_text).
    """
):
    test.case(
        song_name_to_release_month_str,
```
----------
>> Failed Requirement
assert the udpated note has not changed in any other field ignoring content,
updated_at,
using models.changed_field_names.
```python
with test(
    """
    assert the udpated note has not changed in any other field ignoring
content, updated_at,
    using models.changed_field_names.
    """
):
    changed_field_names = models.changed_field_names(
        "simple_note.Note", updated_note.id, ignore=["content", "updated_at"]
```
----------