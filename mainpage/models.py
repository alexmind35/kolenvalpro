from django.db import models


class Hero(models.Model):
    heading_hero = models.CharField("Название", max_length=250)
    image_hero = models.ImageField("Фотография", upload_to="mainpage/hero", default="", blank=True)

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главные"


class Services(models.Model):
    name_services = models.CharField("Название", max_length=250)

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"


class Why(models.Model):
    name_why = models.CharField("Название", max_length=150)
    text_why = models.CharField("Описание", max_length=250)

    class Meta:
        verbose_name = "Почему мы?"
        verbose_name_plural = "Почему мы?"
