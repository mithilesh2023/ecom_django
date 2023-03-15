
from django.contrib import admin
from django.urls import path
from shop.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name="homepage"),
    path('registration/',registration,name="registration"),
    path('login/',login,name="login"),
    path('logout/',logoutAuth,name="logout"),
    path('category/<slug>/',categoryWise,name="categoryWise"),
    path('product/<slug>/',singleView,name="singleView"),
    path("add-to-cart/<slug>/",addToCart,name="addCart"),
    path("remove-from-cart/<slug>/",removeFromCart,name="removeCart"),
    path('cart/',myCart,name='cart'),
    path('addCoupon/',addCoupon,name="addCoupon"),
    path('removecoupon/',removeCoupon,name='removecoupon'),
    path('checkout/',checkout,name='checkout'),
    path("checkout-with-save/",checkoutWithSaveAddress,name="checkoutWithSaveAddress"),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
