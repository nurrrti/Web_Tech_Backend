from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('bookapp.urls')),
        path('api/', include('project_api.urls')),
        path('api/', include('rest_framework.urls')),  # will be added login button
        path('', include('django.contrib.auth.urls')),  # login url, logout url
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
