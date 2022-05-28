# Generated by Django 4.0.3 on 2022-05-14 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_ticket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='Cabin',
        ),
        migrations.AddField(
            model_name='ticket',
            name='Ticket_class',
            field=models.CharField(choices=[('First', 'First'), ('Economy', 'Economy')], default='First', max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='Seat_Number',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='Seat_location',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=1),
        ),
    ]