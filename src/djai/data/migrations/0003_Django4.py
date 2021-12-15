"""Migrations related to Django 4.0."""


# pylint: disable=invalid-name


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Migrations related to Django 4.0."""

    dependencies = [('contenttypes', '0002_remove_content_type_name'),
                    ('AIData', '0002_InDBJSONDataSet')]

    operations = [
        migrations.AlterField(
            model_name='dataschema',
            name='polymorphic_ctype',
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='polymorphic_%(app_label)s.%(class)s_set+',
                to='contenttypes.contenttype')),

        migrations.AlterField(
            model_name='dataset',
            name='polymorphic_ctype',
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='polymorphic_%(app_label)s.%(class)s_set+',
                to='contenttypes.contenttype')),

        migrations.AlterField(
            model_name='indbjsondataset',
            name='dataset_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIData.dataset'))
    ]
