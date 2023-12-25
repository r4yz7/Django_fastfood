
from django.conf import settings
from django.urls import path
from . import views

from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name='home'),
    path('addProduct',views.addProduct ,name='insertProduct'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

