from rest_framework import serializers
from accounts.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'description', 'link', 'pubdate']