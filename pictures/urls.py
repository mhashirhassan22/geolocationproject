from django.urls import path
from pictures.views import index,pictures,add_or_remove_favorite,View_Favorites

app_name ='pictures'

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('pictures', pictures.as_view(), name="pictures"),
    path('add_favorite', add_or_remove_favorite.as_view(), name ="add_favorite"),
    path('favorites', View_Favorites.as_view(), name="favorites")
]