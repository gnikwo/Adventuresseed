from django.contrib import admin

from .models import * 

from .forms import *

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

class SheetInline(admin.TabularInline):
    model = Sheet 
    fieldsets = (
        (
            (None, {
                'fields': ('template', )
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
    inlines = [SheetInline, ]

class SheetAdmin(admin.ModelAdmin):
    form = SheetForm
    inlines = [ValueInline, ]

class ValueAdmin(admin.ModelAdmin):
    form = ValueForm

class GameAdmin(admin.ModelAdmin):
    form = GameForm
    list_display = ['name', 'universe', 'last_played_date', 'selected']
    inlines = [ParticipationInline, NoteInline, MapInline]

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
    list_display = ['map', 'name', 'layer_height', 'player_accessible']
    inlines = [EntityInline, ]

class EntityAdmin(admin.ModelAdmin):
    form = EntityForm

class SpriteAdmin(admin.ModelAdmin):
    form = SpriteForm
    inlines = [EntityInline, ]

admin.site.register(Player, PlayerAdmin)
admin.site.register(Participation, ParticipationAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Sheet, SheetAdmin)
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
