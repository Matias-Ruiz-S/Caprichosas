# Generated by Django 4.2.1 on 2023-05-20 19:28

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0005_remove_ingrediente_nomproducto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='nombre de la categoria')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
                ('is_activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='nombre')),
                ('ubicacion', models.CharField(max_length=50, verbose_name='ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='tipoPago',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Barcode')),
                ('Tnombre', models.CharField(max_length=50, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('Barcode', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Barcode')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
                ('precio', models.IntegerField(verbose_name='precio')),
                ('stock', models.IntegerField(verbose_name='stock')),
                ('descripcion', models.TextField(max_length=600, verbose_name='descripcion')),
                ('is_activo', models.BooleanField(default=True)),
                ('destacado', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenPedido',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('fecha', models.CharField(max_length=50, verbose_name='apellido')),
                ('nomCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('tipoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipopago')),
            ],
        ),
        migrations.CreateModel(
            name='ListaOrdenPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ordenpedido')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='IdIngrediente')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('nomProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('fecha', models.CharField(max_length=50, verbose_name='fecha')),
                ('descripcion', models.CharField(max_length=150, verbose_name='descripcion')),
                ('id_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ordenpedido')),
            ],
        ),
    ]
