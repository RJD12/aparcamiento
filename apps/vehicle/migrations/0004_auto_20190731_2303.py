# Generated by Django 2.2.3 on 2019-08-01 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_remove_vehicle_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park',
            name='floor',
        ),
        migrations.AlterField(
            model_name='park',
            name='parking_spot',
            field=models.CharField(choices=[('1', 'A1'), ('2', 'A2'), ('3', 'A3'), ('4', 'A4'), ('5', 'A5'), ('6', 'A6'), ('7', 'A7'), ('8', 'A8'), ('9', 'A9'), ('10', 'A10'), ('11', 'B1'), ('12', 'B2'), ('13', 'B3'), ('14', 'B4'), ('15', 'B5'), ('16', 'B6'), ('17', 'B7'), ('18', 'B8'), ('19', 'B9'), ('20', 'B10')], max_length=4),
        ),
    ]
