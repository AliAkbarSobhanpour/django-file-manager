from django.urls import path
from .views import gallery_view
urlpatterns = [
    path('gallery/', gallery_view, name='gallery-view')
]
