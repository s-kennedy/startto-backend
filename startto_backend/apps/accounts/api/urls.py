# App
from startto_backend.apps.accounts.api.routers import router

# from django.conf.urls import url, include

app_name="accounts"
urlpatterns = router.urls