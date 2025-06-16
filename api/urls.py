from django.urls import path,include
from.import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees',views.EmployeeViewset ,basename='employee')

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),

    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeeDetail.as_view()),

    path('',include(router.urls)),

    path('blog/',views.BlogView.as_view()),
    path('comment/',views.CommentView.as_view()),

    path('blog/<int:pk>/',views.BlogDetailView.as_view()),
    path('comment/<int:pk>/',views.CommentDetailView.as_view()),



]
    
