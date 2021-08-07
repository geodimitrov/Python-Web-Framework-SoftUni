from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_center.bc_main.urls')),
    path('auth/', include('book_center.bc_auth.urls')),
    path('contact/', include('book_center.bc_contact.urls')),
    path('events/', include('book_center.bc_events.urls')),
    path('profiles/', include('book_center.bc_profiles.urls')),
    path('blog/', include('book_center.bc_blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
