from django.contrib.auth.models import Group, User
from django.db import models

# noinspection PyUnresolvedReferences
import auth0_sso.receivers


class Auth0UserRoleQuerySet(models.QuerySet):

    def get_by_natural_key(self, auth0_role):
        return self.get(auth0_role=auth0_role)


class Auth0UserRole(models.Model):

    auth0_role_id = models.CharField(max_length=20, unique=True, null=True)

    auth0_role = models.CharField(max_length=32, unique=True)

    description = models.TextField(blank=True)

    groups = models.ManyToManyField(Group, blank=True, related_name='auth0_user_roles')

    is_staff = models.BooleanField(default=False)

    class Meta:
        ordering = ('auth0_role',)

    def __str__(self):
        return self.auth0_role

    def natural_key(self):
        return self.auth0_role,


class Auth0UserProfile(models.Model):

    user = models.OneToOneField(User, related_name='auth0_user_profile', on_delete=models.CASCADE)

    created_at = models.DateTimeField()

    updated_at = models.DateTimeField()

    email = models.EmailField()

    name = models.CharField(max_length=100)

    nickname = models.CharField(max_length=100)

    picture = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
