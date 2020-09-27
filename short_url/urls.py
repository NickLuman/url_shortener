from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_post_urls),
    path('<slug:hash_url>', views.get_delete_update_url),
]