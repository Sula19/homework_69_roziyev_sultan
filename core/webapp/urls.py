from django.urls import path
from webapp.views import action, index

urlpatterns = [
    path('', index, name='index'),
    path('add/', action, name='add'),
    path('subtract/', action, name='subtract'),
    path('multiply/', action, name='multiply'),
    path('divide/', action, name='divide'),
]