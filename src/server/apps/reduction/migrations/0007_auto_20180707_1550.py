# Generated by Django 2.0.5 on 2018-07-07 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reduction', '0006_auto_20180707_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='reductionbiosans',
            name='action',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reductionbiosans_action', related_query_name='reductionbiosans_action', to='reduction.Actions'),
        ),
        migrations.AddField(
            model_name='reductiongpsans',
            name='action',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reductiongpsans_action', related_query_name='reductiongpsans_action', to='reduction.Actions'),
        ),
        migrations.AddField(
            model_name='reductionhyspec',
            name='action',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reductionhyspec_action', related_query_name='reductionhyspec_action', to='reduction.Actions'),
        ),
    ]
