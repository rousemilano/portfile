from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name='Description')
    percentage = models.IntegerField(verbose_name='Porcentaje')
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
        
