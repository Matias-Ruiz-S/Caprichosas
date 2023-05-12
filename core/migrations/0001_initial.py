# Generated by Django 4.2.1 on 2023-05-11 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='nombre de la categoria')),
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
                ('precio', models.IntegerField(verbose_name='precio')),
                ('stock', models.IntegerField(verbose_name='stock')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenPedido',
            fields=[
                ('id', models.IntegerField(max_length=50, primary_key=True, serialize=False, verbose_name='id')),
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
            name='Boleta',
            fields=[
                ('id', models.IntegerField(max_length=50, primary_key=True, serialize=False, verbose_name='id')),
                ('fecha', models.CharField(max_length=50, verbose_name='fecha')),
                ('descripcion', models.CharField(max_length=150, verbose_name='descripcion')),
                ('id_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ordenpedido')),
            ],
        ),
    ]
