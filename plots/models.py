from django.db import models
import uuid,json
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.utils.timezone import now

PLOT_TYPE_CHOICES = [
    ('single_storey', 'Single Storey'),
    ('multi_storey', 'Multi Storey'),
]

# Create your models here.
# Create your models here.
class Plot(models.Model):
    plot_number = models.CharField(max_length=100, primary_key=True)
    plot_upload_date = models.DateTimeField(default=now)
    plot_address = models.CharField(max_length=200, default='Thika')
    plot_price = models.PositiveIntegerField(default='10000')
    plot_single = models.BooleanField(default=False, verbose_name='Single')
    plot_bedsitter = models.BooleanField(default=False, verbose_name='Bedsitter')
    plot_1B = models.BooleanField(default=False, verbose_name='1 Bedroom')
    plot_2B = models.BooleanField(default=False, verbose_name='2 Bedroom')
    plot_3B = models.BooleanField(default=False, verbose_name='3 Bedroom')
    plot_rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    plot_bg_pic = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['-plot_number']

    def __str__(self):
        return self.plot_number
    
class PlotPic(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    plot_number = models.ForeignKey(Plot, on_delete=models.CASCADE)
    plot_pic = models.URLField(max_length=200)
    plot_pic_desc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['plot_number', 'plot_pic_desc']

    def __str__(self):
        return self.plot_pic

OCCUPANT_CLASS_CHOICES = [
    ('caretaker', 'Caretaker'),
    ('resident', 'Resident')
]
class PlotOccupant(models.Model):
  plot_number = models.ForeignKey(Plot, on_delete=models.CASCADE)
  plot_occupant_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  plot_occupant_f_name = models.CharField(max_length=100, default='Caretaker')
  plot_occupant_l_name = models.CharField(max_length=100, blank=True, null=True)
  plot_occupant_class = models.CharField(
      max_length=100,
      choices=OCCUPANT_CLASS_CHOICES,
      default='caretaker'
  )
  plot_occupant_phone = models.CharField(
    max_length=20,
    validators=[
      MinLengthValidator(10, message="Phone number must be at least 10 characters long.")
    ],
    unique=True
  )
  plot_occupant_email = models.EmailField(max_length=100, blank=True, null=True)

  class Meta:
    ordering = ['plot_number', 'plot_occupant_f_name']

  def __str__(self):
    return self.plot_occupant_f_name
  