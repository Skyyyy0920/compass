©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 7
Num Failed Tests : 1
Num Total  Tests : 8
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
>> Passed Requirement
assert answers match.
>> Passed Requirement
assert model changes match simple_note.Note.
>> Passed Requirement
obtain added, updated, removed simple_note.Note records using
models.changed_records,
and assert 0 were added or removed.
>> Passed Requirement
assert exactly 1 simple_note.Note was updated.
>> Passed Requirement
assert the updated note has ID private_data.note_id.
>> Passed Requirement
parse the contents of the updated note to obtain song_name_to_artist_names,
song_name_to_release_month_str
and assert the song_name_to_artist_names match
private_data.song_name_to_artist_names (ignore order, normalize_text).
>> Passed Requirement
assert the udpated note has not changed in any other field ignoring content,
updated_at,
using models.changed_field_names.
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Fails ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
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
AssertionError:
{'haunted memories': '11/2022', 'gone astray': '06/2021', 'heartstrings
symphony': '12/2022', 'tangled lies': '2022-12', 'lost in the wilderness of
love': '2022-02', 'whispers of a forgotten love': '2022-02', 'lost in the
twilight of hope': '2022-07', 'the distance between two hearts': '2018-11',
'when all hope seems lost': '2022-04', 'the forgotten pages of time':
'2020-09', "summer's end": '2022-04', 'a tale of unspoken longing': '2022-02',
'cracks in the facade of love': '2020-07', 'a fading reflection in water':
'2020-07', 'trapped in a daydream': '2021-04', 'mystic voyage to avalon':
'2020-08'}
==
{'haunted memories': '11/2022', 'gone astray': '06/2021', 'heartstrings
symphony': '12/2022', 'tangled lies': '12/2022', 'lost in the wilderness of
love': '02/2022', 'whispers of a forgotten love': '02/2022', 'lost in the
twilight of hope': '07/2022', 'the distance between two hearts': '11/2018',
'when all hope seems lost': '04/2022', 'the forgotten pages of time':
'09/2020', "summer's end": '04/2022', 'a tale of unspoken longing': '02/2022',
'cracks in the facade of love': '07/2020', 'a fading reflection in water':
'07/2020', 'trapped in a daydream': '04/2021', 'mystic voyage to avalon':
'08/2020'}

Original values:
{'Haunted Memories': '11/2022', 'Gone Astray': '06/2021', 'Heartstrings
Symphony': '12/2022', 'Tangled Lies': '2022-12', 'Lost in the Wilderness of
Love': '2022-02', 'Whispers of a Forgotten Love': '2022-02', 'Lost in the
Twilight of Hope': '2022-07', 'The Distance Between Two Hearts': '2018-11',
'When All Hope Seems Lost': '2022-04', 'The Forgotten Pages of Time':
'2020-09', "Summer's End": '2022-04', 'A Tale of Unspoken Longing': '2022-02',
'Cracks in the Facade of Love': '2020-07', 'A Fading Reflection in Water':
'2020-07', 'Trapped in a Daydream': '2021-04', 'Mystic Voyage to Avalon':
'2020-08'}
==
Munch({'Haunted Memories': '11/2022', 'Gone Astray': '06/2021', 'Heartstrings
Symphony': '12/2022', 'Tangled Lies': '12/2022', 'Lost in the Wilderness of
Love': '02/2022', 'Whispers of a Forgotten Love': '02/2022', 'Lost in the
Twilight of Hope': '07/2022', 'The Distance Between Two Hearts': '11/2018',
'When All Hope Seems Lost': '04/2022', 'The Forgotten Pages of Time':
'09/2020', "Summer's End": '04/2022', 'A Tale of Unspoken Longing': '02/2022',
'Cracks in the Facade of Love': '07/2020', 'A Fading Reflection in Water':
'07/2020', 'Trapped in a Daydream': '04/2021', 'Mystic Voyage to Avalon':
'08/2020'})