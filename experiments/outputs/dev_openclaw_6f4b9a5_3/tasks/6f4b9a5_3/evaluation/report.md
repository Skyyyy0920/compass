©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 6
Num Failed Tests : 2
Num Total  Tests : 8
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Passes ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
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
AssertionError:
"# spotify liked songs\n- when angels weep for us by lucas grey, velvet echo
released_at 07/2022\n- unspoken words by aria sterling released_at 06/2021\n-
time's hold by aria sterling released_at 11/2022\n- bleeding sun by aria
sterling released_at 11/2022\n- distant love by ava morgan released_at
12/2022\n- silver lining by ava morgan released_at 12/2022\n- walking through
the valley of shadows by lily moon, zoey james released_at 08/2022\n- where
shadows come to life by olivia roberts released_at todo\n- eternal melancholy
by olivia roberts released_at todo\n- crimson veil by phoenix rivers
released_at todo\n- elusive joy by orion steele released_at todo\n- ephemeral
beauty by eliana harper released_at todo\n- stardust serenade by violet cascade
released_at todo\n- veiled behind a mask of joy by liam palmer released_at
todo\n- in the wake of unspoken promises by isabella cruz released_at todo\n-
wading through the ashes of love by marcus lane released_at todo\n- fading like
a distant star by hazel winter released_at todo\n- wilted grace by felix
blackwood released_at todo"
==
'null'
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
lining': '12/2022', 'walking through the valley of shadows': '08/2022', 'where
shadows come to life': 'todo', 'eternal melancholy': 'todo', 'crimson veil':
'todo', 'elusive joy': 'todo', 'ephemeral beauty': 'todo', 'stardust serenade':
'todo', 'veiled behind a mask of joy': 'todo', 'in the wake of unspoken
promises': 'todo', 'wading through the ashes of love': 'todo', 'fading like a
distant star': 'todo', 'wilted grace': 'todo'}
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
Lining': '12/2022', 'Walking Through the Valley of Shadows': '08/2022', 'Where
Shadows Come to Life': 'TODO', 'Eternal Melancholy': 'TODO', 'Crimson Veil':
'TODO', 'Elusive Joy': 'TODO', 'Ephemeral Beauty': 'TODO', 'Stardust Serenade':
'TODO', 'Veiled Behind a Mask of Joy': 'TODO', 'In the Wake of Unspoken
Promises': 'TODO', 'Wading Through the Ashes of Love': 'TODO', 'Fading Like a
Distant Star': 'TODO', 'Wilted Grace': 'TODO'}
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