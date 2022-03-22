from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  # Errors Page
                  path('404', views.Error404, name='404'),
                  path('admin/', admin.site.urls),
                  path('', views.HOME, name='home'),
                  path('base/', views.BASE, name='base'),
                  path('product/<slug:slug>', views.PRODUCT_DETAILS, name='product_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
