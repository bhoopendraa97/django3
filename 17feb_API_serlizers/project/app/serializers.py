from rest_framework import serializers
from.models import Student

class Stu_Serializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    stu_name= serializers.CharField( max_length=50)
    stu_email= serializers.EmailField()
    stu_contact= serializers.IntegerField()
    stu_city = serializers.CharField(max_length=50)
 

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('stu_name', instance.title)
        instance.code = validated_data.get('stu_email', instance.code)
        instance.linenos = validated_data.get('stu_contact', instance.linenos)
        instance.language = validated_data.get('stu_city', instance.language)
        instance.save()
        return instance
