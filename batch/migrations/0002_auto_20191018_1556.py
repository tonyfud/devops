# Generated by Django 2.2.3 on 2019-10-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batchcmdlog',
            options={'ordering': ['-create_time'], 'verbose_name': '批量日志', 'verbose_name_plural': '批量日志'},
        ),
        migrations.AddField(
            model_name='batchcmdlog',
            name='script',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='脚本(文件名)'),
        ),
        migrations.AddField(
            model_name='batchcmdlog',
            name='type',
            field=models.SmallIntegerField(choices=[(1, '命令'), (2, '脚本')], default=1, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='batchcmdlog',
            name='cmd',
            field=models.TextField(blank=True, null=True, verbose_name='命令详情/脚本'),
        ),
    ]
