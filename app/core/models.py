"""
Database models.
"""
from simple_history.models import HistoricalRecords
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manage for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Task(models.Model):
    """Task object."""
    class Status(models.TextChoices):
        NEW = "nowy", "Nowy"
        IN_PROGRESS = "w_toku", "W_toku"
        RESOLVED = "rozwiazany", "Rozwiazany"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
        verbose_name="Przypisany użytkownik"
    )
    name = models.CharField("Nazwa", max_length=255)
    description = models.TextField("Opis", blank=True)
    status = models.CharField(
        "Status",
        max_length=12,
        choices=Status.choices,
        default=Status.NEW,
    )
    history = HistoricalRecords()

    def __str__(self):
        return self.name