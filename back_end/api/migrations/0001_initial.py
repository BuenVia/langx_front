# Generated by Django 5.0.7 on 2024-07-28 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrammarBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('author', models.CharField(max_length=90)),
                ('body', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'grammarblog',
            },
        ),
        migrations.CreateModel(
            name='GrammarCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'grammarcategory',
            },
        ),
        migrations.CreateModel(
            name='Vocab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GrammarBlogAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=45)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.grammarblog')),
            ],
            options={
                'db_table': 'grammarblogassessment',
            },
        ),
        migrations.CreateModel(
            name='GrammarSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.grammarcategory')),
            ],
            options={
                'db_table': 'grammarsubcategory',
            },
        ),
        migrations.AddField(
            model_name='grammarblog',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.grammarsubcategory'),
        ),
        migrations.CreateModel(
            name='GrammarTestSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('instruction', models.TextField(blank=True)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.grammarsubcategory')),
            ],
            options={
                'db_table': 'grammartestsection',
            },
        ),
        migrations.CreateModel(
            name='GrammarTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.IntegerField()),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('option_one', models.CharField(blank=True, max_length=255)),
                ('option_two', models.CharField(blank=True, max_length=255)),
                ('option_three', models.CharField(blank=True, max_length=255)),
                ('feedback', models.CharField(blank=True, max_length=255)),
                ('test_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.grammartestsection')),
            ],
            options={
                'db_table': 'grammartests',
            },
        ),
    ]
