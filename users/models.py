from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, name, nusp, email, password=None):
        if not name:
            raise ValueError("name is required")
        if not nusp:
            raise ValueError("nusp is required")
        if not email:
            raise ValueError("email is required")

        user = self.model(
            name = name,
            nusp = nusp,
            email = email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, nusp, email, password=None):
        user = self.create_user(
            name = name,
            nusp = nusp,
            email = email,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    name = models.CharField(
        verbose_name="name",
        max_length=255,
        unique=True
    )

    nusp = models.CharField(
        verbose_name="nusp",
        max_length=255,
        unique=True
    )

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True
    )

    date_joined = models.DateTimeField(
        verbose_name="date joined",
        auto_now=True
    )

    last_login = models.DateTimeField(
        verbose_name="last login",
        auto_now=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'name'

    REQUIRED_FIELDS = ['nusp', 'email']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True