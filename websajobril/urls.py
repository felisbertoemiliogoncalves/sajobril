
from django.contrib import admin
from django.urls import path



from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static



from django.contrib import admin
from django.urls import path, include


from django.urls import re_path
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('visitor.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)