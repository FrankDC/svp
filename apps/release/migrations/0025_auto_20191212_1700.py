# Generated by Django 2.2.3 on 2019-12-12 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0024_auto_20191211_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abtest',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='idc_abtest', to='assets.IDC', verbose_name='按机房'),
        ),
        migrations.AlterField(
            model_name='abtest',
            name='percent',
            field=models.SmallIntegerField(blank=True, choices=[(10, '10%'), (30, '30%'), (50, '50%'), (80, '80%')], null=True, verbose_name='按比例'),
        ),
    ]