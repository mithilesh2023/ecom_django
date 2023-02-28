
from django.contrib import admin
from django.urls import path
from shop import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="homepage"),
    path('registration/',views.registration,name="registration"),
    path('category/<slug>/',views.categoryWise,name="categoryWise"),
    path('product/<slug>/',views.singleView,name="singleView"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
