from rest_framework import serializers



class CategorySerializer(serializers.Serializer):
	name = serializers.CharField(max_length=60)
	description = serializers.CharField()
	created_at = serializers.DateTimeField()
	updated_at = serializers.DateTimeField()