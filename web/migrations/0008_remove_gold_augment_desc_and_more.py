# Generated by Django 5.1 on 2024-09-09 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_gold_augment_prismatic_augment_silver_augment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gold_augment',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='prismatic_augment',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='silver_augment',
            name='desc',
        ),
    ]
