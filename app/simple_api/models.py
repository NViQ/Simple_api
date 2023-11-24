from django.db import models
import uuid


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Log(UUIDMixin):
    request_data = models.TextField()
    response_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}: {self.request_data} - {self.response_data}"

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
