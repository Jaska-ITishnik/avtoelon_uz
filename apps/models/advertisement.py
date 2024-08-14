from django.db.models import Model, ForeignKey, CASCADE, DateTimeField, \
    BooleanField, TextField, ImageField


class Adv(Model):
    subcategory = ForeignKey('apps.SubCategory', on_delete=CASCADE)
    owner = ForeignKey('apps.User', on_delete=CASCADE)
    is_barging = BooleanField(default=False)
    addition_info = TextField(null=True, blank=True)
    region = ForeignKey('apps.Region', on_delete=CASCADE)
    district = ForeignKey('apps.District', on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = 'adv'


class AdvImage(Model):
    adv = ForeignKey('apps.Adv', on_delete=CASCADE)
    photo = ImageField(upload_to='adv_images/%Y/%m/%d', null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = 'adv_images'


class AdvSubcategoryField(Model):
    subcategory_field = ForeignKey('apps.Field', on_delete=CASCADE)
    adv = ForeignKey('apps.Adv', on_delete=CASCADE)