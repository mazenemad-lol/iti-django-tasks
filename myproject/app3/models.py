from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم / Name")
    email = models.EmailField(verbose_name="البريد الإلكتروني / Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="رقم الهاتف / Phone")
    notes = models.TextField(blank=True, verbose_name="ملاحظات / Notes")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة / Created At")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "جهة اتصال / Contact"
        verbose_name_plural = "جهات الاتصال / Contacts"

    def __str__(self):
        return f"{self.name} ({self.email})"
