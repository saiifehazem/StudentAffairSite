# Generated by Django 5.0.dev20230505072651 on 2023-05-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_alter_student_department_alter_student_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]