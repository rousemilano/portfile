from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    percentage = models.IntegerField(verbose_name='Porcentaje')
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
        
class Interests(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    icon = models.FileField(upload_to='about/img', verbose_name='Icon')

    class Meta:
        verbose_name = 'Interes'
        verbose_name_plural = 'Intereses'
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name