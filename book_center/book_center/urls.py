from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_center.main.urls')),
    path('auth/', include('book_center.bc_auth.urls')),
]
