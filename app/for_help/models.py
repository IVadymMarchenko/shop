from django.db import models

# Create your models here.


class ForHelp(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=12)
    created_timestamp = models.DateTimeField(auto_now_add=True,verbose_name='Час додавання')
    
    class Meta:
        db_table = 'consultation'
        verbose_name = 'Консультація' # для отображения названия табл в адм панеле
        verbose_name_plural = 'Консультації' # для отображения названия табл в адм панеле
        
    def __str__(self):
         return f"ім'я {self.name} Телефон - {self.phone}"  # для отображения названия в адм панеле