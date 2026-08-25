©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Overall Stats ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
Num Passed Tests : 6
Num Failed Tests : 2
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
assert the udpated note has not changed in any other field ignoring content,
updated_at,
using models.changed_field_names.
©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤ Fails ©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤©¤
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
AssertionError:
{'when angels weep for us': ['lucas grey', 'velvet echo'], 'unspoken words':
['aria sterling'], "time's hold": ['aria sterling'], 'the last goodbye':
['velvet echo'], 'lost in the moment': ['aria sterling', 'lucas grey'], 'echoes
of silence': ['velvet echo'], 'shattered glass': ['lucas grey'], 'midnight
reverie': ['aria sterling']}
==
{'when angels weep for us': ['lucas grey', 'velvet echo'], 'unspoken words':
['aria sterling'], "time's hold": ['aria sterling'], 'bleeding sun': ['aria
sterling'], 'distant love': ['ava morgan'], 'silver lining': ['ava morgan'],
'walking through the valley of shadows': ['lily moon', 'zoey james'], 'where
shadows come to life': ['olivia roberts'], 'eternal melancholy': ['olivia
roberts'], 'crimson veil': ['phoenix rivers'], 'elusive joy': ['orion steele'],
'ephemeral beauty': ['eliana harper'], 'stardust serenade': ['violet cascade'],
'veiled behind a mask of joy': ['liam palmer'], 'in the wake of unspoken
promises': ['isabella cruz'], 'wading through the ashes of love': ['marcus
lane'], 'fading like a distant star': ['hazel winter'], 'wilted grace': ['felix
blackwood']}

Original values:
{'When Angels Weep for Us': ['Lucas Grey', ' Velvet Echo'], 'Unspoken Words':
['Aria Sterling'], "Time's Hold": ['Aria Sterling'], 'The Last Goodbye':
['Velvet Echo'], 'Lost in the Moment': ['Lucas Grey', ' Aria Sterling'],
'Echoes of Silence': ['Velvet Echo'], 'Shattered Glass': ['Lucas Grey'],
'Midnight Reverie': ['Aria Sterling']}
==
Munch({'When Angels Weep for Us': ['Lucas Grey', 'Velvet Echo'], 'Unspoken
Words': ['Aria Sterling'], "Time's Hold": ['Aria Sterling'], 'Bleeding Sun':
['Aria Sterling'], 'Distant Love': ['Ava Morgan'], 'Silver Lining': ['Ava
Morgan'], 'Walking Through the Valley of Shadows': ['Lily Moon', 'Zoey James'],
'Where Shadows Come to Life': ['Olivia Roberts'], 'Eternal Melancholy':
['Olivia Roberts'], 'Crimson Veil': ['Phoenix Rivers'], 'Elusive Joy': ['Orion
Steele'], 'Ephemeral Beauty': ['Eliana Harper'], 'Stardust Serenade': ['Violet
Cascade'], 'Veiled Behind a Mask of Joy': ['Liam Palmer'], 'In the Wake of
Unspoken Promises': ['Isabella Cruz'], 'Wading Through the Ashes of Love':
['Marcus Lane'], 'Fading Like a Distant Star': ['Hazel Winter'], 'Wilted
Grace': ['Felix Blackwood']})
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
hold": '05/2021', 'the last goodbye': '03/2022', 'lost in the moment':
'11/2022', 'echoes of silence': '06/2022', 'shattered glass': '10/2019',
'midnight reverie': '03/2020'}
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
Hold": '05/2021', 'The Last Goodbye': '03/2022', 'Lost in the Moment':
'11/2022', 'Echoes of Silence': '06/2022', 'Shattered Glass': '10/2019',
'Midnight Reverie': '03/2020'}
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