from django.db.models import Model, ForeignKey, CASCADE, CharField


class Region(Model):
    name = CharField(max_length=220)

    class Meta:
        db_table = 'regions'


class District(Model):
    name = CharField(max_length=220)
    region = ForeignKey('apps.Region', CASCADE)

    #  slug

    class Meta:
        db_table = 'districts'