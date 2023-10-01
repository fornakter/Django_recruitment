from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.img_list, name='img_list'),
    path('list_premium/', views.img_premium, name='list_premium'),
    path('list_ent/', views.img_ent, name='list_ent'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
