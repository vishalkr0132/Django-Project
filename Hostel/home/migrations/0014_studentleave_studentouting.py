# Generated by Django 4.0.4 on 2022-04-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_delete_leaveapprovel_delete_studentleave_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel', models.CharField(max_length=25, null=True)),
                ('room_no', models.CharField(max_length=10)),
                ('roll_no', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=25)),
                ('date_of_outing', models.CharField(max_length=20, null=True)),
                ('date_of_comeing', models.CharField(max_length=20, null=True)),
                ('number_of_days', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=50, null=True)),
                ('status', models.BooleanField(default=False, verbose_name='Aproved')),
                ('Aaa', models.CharField(max_length=50, null=True)),
                ('Aab', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentOuting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel', models.CharField(max_length=25, null=True)),
                ('room_no', models.CharField(max_length=10)),
                ('roll_no', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=50)),
                ('outing_time', models.CharField(max_length=20)),
                ('in_time', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False, verbose_name='Aproved')),
                ('Aaa', models.CharField(max_length=50, null=True)),
                ('Aab', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]