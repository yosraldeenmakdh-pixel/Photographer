from django.urls import path
from . import views
app_name='grapher'
urlpatterns=[
    path('',views.home,name='home'),
    path('log/',views.log,name='log'),
    path('look/<str:pk>',views.look,name='look'),
    path('learn/',views.learn,name='learn'),
    path('all/',views.allprof,name='allprof'),
    path('create/',views.create,name='profile'),
    path('workshops/',views.workshops,name='workshops'),
    path('pay/',views.pay,name='pay'),
    path('register/',views.register,name='register'),
    path('about/',views.about,name='about'),
    path('call/<str:pk>',views.call,name='call'),
    path('update/<str:pk>',views.update_profile,name='update_profile'),
    path('delete/<str:pk>',views.delete_profile,name='delete_profile'),
    path('add/<str:pk>',views.add_img,name='add_my_work'),
    # path('<slug:slug>/',views.photographer_detail,name='photographer_detail'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('photographer_profile/<str:pk>', views.photographer_profile, name='photographer_profile'),
    path('questions/', views.questions, name='questions'),

    

]
