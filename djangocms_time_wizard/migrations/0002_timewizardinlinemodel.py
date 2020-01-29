# Generated by Django 2.2.9 on 2020-01-29 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('djangocms_time_wizard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeWizardInlineModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='djangocms_time_wizard_timewizardinlinemodel',
                    serialize=False,
                    to='cms.CMSPlugin')
                ),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
    ]