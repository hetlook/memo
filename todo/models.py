from django.db import models
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
    IMPORTANT_CHOICE = (
        ('1','不重要不紧急'),
        ('2','重要不紧急'),
        ('3','不重要但紧急'),
        ('4','重要且紧急'),
    )
    FINISH_STATUS = (
        ('doing', '进行中'),
        ('done', '已完成'),
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)
    important = models.CharField(choices=IMPORTANT_CHOICE, max_length=10, default='4')
    finish = models.CharField(max_length=10, choices=FINISH_STATUS, default='doing')
    class_type = models.CharField(max_length=50, default='success')

    def __str__(self):
        return self.title