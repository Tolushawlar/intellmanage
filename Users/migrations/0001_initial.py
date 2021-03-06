# Generated by Django 2.0.7 on 2019-06-02 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Category')),
            ],
            options={
                'ordering': ('-amount',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('budget', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='Users.Project'),
        ),
        migrations.AddField(
            model_name='category',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Project'),
        ),
    ]
