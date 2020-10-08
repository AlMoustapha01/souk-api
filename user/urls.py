from django.urls import path,include

from user.views.user_view import *
from user.views.notify_view import *
from user.views.store_product_view import *
from user.views.follow_price_view import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
import djoser
schema_view = get_schema_view(
   openapi.Info(
      title="SOUK API",
      default_version='v1',
      description="SOUK Api description ...",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
   #### users views
    path('users/',UsersView.as_view(),name='users'),
    path('users/<int:id>/',UsersViewById.as_view(),name='user_by_id'),
   #### notify views
    path('notify/',NotifyView.as_view(),name='notify'),
    path('notify/<int:id>/',NotifyViewById.as_view(),name='notify_by_id'),
   #### follow price views
    path('followprice/',FollowPriceView.as_view(),name='followprice'),
    path('followprice/<int:id>/',NotifyViewById.as_view(),name='followprice_by_id'),
   #### follow price views
    path('storeproduct/',StoreProductView.as_view(),name='storeproduct'),
    path('storeproduct/<int:id>/',StoreProductViewById.as_view(),name='storeproduct_by_id'),
    #authentifation
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
   #### documentation
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
