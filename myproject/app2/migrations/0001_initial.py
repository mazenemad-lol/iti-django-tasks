from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان المهمة / Task Title')),
                ('is_completed', models.BooleanField(default=False, verbose_name='مكتملة / Completed')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء / Created At')),
            ],
            options={
                'verbose_name': 'مهمة / Task',
                'verbose_name_plural': 'مهام / Tasks',
                'ordering': ['is_completed', '-created_at'],
            },
        ),
    ]
