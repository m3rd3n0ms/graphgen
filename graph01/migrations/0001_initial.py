# Generated by Django 4.1.5 on 2023-01-28 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('de_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('de_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('en_code', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='Code')),
                ('en_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Enterprise',
                'verbose_name_plural': 'Enterprises',
                'db_table': 'enterprise',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('st_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('st_name', models.CharField(max_length=100)),
                ('st_enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph01.enterprise')),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
                'db_table': 'store',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('tr_code', models.FloatField(primary_key=True, serialize=False)),
                ('tr_date_time', models.DateTimeField(blank=True, null=True)),
                ('tr_type_doc', models.CharField(max_length=1)),
                ('tr_usd_value', models.FloatField()),
                ('tr_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph01.department')),
                ('tr_enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph01.enterprise')),
                ('tr_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph01.store')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'db_table': 'transaction',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='de_enterprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph01.enterprise'),
        ),
        migrations.AddField(
            model_name='department',
            name='de_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph01.store'),
        ),
    ]
