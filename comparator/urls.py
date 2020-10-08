from django.urls import path
from comparator.views.site_view import *

from comparator.views.category_view import *

from comparator.views.lowcategory_view import *

from comparator.views.product_view import *

from comparator.views.price_view import *

urlpatterns = [
    path('sites/', SiteView.as_view(), name='sites'),
    path('sites/<int:id>/',SiteViewById.as_view(),name='site_by_id'),

    path('categories/', CategoryView.as_view(),name='categories'),
    path('categories/<int:id>/',CategoryViewById.as_view(),name='category_by_id'),

    path('lowcategories/',LowCategoryView.as_view(),name='lowcategories'),
    path('lowcategories/<int:id>/',LowCategoryViewById.as_view(),name='lowcategory_by_id'),

    path('products/',ProductView.as_view(),name='products'),
    path('products/<int:id>/',ProductViewById.as_view(),name='product_by_id'),

    path('prices/',PriceView.as_view(),name='prices'),
    path('prices/<int:id>/',PriceViewById.as_view(),name='price_by_id'),

]
