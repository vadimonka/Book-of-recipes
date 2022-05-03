from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recipes/$', views.RecipesListView.as_view(), name='recipes'),
    url(r'^recipe/(?P<pk>\d+)$', views.recipes_view, name='recipe-detail'),
    url(r'^blog/$', views.PostsListView.as_view(), name='posts'),
    url(r'^post/(?P<pk>\d+)$', views.PostsDetailView.as_view(), name='post-detail'),
    url(r'^category/(?P<pk>\d+)$', views.get_recipes_from_category, name='recipes-from-category'),
]
