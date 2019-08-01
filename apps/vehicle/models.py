from django.db import models

class VehicleType(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name

class Park(models.Model):
    pk = [
        ("1","A1"),
        ("2","A2"),
        ("3","A3"),
        ("4","A4"),
        ("5","A5"),
        ("6","A6"),
        ("7","A7"),
        ("8","A8"),
        ("9","A9"),
        ("10","A10"),
        ("11","B1"),
        ("12","B2"),
        ("13","B3"),
        ("14","B4"),
        ("15","B5"),
        ("16","B6"),
        ("17","B7"),
        ("18","B8"),
        ("19","B9"),
        ("20","B10"),
    ]
    parking_spot = models.CharField(max_length=4, choices=pk)
    def __str__(self):
        return " Slot " + self.parking_spot

class Vehicle(models.Model):
    Vehicle_type = models.ForeignKey(VehicleType, on_delete = models.PROTECT)
    plate = models.CharField(max_length=10)
    color = models.TextField(max_length=10)
    slot = models.ManyToManyField(Park, through="Asign")

    def __str__(self):
        return self.plate

class Asign(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    slot = models.ForeignKey(Park, on_delete=models.CASCADE)
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    def __str__(self):
        return self.vehicle.plate



    
