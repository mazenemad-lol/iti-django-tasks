from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'إنشاء حساب مستخدم مسؤول (Superuser) للوحة تحكم Django Admin تلقائياً'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'admin'
        password = 'adminpassword123'
        email = 'admin@example.com'

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'المستخدم المسؤول "{username}" موجود بالفعل مسبقاً.'))
        else:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(
                f'تم إنشاء حساب الأدمن بنجاح!\n'
                f'اسم المستخدم (Username): {username}\n'
                f'كلمة المرور (Password): {password}\n'
                f'الرابط: http://127.0.0.1:8000/admin/'
            ))
