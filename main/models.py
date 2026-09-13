from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True
    )

    title = models.CharField(max_length=200)

    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    due_date = models.DateField(
        null=True,
        blank=True
    )

    priority = models.CharField(
        max_length=10,
        choices=[
            ("high", "High"),
            ("medium", "Medium"),
            ("low", "Low"),
        ],
        default="medium"
    )

    def __str__(self):
        return self.title


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        null=True,
        blank=True
    )

    # Profile Photo
    photo = models.ImageField(
        upload_to="profile_photos/",
        blank=True,
        null=True
    )

    # Personal Information
    full_name = models.CharField(
        max_length=150,
        blank=True
    )

    joining_date = models.DateField(
        null=True,
        blank=True
    )

    # Education
    education = models.TextField(
        blank=True
    )

    # Skills
    skills = models.TextField(
        blank=True
    )

    # About
    about_me = models.TextField(
        blank=True
    )

    # Projects
    projects = models.TextField(
        blank=True
    )

    # Achievements
    achievements = models.TextField(
        blank=True
    )

    # Certifications
    certifications = models.TextField(
        blank=True
    )

    def __str__(self):

        if self.user:
            return f"{self.user.username} Profile"

        return "Profile"
    