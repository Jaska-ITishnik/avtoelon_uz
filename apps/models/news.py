from django.db.models import Model, ForeignKey, CASCADE, PositiveIntegerField, DateTimeField, ImageField, CharField
from django_ckeditor_5.fields import CKEditor5Field


class News(Model):
    title = CharField(max_length=255)
    author = ForeignKey('apps.User', on_delete=CASCADE)
    views_count = PositiveIntegerField(default=0, editable=False)
    content = CKEditor5Field()
    created_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'


class NewsImage(Model):
    news = ForeignKey(News, on_delete=CASCADE)
    photo = ImageField(upload_to='news_images/', null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = 'news_images'

