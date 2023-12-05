from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="ICQ:Isekai API",
      default_version='v1',
      description="don't click ⬇",
      terms_of_service="https://takeb1nzyto.space/",
      contact=openapi.Contact(email="nepishisudabolsheponyal@nahuy.da"),
      license=openapi.License(name="EDIK PEDIK License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)