from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("login/", views.login_user, name="login-user"),
  path("logout/", views.logout_user, name="logout-user"),
  path("signup/", views.signup_user, name="signup-user"),
  path('update_user/', views.update_user, name="update-user"),
  path('update_info/', views.update_info, name="update-info"),
  path('update_password/', views.update_password, name="update-password"),
  path('category/', views.category_summary, name="category-summary"),
  path('search/', views.search, name="search"),
  path("product/<int:pk>/", views.product, name="product"),
  path("category/<str:cat>/", views.category, name="category"),

]