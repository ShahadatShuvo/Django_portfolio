from django.contrib import admin
from django.urls import path, include
from .views import (
    homePage,
    projectsPage,
    projectDetail,
    search,
    handler404,
)

from django.conf import settings
from django.conf.urls.static import static


handler404 = handler404

urlpatterns = [

    # path('', homePage, name='homePage'),
    path('projects/', projectsPage, name='projectsPage'),
    path('projects/<str:slug>/', projectDetail, name='projectDetail'),
    path('search/', search, name='search'),

    path('dashboard/', include('dashboard.urls')),
    # path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# rom django.contrib import admin
# from django.urls import path, include
# from django.conf.urls import url
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.views.static import serve as mediaserve
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls', namespace='blog')),
#     path('summernote/', include('django_summernote.urls'))
#
# ]
#
# urlpatterns.append(url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
#                      mediaserve, {'document_root': settings.MEDIA_ROOT}))
#
# urlpatterns += staticfiles_urlpatterns()
#
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT)
