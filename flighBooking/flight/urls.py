from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('fligths', views.FlightviewSet)
router.register('passenger', views.PassengerViewSet)
router.register('reservation', views.ReservationViewSet)

urlpatterns = [
    path('flightService/', include(router.urls)),
    path('flightService/findFlight/', views.find_flights),
    path('flightService/saveReservation/', views.save_reservation)
]
