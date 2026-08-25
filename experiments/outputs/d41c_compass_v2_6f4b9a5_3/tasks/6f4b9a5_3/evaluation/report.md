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
{'when angels weep for us': '07/2022', 'unspoken words': '06/2021', "time's
hold": '11/2022', 'bleeding sun': '11/2022', 'distant love': '12/2022', 'silver
lining': 'todo (release: 2022-12)', 'walking through the valley of shadows':
'todo (release: 2022-08)', 'where shadows come to life': 'todo (release:
2023-01)', 'eternal melancholy': 'todo (release: 2023-04)', 'crimson veil':
'todo (release: 2020-01)', 'elusive joy': 'todo (release: 2021-03)', 'ephemeral
beauty': 'todo (release: 2020-01)', 'stardust serenade': 'todo (release:
2019-04)', 'veiled behind a mask of joy': 'todo (release: 2022-10)', 'in the
wake of unspoken promises': 'todo (release: 2022-07)', 'wading through the
ashes of love': 'todo (release: 2020-09)', 'fading like a distant star': 'todo
(release: 2019-01)', 'wilted grace': 'todo (release: 2022-01)'}
==
{'when angels weep for us': '07/2022', 'unspoken words': '06/2021', "time's
hold": '11/2022', 'bleeding sun': '11/2022', 'distant love': '12/2022', 'silver
lining': '12/2022', 'walking through the valley of shadows': '08/2022', 'where
shadows come to life': '01/2023', 'eternal melancholy': '04/2023', 'crimson
veil': '01/2020', 'elusive joy': '03/2021', 'ephemeral beauty': '01/2020',
'stardust serenade': '04/2019', 'veiled behind a mask of joy': '10/2022', 'in
the wake of unspoken promises': '07/2022', 'wading through the ashes of love':
'09/2020', 'fading like a distant star': '01/2019', 'wilted grace': '01/2022'}

Original values:
{'When Angels Weep for Us': '07/2022', 'Unspoken Words': '06/2021', "Time's
Hold": '11/2022', 'Bleeding Sun': '11/2022', 'Distant Love': '12/2022', 'Silver
Lining': 'TODO (Release: 2022-12)', 'Walking Through the Valley of Shadows':
'TODO (Release: 2022-08)', 'Where Shadows Come to Life': 'TODO (Release:
2023-01)', 'Eternal Melancholy': 'TODO (Release: 2023-04)', 'Crimson Veil':
'TODO (Release: 2020-01)', 'Elusive Joy': 'TODO (Release: 2021-03)', 'Ephemeral
Beauty': 'TODO (Release: 2020-01)', 'Stardust Serenade': 'TODO (Release:
2019-04)', 'Veiled Behind a Mask of Joy': 'TODO (Release: 2022-10)', 'In the
Wake of Unspoken Promises': 'TODO (Release: 2022-07)', 'Wading Through the
Ashes of Love': 'TODO (Release: 2020-09)', 'Fading Like a Distant Star': 'TODO
(Release: 2019-01)', 'Wilted Grace': 'TODO (Release: 2022-01)'}
==
Munch({'When Angels Weep for Us': '07/2022', 'Unspoken Words': '06/2021',
"Time's Hold": '11/2022', 'Bleeding Sun': '11/2022', 'Distant Love': '12/2022',
'Silver Lining': '12/2022', 'Walking Through the Valley of Shadows': '08/2022',
'Where Shadows Come to Life': '01/2023', 'Eternal Melancholy': '04/2023',
'Crimson Veil': '01/2020', 'Elusive Joy': '03/2021', 'Ephemeral Beauty':
'01/2020', 'Stardust Serenade': '04/2019', 'Veiled Behind a Mask of Joy':
'10/2022', 'In the Wake of Unspoken Promises': '07/2022', 'Wading Through the
Ashes of Love': '09/2020', 'Fading Like a Distant Star': '01/2019', 'Wilted
Grace': '01/2022'})