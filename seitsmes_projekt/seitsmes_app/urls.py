#from django.contrib import admin
from django.urls import path, include
from seitsmes_app import views

app_name = 'seitsmes_app'

urlpatterns = [
    #path("", views.index, name = "index"),
    path('register/', views.register, name = 'register'),
    path('user_login/',views.user_login,name='user_login'),
    #path('login/', views.login, name = 'login'),
    #path('admin/', admin.site.urls),
]
