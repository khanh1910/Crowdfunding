from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('Project_<int:Project_id>/', views.haha, name='hoho'),
    path('Project_<int:Project_id>/fund/', views.e, name='fund'),
    path('fund/', views.fund, name='hoho1'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)