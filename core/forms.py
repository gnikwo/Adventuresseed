from django import forms
import datetime

from .models import *

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['game', 'name', 'player', 'chat_name', 'color', 'profile_picture', 'template', 'notes']


class ValueForm(forms.ModelForm):
    class Meta:
        model = Value
        fields = ['character', 'attribute', 'value']


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'universe', 'active', 'last_played_date', 'notes']

    def save(self, commit=True):
        instance = super(GameForm, self).save(commit=False)
        if getattr(self.changed_data, 'active', True):
            instance.last_played_date = datetime.datetime.now()
            instance.save()
            Game.objects.all().update(active=False);
        return instance

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'game', 'character', 'image']


class UniverseForm(forms.ModelForm):
    class Meta:
        model = Universe
        fields = ['name']


class CharacterTemplateForm(forms.ModelForm):
    class Meta:
        model = CharacterTemplate
        fields = ['name', 'universe']


class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = ['name', 'category']


class AttributeCategoryForm(forms.ModelForm):
    class Meta:
        model = AttributeCategory
        fields = ['name', 'template']


class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['game', 'name', 'active', 'order']


class LayerForm(forms.ModelForm):
    class Meta:
        model = Layer
        fields = ['map', 'name', 'order', 'editable']


class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ['layer', 'sprite', 'position_x', 'position_y', 'scale_x', 'scale_y', 'rotation']


class SpriteForm(forms.ModelForm):
    class Meta:
        model = Sprite
        fields = ['category', 'image']


class SpriteCategoryForm(forms.ModelForm):
    class Meta:
        model = SpriteCategory
        fields = ['name']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image']
