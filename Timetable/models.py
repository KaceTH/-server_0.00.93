from django.db import models

# Create your models here.


class TableCell(models.Model):
    subject = models.CharField(blank=True, max_length=40)
    location = models.CharField(blank=True, max_length=40)
    teacher = models.CharField(blank=True, max_length=40)
    number = models.IntegerField(blank=True, null=True)
    start = models.TimeField(blank=True)
    end = models.TimeField(blank=True)


class TimeTable(models.Model):
    grade_number = models.IntegerField(blank=True, null=True)
    class_number = models.IntegerField(blank=True, null=True)

    sun = models.ManyToManyField(
        TableCell,
        blank=True,
        related_name="sun"
    )
    mon = models.ManyToManyField(
        TableCell,
        blank=True,
        related_name="mon"
    )
    tue = models.ManyToManyField(
        TableCell,
        blank=True,
        related_name="tue"
    )
    wed = models.ManyToManyField(
        TableCell,
        blank=True,
        related_name="wed"
    )
    thu = models.ManyToManyField(
        TableCell,
        blank=True,
        related_name="thu"
    )
    fri = models.ManyToManyField(
        TableCell,
        blank=True,
        related_name="fri"
    )
    set = models.ManyToManyField(
        TableCell,
        blank=True,
        related_name="set"
    )