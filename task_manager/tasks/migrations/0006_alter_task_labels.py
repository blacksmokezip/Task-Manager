# Generated by Django 4.0 on 2023-11-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0003_alter_label_options_alter_label_created_at_and_more'),
        ('tasks', '0005_alter_task_author_alter_task_executor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', through='tasks.TaskLabelRelation', to='labels.Label', verbose_name='Labels'),
        ),
    ]
