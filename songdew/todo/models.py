from django.db import models, transaction
from django.conf import settings
from django.urls import reverse
from django.db import models


from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    details=models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    is_priority = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.is_priority:
            return super(Todo,self).save(*args, **kwargs)
        with transaction.atomic():
            Todo.objects.filter(is_priority=True,user=self.user).update(is_priority=False)
            return super(Todo,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "todo:for_user",
            kwargs={
                "username": self.user.username
            }
        )


    class Meta:
        ordering = ["-created_at"]
