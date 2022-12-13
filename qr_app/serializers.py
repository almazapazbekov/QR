from rest_framework import serializers

from .models import Category, Item


def spec_symbol(value):
    for i in value:
        if i in '!@#$%^&*':
            raise serializers.ValidationError('Имя не может хранить спец символы')
    return value


def qr_generator(value):
    # print(value)
    return f'{value["category_id"].id}C{value["price"]}P{value["item_id"]}I'
 #asdasdasdasdasd

class CategorySerializer(serializers.Serializer):
    id = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=20, validators=[spec_symbol, ])
    description = serializers.CharField(max_length=256)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.name = validated_data['description']
        instance.save()
        return instance


class ItemSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    price = serializers.IntegerField()
    qr_code = serializers.CharField(max_length=50, read_only=True)

    def create(self, validated_data):
        test = validated_data
        test['qr_code'] = qr_generator(validated_data)
        return Item.objects.create(**test)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.category_id = validated_data['category_id']
        instance.price = validated_data['price']
        instance.qr = validated_data['qr']
        instance.save()
        return instance
