from django.db import models


class User(models.Model):

    ChoiseOne = (
        ("1", "Jismoniy shaxs"),
        ("2", "Yuridik shaxs"),
    )

    ChoiseTwo = (
        ("1", True),
        ("2", False)
    )

    UserNameOne = models.CharField(max_length=50, choices=ChoiseOne, null=False, blank=False)
    UserNameTwo = models.CharField(max_length=50, null=False, blank=False)
    UserEmail = models.EmailField(max_length=100, null=False, blank=False)
    UserPassword = models.CharField(max_length=100, null=False, blank=False)
    UserPhone = models.CharField(max_length=100, null=False, blank=False)
    UserOferta = models.BooleanField(max_length=50, choices=ChoiseTwo, null=False, blank=True)
    UserTime = models.DateTimeField(null=False)

    def __str__(self):
        return self.UserNameOne