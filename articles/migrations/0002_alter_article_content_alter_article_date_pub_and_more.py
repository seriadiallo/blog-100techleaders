# Generated by Django 4.2 on 2024-08-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='contenu'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_pub',
            field=models.DateField(null=True, verbose_name='date de publication'),
        ),
        migrations.AlterField(
            model_name='article',
            name='sumary',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='resume'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='titre'),
        ),
    ]