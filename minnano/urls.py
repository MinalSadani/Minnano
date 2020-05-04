from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('login/', views.signin, name="login"),
    path('postsign/', views.postsign),
    path("postsign/logout/", LogoutView.as_view(), name="logout"),
    path('parent/', views.register_parent, name="register"),
    path('school/', views.register_school, name="register"),
    path('activist/', views.register_activist, name="register"),
    path('mentor/', views.register_mentor, name="register"),
    path('counselor/', views.register_counselor, name="register"),
    path("postregister_parent/", views.postregister_parent, name="postregister_parent"),
    path("postregister_school/", views.postregister_school, name="postregister_school"),
    path("postregister_activist/", views.postregister_activist, name="postregister_activist"),
    path("postregister_mentor/", views.postregister_mentor, name="postregister_mentor"),
    path("postregister_counselor/", views.postregister_counselor, name="postregister_counselor"),

]
