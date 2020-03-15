from django.urls import path

from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),

    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSettings, name='account'),

    path('reset_password/', auth_views.PasswordResetView, name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView, name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView, name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView, name="password_reset_complete"),

]
