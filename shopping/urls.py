from django.conf.urls import url
from shopping.views import *


urlpatterns = [
    url(r'^$', ProductList.as_view(), name='productlist'),
    url(r'^(?P<pk>\d+)/$', ProductDetail.as_view(), name='productdetail'),

]