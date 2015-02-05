from django.db import models


class Projects(models.Model):
    name = models.TextField(editable=True)

    class Meta:
        app_label = "projects"
