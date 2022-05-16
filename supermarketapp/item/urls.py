from django.urls import path

from item.views import item_create_view, item_delete_view, item_detail_view, item_list_view, item_update_view, login_account, logout_account, register_account

urlpatterns = [
    path('', item_list_view, name='item_list'),
    path('create/', item_create_view, name='item_create'),
    path('<int:id>', item_detail_view, name='item_detail'),
    path('<int:id>/update', item_update_view, name='item_update'),
    path('<int:id>/delete', item_delete_view, name='item_delete'),
    path('login/', login_account, name='login'),
    path('register/', register_account, name='register'),
    path('logout/', logout_account, name='logout'),
]
