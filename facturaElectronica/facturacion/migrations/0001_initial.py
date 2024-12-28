# Generated by Django 5.0.1 on 2024-12-18 15:28

import django.core.validators
import facturacion.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apendice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo', models.CharField(max_length=25, verbose_name='Nombre del campo')),
                ('etiqueta', models.TextField(max_length=50, verbose_name='Descripccion')),
                ('valor', models.CharField(max_length=150, verbose_name='Valor/Dato')),
            ],
            options={
                'verbose_name_plural': 'Apendices',
            },
        ),
        migrations.CreateModel(
            name='ComprobanteDonacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoEstblacimiento', models.CharField(choices=[('01', 'Sucursal/Agencia'), ('02', 'Casa Matriz'), ('04', 'Bodega'), ('07', 'Predio y/o patio'), ('20', 'Otro')], max_length=25, verbose_name='Tipo de Establecimiento')),
                ('codDomiciliado', models.CharField(choices=[('1', 'Domiciliado'), ('2', 'No Domiciliado')], max_length=25, verbose_name='Domicilio Fiscal')),
                ('valorTotal', models.DecimalField(decimal_places=2, max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Total de la donacion')),
                ('totalLetras', models.CharField(max_length=200, verbose_name='Total en letras')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('fechaTransmicion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Transmicion')),
                ('transmitido', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Comprobantes de Donaciones',
            },
        ),
        migrations.CreateModel(
            name='CuerpoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numItem', models.IntegerField(help_text='N° ítem, debe estar entre 1 y 2000', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2000)], verbose_name='N° item')),
                ('tipoDonacion', models.CharField(choices=[('1', 'Efectivo'), ('2', 'Bien'), ('3', 'Servicio')], max_length=20, verbose_name='Tipo de donacion')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Cantidad')),
                ('codigo', models.CharField(blank=True, max_length=25, null=True, verbose_name='Codigo')),
                ('descripccion', models.CharField(max_length=1000, verbose_name='Descripccion')),
                ('depreciacion', models.DecimalField(decimal_places=2, max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Depreciacion')),
                ('valorUni', models.DecimalField(decimal_places=2, max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Valor Unitario')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Valor Donado')),
            ],
            options={
                'verbose_name_plural': 'Cuerpos del documento',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(code='invalid_code', message='El código debe ser un número del 01 al 14.', regex='^0[1-9]|1[0-4]$')], verbose_name='Codigo del departamento')),
                ('valor', models.CharField(max_length=100, verbose_name='Nombre del departamento')),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complementoDireccion', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Direccion complemento')),
            ],
            options={
                'verbose_name_plural': 'Direcciones',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numItem', models.IntegerField(help_text='N° ítem, debe estar entre 1 y 2000', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2000)], verbose_name='N° item')),
                ('tipoItem', models.CharField(choices=[('1', 'Bienes'), ('2', 'Servicios'), ('3', 'Ambos(Bienes y Servicios)'), ('4', 'Otros Tributos por Item')], max_length=6, verbose_name='Tipo de Item')),
                ('numeroDocumento', models.CharField(blank=True, max_length=36, null=True, verbose_name='Numero de Documento Relacionado')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(1e-08), django.core.validators.MaxValueValidator(100000000000.0)])),
                ('codigo', models.CharField(blank=True, max_length=25, null=True, verbose_name='Codigo')),
                ('codTributo', models.CharField(blank=True, choices=[(None, 'Ninguno'), ('A8', 'Impuesto Especial al Combustible (0%, 0.5%, 1%)'), ('57', 'Impuesto Industria de Cemento'), ('90', 'Impuesto Especial a la Primera Matricula'), ('D4', 'Otros Impuestos Casos Especiales'), ('D5', 'Otras Tasas Casos Especiales'), ('A6', 'Impuesto AD-Valorem, Armas de Fuego, Municiones Explosivas y Articulos Similares')], max_length=2, null=True, verbose_name='Tributo sujeto a cálculo de IVA')),
                ('descripccion', models.CharField(max_length=1000, verbose_name='Descripccion')),
                ('precioUni', models.DecimalField(decimal_places=2, help_text='Precio Unitario debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Precio Unitario')),
                ('montoDescu', models.DecimalField(decimal_places=2, help_text='Descuento, Bonificación, Rebajas por ítem. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Descuento, Bonificacion, Rebajas por Item')),
                ('ventaNoSuj', models.DecimalField(decimal_places=2, help_text='Ventas no Sujetas. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Ventas no Sujetas')),
                ('ventaExenta', models.DecimalField(decimal_places=2, help_text='Ventas Exentas. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Ventas Exentas')),
                ('ventaGrabada', models.DecimalField(decimal_places=2, help_text='Ventas Gravadas. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Ventas Gravadas')),
                ('tributos', models.CharField(blank=True, max_length=2, null=True, verbose_name='Codigo del Tributo')),
                ('psv', models.DecimalField(decimal_places=2, help_text='Precio Sujerido de Venta. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Precio Sujerido de Venta')),
                ('noGravado', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(-100000000000.0), django.core.validators.MaxValueValidator(100000000000.0)], verbose_name='Cargos/Abonos que no afectan la base imponible')),
                ('ivaItem', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='IVA por Item')),
            ],
            options={
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='DocumentoRelacionado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDocumento', models.CharField(choices=[('04', 'Nota de remision'), ('08', 'Comprobante de liquidacion'), ('09', 'Documento contable de liquidacion')], max_length=20, verbose_name='Tipo de Documento')),
                ('tipoGeneracion', models.CharField(choices=[('1', 'Fisico'), ('2', 'Electronico')], max_length=20, verbose_name='Tipo de Generacion')),
                ('numeroDocumento', models.CharField(max_length=36, verbose_name='Numero de Documento Relacionados')),
                ('fechaEmision', models.DateField(verbose_name='Fecha de Generacion del documento Relacionados')),
            ],
            options={
                'verbose_name_plural': 'Documentos Relacionados',
            },
        ),
        migrations.CreateModel(
            name='Extencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombEntrega', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre del responsable que Genera el DTE')),
                ('docuEntrega', models.CharField(blank=True, max_length=25, null=True, verbose_name='Documento de identificación de quien genera el DTE')),
                ('nombRecibe', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre del responsable de la operación por parte del receptor')),
                ('docuRecibe', models.CharField(blank=True, max_length=25, null=True, verbose_name='Documento de identificación del responsable de la operación por parte del receptor')),
                ('observaciones', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Observaciones')),
                ('placaVehiculo', models.CharField(blank=True, max_length=10, null=True, verbose_name='Placa de vehículo')),
            ],
            options={
                'verbose_name_plural': 'Extenciones',
            },
        ),
        migrations.CreateModel(
            name='FacturaElectronica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_factura_electronica', models.BooleanField(default=True, verbose_name='¿Es Factura Electrónica?')),
                ('totalNoSuj', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Total de Operaciones no sujetas')),
                ('totalExenta', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Total de Operaciones exentas')),
                ('totalGravada', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Total de Operaciones Gravadas')),
                ('subTotalVentas', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Suma de operaciones sin impuestos')),
                ('descuNoSuj', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Monto global de Descuento, Bonificación, Rebajas y otros a ventas no sujetas')),
                ('descuExenta', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Monto global de Descuento, Bonificación, Rebajas y otros a ventas exentas')),
                ('descuGravada', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Monto global de Descuento, Bonificación, Rebajas y otros a ventas gravadas')),
                ('porcentajeDescuento', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Porcentaje del monto global de Descuento, Bonificación, Rebajas y otros')),
                ('totalDescu', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Total del monto de Descuento, Bonificación, Rebajas')),
                ('subTotal', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Sub-Total')),
                ('ivaPerci1', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='IVA Percibido')),
                ('ivaRete1', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='IVA Retenido')),
                ('reteRenta', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Retención Renta')),
                ('montoTotalOperacion', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Monto Total de la Operación')),
                ('totalNoGravado', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(-99999999999.99), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Total Cargos/Abonos que no afectan la base imponible')),
                ('totalPagar', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Total a Pagar')),
                ('totalLetras', models.CharField(max_length=200, verbose_name='Valor en Letras')),
                ('totalIva', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='IVA 13%')),
                ('saldoFavor', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Saldo a Favor')),
                ('condicionOperacion', models.CharField(choices=[('1', 'Contado'), ('2', 'A credito'), ('3', 'Otro')], max_length=25, verbose_name='Condicion de la Operacion')),
                ('numPagoElectronico', models.CharField(blank=True, max_length=100, null=True, verbose_name='Número de pago Electrónico')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('fechaTransmicion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Transmicion')),
                ('transmitido', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Facturas Electronicas',
            },
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(code='invalid_codigo', message='El código debe ser 01-14 o 99.', regex='^(0[1-9]|1[0-4]|99)$')], verbose_name='Codigo')),
                ('valor', models.CharField(max_length=50, verbose_name='Valores')),
            ],
            options={
                'verbose_name_plural': 'Formas de pago',
            },
        ),
        migrations.CreateModel(
            name='Identificador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=10, verbose_name='Version')),
                ('ambiente', models.CharField(choices=[('00', 'Modo Prueba'), ('01', 'Modo Produccion')], max_length=20, verbose_name='Ambiente de destino')),
                ('numeroControl', models.CharField(default=facturacion.models.generateNumeroControl, editable=False, max_length=31, verbose_name='Numero de control')),
                ('codigoGeneracion', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('tipoModelo', models.CharField(choices=[('1', 'Modelo de Facturacion previo'), ('2', 'Modelo de Facturacion diferido')], max_length=50, verbose_name='Modelo de facturacion')),
                ('tipoOperacion', models.CharField(choices=[('1', 'Transmision normal'), ('2', 'Transmision por contingencia')], default='1', max_length=50, verbose_name='Tipo de Transmicion')),
                ('tipoContingencia', models.CharField(blank=True, choices=[('', 'Seleccione opcion'), ('1', 'No disponibilidad de sistema del MH'), ('2', 'No disponibilidad de sistema del emisor'), ('3', 'Falla en el suministro de servicio de Internet del Emisor'), ('4', 'Falla en el suministro de servicio de energia electrica del emisor que impida la transmision de los DTE'), ('5', 'Otro (debera digitar un maximo de 500 caracteres explicando el motivo)')], default='', max_length=50, null=True, verbose_name='Tipo de Contingencia')),
                ('motivoContin', models.CharField(blank=True, max_length=500, null=True, verbose_name='Motivo de Contingencia')),
                ('tipoMoneda', models.CharField(default='USD', help_text='Tipo de Moneda', max_length=30, verbose_name='Tipo de Moneda')),
            ],
            options={
                'verbose_name_plural': 'Identificaciones',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del medico que presta el servicio')),
                ('nit', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(code='invalid_nit', message='El nit debe tener exactamente 14 o 9 dígitos.', regex='^([0-9]{14}|[0-9]{9})$')], verbose_name='NIT del medico que presta el servicio')),
                ('docIdentificacion', models.CharField(blank=True, max_length=25, null=True, verbose_name='Documento de identificacion de medico no domiciliados')),
                ('tipoServicio', models.CharField(choices=[('1', 'Cirujia'), ('2', 'Operacion'), ('3', 'Tratamiento medico'), ('4', 'Cirujia instituto salvadoreño de Binestar Magisterial'), ('5', 'Operacion Instituto Salvadoreño de Binestar Magisterial'), ('6', 'Tratamiento medico Instituto Salvadoreño de Binestar Magisterial')], max_length=6, verbose_name='Codigo del Sevicio Realizado')),
            ],
            options={
                'verbose_name_plural': 'Medicos',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(code='invalid_code', message='El valor debe ser un número de exactamente dos dígitos.', regex='^^[0-9]{2}$')], verbose_name='Codigo del municipio')),
                ('valor', models.CharField(max_length=100, verbose_name='Nombre del municipio')),
            ],
            options={
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='OperacionesSujetoExcluido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numItem', models.IntegerField(help_text='N° ítem, debe estar entre 1 y 2000', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2000)], verbose_name='N° item')),
                ('tipoItem', models.CharField(choices=[('1', 'Bienes'), ('2', 'Servicios'), ('3', 'Ambos (Bienes y servicios)'), ('4', 'Otros tributos por item')], max_length=25, verbose_name='Tipo de item')),
                ('codigo', models.CharField(blank=True, max_length=25, null=True, verbose_name='Codigo')),
                ('cantidad', models.DecimalField(decimal_places=2, help_text='Cantidad debe ser mayor que 0, menor que 100000000000 y múltiplo de 0.00000001', max_digits=22, validators=[facturacion.models.validate_exclusive_min, facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Cantidad')),
                ('montoDescu', models.DecimalField(decimal_places=2, help_text='Descuento, Bonificación, Rebajas por ítem. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Monto')),
                ('compra', models.DecimalField(decimal_places=2, help_text='Ventas. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Ventas')),
                ('retencion', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Retencion')),
                ('descripccion', models.TextField(max_length=1000, verbose_name='Descripccion')),
                ('precioUni', models.DecimalField(decimal_places=2, help_text='Precio Unitario debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Precio Unitario')),
            ],
            options={
                'verbose_name_plural': 'Operaciones',
            },
        ),
        migrations.CreateModel(
            name='OtroDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codDocAsociado', models.IntegerField(max_length=4, verbose_name='Documento Asociado')),
                ('descDocumento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Identificacion del documento asociado')),
                ('detalleDocumento', models.CharField(blank=True, max_length=300, null=True, verbose_name='Detalle de documento asociado')),
            ],
            options={
                'verbose_name_plural': 'Otros Documentos',
            },
        ),
        migrations.CreateModel(
            name='OtroDocumentoAsociado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codDocAsociado', models.CharField(choices=[('1', 'Emisor'), ('2', 'Receptor'), ('3', 'Medico'), ('4', 'Transporte')], max_length=25, verbose_name='Documento asociado')),
                ('descDocumento', models.CharField(max_length=100, verbose_name='Identificacion del documento asociado')),
                ('detalleDocumento', models.CharField(max_length=300, verbose_name='Descripccion de documento asociado')),
            ],
            options={
                'verbose_name_plural': 'Otros documentos asociados',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montoPago', models.DecimalField(decimal_places=2, help_text='Monto por forma de pago. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01.', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of2], verbose_name='Monto por forma de pago')),
                ('referencia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Referencia de la modalidad de pagos')),
                ('plazo', models.CharField(blank=True, choices=[('', 'Seleccione una opccion'), ('01', 'Dias'), ('02', 'Meses'), ('03', 'Años')], default='', max_length=20, null=True, verbose_name='Plazo')),
                ('periodo', models.IntegerField(blank=True, null=True, verbose_name='Periodo de plazo')),
            ],
            options={
                'verbose_name_plural': 'Pagos',
            },
        ),
        migrations.CreateModel(
            name='PagoDonacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=2, null=True, verbose_name='Codigo de Forma de pago')),
                ('montoPago', models.DecimalField(decimal_places=2, max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of], verbose_name='Monto por Forma de pago')),
                ('referencia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Referencia de la modalidad de pago')),
            ],
            options={
                'verbose_name_plural': 'Pagos de donacion',
            },
        ),
        migrations.CreateModel(
            name='PagoFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(message='El código debe seguir el patrón: 01-09, 10-14, o 99.', regex='^(0[1-9]|1[0-4]|99)$')])),
                ('montoPago', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)])),
                ('referencia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Referencia de modalidad de pago')),
                ('plazo', models.CharField(blank=True, max_length=2, null=True, validators=[django.core.validators.RegexValidator(message='El plazo debe seguir el patrón: 01-03.', regex='^0[1-3]$')], verbose_name='Plazo')),
                ('periodo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Período de plazo')),
            ],
            options={
                'verbose_name_plural': 'Pagos de Facturas',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5, verbose_name='Codigo del pais')),
                ('valor', models.CharField(max_length=100, verbose_name='Nombre del pais')),
            ],
            options={
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Receptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('13', 'DUI'), ('36', 'NIT'), ('37', 'Otro'), ('03', 'Pasaporte'), ('02', 'Carnet de Residente')], max_length=25, verbose_name='Tipo de Documento')),
                ('homologado', models.CharField(choices=[('DUI', 'Documento Homologado'), ('NIT', 'Documento No Homologado')], max_length=30, verbose_name='Homologacion')),
                ('numero', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Numero del documento sin guion')),
                ('nrc', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(code='invalid_nrc', message='El nrc debe tener entre 1 y 8 dígitos.', regex='^[0-9]{1,8}$')], verbose_name='NRC')),
                ('nombre', models.CharField(max_length=250, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Nombre, Denominacion o Razon Social del contribuyente')),
                ('cellphone', models.CharField(help_text='Colocar el número sin identificador de país, sin espacios y sin guion.', max_length=30, verbose_name='Telefono movil del usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electronico de el receptor')),
            ],
            options={
                'verbose_name_plural': 'Receptores',
            },
        ),
        migrations.CreateModel(
            name='ResponseHacienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('datosJson', models.JSONField()),
                ('status', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Responses',
            },
        ),
        migrations.CreateModel(
            name='SujetoExcluido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalCompra', models.DecimalField(decimal_places=2, help_text='Total de Operaciones. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of2], verbose_name='Total de operaciones')),
                ('descu', models.DecimalField(decimal_places=2, help_text='Monto global de Descuento, Bonificacion, Rebajas', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of2], verbose_name='Monto global de Descuento, Bonificacion, Rebajas')),
                ('totalDescu', models.DecimalField(decimal_places=2, help_text='Total del monto de Descuento, Bonificación, Rebajas.', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of2], verbose_name='Total del monto de Descuento, Bonificacion, Rebajas')),
                ('subTotal', models.DecimalField(decimal_places=2, help_text='Sub-Total. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of2], verbose_name='Subtotal')),
                ('retencionIVAMH', models.CharField(blank=True, choices=[('', 'Seleccione una opccion'), ('22', 'Retencion IVA 1%'), ('C4', 'Retencion IVA 13%'), ('C9', 'Otras retenciones IVA casos especiales')], default='', max_length=30, null=True, verbose_name='Retencion IVA MH')),
                ('ivaRete1', models.DecimalField(decimal_places=2, help_text='IVA Retenido. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of2], verbose_name='IVA Retenido')),
                ('reteRenta', models.DecimalField(decimal_places=2, help_text='Retención Renta. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of2], verbose_name='Rentencion de Renta')),
                ('totalPagar', models.DecimalField(decimal_places=2, help_text='Total a Pagar. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01', max_digits=22, validators=[django.core.validators.MinValueValidator(0), facturacion.models.validate_exclusive_max, facturacion.models.validate_multiple_of2], verbose_name='Total a Pagar')),
                ('totalLetras', models.CharField(max_length=200, verbose_name='Total en letras')),
                ('condicionOperacion', models.CharField(choices=[('1', 'Contado'), ('2', 'A credito'), ('3', 'Otro')], max_length=25, verbose_name='Condicion de la Operacion')),
                ('observaciones', models.TextField(verbose_name='Observaciones')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('fechaTransmicion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Transmicion')),
                ('transmitido', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Sujetos Excluidos',
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, verbose_name='Codigo')),
                ('valor', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name_plural': 'Tipos de Documentos',
            },
        ),
        migrations.CreateModel(
            name='Tributo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=2, verbose_name='Codigo')),
                ('descripcion', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripcion')),
                ('valor', models.CharField(max_length=150, verbose_name='Valores')),
            ],
            options={
                'verbose_name_plural': 'Tributos del resumen',
            },
        ),
        migrations.CreateModel(
            name='TributoResumen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999.99)], verbose_name='Valor del Tributo')),
            ],
            options={
                'verbose_name_plural': 'Tributos del resumen de Facturas Electronicas',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, verbose_name='Codigo')),
                ('valor', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name_plural': 'Unidades de medida',
            },
        ),
        migrations.CreateModel(
            name='VentaTercero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_nit', message='El nit debe tener exactamente 14 o 9 dígitos.', regex='^([0-9]{14}|[0-9]{9})$')], verbose_name='Numero de NIT sin guiones')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre, denominacion o razon social del Tercero')),
            ],
            options={
                'verbose_name_plural': 'Ventas a Terceros',
            },
        ),
    ]
