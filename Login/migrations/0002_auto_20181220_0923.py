# Generated by Django 2.1.3 on 2018-12-20 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=400, verbose_name='联系内容')),
                ('description', models.CharField(blank=True, max_length=50, verbose_name='联系描述')),
                ('contacted_at', models.DateTimeField(auto_now_add=True, verbose_name='联系时间')),
                ('Contacted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL, verbose_name='联系人')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_img',
            field=models.ImageField(null=True, upload_to='post_img', verbose_name='图片'),
        ),
        migrations.AddField(
            model_name='topic',
            name='img',
            field=models.ImageField(null=True, upload_to='img', verbose_name='图片'),
        ),
    ]