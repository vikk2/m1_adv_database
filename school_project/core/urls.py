from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.create_student),
    path('course/', views.create_course),
    path('report/<id>/', views.course_report),
    path('courses/', views.course_list),
]