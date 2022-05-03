from django.db.models import Q
from django.shortcuts import render

from .models import *
from django.views import generic


def index(request):
    ingredient_categories = IngredientCategories.objects.all()
    ingredients = Ingredients.objects.all()
    return render(
        request,
        'index.html',
        context={'ingredients': ingredients, 'ingredient_categories': ingredient_categories}
    )


def categories_base(request):
    return {'categories_base': Categories.objects.all().order_by('name')}


# вывод рецептов по категории
def get_recipes_from_category(request, pk):
    categ = Categories.objects.get(pk=pk)
    recipes = Recipes.objects.all()

    return render(
        request,
        'recipes-from-category.html',
        context={'categ': categ, 'recipes': recipes})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class RecipesListView(generic.ListView):
    model = Recipes

    def get_queryset(self):
        query = self.request.GET.get('q')
        query_ingred = self.request.GET.get('qi')
        if query_ingred:
            query_ingred = query_ingred.split(',')

        if query:
            return Recipes.objects.filter(Q(name__icontains=query) | Q(name__icontains=query.title()) | Q(name__icontains=query.capitalize())
                                          | Q(name__icontains=query.lower()) | Q(name__icontains=query.upper()))
        elif query_ingred:
            recipes_list = Recipes.objects.all()
            for ingred in query_ingred:
                recipes_list = recipes_list.filter(ingredient__name=ingred)
            return recipes_list
        else:
            return Recipes.objects.all()


def recipes_view(request, pk):
    recipe = Recipes.objects.get(pk=pk)

    ip = get_client_ip(request)

    Ip.objects.get_or_create(ip=ip)
    recipe.views.add(Ip.objects.get(ip=ip))

    return render(
        request,
        'catalog/recipes_detail.html',
        context={'recipe': recipe})


class PostsListView(generic.ListView):
    model = Posts


class PostsDetailView(generic.DetailView):
    model = Posts
