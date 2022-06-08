from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewAuthView.as_view(), name='auth_view'),
    path('signup/', views.UserCreateView.as_view(), name='sign_up'),
]