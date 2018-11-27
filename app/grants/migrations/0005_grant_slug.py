# Generated by Django 2.1.2 on 2018-11-20 20:29

from django.db import migrations
import django_extensions.db.fields


def update_grants(apps, schema_editor):
    """Handle the data migration for grant.slug."""
    Grant = apps.get_model('grants', 'Grant')

    grants = Grant.objects.all()
    for grant in grants:
        grant.save()


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0004_auto_20181120_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title'),
        ),
        migrations.RunPython(update_grants),
    ]
