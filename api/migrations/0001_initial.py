# Generated by Django 2.2.5 on 2019-09-16 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('key', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('locale', models.CharField(blank=True, default='xx_XX', max_length=32)),
                ('name_en', models.CharField(blank=True, default='', max_length=32)),
                ('name', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=32)),
                ('data_start_row', models.PositiveSmallIntegerField(default=3)),
                ('translation_start_col', models.PositiveSmallIntegerField(default=4)),
                ('key_col', models.PositiveSmallIntegerField(default=4)),
                ('default_col', models.PositiveSmallIntegerField(default=4)),
                ('regex', models.CharField(default='\\.([a-zA-Z]{2})_(.*)', max_length=128)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='UniqueText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('textlabel', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trans', models.TextField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Language')),
                ('uniquetext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UniqueText')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='BaseText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Base')),
                ('uniquetext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UniqueText')),
            ],
        ),
        migrations.AddField(
            model_name='base',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Platform'),
        ),
    ]
