# Generated by Django 4.1.1 on 2022-09-15 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_rename_recipe_steps_recipe_recipe_step_reccipe_step'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_step',
        ),
    ]
