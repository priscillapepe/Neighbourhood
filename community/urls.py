from django.urls import path
from .views import home
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('town/', views.town, name='town'),
    path('mshomo/', views.index, name='mshomo'),
    path('user/(?P<username>\)', views.profile, name='profile'),
    path('upload/', views.upload_post, name='upload_post'),
    path('accounts/edit/', views.edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
