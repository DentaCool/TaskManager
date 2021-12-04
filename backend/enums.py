from django.db import models
from django.utils.translation import gettext_lazy as _


class Priority(models.TextChoices):
    low = "L", _("Low")
    medium = "M", _("Medium")
    high = "H", _("High")


class Status(models.TextChoices):
    backlog = "BL", _("Backlog")
    in_progress = "IP", _("In Progress")
    done = "DN", _("Done")
