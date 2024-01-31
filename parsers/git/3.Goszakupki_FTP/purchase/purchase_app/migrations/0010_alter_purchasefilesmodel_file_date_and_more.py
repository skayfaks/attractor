# Generated by Django 4.2.3 on 2023-07-15 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_app', '0009_remove_requestmodel_status_requestmodel_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasefilesmodel',
            name='file_date',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasefilesmodel',
            name='filename',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasefilesmodel',
            name='import_date',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasefilesmodel',
            name='record_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasefilesmodel',
            name='status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='externalId',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='externalId_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_app.purchaseplanmodel', to_field='externalId'),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='publish_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchase_files',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchase_files_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_app.purchasefilesmodel'),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchase_object_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseplanmodel',
            name='archive_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseplanmodel',
            name='filename',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseplanmodel',
            name='planNumber',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseplanmodel',
            name='versionNumber',
            field=models.TextField(blank=True, null=True),
        ),
    ]