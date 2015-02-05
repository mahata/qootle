from django.db import models
from projects.models import Projects


class Units(models.Model):
    project = models.ForeignKey(Projects, db_index=True)
    source = models.TextField(editable=True)
    source_plural = models.TextField(editable=True)
    context = models.TextField(editable=True)
    target = models.TextField(editable=True)

    class Meta:
        app_label = "units"
