from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class ManagerUsers(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class Users(AbstractUser):
    """User model."""

    username = models.CharField(max_length=50, null=True, unique=True)
    email=models.EmailField(max_length=50, null=True, unique=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ManagerUsers()


class Post(models.Model):
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True,null=True)
    updated_at = models.DateTimeField(null=True, blank=True)