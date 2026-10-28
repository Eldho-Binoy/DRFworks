from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.EmployeeList.as_view()),
    path('create/', views.EmployeeCreate.as_view()),
    path('detail/<int:i>', views.EmployeeRetrieve.as_view()),
    path('update/<int:i>', views.EmployeeUpdate.as_view()),
    path('partial_update/<int:i>', views.EmployeePartialUpdate.as_view()),
    path('delete/<int:i>', views.EmployeeDelete.as_view()),
]
