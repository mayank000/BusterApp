from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _



class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		"""
		Creates and saves a User with the given email and password.
		"""
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_staff', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('email address'), unique=True)
	name = models.CharField(_('first name'), max_length=30, blank=True)
	added_on = models.DateTimeField(_('date joined'), auto_now_add=True)
	update_on = models.DateTimeField(_('date updated'), auto_now=True)
	is_active = models.BooleanField(_('active'), default=True)
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
	is_staff = models.BooleanField(_('staff status'),default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')
		db_table = 'users'

	def get_full_name(self):
		
		return self.name.strip() if self.name else ''

	def get_short_name(self):

		return self.name
	
	def __str__(self):
		
		return "%s - %s" %(self.email, self.id)