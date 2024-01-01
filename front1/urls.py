
from front1 import views
from django.urls import path

urlpatterns=[
    path('', views.home, name="home"),
    path('sample/', views.sample, name='sample'),
    path('register/', views.register, name="register"),
    path('registersave/', views.registersave, name="registersave"),
    path('login/', views.login, name="login"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('logout/', views.logout, name="logout"),

    path('addfood/', views.addfood, name="addfood"),
    path('sample_2/', views.sample_2, name="sample_2"),
    path('sample_3/', views.sample_3, name="sample_3"),
    path('itemsave/', views.itemsave, name="itemsave"),
    path('singleproduct/<int:proid>/', views.singleproduct, name="singleproduct"),

# --------FOR CATACRISED PRODUCT VIEW------------
    path('pro/<cat_name>/', views.pro, name="pro"),
# --------FOR CATACRISED PRODUCT VIEW------------


    path('useradds/', views.useradds, name="useradds"),
    path('editp/<int:dataid>/', views.editp, name="editp"),
    path('productdeletee/<int:proid>/', views.productdeletee, name="productdeletee"),
    path('categoryupdatee/<int:dataid>/', views.categoryupdatee, name="categoryupdatee"),


]