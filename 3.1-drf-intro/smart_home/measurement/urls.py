from django.urls import path

from measurement.views import GetSensor, ShowSensors, ShowMeasurements

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', ShowSensors.as_view()),
    path('sensors/<pk>/', GetSensor.as_view()),
    path('measurements/', ShowMeasurements.as_view()),
]