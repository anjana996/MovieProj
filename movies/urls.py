# movies/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('list', views.movie_list, name='list'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('rate_movie/<int:movie_id>/', views.rate_movie, name='rate_movie'),
    path('admin/add_category/', views.add_category, name='add_category'),
    path('admin/add_movie/', views.admin_add_movie, name='admin_add_movie'),
    path('admin/delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('admin/delete_profile/<int:profile_id>/', views.delete_profile, name='delete_profile'),
    path('admin-new/', views.admin_panel, name='admin_panel'),
]




