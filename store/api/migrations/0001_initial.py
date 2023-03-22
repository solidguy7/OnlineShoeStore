# Generated by Django 4.1.7 on 2023-03-22 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['brand_name'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=10)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.brand')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='api.item')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='api.size')),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
        migrations.AddIndex(
            model_name='brand',
            index=models.Index(fields=['brand_name'], name='api_brand_brand_n_c97533_idx'),
        ),
        migrations.AddIndex(
            model_name='size',
            index=models.Index(fields=['title'], name='api_size_title_0665b4_idx'),
        ),
        migrations.AddIndex(
            model_name='price',
            index=models.Index(fields=['-updated'], name='api_price_updated_b95de0_idx'),
        ),
        migrations.AddIndex(
            model_name='item',
            index=models.Index(fields=['title'], name='api_item_title_f02de9_idx'),
        ),
    ]
