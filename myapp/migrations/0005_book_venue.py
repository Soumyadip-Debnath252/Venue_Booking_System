# Generated by Django 3.2.8 on 2022-06-14 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='venue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='venue', to='myapp.venue', verbose_name='Venue Name'),
            preserve_default=False,
        ),
    ]