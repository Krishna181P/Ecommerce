"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommerce import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home_view'),
    path('reg',views.RegisterView.as_view(),name='reg_view'),
    path('login',views.UserLogin.as_view(),name='login_view'),
    # path('userlog',views.Userhome.as_view(),name='userhome_view'),
    path('logout',views.UserLogout.as_view(),name='logout_view'),
    path('productdetail/<int:id>',views.ProductDetailView.as_view(),name='product_detail'),
    path('addtocart/<int:id>',views.AddtoCart.as_view(),name='addto_cart'),
    path('cartlist',views.CartUserList.as_view(),name='cart_list'),
    path('placeorder/<int:cart_id>',views.PlaceOrderView.as_view(),name='place_order'),
    path('cartdelete/<int:id>',views.CartDelete.as_view(),name='cart_delete'),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
