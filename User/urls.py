from django.urls import path

from .import views

urlpatterns=[
    path('',views.login,name='login'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
    path('home',views.index,name='index'),
    path('register',views.register,name='register'),
    path('attrition',views.attrition,name='attrition'),
    path('attritionpredict',views.attritionpredict,name='attritionpredict'),

]