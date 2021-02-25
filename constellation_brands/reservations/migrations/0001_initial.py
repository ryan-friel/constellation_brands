# Generated by Django 3.1.7 on 2021-02-25 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wineries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserveration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_time', models.DateField()),
                ('resveration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wineries.winery')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
