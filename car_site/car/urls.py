from django.urls import path
from .views import *
urlpatterns = [

path('users', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='users_list'),
path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='users_detail'),

path('category', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='category_detail'),


path('mark', MarkViewSet.as_view({'get': 'list', 'post': 'create'}), name='mark_list'),
path('mark/<int:pk>/', MarkViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='mark_detail'),


path('', CarListViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_list'),
path('<int:pk>/', CarDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='car_detail'),


path('car_image', CarImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_image_list'),
path('car_image/<int:pk>/', CarImageViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='car_image_detail'),



path('owner', OwnerViewSet.as_view({'get': 'list', 'post': 'create'}), name='owner_list'),
path('owner/<int:pk>/', OwnerViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='owner_list'),
]