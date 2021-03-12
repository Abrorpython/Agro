from django.db import models
from django.contrib.postgres.fields import ArrayField


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
        return "%s  -  %s" % (self.UserNameOne, self.UserNameTwo)


class Province(models.Model):
    ProName = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "%s - %s" % (self.id, self.ProName)


class Region(models.Model):
    RegPro = models.ForeignKey(Province, related_name="sort", null=True, blank=True, on_delete=models.SET_NULL)
    RegName = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.RegPro, self.RegName)


class Categoriya(models.Model):
    CategoriyName=models.CharField(max_length=100,null=False,blank=False)


    def __str__(self):
        return "%s - %s" % (self.id,self.CategoriyName)


class Obyavleniya(models.Model):
    obyavName=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return "%s - %s" % (self.id, self.obyavName)


class Sostayanie(models.Model):
    SostayanieName=models.CharField(max_length=30,null=False,blank=False)

    def __str__(self):
        return "%s" % (self.SostayanieName)


class ChastnoLitso(models.Model):
    PrivatePersonName=models.CharField(max_length=40,null=False,blank=False)

    def __str__(self):
        return "%s" % (self.PrivatePersonName)


class Nalichie(models.Model):
    NalichieName=models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return "%s" % (self.NalichieName)


class Edinitsva(models.Model):
    EdinitsvaName=models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return "%s" % (self.EdinitsvaName)


class Dogovornaya(models.Model):
    DogovornayaName=models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
       return "%s" % (self.DogovornayaName)


class News(models.Model):
    Category = models.ForeignKey(Categoriya,null=True,blank=True,on_delete=models.SET_NULL)
    Regions = models.ForeignKey(Province,null=True,blank=True,on_delete=models.SET_NULL)
    Obyav = models.ForeignKey(Obyavleniya,null=True,blank=True,on_delete=models.SET_NULL)
    Heading = models.CharField(max_length=1000,null=False,blank=False)
    Sosta = models.ForeignKey(Sostayanie,null=True,blank=True,on_delete=models.SET_NULL)
    Litso = models.ForeignKey(ChastnoLitso,null=True,blank=True,on_delete=models.SET_NULL)
    Nalich = models.ForeignKey(Nalichie,null=True,blank=True,on_delete=models.SET_NULL)
    Stoim = models.FloatField(max_length=20,null=False,blank=False)
    Sum = models.ForeignKey(Edinitsva,null=True,blank=True,on_delete=models.SET_NULL)
    Dogovr = models.ForeignKey(Dogovornaya,null=True,blank=True,on_delete=models.SET_NULL)
    OpisaniyaName = models.TextField(null=False, blank=False)
    Images = ArrayField(models.ImageField(upload_to='news_image', null=True), default=[])






