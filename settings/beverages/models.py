from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название кофе')
    description = models.TextField(verbose_name='Описание кофе')
    image = models.TextField(verbose_name='Фотография кофе')
    stars = models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Step(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название шага')
    description = models.TextField(verbose_name='Описание шага')
    video = models.TextField('шаг')
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name='steps')
    step_number = models.IntegerField(verbose_name='Номер шага')

    def __str__(self):
        return f'Шаг № {self.step_number}. Напиток - {self.coffee}'

