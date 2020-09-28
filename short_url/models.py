from django.db import models

from hashlib import md5


class URL(models.Model):
    base_url = models.URLField(unique=True)
    hash_url = models.URLField(unique=True)
    clicks = models.PositiveIntegerField(default=0) 
    created_at = models.DateField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __repr__(self):
        return self.base_url + ' is shortened to ' + self.hash_url
