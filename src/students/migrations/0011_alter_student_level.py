# Generated by Django 5.0.dev20230505072651 on 2023-05-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_alter_student_department_alter_student_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('1', 'Level One'), ('2', 'Level Two'), ('3', 'Level Three'), ('4', 'Level Four')], max_length=1),
        ),
    ]