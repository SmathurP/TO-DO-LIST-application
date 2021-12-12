from django.contrib import admin
from django.urls import path
from todoapp import views

app_name="todoapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('delete/<str:pk>',views.delete,name='delete')
]
