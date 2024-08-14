from django.db.models import Model, ForeignKey, CASCADE, PositiveIntegerField, DateTimeField
from django_ckeditor_5.fields import CKEditor5Field


class News(Model):
    author = ForeignKey('apps.User', on_delete=CASCADE)
    views_count = PositiveIntegerField(default=0, editable=False)
    content = CKEditor5Field()
    created_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = 'news'
