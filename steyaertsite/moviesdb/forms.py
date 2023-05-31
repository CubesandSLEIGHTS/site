from django import forms

RATINGS = [
    ('rating', 'Rating...'),
    ('G', 'G'),
    ('PG', 'PG'),
    ('PG-13', 'PG-13'),
    ('R', 'R'),
    ('NR', 'NR'),
    ('TV', 'TV')
]

DISKS = [
    ('disk', 'Disk Type'),
    ('4k', '4K Ultra HD'),
    ('blu-ray', 'Blu-Ray'),
    ('dvd', 'DVD'),
]

class AddMovie(forms.Form):
    title = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Title', 'class':'form'}))
    rating = forms.ChoiceField(widget=forms.Select(attrs={'class':'choose'}), choices=RATINGS)
    disk = forms.ChoiceField(widget=forms.Select(attrs={'class':'choose'}), choices=DISKS)