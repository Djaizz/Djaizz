"""Migrations related to Django 4.0."""


# pylint: disable=invalid-name


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Migrations related to Django 4.0."""

    dependencies = [('contenttypes', '0002_remove_content_type_name'),
                    ('AIModel', '0005_GoogleTranslate')]

    operations = [
        migrations.AlterField(
            model_name='aimodel',
            name='polymorphic_ctype',
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='polymorphic_%(app_label)s.%(class)s_set+',
                to='contenttypes.contenttype')),

        migrations.AlterField(
            model_name='cloudaiservice',
            name='aimodel_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.aimodel')),

        migrations.AlterField(
            model_name='googletranslate',
            name='cloudaiservice_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.cloudaiservice')),

        migrations.AlterField(
            model_name='pretrainedhuggingfaceaudioclassifier',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfaceimageclassifier',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacemaskfiller',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfaceobjectdetector',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacequestionanswerer',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacespeechrecognizer',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacetablequestionanswerer',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacetext2textgenerator',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacetextclassifier',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacetextgenerator',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacetextsummarizer',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacetokenclassifier',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacetransformer',
            name='aimodel_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.aimodel')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacetranslator',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedhuggingfacezeroshotclassifier',
            name='pretrainedhuggingfacetransformer_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.pretrainedhuggingfacetransformer')),

        migrations.AlterField(
            model_name='pretrainedkerasimagenetclassifier',
            name='aimodel_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='AIModel.aimodel'))
    ]
