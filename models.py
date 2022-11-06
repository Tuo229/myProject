from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.shortcuts import reverse
from django.utils import timezone
from django.conf import settings

class UserManager(BaseUserManager):

    usse_in_migrations = True

    def _create_user(self,  email, username, phone, password, **extra_fields):
        values = [username, email, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('La valeur {} doit être définie'.format(field_name))
            
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.phone = phone
        user.save(using=self._db)
        return user

    def create_user(self, email, username, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)  
        extra_fields.setdefault('is_superuser', False)

        return self._create_user( email, username, phone, password, **extra_fields)

    def create_superuser(self, email, username, phone, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Le champ est staff doit être défini à True")
            

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Le champ est admin doit être défini à True")

        return self._create_user(email, username, phone, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField('Nom', max_length=50, blank=True)
    last_name = models.CharField('Prénom', max_length=50, blank=True)
    email = models.EmailField("Email", max_length=254, unique=True)
    phone = models.CharField("Contact", max_length=50, unique=True, null=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']



    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
    
        self.password = self.set_password(self.password)
        super(User, self).save(*args, **kwargs)


class Ville(models.Model):
    
    name = models.CharField("Nom ville", max_length=128)

    def __str__(self):
        return self.name


class Immobilier(models.Model):
    
    city = models.ForeignKey("Ville", verbose_name="Ville", on_delete=models.CASCADE, null=True)
    country = models.CharField("Pays", max_length=128)
    types = models.CharField("Type", max_length=128)
    price = models.IntegerField("Prix")
    status = models.CharField("Status", max_length=128)
    area = models.IntegerField('Superficie')
    desc = models.CharField("Description votre bien", max_length=1000)
    picture_one = models.ImageField("image", upload_to=settings.MEDIA_ROOT)
    picture_two = models.ImageField("image 1", upload_to=settings.MEDIA_ROOT, blank=True)
    picture_three = models.ImageField("image 2", upload_to=settings.MEDIA_ROOT, blank=True)



    def __str__(self):
        return self.types


class Appart(Immobilier):

    num_piece = models.IntegerField('Nombre de pièce')
    num_toilete = models.IntegerField('Nombre de toillete')


class Besoin(models.Model):
    
    needed_type = models.CharField('Type de besoin', max_length=50)
    city = models.CharField('Ville', max_length=50)
    country = models.CharField("Pays", max_length=50)
    min_price = models.IntegerField("Prix min")
    max_price = models.IntegerField("Prix max")
    area = models.IntegerField("Superficie")
    published_by = models.ForeignKey("User", verbose_name="Publié par", on_delete=models.CASCADE)
    published_date = models.DateTimeField("Date de publicatication", default=timezone.now)
    

    def __str__(self):
        return self.needed_type



