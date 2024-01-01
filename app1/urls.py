
from app1 import views
from django.urls import path

urlpatterns=[
    path('', views.back_home, name='home'),
    path('add_catacory/', views.add_catacory, name='add_catacory'),
    path('categorysave', views.categorysave, name='categorysave'),
    path('categorydisp', views.categorydisp, name='categorydisp'),
    path('categoryedit/<int:dataid>/', views.categoryedit, name="categoryedit"),
    path('categoryupdate/<int:dataid>/', views.categoryupdate, name="categoryupdate"),
    path('categorydelete/<int:dataid>/', views.categorydelete, name="categorydelete"),

]