from django.db import models
from django.utils import timezone

class CheckIn(models.Model):
    full_name = models.CharField("Họ và tên", max_length=150)
    email = models.EmailField("Email")
    timestamp = models.DateTimeField("Thời gian điểm danh", default=timezone.now)
    note = models.TextField("Ghi chú", blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} lúc {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
