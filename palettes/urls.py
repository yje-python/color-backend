from django.urls import path
from . import views

urlpatterns = [
    path('liked/', views.liked_colors),
    path('like/', views.like_color),

    path('saved/', views.saved_palettes),
    path('save/', views.save_palette),
    path('unlike/', views.unlike_color),
    path('delete/', views.delete_palette),
]