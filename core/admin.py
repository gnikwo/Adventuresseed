from django.contrib import admin

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

from .forms import PlayerForm
from .forms import ParticipationForm
from .forms import CharacterForm
from .forms import ValueForm
from .forms import GameForm
from .forms import NoteForm
from .forms import UniverseForm
from .forms import TemplateForm
from .forms import FieldForm
from .forms import MapForm
from .forms import LayerForm
from .forms import EntityForm
from .forms import SpriteForm

class ParticipationInline(admin.TabularInline):
    model = Participation
    fieldsets = (
        (
            (None, {
                'fields': ('player', 'character')
            })
        ),
    )

    extra = 0

class ValueInline(admin.TabularInline):
    model = Value
    fieldsets = (
        (
            (None, {
                'fields': ('field', 'value')
            })
        ),
    )

    extra = 0

class GameInline(admin.TabularInline):
    model = Game
    fieldsets = (
        (
            (None, {
                'fields': ('name', 'universe')
            })
        ),
    )

    extra = 0

class NoteInline(admin.TabularInline):
    model = Note
    fieldsets = (
        (
            (None, {
                'fields': ('name', 'text')
            })
        ),
    )

    extra = 0

class TemplateInline(admin.TabularInline):
    model = Template
    fieldsets = (
        (
            (None, {
                'fields': ('name', 'image')
            })
        ),
    )

    extra = 0

class FieldInline(admin.TabularInline):
    model = Field
    fieldsets = (
        (
            (None, {
                'fields': ('name', )
            })
        ),
    )

    extra = 0

class MapInline(admin.TabularInline):
    model = Map
    fieldsets = (
        (
            (None, {
                'fields': ('name', 'active')
            })
        ),
    )

    extra = 0

class LayerInline(admin.TabularInline):
    model = Layer
    fieldsets = (
        (
            (None, {
                'fields': ('name', 'layer_height')
            })
        ),
    )

    extra = 0

class EntityInline(admin.TabularInline):
    model = Entity
    fieldsets = (
        (
            (None, {
                'fields': ('sprite', )
            })
        ),
    )

    extra = 0

class PlayerAdmin(admin.ModelAdmin):
    form = PlayerForm
    inlines = [ParticipationInline, ]

class ParticipationAdmin(admin.ModelAdmin):
    form = ParticipationForm

class CharacterAdmin(admin.ModelAdmin):
    form = CharacterForm
    inlines = [ValueInline, ]

class ValueAdmin(admin.ModelAdmin):
    form = ValueForm

class GameAdmin(admin.ModelAdmin):
    form = GameForm
    inlines = [ParticipationInline, NoteInline]

class NoteAdmin(admin.ModelAdmin):
    form = NoteForm

class UniverseAdmin(admin.ModelAdmin):
    form = UniverseForm
    inlines = [TemplateInline, ]

class TemplateAdmin(admin.ModelAdmin):
    form = TemplateForm
    inlines = [FieldInline, ]

class FieldAdmin(admin.ModelAdmin):
    form = FieldForm

class MapAdmin(admin.ModelAdmin):
    form = MapForm
    inlines = [LayerInline, ]

class LayerAdmin(admin.ModelAdmin):
    form = LayerForm
    inlines = [EntityInline, ]

class EntityAdmin(admin.ModelAdmin):
    form = EntityForm

class SpriteAdmin(admin.ModelAdmin):
    form = SpriteForm
    inlines = [EntityInline, ]

admin.site.register(Player, PlayerAdmin)
admin.site.register(Participation, ParticipationAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Value, ValueAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Universe, UniverseAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(Layer, LayerAdmin)
admin.site.register(Entity, EntityAdmin)
admin.site.register(Sprite, SpriteAdmin)
