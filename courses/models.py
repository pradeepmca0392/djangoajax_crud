from django.db import models

class Course(models.Model):
    COURSE_TYPES = (
        (1, 'BCA'),
        (2, 'MCA'),
        (3, 'MBA'),
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    no_subjects = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True)
    course_type = models.PositiveSmallIntegerField(choices=COURSE_TYPES)
