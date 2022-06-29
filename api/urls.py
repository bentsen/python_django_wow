from django.urls import path
from api import views


urlpatterns = [
    path('item/<int:itemId>', views.get_item),
    path('character/media/<str:region>/<str:realmSlug>/<str:characterName>', views.get_character_media),
    path('mount', views.get_mounts),
    path('mount/<int:mountId>', views.get_mount)
]