from django.urls import path
from . import views


app_name = 'shorturls'

urlpatterns = [
    path('', views.shorten_url_view, name='index'),
    path('shortened/<str:shortened_url>', views.shortened_url_view, name='shortened_url'),
    path('all_links/', views.all_links_view, name='all_links'),

]