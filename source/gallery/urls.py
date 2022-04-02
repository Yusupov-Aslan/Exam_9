from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from gallery import views
app_name = 'gallery'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('photos/', views.PhotoListView.as_view(), name='photo_list'),
    path('photos/create/', views.PhotoCreateView.as_view(), name='photo_create'),
    path('photos/<int:pk>/', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('photos/<int:pk>/update/', views.PhotoUpdateView.as_view(), name='photo_update'),
    path('photos/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo_delete'),
    path('albums/', views.AlbumListView.as_view(), name='album_list'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('albums/create/', views.AlbumCreateView.as_view(), name='album_create'),
    path('albums/<int:pk>/update/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('albums/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
