# Generated by Django 5.0.7 on 2024-07-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_grammartest_instruction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrammarTestSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'grammartestsection',
            },
        ),
    ]