from django.db import models

# Create your models here.

class RegistrationModel(models.Model):
    Name= models.CharField(max_length=200)
    Email= models.EmailField()
    Number= models.IntegerField()
    Password= models.CharField(max_length=200)
    C_Password = models.CharField(max_length=200)

    class Meta:
        verbose_name='Registration'
        db_table ='Registration'
    
    def __str__(self):
        return self.Name