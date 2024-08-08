from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]

    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(1886)
            # Assuming cars were not made before 1886
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
