from django.db import models

class URL(models.Model):
    def __str__(self):
        return self.short_url
    # user_id = models.CharField(max_length=256)
    long_url = models.CharField(max_length=1024)
    short_url = models.CharField(max_length=1024)
    ttl = models.IntegerField()

class User(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=256)
    no_of_urls = models.IntegerField()


class Utility(models.Model):
    def __str__(self):
        return str(self.current_url_no)
    current_url_no = models.IntegerField()
