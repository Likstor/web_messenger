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


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    
    username_validator = UnicodeUsernameValidator()
    
    username = models.CharField(
        _('username'),
        max_length=30,
        help_text=_(
            "30 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
    )
    phone = PhoneNumberField(null=True, blank=False, unique=False)
    description = models.TextField(_('description'))
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
        upload_to='files/user_avatars/', 
        default='files/default/user_avatar.jpg')

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

    def get_username(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)