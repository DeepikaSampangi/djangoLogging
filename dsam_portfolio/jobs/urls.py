
from django.urls import path

from .views import home, job_details

urlpatterns = [path('',home, name='home'),
               path('<int:job_id>', job_details, name='job_details')
               ]
