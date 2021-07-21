from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_center.main.urls')),
    path('auth/', include('book_center.bc_auth.urls')),
    path('events/', include('book_center.events.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
