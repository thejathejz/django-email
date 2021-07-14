from django.urls import path
  
# importing views from views..py
from . import views 
urlpatterns = [
    path('geeksview/', views.geeks_view, name="geeks_view"),
    path('geeksview1/', views.geeks_view1, name="geeks_view1"),
    path('geeksview2/', views.geeks_view2, name="geeks_view2"),
    path('geeksview3/', views.geeks_view3, name="geeks_view3"),
]

