from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('post/<int:id>/', views.about, name='post_details'),

    path('contact/', views.contact_view, name='contact'),
    path('global/', views.global_view, name='global'),
    path('sport/', views.sport_view, name='sport'),
    path('techno/', views.techno_view, name='techno'),
    path('science/', views.science_view, name='science'),
    path('uzbekistan/', views.uzb_view, name='uzbekistan'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('category/<str:category_name>/', views.category_posts, name='category_posts'),
]
