# Generated by Django 4.0.3 on 2022-06-02 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_rename_author_step_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.FloatField(null=True),
        ),
    ]
