──────────────────────────────── Overall Stats ────────────────────────────────
Num Passed Tests : 7
Num Failed Tests : 1
Num Total  Tests : 8
─────────────────────────────────── Passes ────────────────────────────────────
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
──────────────────────────────────── Fails ────────────────────────────────────
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
lining': '2022-12', 'walking through the valley of shadows': '2022-08', 'where
shadows come to life': '2023-01', 'eternal melancholy': '2023-04', 'crimson
veil': '2020-01', 'elusive joy': '2021-03', 'ephemeral beauty': '2020-01',
'stardust serenade': '2019-04', 'veiled behind a mask of joy': '2022-10', 'in
the wake of unspoken promises': '2022-07', 'wading through the ashes of love':
'2020-09', 'fading like a distant star': '2019-01', 'wilted grace': '2022-01'}
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
Lining': '2022-12', 'Walking Through the Valley of Shadows': '2022-08', 'Where
Shadows Come to Life': '2023-01', 'Eternal Melancholy': '2023-04', 'Crimson
Veil': '2020-01', 'Elusive Joy': '2021-03', 'Ephemeral Beauty': '2020-01',
'Stardust Serenade': '2019-04', 'Veiled Behind a Mask of Joy': '2022-10', 'In
the Wake of Unspoken Promises': '2022-07', 'Wading Through the Ashes of Love':
'2020-09', 'Fading Like a Distant Star': '2019-01', 'Wilted Grace': '2022-01'}
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