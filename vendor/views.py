from django.shortcuts import render
from rest_framework_jwt.settings import api_settings
from rest_framework import generics, mixins
from .models import VendorDetail
#from .permissions import IsOwnerOrReadOnly
#from django.db.models import Q
from rest_framework import viewsets
from .serializers import VendorDetailSerializer
from django.contrib.auth.models import User, Group


def jwt_response_payload_handler(token, user=None, request=None):

   return {
       'token': token,
       'vendor': {
            'email': vendor.email,
       }
   }

class VendorDetailAPIView(generics.CreateAPIView):
    pass
    lookup_field = 'pk'
    # queryset = VendorDetail.object.all()
    serializer_class = VendorDetailSerializer

    def get_queryset(self):
        return VendorDetail.objects.all()
    def perform_create(self,serializer):
        serializer.save(vendor = self.request.user)