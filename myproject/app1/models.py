from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="العنوان / Title")
    content = models.TextField(verbose_name="المحتوى / Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء / Created At")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "مقال / Article"
        verbose_name_plural = "مقالات / Articles"

    def __str__(self):
        return self.title
