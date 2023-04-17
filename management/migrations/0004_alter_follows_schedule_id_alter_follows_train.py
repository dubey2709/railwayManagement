# Generated by Django 4.2 on 2023-04-08 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_moves_on_train'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follows',
            name='schedule_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.schedule', unique=True),
        ),
        migrations.AlterField(
            model_name='follows',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.train', unique=True),
        ),
    ]
