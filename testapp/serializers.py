from rest_framework import serializers
from testapp.models import *
class userAuthSerializer(serializers.ModelSerializer):
  class Meta:
    model = userAuth
    fields = "__all__"
