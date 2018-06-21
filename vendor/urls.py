from django.conf.urls import url
from django.urls import path
from .views import VendorDetailAPIView

urlpatterns = [
    path('', VendorDetailAPIView.as_view(),name='vendor-list'),
    #url(r'^list/$', BlogPostListAPIView.as_view(),name='post-list-without-create'),
    #url(r'^create/$', BlogPostAPIView.as_view(),name='post-create'),
    #url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(),name='post-rud')
]
