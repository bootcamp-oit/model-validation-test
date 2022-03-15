from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentListAPIView(ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            response = super(AppointmentListAPIView, self).post(request)
            return Response(data=response.data, status=HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"detail": str(e)}, status=HTTP_400_BAD_REQUEST)


class AppointmentDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
