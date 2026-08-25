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
{'gone astray': ['aria sterling'], 'tangled lies': ['ava morgan'], 'lost in the
wilderness of love': ['lily moon', 'zoey james'], 'whispers of a forgotten
love': ['lily moon', 'zoey james'], 'lost in the twilight of hope': ['felix
blackwood'], 'the distance between two hearts': ['jasper skye'], 'when all hope
seems lost': ['seraphina dawn'], 'the forgotten pages of time': ['luna
starlight'], "summer's end": ['ethan wallace'], 'a tale of unspoken longing':
['emily rivers'], 'cracks in the facade of love': ['velvet echo'], 'a fading
reflection in water': ['lucas grey'], 'trapped in a daydream': ['nova
harmony'], 'mystic voyage to avalon': ['nova harmony']}
==
{'haunted memories': ['apollo serenade', 'phoenix rivers'], 'gone astray':
['aria sterling'], 'heartstrings symphony': ['ava morgan'], 'tangled lies':
['ava morgan'], 'lost in the wilderness of love': ['lily moon', 'zoey james'],
'whispers of a forgotten love': ['lily moon', 'zoey james'], 'lost in the
twilight of hope': ['felix blackwood'], 'the distance between two hearts':
['jasper skye'], 'when all hope seems lost': ['seraphina dawn'], 'the forgotten
pages of time': ['luna starlight'], "summer's end": ['ethan wallace'], 'a tale
of unspoken longing': ['emily rivers'], 'cracks in the facade of love':
['velvet echo'], 'a fading reflection in water': ['lucas grey'], 'trapped in a
daydream': ['nova harmony'], 'mystic voyage to avalon': ['nova harmony']}

Original values:
{'Gone Astray': ['Aria Sterling'], 'Tangled Lies': ['Ava Morgan'], 'Lost in the
Wilderness of Love': ['Lily Moon', ' Zoey James'], 'Whispers of a Forgotten
Love': ['Lily Moon', ' Zoey James'], 'Lost in the Twilight of Hope': ['Felix
Blackwood'], 'The Distance Between Two Hearts': ['Jasper Skye'], 'When All Hope
Seems Lost': ['Seraphina Dawn'], 'The Forgotten Pages of Time': ['Luna
Starlight'], "Summer's End": ['Ethan Wallace'], 'A Tale of Unspoken Longing':
['Emily Rivers'], 'Cracks in the Facade of Love': ['Velvet Echo'], 'A Fading
Reflection in Water': ['Lucas Grey'], 'Trapped in a Daydream': ['Nova
Harmony'], 'Mystic Voyage to Avalon': ['Nova Harmony']}
==
Munch({'Haunted Memories': ['Apollo Serenade', 'Phoenix Rivers'], 'Gone
Astray': ['Aria Sterling'], 'Heartstrings Symphony': ['Ava Morgan'], 'Tangled
Lies': ['Ava Morgan'], 'Lost in the Wilderness of Love': ['Lily Moon', 'Zoey
James'], 'Whispers of a Forgotten Love': ['Lily Moon', 'Zoey James'], 'Lost in
the Twilight of Hope': ['Felix Blackwood'], 'The Distance Between Two Hearts':
['Jasper Skye'], 'When All Hope Seems Lost': ['Seraphina Dawn'], 'The Forgotten
Pages of Time': ['Luna Starlight'], "Summer's End": ['Ethan Wallace'], 'A Tale
of Unspoken Longing': ['Emily Rivers'], 'Cracks in the Facade of Love':
['Velvet Echo'], 'A Fading Reflection in Water': ['Lucas Grey'], 'Trapped in a
Daydream': ['Nova Harmony'], 'Mystic Voyage to Avalon': ['Nova Harmony']})
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
{'gone astray': '06/2021 (release: february 2022)', 'tangled lies': 'todo |
release month: december 2022 (release: november 2018) | release month: april
2022', 'lost in the wilderness of love': 'todo | release month: february 2022',
'whispers of a forgotten love': 'todo | release month: february 2022 | release
month: february 2022', 'lost in the twilight of hope': 'todo', 'the distance
between two hearts': 'todo | release month: november 2018', 'when all hope
seems lost': 'todo | release month: april 2022', 'the forgotten pages of time':
'todo | release month: september 2020', "summer's end": 'todo | release month:
april 2022', 'a tale of unspoken longing': 'todo | release month: february
2022', 'cracks in the facade of love': 'todo | release month: july 2020', 'a
fading reflection in water': 'todo | release month: july 2020', 'trapped in a
daydream': 'todo | release month: april 2021', 'mystic voyage to avalon': 'todo
| release month: august 2020'}
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
{'Gone Astray': '06/2021 (Release: February 2022)', 'Tangled Lies': 'TODO |
release month: December 2022 (Release: November 2018) | Release Month: April
2022', 'Lost in the Wilderness of Love': 'TODO | release month: February 2022',
'Whispers of a Forgotten Love': 'TODO | release month: February 2022 | Release
Month: February 2022', 'Lost in the Twilight of Hope': 'TODO', 'The Distance
Between Two Hearts': 'TODO | Release Month: November 2018', 'When All Hope
Seems Lost': 'TODO | Release Month: April 2022', 'The Forgotten Pages of Time':
'TODO | Release Month: September 2020', "Summer's End": 'TODO | Release Month:
April 2022', 'A Tale of Unspoken Longing': 'TODO | Release Month: February
2022', 'Cracks in the Facade of Love': 'TODO | Release Month: July 2020', 'A
Fading Reflection in Water': 'TODO | Release Month: July 2020', 'Trapped in a
Daydream': 'TODO | Release Month: April 2021', 'Mystic Voyage to Avalon': 'TODO
| Release Month: August 2020'}
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