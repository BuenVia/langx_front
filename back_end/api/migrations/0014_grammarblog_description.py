# Generated by Django 5.0.7 on 2024-07-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_grammartest_instruction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grammarblog',
            name='description',
            field=models.CharField(default='TBC', max_length=255),
            preserve_default=False,
        ),
    ]
