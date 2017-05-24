from django.db import models

# Create your models here.


class Faq(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    ordering = models.IntegerField()
    show_on_registration = models.BooleanField(default=False)
    show_on_sponsors = models.BooleanField(default=False)
    show_on_home = models.BooleanField(default=False)

    def __str__(self):
        return "{}: {}".format(self.title, self.body)
