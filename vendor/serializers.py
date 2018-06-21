from rest_framework import serializers

from vendor.models import VendorDetail

class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorDetail
        fields = [
            'pk',
            'name',
            'phone',
            'email',
            'gender',
            'description',
            'timestamp',
        ]


