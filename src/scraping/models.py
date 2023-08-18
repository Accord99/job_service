from django.db import models

from scraping.utils import from_cyrillic_to_eng


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Название населённого пункта',
                            unique=True)
    slag = models.CharField(max_length=50,
                            blank=True,
                            unique=True)

    class Meta:
        verbose_name = 'Название населённого пункта'
        verbose_name_plural = 'Название населённых пунктов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slag:
            self.slag = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)




class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Язык программирования',
                            unique=True)
    slag = models.CharField(max_length=50,
                            blank=True,
                            unique=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slag:
            self.slag = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)
