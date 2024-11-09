from rest_framework import serializers
from basecom.models import FoComments
from django.db import models


class FoCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoComments
        fields = ("comment_id","display_authorname","comment_content","created_at")
        read_only_fields = ("comment_id","display_authorname","comment_content","created_at")
