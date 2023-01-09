from django.urls import path
from .views import *

urlpatterns = [
    path('emp/',empform,name="empform"),
    path('emp/get_state/',getStateDetails,name="getStateDetails"),
    path('emp/get_dist/',getDistDetails,name="getDistDetails"),
    path('emp/<int:pk>/empviewdetails/',getEmpViewDetails,name="empviewdetails"),
    path('emp/get_search/',getSeachDetails,name="getSeachDetails")
]
