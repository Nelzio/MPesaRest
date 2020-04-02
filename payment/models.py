from django.db import models


class EntradasApi(models.Model):
    page = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, page):
        entrada = cls(page=page)
        return entrada


class UsersApiProduction(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    code = models.IntegerField(default=0, null=True, blank=True)
    shortApiKey = models.CharField(max_length=5, null=True, blank=True)
