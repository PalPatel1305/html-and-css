# Generated by Django 3.2.9 on 2021-11-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='edu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('persentage', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='experince',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_due', models.CharField(max_length=50)),
                ('ex_about', models.CharField(max_length=500)),
                ('ex_post', models.CharField(max_length=50)),
                ('ex_deg', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='INFO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desi', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=500)),
                ('lang', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_name', models.CharField(max_length=100)),
                ('pr_about', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=10)),
                ('cap', models.CharField(max_length=4)),
            ],
        ),
    ]