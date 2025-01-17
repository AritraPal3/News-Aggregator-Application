# Generated by Django 5.0.7 on 2024-08-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_article_source_alter_article_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='source',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=300),
        ),
    ]