from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['comment', 'owner', 'task']
        model = Comment
