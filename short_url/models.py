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
        if not self.id:
            self.hash_url = md5(self.base_url.encode()).hexdigest()[:10]

        return super().save(*args, **kwargs)

    def __repr__(self):
        return self.base_url + ' is shortened to ' + self.hash_url
