# Generated by Django 2.2.5 on 2019-10-09 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_student_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='select_batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='batchapp.Batch'),
        ),
    ]
