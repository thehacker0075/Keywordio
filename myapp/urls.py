from textwrap import indent
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('add_book/',views.add_book,name='add_book'),
    path('view_book/',views.view_book,name='view_book'),
    path('admin_edit_book/<int:pk>',views.admin_edit_book,name='admin_edit_book'),
    path('admin_delete_book/<int:pk>/',views.admin_delete_book,name='admin_delete_book'),
]