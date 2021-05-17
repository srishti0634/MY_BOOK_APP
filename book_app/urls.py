from django.urls import path
from book_app.views import delete_from_cart
from book_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('sell/',views.sell, name="sell"),
    path('sellformcreated/',views.sellformcreated, name="sellformcreated"),
    path('borrow/', views.borrow, name='borrow'),
    path('all_sell_items/',views.all_sell_items, name="all_sell_items"),
    path('book_detail/<uuid>', views.book_detail, name='book_detail'),
    path('all_cart_items/', views.all_cart_items, name='all_cart_items'),
    path('add_to_cart/<uuid>', views.add_to_cart, name='add_to_cart'),
    path('cart/<pk>/delete', delete_from_cart.as_view(), name='delete_from_cart'),
    path('search/', views.search, name='search'),
]
