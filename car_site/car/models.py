from decimal import Decimal

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(15), MaxValueValidator(80)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.category


class Mark(models.Model):
    CAR_MAKES = (
        ("toyota", "Toyota"),
        ("honda", "Honda"),
        ("bmw", "BMW"),
        ("audi", "Audi"),
        ("mercedes", "Mercedes-Benz"),
        ("ford", "Ford"),
        ("chevrolet", "Chevrolet"),
        ("nissan", "Nissan"),
        ("volkswagen", "Volkswagen"),
        ("hyundai", "Hyundai"),
        ("kia", "Kia"),
        ("lexus", "Lexus"),
        ("mazda", "Mazda"),
        ("subaru", "Subaru"),
        ("volvo", "Volvo"),
        ("porsche", "Porsche"),
        ("tesla", "Tesla"),
        ("jaguar", "Jaguar"),
        ("land_rover", "Land Rover"),
        ("fiat", "Fiat"),
        ("peugeot", "Peugeot"),
        ("renault", "Renault"),
        ("mitsubishi", "Mitsubishi"),
        ("acura", "Acura"),
        ("infiniti", "Infiniti"),
        ("lincoln", "Lincoln"),
        ("cadillac", "Cadillac"),
        ("buick", "Buick"),
        ("mini", "Mini"),
        ("alfa_romeo", "Alfa Romeo"),
        ("aston_martin", "Aston Martin"),
        ("bentley", "Bentley"),
        ("rolls_royce", "Rolls-Royce"),
        ("ferrari", "Ferrari"),
        ("lamborghini", "Lamborghini"),
        ("maserati", "Maserati"),
        ("mcLaren", "McLaren"),
        ("bugatti", "Bugatti"),
        ("pagani", "Pagani"),
    )

    car_mark = models.CharField(max_length=50, choices=CAR_MAKES, null=True)

    def __str__(self):
        return self.car_mark


class Owner(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owners')
    owner_image = models.ImageField(upload_to='owner_image/', null=True, blank=True)

    def __str__(self):
        return f'{self.owner} - {self.owner_image}'

class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    mileage = models.PositiveIntegerField(null=True, blank=True)
    CAR_BODY_TYPES = (
        ("sedan", "Sedan"),
        ("hatchback", "Hatchback"),
        ("suv", "SUV"),
        ("coupe", "Coupe"),
        ("convertible", "Convertible"),
        ("wagon", "Wagon"),
        ("pickup", "Pickup"),
        ("van", "Van"),
        ("minivan", "Minivan"),
        ("crossover", "Crossover"),
        ("roadster", "Roadster"),
        ("targa", "Targa"),
        ("limousine", "Limousine"),
        ("microcar", "Microcar"),
        ("offroad", "Off-road"),
        ("truck", "Truck"),
    )
    body = models.CharField(max_length=50, choices=CAR_BODY_TYPES)
    color = models.CharField(max_length=100)
    engine = models.CharField(max_length=50)
    GAERBOX_CHOICES = (
        ('automatic', 'automatic'),
        ('manual', 'manual')
    )

    gearbox = models.CharField(max_length=10, choices=GAERBOX_CHOICES)
    DRIVE_CHOICES = (
        ('FWD', 'front'),
        ('RWD', 'rear'),
        ('AWD', '4wd'),

    )
    drive = models.CharField(max_length=5, choices=DRIVE_CHOICES)
    STEERING_WHEEL = (
        ('RIGHT', 'right'),
        ('LEFT', 'left')
    )

    steering_wheel = models.CharField(max_length=6, choices=STEERING_WHEEL)
    condition = models.CharField(max_length=50)
    CUSTOMS_CHOICES = (
        ('CUSTOMS_CLEARED', 'customs cleared'),
        ('CUSTOMS_NOT_CLEARED', 'customs not cleared')
    )
    customs = models.CharField(max_length=20, choices=CUSTOMS_CHOICES)
    exchange = models.CharField(max_length=100)
    active = models.BooleanField(default=True, verbose_name='в наличии')
    region = models.CharField(max_length=100)
    registration = models.CharField(max_length=100)
    other = models.CharField(max_length=200)
    description = models.TextField(verbose_name="Owner's comments")
    car_mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='car_marks')
    price_usd = models.DecimalField(max_digits=20, decimal_places=2)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


    def get_price_som(self):
        curs = Decimal('86.9')
        return self.price_usd * curs

    def get_price_rub(self):
        curs = Decimal('99.9')
        return self.price_usd * curs

    def get_price_tenge(self):
        curs = Decimal('488.93')
        return self.price_usd * curs


class CarImage(models.Model):
    image = models.ImageField(upload_to='car_image/', null=True, blank=True)
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)






