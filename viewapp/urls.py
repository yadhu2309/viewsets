from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'students', StudentViewset)




urlpatterns = [
    path('student/',StudentGenericView.as_view()),
 ]
urlpatterns += router.urls