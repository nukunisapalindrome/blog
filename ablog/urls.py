from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    # path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

