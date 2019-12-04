# Generated by Django 2.0.3 on 2018-11-17 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('already_ordered', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=4)),
                ('add_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PastaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('already_ordered', models.BooleanField(default=False)),
                ('pizza_size', models.CharField(choices=[('sm', 'small'), ('lg', 'large')], max_length=2)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=4)),
                ('add_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('price_sm_0', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('price_sm_1', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('price_sm_2', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('price_sm_3', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('price_sm_4', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('price_lg_0', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('price_lg_1', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('price_lg_2', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('price_lg_3', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('price_lg_4', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('already_ordered', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=4)),
                ('plattersize', models.CharField(choices=[('small', 'small'), ('large', 'large')], default='small', max_length=60)),
                ('add_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlatterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='ProperOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_timestamp', models.DateTimeField(auto_now_add=True)),
                ('order_price', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('order_done', models.BooleanField(default=False)),
                ('order_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('already_ordered', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=4)),
                ('add_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('in_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salads', to='orders.ProperOrder')),
            ],
        ),
        migrations.CreateModel(
            name='SaladType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('already_ordered', models.BooleanField(default=False)),
                ('additional_cheese', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=4)),
                ('subsize', models.CharField(choices=[('small', 'small'), ('large', 'large')], default='small', max_length=60)),
                ('add_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('in_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='orders.ProperOrder')),
            ],
        ),
        migrations.CreateModel(
            name='SubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('small_price', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('only_big_size', models.BooleanField(default=False, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='sub',
            name='subtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.SubType'),
        ),
        migrations.AddField(
            model_name='salad',
            name='saladtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.SaladType'),
        ),
        migrations.AddField(
            model_name='platter',
            name='in_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='platters', to='orders.ProperOrder'),
        ),
        migrations.AddField(
            model_name='platter',
            name='plattertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.PlatterType'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='in_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='orders.ProperOrder'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizzatype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.PizzaType'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='orders.PizzaTopping'),
        ),
        migrations.AddField(
            model_name='pasta',
            name='in_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pastas', to='orders.ProperOrder'),
        ),
        migrations.AddField(
            model_name='pasta',
            name='pastatype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.PastaType'),
        ),
    ]
