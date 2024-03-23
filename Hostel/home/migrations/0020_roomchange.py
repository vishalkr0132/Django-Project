# Generated by Django 4.0.4 on 2022-04-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_delete_roomchange'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=50)),
                ('hostel', models.CharField(max_length=20)),
                ('old_room_no', models.IntegerField()),
                ('new_room_no', models.IntegerField()),
                ('student_name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('reasion', models.CharField(max_length=50)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('Aaa', models.CharField(max_length=50, null=True)),
                ('Aab', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
