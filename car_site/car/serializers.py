from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
         model = UserProfile
         fields = ('username', 'email', 'password', 'first_name', 'last_name',
                   'age', 'phone_number')


class UserOwnerProfileSerializers(serializers.ModelSerializer):
    class Meta:
         model = UserProfile
         fields = ['username', 'phone_number']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category', 'group']


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['car_mark']


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['image']


class OwnerSerializer(serializers.ModelSerializer):
    owner = UserOwnerProfileSerializers()
    class Meta:
        model = Owner
        fields = ['owner', 'owner_image']


class CarListSerializer(serializers.ModelSerializer):
    price_som = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['name', 'year', 'region', 'price_som', 'price_usd']


    def get_price_som(self, obj):
        return obj.get_price_som()


class CarDetailSerializer(serializers.ModelSerializer):
    price_som = serializers.SerializerMethodField()
    price_rub = serializers.SerializerMethodField()
    price_tenge = serializers.SerializerMethodField()
    owner = OwnerSerializer(read_only=True)
    images = CarImageSerializer(read_only=True, many=True)
    car_mark = MarkSerializer(read_only=True)
    similar_cars = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['name', 'owner', 'year', 'mileage', 'body', 'color', 'engine', 'gearbox', 'drive', 'steering_wheel', 'condition',
                  'customs', 'exchange', 'active', 'region', 'registration', 'description', 'other', 'images', 'car_mark', 'price_usd',
                  'price_som', 'price_rub', 'price_tenge', 'similar_cars']

    def get_similar_cars(self, obj):
        similar = Car.objects.filter(car_mark=obj.car_mark).exclude(id=obj.id)
        return CarListSerializer(similar, many=True).data


    def get_price_som(self, obj):
        return obj.get_price_som()

    def get_price_rub(self, obj):
        return obj.get_price_rub()

    def get_price_tenge(self, obj):
        return obj.get_price_tenge()
