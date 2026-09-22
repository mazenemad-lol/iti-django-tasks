from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المهمة / Task Title")
    is_completed = models.BooleanField(default=False, verbose_name="مكتملة / Completed")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء / Created At")

    class Meta:
        ordering = ['is_completed', '-created_at']
        verbose_name = "مهمة / Task"
        verbose_name_plural = "مهام / Tasks"

    def __str__(self):
        return self.title
