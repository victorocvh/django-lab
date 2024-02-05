from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager, BaseUserManager

class CustomUserManager(BaseUserManager):

    def _create_user(self,nome, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            email=self.normalize_email(email)
        )
       
        user.nome = nome
        user.is_staff = extra_fields['is_staff']
        user.is_superuser = extra_fields['is_superuser']
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nome=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(nome, email, password, **extra_fields)

class CustomUser(AbstractBaseUser):

    TIPO_USUARIO = (
        ('normal','normal'),
        ('estudante','estudante'),
        ('moderador','moderador')
    )

    email = models.EmailField(unique=True,null=False)
    tipo_usuario = models.CharField(max_length=100, choices=TIPO_USUARIO, default='normal')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser 
    
    def has_module_perms(self, app_label):
        return self.is_superuser
    