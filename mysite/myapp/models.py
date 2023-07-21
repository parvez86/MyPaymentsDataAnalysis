from django.db import models

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=50)
    company_url = models.URLField()
    genre_id = models.IntegerField()
    release_date = models.DateTimeField()
    artwork_large_url = models.URLField()
    seller_name = models.CharField(max_length=50)
    five_star_ratings = models.IntegerField()
    four_star_ratings = models.IntegerField()
    three_star_ratings = models.IntegerField()
    two_star_ratings = models.IntegerField()
    one_star_ratings = models.IntegerField()

    def __str__(self):
        return self.name


class Sdk(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name


class AppSdk(models.Model):
    app = models.ForeignKey('App', on_delete=models.SET_NULL, null=True)
    sdk = models.ForeignKey('Sdk', on_delete=models.SET_NULL, null=True)
    # app_id = models.IntegerField()
    # sdk_id = models.IntegerField()
    installed = models.BooleanField(default=False, null=True, blank=True)