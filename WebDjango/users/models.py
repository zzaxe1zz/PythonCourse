from django.db import models
# from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def full_name(self) -> str:
        def get_full_name(self):
            return '{},{}'.format(self.first_name, self.last_name)

    @property
    def direccion_envio(self):
        return self.direccionenvio_set.filter(default=True).first()

    def has_direccion_envio(self):
        return self.direccion_envio is not None


class Cliente(User):
    class Meta:
        proxy = True

    def get_products(self):
        return []


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    biografia = models.TextField()
