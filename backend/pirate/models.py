from django.db import models

 
class Reestr(models.Model):
    title = models.CharField("Название", max_length=256)
    description = models.TextField("Описание", blank=True, null=True)
    url = models.URLField("URL адрес")

    def __str__(self) -> str:
        return self.title
