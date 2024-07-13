from django.db import models
from django.db.models import Manager

from task.managers import TaskTodoManager, TaskDoneManager, TaskDeleteManager, TaskDoneDeleteManager


# Create your models here.


class Task(models.Model):
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Topshiriq'
        verbose_name_plural = 'Topshiriqlar'

    title = models.CharField(max_length=255, verbose_name='Sarlavha...')
    description = models.TextField(verbose_name='Tavsif:')
    is_done = models.BooleanField(default=False, verbose_name='Bajarildi')
    is_delete = models.BooleanField(default=False, verbose_name='O`chirildi')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # managers #Task.objects.all()
    objects = Manager() #Task.objects.all()
    todo = TaskTodoManager()
    done = TaskDoneManager() #Task.done.all()
    delete = TaskDeleteManager() #Task.delete.all()
    done_delete = TaskDoneDeleteManager() #Task.done_delete.all()

    def __str__(self):
        return self.title

    @property
    def status(self):
        code = "DONE & DELETE" if self.is_done and self.is_delete else "DONE" if self.is_done else "DELETE" if self.is_delete else "TODO"
        return code

    @property
    def css_class(self):
        cls = "dark" if self.is_done and self.is_delete else "success" if self.is_done else "danger" if self.is_delete else "warning"
        return cls