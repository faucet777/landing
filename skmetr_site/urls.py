from django.conf.urls.static import static
from django.urls import path
from skmetr_site.views import *

from skmetrru import settings

urlpatterns = [
    path("", MainPage.as_view(), name='home'),
    path("services/<slug:service_tag>/", ServicesPage.as_view(), name="this_service"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = exeption404

