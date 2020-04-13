from django import forms
import datetime

from .models import * 

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'color']

class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ['game', 'player', 'character']

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', ]

class SheetForm(forms.ModelForm):
    class Meta:
        model = Sheet 
        fields = ['character', 'template']

class ValueForm(forms.ModelForm):
    class Meta:
        model = Value
        fields = ['sheet', 'field', 'value']

    #field = forms.ModelChoiceField(queryset=Universe.objects.all()[0].template.get().fields, empty_label="(Nothing)")

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'universe', 'last_played_date', 'selected']

    def save(self, commit=True):
        instance = super(GameForm, self).save(commit=False)
        if getattr(self.changed_data, 'selected', True):
            instance.last_played_date = datetime.datetime.now()
            instance.save()
            Game.objects.all().update(selected=False);
        return instance

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
        fields = ['map', 'name', 'layer_height', 'player_accessible']

class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ['layer', 'sprite', 'position_x', 'position_y', 'scale_x', 'scale_y']

class SpriteForm(forms.ModelForm):
    class Meta:
        model = Sprite
        fields = ['name', 'image']
