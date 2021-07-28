# Generated by Django 3.2.5 on 2021-07-28 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_module_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='module_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='course.module'),
        ),
    ]
