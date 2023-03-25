from django.urls import path

from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('attrition',views.attrition,name='attrition'),
    path('attritionpredict',views.attritionpredict,name='attritionpredict'),

]