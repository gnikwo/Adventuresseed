from django.db import models
import os
from uuid import uuid4

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper


class Character(models.Model):
    game = models.ForeignKey('Game', related_name='characters', on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=40, blank=False)
    player = models.CharField(max_length=40, blank=True)
    chat_name = models.CharField(max_length=40, blank=True)
    notes = models.TextField(blank=True)
    color = models.CharField(max_length=6, blank=False)
    profile_picture = models.ForeignKey('Image', related_name='profile_pictures', on_delete=models.CASCADE, null=True, blank=True)
    template = models.ForeignKey('CharacterTemplate', related_name='characters', on_delete=models.CASCADE, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Value(models.Model):
    character = models.ForeignKey('CharacterTemplate', related_name='values', on_delete=models.CASCADE, null=False)
    attribute = models.ForeignKey('Attribute', related_name='values', on_delete=models.CASCADE, null=False)
    value = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.character) + ': '


class Game(models.Model):
    name = models.CharField(max_length=50, blank=False)
    universe = models.ForeignKey('Universe', related_name='games', on_delete=models.CASCADE, null=False)
    notes = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    last_played_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField(blank=True)
    game = models.ForeignKey('Game', related_name='messages', on_delete=models.CASCADE, null=False)
    character = models.ForeignKey('CharacterTemplate', related_name='messages', on_delete=models.CASCADE, null=False)
    image = models.ForeignKey('Sprite', related_name='messages', on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Universe(models.Model):
    name = models.CharField(max_length=20, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CharacterTemplate(models.Model):
    name = models.CharField(max_length=50, blank=False)
    universe = models.ForeignKey('Universe', related_name='template', on_delete=models.CASCADE, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.universe) + ' - ' + str(self.name)


class Attribute(models.Model):
    name = models.CharField(max_length=40, blank=False)
    category = models.ForeignKey('AttributeCategory', related_name='attributes', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class AttributeCategory(models.Model):
    name = models.CharField(max_length=40, blank=False)
    template = models.ForeignKey('CharacterTemplate', related_name='fields', on_delete=models.CASCADE, null=False)
    order = models.IntegerField(null=False)


class Map(models.Model):
    name = models.CharField(max_length=40, blank=False)
    active = models.BooleanField()
    game = models.ForeignKey('Game', related_name='maps', on_delete=models.CASCADE, null=False)
    order = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Layer(models.Model):
    name = models.CharField(max_length=40, blank=False)
    editable = models.BooleanField(default=False)
    order = models.IntegerField(null=False)
    map = models.ForeignKey('Map', related_name='layers', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Entity(models.Model):
    class Meta:
        verbose_name_plural = 'Entities'
    position_x = models.IntegerField(null=False, default=0)
    position_y = models.IntegerField(null=False, default=0)
    scale_x = models.IntegerField(null=False, default=0)
    scale_y = models.IntegerField(null=False, default=0)
    rotation = models.FloatField(null=False, default=0)
    layer = models.ForeignKey('Layer', related_name='entities', on_delete=models.CASCADE, null=False)
    sprite = models.ForeignKey('Sprite', related_name='entities', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.sprite)


class Sprite(models.Model):
    image = models.ForeignKey('Image', related_name='sprites', on_delete=models.CASCADE, null=False)
    category = models.ForeignKey('SpriteCategory', related_name='attributes', on_delete=models.CASCADE, null=False)


class SpriteCategory(models.Model):
    name = models.CharField(max_length=40, blank=False)


class Image(models.Model):
    name = models.CharField(max_length=40, blank=False)
    image = models.ImageField(upload_to='media/sprites/', null=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


