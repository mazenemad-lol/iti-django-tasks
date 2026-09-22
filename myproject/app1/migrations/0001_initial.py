from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='العنوان / Title')),
                ('content', models.TextField(verbose_name='المحتوى / Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء / Created At')),
            ],
            options={
                'verbose_name': 'مقال / Article',
                'verbose_name_plural': 'مقالات / Articles',
                'ordering': ['-created_at'],
            },
        ),
    ]
