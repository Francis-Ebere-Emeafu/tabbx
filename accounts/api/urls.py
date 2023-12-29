from django.urls import include, path
from rest_framework import routers

from accounts.api import views


router = routers.DefaultRouter()
router.register(r'students', views.StudentView, 'students-views')
# router.register(r'register-student', views.UserCreateAPIView, 'register_api-views')
# router.register(r'register-student-', views.register_student, 'students-register')

# app_name = 'todo'

urlpatterns = [
    path('', include(router.urls)),
    path('register/student/', views.register_student, name="register_student"),
    path('register-judge/', views.JudgeRegistrationAPIView1.as_view(), name="register_judge_api"),
    path('register-student/', views.StudentRegistrationAPIView.as_view(), name="register_student_api"),
]

