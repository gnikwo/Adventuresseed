from django.contrib import admin

from .models import *

from .forms import *

class ValueInline(admin.TabularInline):
    model = Value
    fieldsets = (
        (
            (None, {
                'fields': ('character', 'value')
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

class MessageInline(admin.TabularInline):
    model = Message
    fieldsets = (
        (
            (None, {
                'fields': ('name', 'text')
            })
        ),
    )

    extra = 0

class CharacterTemplateInline(admin.TabularInline):
    model = CharacterTemplate
    fieldsets = (
        (
            (None, {
                'fields': ('name', 'image')
            })
        ),
    )

    extra = 0

class AttributeInline(admin.TabularInline):
    model = Attribute
    fieldsets = (
        (
            (None, {
                'fields': ('name', )
            })
        ),
    )

    extra = 0

class AttributeCategoryInline(admin.TabularInline):
    model = AttributeCategory
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
                'fields': ('name', 'order')
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

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    form = CharacterForm


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    form = ValueForm


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    form = GameForm
    list_display = ['name', 'universe', 'last_played_date', 'active']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    form = MessageForm


@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
    form = UniverseForm


@admin.register(CharacterTemplate)
class CharacterTemplateAdmin(admin.ModelAdmin):
    form = CharacterTemplateForm


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    form = AttributeForm


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    form = MapForm


@admin.register(Layer)
class LayerAdmin(admin.ModelAdmin):
    form = LayerForm
    list_display = ['map', 'name', 'order', 'editable']


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    form = EntityForm


@admin.register(Sprite)
class SpriteAdmin(admin.ModelAdmin):
    form = SpriteForm


@admin.register(SpriteCategory)
class SpriteCategoryAdmin(admin.ModelAdmin):
    form = SpriteCategoryForm


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    form = ImageForm


