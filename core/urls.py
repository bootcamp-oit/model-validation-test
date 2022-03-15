from django.urls import path

from .views import AppointmentListAPIView, AppointmentDetailAPIView

urlpatterns = [
    path('appointments/', AppointmentListAPIView.as_view(), name='appointment'),
    path('appointment/<int:pk>/',
         AppointmentDetailAPIView.as_view(), name='appointment-detail'),

]
