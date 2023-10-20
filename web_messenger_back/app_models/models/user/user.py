from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from ..status.status import Status
from django.core.mail import send_mail
from .manager import UserManager
from phonenumber_field.modelfields import PhoneNumberField


def user_directory_path(instance, filename):
    return 'users/user_{0}/{1}'.format(instance.id, filename)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    
    user_name = models.CharField(
        _('username'),
        max_length=30,
        help_text=_(
            "30 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )
    phone = PhoneNumberField(null=True, blank=True)
    description = models.TextField(_('description'), null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    
    is_banned = models.BooleanField(_('is banned'), default=False)
    date_banned = models.DateTimeField(_('date banned'), null=True, blank=True)
    
    is_active = models.BooleanField(_('is active'), default=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    
    status_id = models.ForeignKey(
        Status, 
        on_delete=models.SET_NULL,
        null=True
        )
    
    avatar = models.ImageField(
        upload_to=user_directory_path, 
        default='default/user_avatar.png')

    objects = UserManager()
    
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_name(self):
        return self.user_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)