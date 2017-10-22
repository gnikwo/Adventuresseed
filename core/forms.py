from django import forms

from .models import Player
from .models import Participation
from .models import Character
from .models import Value
from .models import Game
from .models import Note
from .models import Universe
from .models import Template
from .models import Field
from .models import Map
from .models import Layer
from .models import Entity
from .models import Sprite

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', ]

class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ['game', 'player', 'character']

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'template']

class ValueForm(forms.ModelForm):
    class Meta:
        model = Value
        fields = ['character', 'field', 'value']

    #field = forms.ModelChoiceField(queryset=Universe.objects.all()[0].template.get().fields, empty_label="(Nothing)")

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'universe']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'text']

class UniverseForm(forms.ModelForm):
    class Meta:
        model = Universe
        fields = ['name']

class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'universe', 'image']

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['template', 'name', 'position_x', 'position_y', 'scale_x', 'scale_y']

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['game', 'name', 'active']

class LayerForm(forms.ModelForm):
    class Meta:
        model = Layer
        fields = ['map', 'name', 'layer_height']

class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ['layer', 'sprite', 'position_x', 'position_y', 'scale_x', 'scale_y']

class SpriteForm(forms.ModelForm):
    class Meta:
        model = Sprite
        fields = ['name', 'image']
