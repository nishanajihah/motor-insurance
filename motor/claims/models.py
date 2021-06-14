import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

# MAIN: DRIVER INFORMATION
class UserInformation(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField(max_length=50, blank=True)
    mobile = models.IntegerField(blank=True, null=True)

    STATUS_CHOICES = (
        ('IN_PROGRESS','In Progress'),
        ('ACCEPTED','Accepted'),
    )

    status = models.CharField(max_length=30, default="IN_PROGRESS", choices=STATUS_CHOICES)

    class Meta:
        verbose_name_plural = "User Informations"

    def __str__(self):
        return self.name

# SUBMAIN: VEHICLE INFORMATION
class Vehicle(models.Model):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    vehicle_year = models.DateField(verbose_name='vehicle year make')
    
    vehicle_model = models.CharField(max_length=50, verbose_name="vehicle model") 
    vehicle_num = models.CharField(max_length=5, verbose_name = "vehicle no.")

    class Meta:
        verbose_name_plural = "vehicle details"

    def __str__(self):
        return f"{self.vehicle_year.year}, {self.vehicle_model}, {self.vehicle_num}"

# SUBMAIN: LOSS INFORMATION
class Loss(models.Model):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    accident_datetime = models.DateTimeField(verbose_name = 'date and time of accident');
    accident_location = models.CharField(max_length=150, verbose_name="Location")

    LOSS_CHOICES = (
        ('OWN_DAMAGE','Own Damage'),
        ('KNOCK_FOR_KNOCK','Knock for Knock'),
        ('WINDSCREEN_DAMAGE','Windscreen Damage'),
        ('THIEF','Thief'),
    )

    accident_losstype = models.CharField(max_length=30,  choices=LOSS_CHOICES)

    accident_description = models.TextField(verbose_name='description of loss')
    accident_police_lodged = models.BooleanField(verbose_name='police report lodged?')
    accident_injured = models.BooleanField(verbose_name = 'anybody injured?')

    class Meta:
        verbose_name_plural = "loss details"

    # def __str__(self):
    #     return self.location

    def __str__(self):
        return f"{self.accident_datetime}, {self.accident_description}, {self.accident_police_lodged}, {self.accident_injured}"

# SUBMAIN: DOCUMENT INFORMATION
class Document(models.Model):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    docFile = models.FileField(upload_to='assets/documents', verbose_name = "Document File")
    photo = models.ImageField(upload_to='assets/photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "claim document details"

    def __str__(self):
        return f"{self.docfile}, {self.photo}"
