# Generated by Django 3.0.6 on 2020-05-27 10:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import education.validate_url


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20200526_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.URLField(validators=[education.validate_url.validator])),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Tasks')),
            ],
        ),
    ]
