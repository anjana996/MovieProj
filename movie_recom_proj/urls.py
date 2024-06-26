# project_name/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    # Add the following line to serve media files during development
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
