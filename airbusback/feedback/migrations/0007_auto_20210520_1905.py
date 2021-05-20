# Generated by Django 3.2.3 on 2021-05-20 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0006_auto_20210520_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='screenshot',
            field=models.FileField(null=True, upload_to='feedback/'),
        ),
        migrations.AlterField(
            model_name='bugreport',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='topic', to='feedback.bugtopics'),
        ),
        migrations.AlterField(
            model_name='bugreport',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]