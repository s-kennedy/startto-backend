# App
from startto_backend.apps.artworks.api.routers import router

# from django.conf.urls import url, include

app_name="artworks"
urlpatterns = router.urls