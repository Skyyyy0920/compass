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
{'the fragrance of fading roses': '10/2022', 'the puzzle of my heart':
'10/2022', "lost in a moment's grace": '11/2022', 'in the depths of despair':
'11/2022', 'lost in the embrace of night': 'todo | release month: 2022-10',
'lonely skies': 'todo | release month: 2022-10', 'caught in a web of lies':
'todo | release month: 2022-10', 'on the border of reality': 'todo | release
month: 2022-10', 'a love that never was': 'todo | release month: 2022-10',
'astral serenity': 'todo | release month: 2022-10', 'between reality and
reverie': 'todo | release month: 2022-10', 'strangers again': 'todo | release
month: 2022-10', 'the mirage of a perfect life': 'todo | release month:
2022-10', 'wilted roses on the vine': 'todo | release month: 2022-10', 'when
all words fail us': 'todo | release month: 2022-10', 'final echo': 'todo |
release month: 2022-10'}
==
{'the fragrance of fading roses': '10/2022', 'the puzzle of my heart':
'10/2022', "lost in a moment's grace": '11/2022', 'in the depths of despair':
'11/2022', 'lost in the embrace of night': '03/2021', 'lonely skies':
'11/2022', 'caught in a web of lies': '03/2021', 'on the border of reality':
'08/2022', 'a love that never was': '10/2020', 'astral serenity': '12/2019',
'between reality and reverie': '03/2020', 'strangers again': '06/2022', 'the
mirage of a perfect life': '11/2020', 'wilted roses on the vine': '02/2020',
'when all words fail us': '07/2020', 'final echo': '07/2022'}

Original values:
{'The Fragrance of Fading Roses': '10/2022', 'The Puzzle of My Heart':
'10/2022', "Lost in a Moment's Grace": '11/2022', 'In the Depths of Despair':
'11/2022', 'Lost in the Embrace of Night': 'TODO | Release Month: 2022-10',
'Lonely Skies': 'TODO | Release Month: 2022-10', 'Caught in a Web of Lies':
'TODO | Release Month: 2022-10', 'On the Border of Reality': 'TODO | Release
Month: 2022-10', 'A Love That Never Was': 'TODO | Release Month: 2022-10',
'Astral Serenity': 'TODO | Release Month: 2022-10', 'Between Reality and
Reverie': 'TODO | Release Month: 2022-10', 'Strangers Again': 'TODO | Release
Month: 2022-10', 'The Mirage of a Perfect Life': 'TODO | Release Month:
2022-10', 'Wilted Roses on the Vine': 'TODO | Release Month: 2022-10', 'When
All Words Fail Us': 'TODO | Release Month: 2022-10', 'Final Echo': 'TODO |
Release Month: 2022-10'}
==
Munch({'The Fragrance of Fading Roses': '10/2022', 'The Puzzle of My Heart':
'10/2022', "Lost in a Moment's Grace": '11/2022', 'In the Depths of Despair':
'11/2022', 'Lost in the Embrace of Night': '03/2021', 'Lonely Skies':
'11/2022', 'Caught in a Web of Lies': '03/2021', 'On the Border of Reality':
'08/2022', 'A Love That Never Was': '10/2020', 'Astral Serenity': '12/2019',
'Between Reality and Reverie': '03/2020', 'Strangers Again': '06/2022', 'The
Mirage of a Perfect Life': '11/2020', 'Wilted Roses on the Vine': '02/2020',
'When All Words Fail Us': '07/2020', 'Final Echo': '07/2022'})