from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model


from posts.models import Comment, Post, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        read_only_fields = ('post',)
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    following = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(), slug_field='username')

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']

        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя.')

        return data
