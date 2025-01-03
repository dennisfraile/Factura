from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def load_catalogs(sender, **kwargs):
    Departamento = apps.get_model('your_app_name', 'Departamento')
    Municipio = apps.get_model('your_app_name', 'Municipio')
    UnidadMedida = apps.get_model('', 'UnidadMedida')
    FormaPago = apps.get_model('your_app_name', 'FormaPago')
    TipoDocumento = apps.get_model('your_app_name', 'TipoDocumento')
    Tributo = apps.get_model('your_app_name', 'Tributo')
    TributoItem = apps.get_model('', 'TributoItem')

    # Datos de ejemplo para Departamentos
    departamentos_data = [
        {'codigo': '01', 'valor': 'Ahuachapan'},
        {'codigo': '02', 'valor': 'Santa Ana'},
        {'codigo': '03', 'valor': 'Sonsonate'},
        {'codigo': '04', 'valor': 'Chalatenango'},
        {'codigo': '05', 'valor': 'La Libertad'},
        {'codigo': '06', 'valor': 'San Salvador'},
        {'codigo': '07', 'valor': 'Cuscatlan'},
        {'codigo': '08', 'valor': 'La Paz'},
        {'codigo': '09', 'valor': 'Cabañas'},
        {'codigo': '10', 'valor': 'San Vicente'},
        {'codigo': '11', 'valor': 'Usulutan'},
        {'codigo': '12', 'valor': 'San Miguel'},
        {'codigo': '13', 'valor': 'Morazan'},
        {'codigo': '14', 'valor': 'La Union'}
    ]

    # Crear departamentos
    for departamento_data in departamentos_data:
        Departamento.objects.get_or_create(**departamento_data)

    # Datos de ejemplo para Municipios
    municipios_data = [
        {'codigo': '00', 'valor': 'Otro Pais', 'departamento_codigo': '00'},
        {'codigo': '01', 'valor': 'AHUACHAPAN', 'departamento_codigo': '01'},
        {'codigo': '02', 'valor': 'APANECA', 'departamento_codigo': '01'},
        {'codigo': '03', 'valor': 'ATIQUIZAYA', 'departamento_codigo': '01'},
        {'codigo': '04', 'valor': 'CONCEPCCION DE ATACO', 'departamento_codigo': '01'},
        {'codigo': '05', 'valor': 'EL REFUGIO', 'departamento_codigo': '01'},
        {'codigo': '06', 'valor': 'GUAYMANGO', 'departamento_codigo': '01'},
        {'codigo': '07', 'valor': 'JUJUTLA', 'departamento_codigo': '01'},
        {'codigo': '08', 'valor': 'SAN FRANCISCO MENENDEZ', 'departamento_codigo': '01'},
        {'codigo': '09', 'valor': 'SAN LORENZO', 'departamento_codigo': '01'},
        {'codigo': '10', 'valor': 'SAN PEDRO PUXTLA', 'departamento_codigo': '01'},
        {'codigo': '11', 'valor': 'TACUBA', 'departamento_codigo': '01'},
        {'codigo': '12', 'valor': 'TURIN', 'departamento_codigo': '01'},
        {'codigo': '01', 'valor': 'CANDELARIA DE LA FRONTERA', 'departamento_codigo': '02'},
        {'codigo': '02', 'valor': 'COATEPEQUE', 'departamento_codigo': '02'},
        {'codigo': '03', 'valor': 'CHALCHUAPA', 'departamento_codigo': '02'},
        {'codigo': '04', 'valor': 'EL CONGO', 'departamento_codigo': '02'},
        {'codigo': '05', 'valor': 'EL PROVENIR', 'departamento_codigo': '02'},
        {'codigo': '06', 'valor': 'MASAHUAT', 'departamento_codigo': '02'},
        {'codigo': '07', 'valor': 'METAPAN', 'departamento_codigo': '02'},
        {'codigo': '08', 'valor': 'SAN ANTONIO PAJONAL', 'departamento_codigo': '02'},
        {'codigo': '09', 'valor': 'SAN SEBASTIAN SALITRILLO', 'departamento_codigo': '02'},
        {'codigo': '10', 'valor': 'SANTA ANA', 'departamento_codigo': '02'},
        {'codigo': '11', 'valor': 'STA ROSA GUACHI', 'departamento_codigo': '02'},
        {'codigo': '12', 'valor': 'STGO DE LA FORNTERA', 'departamento_codigo': '02'},
        {'codigo': '13', 'valor': 'TEXISTEPEQUE', 'departamento_codigo': '02'},
        {'codigo': '01', 'valor': 'ACAJUTLA', 'departamento_codigo': '03'},
        {'codigo': '02', 'valor': 'ARMENIA', 'departamento_codigo': '03'},
        {'codigo': '03', 'valor': 'CALUCO', 'departamento_codigo': '03'},
        {'codigo': '04', 'valor': 'CUISNAHUAT', 'departamento_codigo': '03'},
        {'codigo': '05', 'valor': 'STA ISHUATAN', 'departamento_codigo': '03'},
        {'codigo': '06', 'valor': 'IZALCO', 'departamento_codigo': '03'},
        {'codigo': '07', 'valor': 'JUAYUA', 'departamento_codigo': '03'},
        {'codigo': '08', 'valor': 'NAHUIZALCO', 'departamento_codigo': '03'},
        {'codigo': '09', 'valor': 'NAHULINGO', 'departamento_codigo': '03'},
        {'codigo': '10', 'valor': 'SALCOATITAN', 'departamento_codigo': '03'},
        {'codigo': '11', 'valor': 'SAN ANTONIO DEL MONTE', 'departamento_codigo': '03'},
        {'codigo': '12', 'valor': 'SAN JULIAN', 'departamento_codigo': '03'},
        {'codigo': '13', 'valor': 'STA C MASAHUAT', 'departamento_codigo': '03'},
        {'codigo': '14', 'valor': 'SANTO DOMINGO GUZMAN', 'departamento_codigo': '03'},
        {'codigo': '15', 'valor': 'SONSONATE', 'departamento_codigo': '03'},
        {'codigo': '16', 'valor': 'SONZACATE', 'departamento_codigo': '03'},
        {'codigo': '01', 'valor': 'AGUA CALIENTE', 'departamento_codigo': '04'},
        {'codigo': '02', 'valor': 'ARCATAO', 'departamento_codigo': '04'},
        {'codigo': '03', 'valor': 'AZACUALPA', 'departamento_codigo': '04'},
        {'codigo': '04', 'valor': 'CITALA', 'departamento_codigo': '04'},
        {'codigo': '05', 'valor': 'COMALAPA', 'departamento_codigo': '04'},
        {'codigo': '06', 'valor': 'CONCEPCCION QUEZALTEPEQUE', 'departamento_codigo': '04'},
        {'codigo': '07', 'valor': 'CHALATENANGO', 'departamento_codigo': '04'},
        {'codigo': '08', 'valor': 'DULCE NOMBRE DE MARIA', 'departamento_codigo': '04'},
        {'codigo': '09', 'valor': 'EL CARRIZAL', 'departamento_codigo': '04'},
        {'codigo': '10', 'valor': 'EL PARAISO', 'departamento_codigo': '04'},
        {'codigo': '11', 'valor': 'LA LAGUNA', 'departamento_codigo': '04'},
        {'codigo': '12', 'valor': 'LA PALMA', 'departamento_codigo': '04'},
        {'codigo': '13', 'valor': 'LA REINA', 'departamento_codigo': '04'},
        {'codigo': '14', 'valor': 'LAS VUELTAS', 'departamento_codigo': '04'},
        {'codigo': '15', 'valor': 'NOMBRE DE JESUS', 'departamento_codigo': '04'},
        {'codigo': '16', 'valor': 'NUEVA CONCEPCCION', 'departamento_codigo': '04'},
        {'codigo': '17', 'valor': 'NUEVA TRINIDAD', 'departamento_codigo': '04'},
        {'codigo': '18', 'valor': 'OJOS DE AGUA', 'departamento_codigo': '04'},
        {'codigo': '19', 'valor': 'POTONICO', 'departamento_codigo': '04'},
        {'codigo': '20', 'valor': 'SAN ANT LA CRUZ', 'departamento_codigo': '04'},
        {'codigo': '21', 'valor': 'SAN ANT RANCHOS', 'departamento_codigo': '04'},
        {'codigo': '22', 'valor': 'SAN FERNANDO', 'departamento_codigo': '04'},
        {'codigo': '23', 'valor': 'SAN FRANCISCO LEMPA', 'departamento_codigo': '04'},
        {'codigo': '24', 'valor': 'SAN FRANCISCO MORAZAN', 'departamento_codigo': '04'},
        {'codigo': '25', 'valor': 'SAN IGNACIO', 'departamento_codigo': '04'},
        {'codigo': '26', 'valor': 'SAN IGNACIO LABRADOR ', 'departamento_codigo': '04'},
        {'codigo': '27', 'valor': 'SAN JOSE CANCASQUE', 'departamento_codigo': '04'},
        {'codigo': '28', 'valor': 'SAN JOSE LAS FLORES', 'departamento_codigo': '04'},
        {'codigo': '29', 'valor': 'SAN LUIS CARMEN', 'departamento_codigo': '04'},
        {'codigo': '30', 'valor': 'SN MIG MERCEDES', 'departamento_codigo': '04'},
        {'codigo': '31', 'valor': 'SAN RAFAEL', 'departamento_codigo': '04'},
        {'codigo': '32', 'valor': 'SANTA RITA', 'departamento_codigo': '04'},
        {'codigo': '33', 'valor': 'TEJUTLA', 'departamento_codigo': '04'},
        {'codigo': '01', 'valor': 'ANTIGUO CUSCATLAN', 'departamento_codigo': '05'},
        {'codigo': '02', 'valor': 'CIUDAD ARCE', 'departamento_codigo': '05'},
        {'codigo': '03', 'valor': 'COLON', 'departamento_codigo': '05'},
        {'codigo': '04', 'valor': 'COMASAGUA', 'departamento_codigo': '05'},
        {'codigo': '05', 'valor': 'CHILTIUPAN', 'departamento_codigo': '05'},
        {'codigo': '06', 'valor': 'HUIZUCAR', 'departamento_codigo': '05'},
        {'codigo': '07', 'valor': 'JAYAQUE', 'departamento_codigo': '05'},
        {'codigo': '08', 'valor': 'JICALAPA', 'departamento_codigo': '05'},
        {'codigo': '09', 'valor': 'LA LIBERTAD', 'departamento_codigo': '05'},
        {'codigo': '10', 'valor': 'NUEVO CUSCATLAN', 'departamento_codigo': '05'},
        {'codigo': '11', 'valor': 'SANTA TECLA', 'departamento_codigo': '05'},
        {'codigo': '12', 'valor': 'QUEZALTEPEQUE', 'departamento_codigo': '05'},
        {'codigo': '13', 'valor': 'SACACOYO', 'departamento_codigo': '05'},
        {'codigo': '14', 'valor': 'SAN JOSE VILLANUEVA', 'departamento_codigo': '05'},
        {'codigo': '15', 'valor': 'SAN JUAN OPICO', 'departamento_codigo': '05'},
        {'codigo': '16', 'valor': 'SAN MATIAS', 'departamento_codigo': '05'},
        {'codigo': '17', 'valor': 'SAN PABLO TACACHICO', 'departamento_codigo': '05'},
        {'codigo': '18', 'valor': 'TAMANIQUE', 'departamento_codigo': '05'},
        {'codigo': '19', 'valor': 'TALNIQUE', 'departamento_codigo': '05'},
        {'codigo': '20', 'valor': 'TEOTEPEQUE', 'departamento_codigo': '05'},
        {'codigo': '21', 'valor': 'TEPECOYO', 'departamento_codigo': '05'},
        {'codigo': '22', 'valor': 'ZARAGOZA', 'departamento_codigo': '05'},
        {'codigo': '01', 'valor': 'AGUILARES', 'departamento_codigo': '06'},
        {'codigo': '02', 'valor': 'APOPA', 'departamento_codigo': '06'},
        {'codigo': '03', 'valor': 'AYUTUXTEPEQUE', 'departamento_codigo': '06'},
        {'codigo': '04', 'valor': 'CUSCATANCINGO', 'departamento_codigo': '06'},
        {'codigo': '05', 'valor': 'EL PAISNAL', 'departamento_codigo': '06'},
        {'codigo': '06', 'valor': 'GUAZAPA', 'departamento_codigo': '06'},
        {'codigo': '07', 'valor': 'ILOPANGO', 'departamento_codigo': '06'},
        {'codigo': '08', 'valor': 'MEJICANOS', 'departamento_codigo': '06'},
        {'codigo': '09', 'valor': 'NEJAPA', 'departamento_codigo': '06'},
        {'codigo': '10', 'valor': 'PANCHIMALCO', 'departamento_codigo': '06'},
        {'codigo': '11', 'valor': 'ROSARIO DE MORA', 'departamento_codigo': '06'},
        {'codigo': '12', 'valor': 'SAN MARCOS', 'departamento_codigo': '06'},
        {'codigo': '13', 'valor': 'SAN MARTIN', 'departamento_codigo': '06'},
        {'codigo': '14', 'valor': 'SAN SALVADOR', 'departamento_codigo': '06'},
        {'codigo': '15', 'valor': 'SANTIAGO TEXACUANGOS', 'departamento_codigo': '06'},
        {'codigo': '16', 'valor': 'SANTO TOMAS', 'departamento_codigo': '06'},
        {'codigo': '17', 'valor': 'SOYAPANGO', 'departamento_codigo': '06'},
        {'codigo': '18', 'valor': 'TONACATEPEQUE', 'departamento_codigo': '06'},
        {'codigo': '19', 'valor': 'CIUDAD DELGADO', 'departamento_codigo': '06'},
        {'codigo': '01', 'valor': 'CANDELARIA', 'departamento_codigo': '07'},
        {'codigo': '02', 'valor': 'COJUTEPEQUE', 'departamento_codigo': '07'},
        {'codigo': '03', 'valor': 'EL CARMEN', 'departamento_codigo': '07'},
        {'codigo': '04', 'valor': 'EL ROSARIO', 'departamento_codigo': '07'},
        {'codigo': '05', 'valor': 'MONTE SAN JUAN', 'departamento_codigo': '07'},
        {'codigo': '06', 'valor': 'ORAT CONCEPCION', 'departamento_codigo': '07'},
        {'codigo': '07', 'valor': 'SAN B PEULAPIA', 'departamento_codigo': '07'},
        {'codigo': '08', 'valor': 'SAN CRISTOBAL', 'departamento_codigo': '07'},
        {'codigo': '09', 'valor': 'SAN J GUAYABAL', 'departamento_codigo': '07'},
        {'codigo': '10', 'valor': 'SAN P PERULAPAN', 'departamento_codigo': '07'},
        {'codigo': '11', 'valor': 'SAN RAFAEL CEDROS', 'departamento_codigo': '07'},
        {'codigo': '12', 'valor': 'SAN RAMON', 'departamento_codigo': '07'},
        {'codigo': '13', 'valor': 'STA C ANALQUITO', 'departamento_codigo': '07'},
        {'codigo': '14', 'valor': 'STA C MICHAPA', 'departamento_codigo': '07'},
        {'codigo': '15', 'valor': 'SUCHITOTO', 'departamento_codigo': '07'},
        {'codigo': '16', 'valor': 'TENANCINGO', 'departamento_codigo': '07'},
        {'codigo': '01', 'valor': 'CUYULTITAN', 'departamento_codigo': '08'},
        {'codigo': '02', 'valor': 'EL ROSARIO', 'departamento_codigo': '08'},
        {'codigo': '03', 'valor': 'JERUSALEN', 'departamento_codigo': '08'},
        {'codigo': '04', 'valor': 'MERCED LA CEIBA', 'departamento_codigo': '08'},
        {'codigo': '05', 'valor': 'OLOCUILTA', 'departamento_codigo': '08'},
        {'codigo': '06', 'valor': 'PARAISO OSORIO', 'departamento_codigo': '08'},
        {'codigo': '07', 'valor': 'SN ANT MASAHUAT', 'departamento_codigo': '08'},
        {'codigo': '08', 'valor': 'SAN EMIGDIO', 'departamento_codigo': '08'},
        {'codigo': '09', 'valor': 'SN FCO CHINAMECA', 'departamento_codigo': '08'},
        {'codigo': '10', 'valor': 'SAN JUAN NONUALCO', 'departamento_codigo': '08'},
        {'codigo': '11', 'valor': 'SAN JUAN TALPA', 'departamento_codigo': '08'},
        {'codigo': '12', 'valor': 'SAN JUAN TEPEZONTES', 'departamento_codigo': '08'},
        {'codigo': '13', 'valor': 'SAN LUIS TALPA', 'departamento_codigo': '08'},
        {'codigo': '14', 'valor': 'SAN MIGUEL TEPEZONTES', 'departamento_codigo': '08'},
        {'codigo': '15', 'valor': 'SAN PEDRO MASAHUAT', 'departamento_codigo': '08'},
        {'codigo': '16', 'valor': 'SAN PEDRO NONUALCO', 'departamento_codigo': '08'},
        {'codigo': '17', 'valor': 'SAN RAFAEL OBRAJUELO', 'departamento_codigo': '08'},
        {'codigo': '18', 'valor': 'SANTA MARIA OSTUMA', 'departamento_codigo': '08'},
        {'codigo': '19', 'valor': 'SANTIAGO NONUALCO', 'departamento_codigo': '08'},
        {'codigo': '20', 'valor': 'TAPALHUACA', 'departamento_codigo': '08'},
        {'codigo': '21', 'valor': 'ZACATECOLUCA', 'departamento_codigo': '08'},
        {'codigo': '22', 'valor': 'SAN LUIS LA HERRADURA', 'departamento_codigo': '08'},
        {'codigo': '01', 'valor': 'CINQUERA', 'departamento_codigo': '09'},
        {'codigo': '02', 'valor': 'GUACOTECTI', 'departamento_codigo': '09'},
        {'codigo': '03', 'valor': 'ILOBASCO', 'departamento_codigo': '09'},
        {'codigo': '04', 'valor': 'JUTIAPA', 'departamento_codigo': '09'},
        {'codigo': '05', 'valor': 'SAN ISIDRO', 'departamento_codigo': '09'},
        {'codigo': '06', 'valor': 'SENSUNTEPEQUE', 'departamento_codigo': '09'},
        {'codigo': '07', 'valor': 'TEJUTEPEQUE', 'departamento_codigo': '09'},
        {'codigo': '08', 'valor': 'VICTORIA', 'departamento_codigo': '09'},
        {'codigo': '09', 'valor': 'DOLORES', 'departamento_codigo': '09'},
        {'codigo': '01', 'valor': 'APASTEPEQUE', 'departamento_codigo': '10'},
        {'codigo': '02', 'valor': 'GUADALUPE', 'departamento_codigo': '10'},
        {'codigo': '03', 'valor': 'SAN CAY ISTEPEQ', 'departamento_codigo': '10'},
        {'codigo': '04', 'valor': 'SANTA CLARA', 'departamento_codigo': '10'},
        {'codigo': '05', 'valor': 'SANTO DOMINGO', 'departamento_codigo': '10'},
        {'codigo': '06', 'valor': 'SN EST CATARINA', 'departamento_codigo': '10'},
        {'codigo': '07', 'valor': 'SAN ILDEFONSO', 'departamento_codigo': '10'},
        {'codigo': '08', 'valor': 'SAN LORENZO', 'departamento_codigo': '10'},
        {'codigo': '09', 'valor': 'SAN SEBASTIAN', 'departamento_codigo': '10'},
        {'codigo': '10', 'valor': 'SAN VICENTE', 'departamento_codigo': '10'},
        {'codigo': '11', 'valor': 'TECOLUCA', 'departamento_codigo': '10'},
        {'codigo': '12', 'valor': 'TEPETITAN', 'departamento_codigo': '10'},
        {'codigo': '13', 'valor': 'VERAPAZ', 'departamento_codigo': '10'},
        {'codigo': '01', 'valor': 'ALEGRIA', 'departamento_codigo': '11'},
        {'codigo': '02', 'valor': 'BERLIN', 'departamento_codigo': '11'},
        {'codigo': '03', 'valor': 'CALIFORNIA', 'departamento_codigo': '11'},
        {'codigo': '04', 'valor': 'CONCEP BATRES', 'departamento_codigo': '11'},
        {'codigo': '05', 'valor': 'EL TRIUNFO', 'departamento_codigo': '11'},
        {'codigo': '06', 'valor': 'EREGUAYQUIN', 'departamento_codigo': '11'},
        {'codigo': '07', 'valor': 'ESTANZUELAS', 'departamento_codigo': '11'},
        {'codigo': '08', 'valor': 'JIQUILISCO', 'departamento_codigo': '11'},
        {'codigo': '09', 'valor': 'JUCUAPA', 'departamento_codigo': '11'},
        {'codigo': '10', 'valor': 'JUCUARAN', 'departamento_codigo': '11'},
        {'codigo': '11', 'valor': 'MERCEDES HUMAÑA', 'departamento_codigo': '11'},
        {'codigo': '12', 'valor': 'NUEVA GRANADA', 'departamento_codigo': '11'},
        {'codigo': '13', 'valor': 'OZATLAN', 'departamento_codigo': '11'},
        {'codigo': '14', 'valor': 'PUERTO EL TRIUNFO', 'departamento_codigo': '11'},
        {'codigo': '15', 'valor': 'SAN AGUSTIN', 'departamento_codigo': '11'},
        {'codigo': '16', 'valor': 'SAN BUENAVENTURA', 'departamento_codigo': '11'},
        {'codigo': '17', 'valor': 'SAN DIONISIO', 'departamento_codigo': '11'},
        {'codigo': '18', 'valor': 'SANTA ELENA', 'departamento_codigo': '11'},
        {'codigo': '19', 'valor': 'SAN FRANCISCO JAVIER', 'departamento_codigo': '11'},
        {'codigo': '20', 'valor': 'SANTA MARIA', 'departamento_codigo': '11'},
        {'codigo': '21', 'valor': 'SANTIAGO DE MARIA', 'departamento_codigo': '11'},
        {'codigo': '22', 'valor': 'TECAPAN', 'departamento_codigo': '11'},
        {'codigo': '23', 'valor': 'USULUTAN', 'departamento_codigo': '11'},
        {'codigo': '01', 'valor': 'CAROLINA', 'departamento_codigo': '12'},
        {'codigo': '02', 'valor': 'CIUDAD BARRIOS', 'departamento_codigo': '12'},
        {'codigo': '03', 'valor': 'COMACARAN', 'departamento_codigo': '12'},
        {'codigo': '04', 'valor': 'CHAPELTIQUE', 'departamento_codigo': '12'},
        {'codigo': '05', 'valor': 'CHINAMECA', 'departamento_codigo': '12'},
        {'codigo': '06', 'valor': 'CHIRILAGUA', 'departamento_codigo': '12'},
        {'codigo': '07', 'valor': 'EL TRANSITO', 'departamento_codigo': '12'},
        {'codigo': '08', 'valor': 'LOLOTIQUE', 'departamento_codigo': '12'},
        {'codigo': '09', 'valor': 'MONCAGUA', 'departamento_codigo': '12'},
        {'codigo': '10', 'valor': 'NUEVA GUADALUPE', 'departamento_codigo': '12'},
        {'codigo': '11', 'valor': 'NUEVO EDEN SAN JUAN', 'departamento_codigo': '12'},
        {'codigo': '12', 'valor': 'QUELEPA', 'departamento_codigo': '12'},
        {'codigo': '13', 'valor': 'SAN ANTONIO DE MOSCO', 'departamento_codigo': '12'},
        {'codigo': '14', 'valor': 'SAN GERARDO', 'departamento_codigo': '12'},
        {'codigo': '15', 'valor': 'SAN JORGE', 'departamento_codigo': '12'},
        {'codigo': '16', 'valor': 'SAN LUIS REINA', 'departamento_codigo': '12'},
        {'codigo': '17', 'valor': 'SAN MIGUEL', 'departamento_codigo': '12'},
        {'codigo': '18', 'valor': 'SAN RAFAEL ORIENTE', 'departamento_codigo': '12'},
        {'codigo': '19', 'valor': 'SESORI', 'departamento_codigo': '12'},
        {'codigo': '20', 'valor': 'ULUAZAPA', 'departamento_codigo': '12'},
        {'codigo': '01', 'valor': 'ARAMBALA', 'departamento_codigo': '13'},
        {'codigo': '02', 'valor': 'CACAOPERA', 'departamento_codigo': '13'},
        {'codigo': '03', 'valor': 'CORINTO', 'departamento_codigo': '13'},
        {'codigo': '04', 'valor': 'CHILANGA', 'departamento_codigo': '13'},
        {'codigo': '05', 'valor': 'DELIC DE CONCEP', 'departamento_codigo': '13'},
        {'codigo': '06', 'valor': 'EL DIVISADERO', 'departamento_codigo': '13'},
        {'codigo': '07', 'valor': 'EL ROSARIO', 'departamento_codigo': '13'},
        {'codigo': '08', 'valor': 'GUALOCOCTI', 'departamento_codigo': '13'},
        {'codigo': '09', 'valor': 'GUATAJIAGUA', 'departamento_codigo': '13'},
        {'codigo': '10', 'valor': 'JOATECA', 'departamento_codigo': '13'},
        {'codigo': '11', 'valor': 'JOCOAITIQUIE', 'departamento_codigo': '13'},
        {'codigo': '12', 'valor': 'JOCORO', 'departamento_codigo': '13'},
        {'codigo': '13', 'valor': 'LOLOTIQUILLO', 'departamento_codigo': '13'},
        {'codigo': '14', 'valor': 'MEANGUERA', 'departamento_codigo': '13'},
        {'codigo': '15', 'valor': 'OSICALA', 'departamento_codigo': '13'},
        {'codigo': '16', 'valor': 'PERQUIN', 'departamento_codigo': '13'},
        {'codigo': '17', 'valor': 'SAN CARLOS', 'departamento_codigo': '13'},
        {'codigo': '18', 'valor': 'SAN FERNANDO', 'departamento_codigo': '13'},
        {'codigo': '19', 'valor': 'SAN FRANCISCO GOTERA', 'departamento_codigo': '13'},
        {'codigo': '20', 'valor': 'SAN ISIDRO', 'departamento_codigo': '13'},
        {'codigo': '21', 'valor': 'SAN SIMON', 'departamento_codigo': '13'},
        {'codigo': '22', 'valor': 'SENSEMBRA', 'departamento_codigo': '13'},
        {'codigo': '23', 'valor': 'SOCIEDAD', 'departamento_codigo': '13'},
        {'codigo': '24', 'valor': 'TOROLA', 'departamento_codigo': '13'},
        {'codigo': '25', 'valor': 'YAMABAL', 'departamento_codigo': '13'},
        {'codigo': '26', 'valor': 'YOLOAIQUIN', 'departamento_codigo': '13'},
        {'codigo': '01', 'valor': 'ANAMOROS', 'departamento_codigo': '14'},
        {'codigo': '02', 'valor': 'BOLIVAR', 'departamento_codigo': '14'},
        {'codigo': '03', 'valor': 'CONCEP DE ORIENTE', 'departamento_codigo': '14'},
        {'codigo': '04', 'valor': 'CONCHAGUA', 'departamento_codigo': '14'},
        {'codigo': '05', 'valor': 'EL CARMEN', 'departamento_codigo': '14'},
        {'codigo': '06', 'valor': 'EL SAUCE', 'departamento_codigo': '14'},
        {'codigo': '07', 'valor': 'INTIPUCA', 'departamento_codigo': '14'},
        {'codigo': '08', 'valor': 'LA UNION', 'departamento_codigo': '14'},
        {'codigo': '09', 'valor': 'LISLIQUE', 'departamento_codigo': '14'},
        {'codigo': '10', 'valor': 'MEANGUERA DEL GOLFO', 'departamento_codigo': '14'},
        {'codigo': '11', 'valor': 'NUEVA ESPARTA', 'departamento_codigo': '14'},
        {'codigo': '12', 'valor': 'PASAQUINA', 'departamento_codigo': '14'},
        {'codigo': '13', 'valor': 'POLOROS', 'departamento_codigo': '14'},
        {'codigo': '14', 'valor': 'SAN ALEJO', 'departamento_codigo': '14'},
        {'codigo': '15', 'valor': 'SAN JOSE', 'departamento_codigo': '14'},
        {'codigo': '16', 'valor': 'SANTA ROSA DE LIMA', 'departamento_codigo': '14'},
        {'codigo': '17', 'valor': 'YAYANTIQUE', 'departamento_codigo': '14'},
        {'codigo': '18', 'valor': 'YUCUAIQUIN', 'departamento_codigo': '14'},
    ]

    # Crear municipios
    for municipio_data in municipios_data:
        departamento = Departamento.objects.get(codigo=municipio_data['departamento_codigo'])
        Municipio.objects.get_or_create(codigo=municipio_data['codigo'], valor=municipio_data['valor'], departamento=departamento)
    
    unidadesMedida_data = [
        { 'codigo': '01', 'valor': 'Metro'},
        { 'codigo': '02', 'valor': 'Yarda'},
        { 'codigo': '03', 'valor': 'Vara'},
        { 'codigo': '04', 'valor': 'Pie'},
        { 'codigo': '05', 'valor': 'Pulgada'},
        { 'codigo': '06', 'valor': 'Milimetro'},
        { 'codigo': '08', 'valor': 'Milla cuadrada'},
        { 'codigo': '09', 'valor': 'Kilometro cuadrado'},
        { 'codigo': '10', 'valor': 'Hectarea'},
        { 'codigo': '11', 'valor': 'Manzana'},
        { 'codigo': '12', 'valor': 'Acre'},
        { 'codigo': '13', 'valor': 'Metro cuadrado'},
        { 'codigo': '14', 'valor': 'Yarda cuadrada'},
        { 'codigo': '15', 'valor': 'Vara cuadrada'},
        { 'codigo': '16', 'valor': 'Pie cuadrado'},
        { 'codigo': '17', 'valor': 'Pulgada cuadrada'},
        { 'codigo': '18', 'valor': 'Metro cubico'},
        { 'codigo': '19', 'valor': 'Yarda cubica'},
        { 'codigo': '20', 'valor': 'Barril'},
        { 'codigo': '21', 'valor': 'Pie cubico'},
        { 'codigo': '22', 'valor': 'Galon'},
        { 'codigo': '23', 'valor': 'Litro'},
        { 'codigo': '24', 'valor': 'Botella'},
        { 'codigo': '25', 'valor': 'Pulgada cubica'},
        { 'codigo': '26', 'valor': 'Milimetro'},
        { 'codigo': '27', 'valor': 'Onza fluida'},
        { 'codigo': '29', 'valor': 'Tonelada metrica'},
        { 'codigo': '30', 'valor': 'Tonelada'},
        { 'codigo': '31', 'valor': 'Quintal metrico'},
        { 'codigo': '32', 'valor': 'Quintal'},
        { 'codigo': '33', 'valor': 'Arroba'},
        { 'codigo': '34', 'valor': 'Kilogramo'},
        { 'codigo': '35', 'valor': 'Libra troy'},
        { 'codigo': '36', 'valor': 'Libra'},
        { 'codigo': '37', 'valor': 'Onza troy'},
        { 'codigo': '38', 'valor': 'Onza'},
        { 'codigo': '39', 'valor': 'Gramo'},
        { 'codigo': '40', 'valor': 'Miligramo'},
        { 'codigo': '42', 'valor': 'Megawatt'},
        { 'codigo': '43', 'valor': 'Kilowatt'},
        { 'codigo': '44', 'valor': 'Watt'},
        { 'codigo': '45', 'valor': 'Megavoltio-amperio'},
        { 'codigo': '46', 'valor': 'Kilovoltio-amperio'},
        { 'codigo': '47', 'valor': 'Voltio-amperio'},
        { 'codigo': '49', 'valor': 'Gigawatt-hora'},
        { 'codigo': '50', 'valor': 'Megawatt-hora'},
        { 'codigo': '51', 'valor': 'Kilowatt-hora'},
        { 'codigo': '52', 'valor': 'Watt-hora'},
        { 'codigo': '53', 'valor': 'Kilovoltio'},
        { 'codigo': '54', 'valor': 'Voltio'},
        { 'codigo': '55', 'valor': 'Millar'},
        { 'codigo': '56', 'valor': 'Medio millar'},
        { 'codigo': '57', 'valor': 'Ciento'},
        { 'codigo': '58', 'valor': 'Docena'},
        { 'codigo': '59', 'valor': 'Unidad'},
        { 'codigo': '99', 'valor': 'Otra'}, 
    ]
    
    # Crear unidad de medida
    for unidadMedida_data in unidadesMedida_data:
        UnidadMedida.objects.get_or_create(codigo=unidadMedida_data['codigo'], valor=unidadMedida_data['valor'])
        
    formasPago_data = [
        {'codigo': '01', 'valor': 'Billetes y monedas'},
        {'codigo': '02', 'valor': 'Tajeta Debito'},
        {'codigo': '03', 'valor': 'Tarjeta Credito'},
        {'codigo': '04', 'valor': 'Cheque'},
        {'codigo': '05', 'valor': 'Transferencia_ Deposito Bancario'},
        {'codigo': '06', 'valor': 'Vales o Cupones'},
        {'codigo': '08', 'valor': 'Dinero Electronico'},
        {'codigo': '09', 'valor': 'Monedero Electronico'},
        {'codigo': '10', 'valor': 'Certificado o tarjeta de regalo'},
        {'codigo': '11', 'valor': 'Bitcoin'},
        {'codigo': '12', 'valor': 'Otras Criptomonedas'},
        {'codigo': '13', 'valor': 'Cuentas por pagar del receptor'},
        {'codigo': '14', 'valor': 'Giro Bancario'},
        {'codigo': '99', 'valor': 'Otros (se debe indicar el medio de pago)'},
    ]
    
    # Crear forma de pago
    for formaPago_data in formasPago_data:
        FormaPago.objects.get_or_create(codigo=formaPago_data['codigo'], valor=formaPago_data['valor'])
    
    tiposDocumentos_data = [
        {'codigo': '01', 'valor': 'Factura'},
        {'codigo': '03', 'valor': 'Comprobante de credito fiscal'},
        {'codigo': '04', 'valor': 'Nota de remision'},
        {'codigo': '05', 'valor': 'Nota de credito'},
        {'codigo': '06', 'valor': 'Nota de debito'},
        {'codigo': '07', 'valor': 'Comprobante de retencion'},
        {'codigo': '08', 'valor': 'Comprobante de liquidacion'},
        {'codigo': '09', 'valor': 'Documento contable de liquidacion'},
        {'codigo': '11', 'valor': 'Facturas de exportacion'},
        {'codigo': '14', 'valor': 'Factura de sujeto excluido'},
        {'codigo': '15', 'valor': 'Comprobante de donacion'}, 
    ]
    
    # Crear tipos de documentos
    for tipoDocumento_data in tiposDocumentos_data:
        TipoDocumento.objects.get_or_create(codigo=tipoDocumento_data['codigo'], valor=tipoDocumento_data['valor'])

    tributosItems_data = [
        {'codigo': '1' , 'valor': 'TRIBUTOS APLICADOS POR ITEMS REFLEJADOS EN EL RESUMEN DEL DTE'},
        {'codigo': '2' , 'valor': 'TRIBUTOS APLICADOS POR ITEMS REFLEJADOS EN EL CUERPO DEL DOCUMENTO'},
        {'codigo': '3' , 'valor': 'IMPUESTOS AD-VALOREM APLICADOS POR ITEM DE USO INFORMATIVO REFLEJADOS EL RESUMEN DEL DOCUMENTO'},
    ]
    
    #crear items del tributo
    for tributoItem_data in tributosItems_data:
        TributoItem.objects.get_or_create(codigo=tributoItem_data['codigo'], valor=tributoItem_data['valor'])
    
    tributos_data = [
        {'codigo': '20', 'tributoItem_codigo': '1', 'valor': 'Impuesto al Valor Agragado 13%'},
        {'codigo': 'C3', 'tributoItem_codigo': '1', 'valor': 'Impuesto al Valor Agregado (exportaciones) 0% '},
        {'codigo': '59', 'tributoItem_codigo': '1', 'valor': 'Turismo: por alojamiento (5%) '},
        {'codigo': '71', 'tributoItem_codigo': '1', 'valor': 'Turismo: salida del pais por via aerea $7.00'},
        {'codigo': 'D1', 'tributoItem_codigo': '1', 'valor': 'FOVIAL ($0.20 Ctvs. por galon)'},
        {'codigo': 'C8', 'tributoItem_codigo': '1', 'valor': 'COTRANS ($0.10 Ctvs. por galon)'},
        {'codigo': 'D5', 'tributoItem_codigo': '1', 'valor': 'Otras tasas casos especiales'},
        {'codigo': 'D4', 'tributoItem_codigo': '1', 'valor': 'Otros impuestos casos especiales'},
        {'codigo': 'A8', 'tributoItem_codigo': '2', 'valor': 'Ipuesto Especial al Combustible (0%, 0.5%, 1%)'},
        {'codigo': '57', 'tributoItem_codigo': '2', 'valor': 'Impuesto industria de Cemento'},
        {'codigo': '90', 'tributoItem_codigo': '2', 'valor': 'Impuesto especial a la primera matricula'},
        {'codigo': 'D4', 'tributoItem_codigo': '2', 'valor': 'Otros impuestos casos especiales'},
        {'codigo': 'D5', 'tributoItem_codigo': '2', 'valor': 'Otras tasas casos especiales'},
        {'codigo': 'A6', 'tributoItem_codigo': '2', 'valor': 'Impuesto ad-valorem, armas de fuego, municiones explosivas y articulos similares'},
        {'codigo': 'C5', 'tributoItem_codigo': '3', 'valor': 'Impuesto ad-valorem por diferencial de precios de bebidas alcoholicas (8%)'},
        {'codigo': 'C6', 'tributoItem_codigo': '3', 'valor': 'Impuesto ad-valorem por diferencial de precios al tabaco cigarrillos (39%)'},
        {'codigo': 'C7', 'tributoItem_codigo': '3', 'valor': 'Impuesto ad-valorem por diferencial de precios al tabaco cigarrillos (100%)'},
        {'codigo': '19', 'tributoItem_codigo': '3', 'valor': 'Fabricante de Bebidas Gaseosas, Isotonicas, Deportivas, Fortificantes, Energizantes o Estimulante'},
        {'codigo': '28', 'tributoItem_codigo': '3', 'valor': 'Importador de Bebidas Gaseosas, Isotonicas, Deportivas, Fortificantes, Energizantes o Estimulante'},
        {'codigo': '31', 'tributoItem_codigo': '3', 'valor': 'Detallistas o Expendedores de Bebidas Alcoholicas'},
        {'codigo': '32', 'tributoItem_codigo': '3', 'valor': 'Fabricante de Cerveza'},
        {'codigo': '33', 'tributoItem_codigo': '3', 'valor': 'Importador de Cerveza'},
        {'codigo': '34', 'tributoItem_codigo': '3', 'valor': 'Fabricante de Productos de Tabaco'},
        {'codigo': '35', 'tributoItem_codigo': '3', 'valor': 'Importador de Productos de Tabaco'},
        {'codigo': '36', 'tributoItem_codigo': '3', 'valor': 'Fabricante de Armas de Fuego, Municiones y Articulos Similares'},
        {'codigo': '37', 'tributoItem_codigo': '3', 'valor': 'Importador de Armas Fuego, Municiones y Articulos Similares'},
        {'codigo': '38', 'tributoItem_codigo': '3', 'valor': 'Fabricante de Explosivos'},
        {'codigo': '39', 'tributoItem_codigo': '3', 'valor': 'Importador de Explosivos'},
        {'codigo': '42', 'tributoItem_codigo': '3', 'valor': 'Fabricante de Productos Pirotecnicos'},
        {'codigo': '43', 'tributoItem_codigo': '3', 'valor': 'Importador de Productos Pirotecnicos'},
        {'codigo': '44', 'tributoItem_codigo': '3', 'valor': 'Productor de Tabaco'},
        {'codigo': '50', 'tributoItem_codigo': '3', 'valor': 'Distribuidor de Bebidas Gaseosas, Isotonicas, Deportivas, Fortificantes, Energizante o Estimulante'},
        {'codigo': '51', 'tributoItem_codigo': '3', 'valor': 'Bebidas Alcoholicas'},
        {'codigo': '52', 'tributoItem_codigo': '3', 'valor': 'Cerveza'},
        {'codigo': '53', 'tributoItem_codigo': '3', 'valor': 'Productos del Tabaco'},
        {'codigo': '54', 'tributoItem_codigo': '3', 'valor': 'Bebidas Carbonatadas o Gaseosas Simples o Endulzadas'},
        {'codigo': '55', 'tributoItem_codigo': '3', 'valor': 'Otros Especificos'},
        {'codigo': '58', 'tributoItem_codigo': '3', 'valor': 'Alcohol'},
        {'codigo': '77', 'tributoItem_codigo': '3', 'valor': 'Importador de Jugos, Nectares, Bebidas con Jugo y Refrescos'},
        {'codigo': '78', 'tributoItem_codigo': '3', 'valor': 'Distribuidor de Jugos, Nectares, Bebidas con Jugo y Refrescos'},
        {'codigo': '79', 'tributoItem_codigo': '3', 'valor': 'Sobre Llamadas Telefonicas Provenientes del Ext'},
        {'codigo': '85', 'tributoItem_codigo': '3', 'valor': 'Detallistas de Jugos, Nectares, Bebidas con Jugo y Refrescos'},
        {'codigo': '86', 'tributoItem_codigo': '3', 'valor': 'Fabricante de Preparaciones Concentradas o en Polvo para la Elaboracion de Bebidas'},
        {'codigo': '91', 'tributoItem_codigo': '3', 'valor': 'Fabricante de Jugos, Nectares, Bebidas con Jugo y Refrescos'},
        {'codigo': '92', 'tributoItem_codigo': '3', 'valor': 'Importador de Preparaciones Concentradas o en Polvo para la Elaboracion de Bebidas'},
        {'codigo': 'A1', 'tributoItem_codigo': '3', 'valor': 'Especificos y Ad-Valorem'},
        {'codigo': 'A5', 'tributoItem_codigo': '3', 'valor': 'Bebidas Gaseosas, Isotonicas, Deportaivas, Fortificantes, Energizantes o Estimulantes'},
        {'codigo': 'A7', 'tributoItem_codigo': '3', 'valor': 'Alcohol Etilico'},
        {'codigo': 'A9', 'tributoItem_codigo': '3', 'valor': 'Sacos Sinteticos'},    
    ]
    
    # Crear Tributos
    for tributo_data in tributos_data:
        tributoItem = TributoItem.objects.get(codigo=tributo_data['tributoItem_codigo'])
        Tributo.objects.get_or_create(codigo=tributo_data['codigo'], tributoItem=tributoItem , valor=tributo_data['valor'])