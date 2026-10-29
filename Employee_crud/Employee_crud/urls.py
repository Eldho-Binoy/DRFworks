from django.contrib import admin
from django.urls import path,include
from app import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('employee',views.EmployeeView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(router.urls)),
    # path('list/', views.EmployeeList.as_view()),
    # path('create/', views.EmployeeCreate.as_view()),
    # path('detail/<int:pk>', views.EmployeeRetrieve.as_view()),
    # path('update/<int:pk>', views.EmployeeUpdate.as_view()),
    # # path('partial_update/<int:i>', views.EmployeePartialUpdate.as_view()),
    # path('delete/<int:pk>', views.EmployeeDelete.as_view()),
]
