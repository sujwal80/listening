from django.urls import path
from . import views
from musicPlayer import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home_page"),
    path('songs/', views.home_music, name="home_music_page")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)