from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('restaurantDetail/delete',views.Delete_restaurant, name='resDelete'),
    path('restaurantDetail/<str:res_id>',views.restaurantDetail, name='resDetailPage'), # http://localhost:8000/restaurantDetail/1 요청처리
    path('restaurantDetail/updatePage/update',views.Update_restaurant, name='resUpdate'),
    path('restaurantDetail/updatePage/<str:res_id>',views.restaurantUpdate, name='resUpdatePage'), # http://localhost:8000/restaurantDetail/updatePage/1

    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'), #http://localhost:8000/restaurantCreate
    path('restaurantCreate/create',views.Create_restaurant,name='resCreate'), ##http://localhost:8000/restaurantCreate/create

    path('categoryCreate/',views.categoryCreate, name='cateCreatePage'),
    path('categoryCreate/create',views.Create_category, name='cateCreate'),
    path('categoryCreate/delete',views.Delete_category, name='cateDelete'),
    ]

