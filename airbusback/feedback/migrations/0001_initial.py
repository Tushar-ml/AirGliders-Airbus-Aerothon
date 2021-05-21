# Generated by Django 3.2.3 on 2021-05-21 09:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bugTopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicname', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MaxLengthValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=30)),
                ('email', models.EmailField(default='default@gmail.com', max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('description', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('sentiment', models.CharField(default='Neutral', max_length=20)),
                ('score', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='bugReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('screenshot', models.ImageField(null=True, upload_to='feedback/')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='topic', to='feedback.bugtopics')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]