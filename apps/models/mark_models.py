from django.db.models import Model, ForeignKey, CASCADE, JSONField


class MarksModel(Model):
    subcategory_field = ForeignKey('apps.Field', on_delete=CASCADE)
    model_marks = JSONField(default=dict)
