from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class RecipesAdminForm(forms.ModelForm):
    summary = forms.CharField(label=u"Приготовление", widget=CKEditorUploadingWidget())

    class Meta:
        model = Recipes
        fields = '__all__'


class PostsAdminForm(forms.ModelForm):
    content = forms.CharField(label=u"Содержимое поста", widget=CKEditorUploadingWidget())

    class Meta:
        model = Posts
        fields = '__all__'


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_category', 'display_ingredient', 'calories', 'cooking_time')
    search_fields = ['name', 'ingredient__name', 'category__name']
    exclude = ['views']
    form = RecipesAdminForm
    readonly_fields = ["___"]

    @staticmethod
    def ___(obj):
        return mark_safe(f'<img src="{obj.preview.url}" style="max-height: 150px;">')


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    display = 'name'
    search_fields = ['name']


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    display = 'name'
    search_fields = ['name']


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    display = "title"
    search_fields = ['name']
    exclude = ['views']
    form = PostsAdminForm

    readonly_fields = ["___"]

    @staticmethod
    def ___(obj):
        return mark_safe(f'<img src="{obj.preview.url}" style="max-height: 150px;">')


@admin.register(IngredientCategories)
class IngredientCategoriesAdmin(admin.ModelAdmin):
    display = "name"
