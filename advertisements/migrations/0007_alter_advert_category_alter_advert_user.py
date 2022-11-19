# Generated by Django 4.1.3 on 2022-11-19 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0006_alter_advert_image_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='advertisements.category'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
