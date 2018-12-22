from django.db import models


class EntradasApi(models.Model):
    page = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, page):
        entrada = cls(page=page)
        return entrada
