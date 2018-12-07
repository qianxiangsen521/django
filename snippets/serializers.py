from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES,reCommList


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):

        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class ReCommListSerializer(serializers.Serializer):
    commId = serializers.IntegerField(read_only=True)
    reCommId = serializers.IntegerField(read_only=True)
    commTitle = serializers.CharField()
    commContent = serializers.CharField()
    commCtime = serializers.IntegerField(read_only=True)
    commMtype = serializers.CharField(max_length=1,default='type')
    commPhone = serializers.CharField(max_length=11, default='phone')
    imgUrl = serializers.ImageField(default='imgUrl')

    def create(self, validated_data):
        return reCommList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.commId = validated_data.get('commId',instance.commId)
        instance.reCommId = validated_data.get('reCommId',instance.reCommId)
        instance.commTitle = validated_data.get('commTitle',instance.commTitle)
        instance.commContent = validated_data.get('commContent',instance.commContent)
        instance.commCtime = validated_data.get('commCtime',instance.commCtime)
        instance.commMtype =validated_data.get('commMtype',instance.commMtype)
        instance.commPhone = validated_data.get('commPhone',instance.commPhone)
        instance.imgUrl = validated_data.get('imgUrl',instance.imgUrl)
        instance.save()
        return instance


class CommListSerializer(serializers.ModelSerializer):
    class Meta:
        model = reCommList
        fields = ('commId', 'reCommId', 'commTitle', 'commContent', 'commCtime', 'commMtype','commPhone','imgUrl')

