import uuid

from django.db import models
from django.core.validators import RegexValidator

from ckeditor.fields import RichTextField
from main.models import BaseModel
from main.variables import phone_regex


class ContactDetails(BaseModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    # creator = models.ForeignKey("auth.User", blank=True, on_delete=models.CASCADE)
    # updater = models.ForeignKey("auth.User", blank=True, null=True, on_delete=models.CASCADE)
    # date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    # date_updated = models.DateTimeField(auto_now_add=True)
    # is_deleted = models.BooleanField(default=False)
    phone = models.CharField(null=True, blank=True, unique=True, max_length=20)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contact Details"
    def __str__(self):
        return self.phone

class Enquiry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    name = models.CharField(max_length=64)
    # phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}$', message="format: +000 0000000000000")
    phone = models.CharField(validators=[phone_regex] ,max_length=20)
    message = models.TextField()
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Enquiries"
        

    def __str__(self):
        return self.name

class Innovation(BaseModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    # creator = models.ForeignKey("auth.User", blank=True, on_delete=models.CASCADE)
    # updater = models.ForeignKey("auth.User", blank=True, null=True, on_delete=models.CASCADE)
    # date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    # date_updated = models.DateTimeField(auto_now_add=True)
    # is_deleted = models.BooleanField(default=False)
    title = models.CharField(max_length=128)
    image = models.FileField(upload_to='innovation/')
    short_description = RichTextField()
    extra_content = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Innovations"

    def __str__(self):
        return self.title

class Industry(BaseModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    # creator = models.ForeignKey("auth.User", blank=True, on_delete=models.CASCADE)
    # updater = models.ForeignKey("auth.User", blank=True, null=True, on_delete=models.CASCADE)
    # date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    # date_updated = models.DateTimeField(auto_now_add=True)
    # is_deleted = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    image = models.FileField(upload_to='industry/')

    class Meta:
        verbose_name_plural = "Industries"

    def __str__(self):
        return self.name
