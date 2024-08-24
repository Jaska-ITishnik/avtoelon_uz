from django.db.models import Model, ForeignKey, CASCADE, PositiveIntegerField, DateTimeField, ImageField, CharField, \
    SlugField
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class News(Model):
    title = CharField(max_length=255)
    slug = SlugField(max_length=255)
    author = ForeignKey('apps.User', CASCADE)
    views_count = PositiveIntegerField(default=0, editable=False)
    content = CKEditor5Field()
    photo = ImageField(upload_to='news_image/')
    created_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)
