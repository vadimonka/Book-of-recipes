from django.db import models
from django.urls import reverse


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class IngredientCategories(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Категория ингредиента", help_text="Введите название категории ингредиента")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории ингредиентов'
        verbose_name_plural = 'Категории ингредиентов'


class Ingredients(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Ингредиент", help_text="Ведите название ингредиента")
    icon = models.ImageField(upload_to="icon_ingredient/", verbose_name=u"Иконка", help_text="Иконка")
    category = models.ForeignKey(IngredientCategories, related_name='ingredients', verbose_name=u"Категория", on_delete=models.PROTECT, help_text="Выберите "
                                                                                                                                                  "категорию "
                                                                                                                                                  "ингредиента")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Категория", help_text="Введите название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Recipes(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Название", help_text="Введите название рецепта")
    summary = models.TextField(verbose_name=u"Приготовление", help_text="Введите описание приготовления блюда")
    category = models.ManyToManyField(Categories, verbose_name=u"Категории", help_text="Выберите категории")
    ingredient = models.ManyToManyField(Ingredients, verbose_name=u"Ингредиенты", help_text="Выберите ингредиенты")
    calories = models.CharField(max_length=40, verbose_name=u"Калории", help_text="Кол-во калорий")
    cooking_time = models.CharField(max_length=20, verbose_name=u"Время приготовления", help_text="Время приготовления")
    preview = models.ImageField(upload_to="main_picture/", verbose_name=u"Основное изображение")
    views = models.ManyToManyField(Ip, blank=True)

    def __str__(self):
        return self.name

    def display_category(self):
        return ', '.join([category.name for category in self.category.all()])

    def display_ingredient(self):
        return ', '.join([ingredient.name for ingredient in self.ingredient.all()])

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])

    def total_views(self):
        return self.views.count()

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    display_category.short_description = 'Категории'
    display_ingredient.short_description = 'Ингредиенты'


class Posts(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"Заголовок", help_text="Введите заголовок поста")
    content = models.TextField(verbose_name=u"Содержимое поста", help_text="Введите текст поста")
    preview = models.ImageField(upload_to="preview_post/", verbose_name=u"Основное изображение")
    views = models.ManyToManyField(Ip, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def total_views(self):
        return self.views.count()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Блог'
