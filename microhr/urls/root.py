from django.urls import path

from microhr.views import root

urlpatterns = [
    path('', root.home, name='home'),
    path('api/users', root.getWorks, name='works')
]
