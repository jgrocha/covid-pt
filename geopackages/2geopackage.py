import os
import sys
import argparse
from datetime import datetime

# usage: python3 2geopackage.py 2020-04-25

parser = argparse.ArgumentParser(description='Cria um geopackage')
parser.add_argument('date')
args = parser.parse_args()
altdate = datetime.fromisoformat(args.date)

projectName = '../qgis/dados-dgs.qgz'
destfile = '../covid-pt-{}.gpkg'.format(args.date)

os.environ['QT_QPA_PLATFORM'] = 'offscreen'
sys.path.insert(0,'/usr/local/share/qgis/python')
sys.path.insert(1,'/usr/local/share/qgis/python/plugins')

from qgis.core import *
QgsApplication.setPrefixPath("/usr/local", True) 
from qgis.gui import *

from qgis.PyQt.QtGui import QColor, QImage
from qgis.PyQt.QtCore import QSize, QBuffer, QIODevice

qgs = QgsApplication([], False)
qgs.initQgis()

from qgis.analysis import QgsNativeAlgorithms
from qgis import processing
from processing.core.Processing import Processing
Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

project = QgsProject.instance()

print("Abrindo o projeto guardado como {}...".format(projectName))
project.read(projectName)
print("... projeto {} pronto para processar!".format(project.title()))

print("Exportando as camadas para {}...".format(destfile))
print(destfile)

parameters = {
    'LAYERS': [
        'service=\'covid\' sslmode=disable key=\'id\' srid=3763 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"(SELECT * FROM /\"concelho/\"\n)\" (wkb_geometry)',
        'service=\'covid\' sslmode=disable key=\'dico\' checkPrimaryKeyUnicity=\'1\' table=\"public\".\"confirmados_concelho\"',
        'service=\'covid\' sslmode=disable key=\'di\' checkPrimaryKeyUnicity=\'1\' table=\"public\".\"confirmados_distrito_ilha\"',
        'service=\'covid\' sslmode=disable key=\'id\' srid=3763 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"distrito\" (wkb_geometry)',
        'service=\'covid\' sslmode=disable key=\'id\' srid=5015 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"raa_central_concelho\" (wkb_geometry)',
        'service=\'covid\' sslmode=disable key=\'id\' srid=5015 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"raa_central_ilha\" (wkb_geometry)',
        'service=\'covid\' sslmode=disable key=\'id\' srid=5014 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"raa_ocidental_concelho\" (wkb_geometry)',
        'service=\'covid\' sslmode=disable key=\'id\' srid=5014 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"raa_ocidental_ilha\" (wkb_geometry)',
        'service=\'covid\' sslmode=disable key=\'id\' srid=5015 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"raa_oriental_concelho\" (wkb_geometry)',
        'service=\'covid\' sslmode=disable key=\'id\' srid=5015 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"raa_oriental_ilha\" (wkb_geometry)',
        'service=\'covid\' sslmode=disable key=\'id\' srid=5016 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"ram_concelho\" (wkb_geometry)',
        'service=\'covid\' sslmode=disable key=\'id\' srid=5016 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"ram_ilha\" (wkb_geometry)',
        'service=\'covid\' sslmode=disable key=\'id\' checkPrimaryKeyUnicity=\'1\' table=\"public\".\"situacao_epidemiologica\"'],
    'OUTPUT': destfile,
    'OVERWRITE': True,
    'SAVE_STYLES': True}

# processing.algorithmHelp("native:package")
processing.run("native:package", parameters)

manager = QgsProject.instance().layoutManager()

layoutName = 'distritos'
layout = manager.layoutByName(layoutName)
if layout:
    titulo = layout.itemById('titulo');
    titulo.setText("Casos de COVID-19 confirmados por distrito\n{}".format( altdate.strftime("%A, %d de %B de %Y") ))
    exporter = QgsLayoutExporter(layout)
    # print("A exportar a composição {} em PDF...".format(layoutName))
    # exporter.exportToPdf('distrito_continente_{}.pdf'.format(args.date), QgsLayoutExporter.PdfExportSettings())
    print("A exportar a composição {} em PNG...".format(layoutName))
    exporter.exportToImage('../mapas/distrito_continente_{}.png'.format( altdate.strftime("%Y%m%d") ), QgsLayoutExporter.ImageExportSettings()) 

layoutName = 'concelho_continente'
layout = manager.layoutByName(layoutName)
if layout:
    titulo = layout.itemById('titulo');
    titulo.setText("Casos de COVID-19 confirmados por concelho\n{}".format( altdate.strftime("%A, %d de %B de %Y") ))
    exporter = QgsLayoutExporter(layout)
    # print("A exportar a composição {} em PDF...".format(layoutName))
    # exporter.exportToPdf('distrito_continente_{}.pdf'.format(args.date), QgsLayoutExporter.PdfExportSettings())
    print("A exportar a composição {} em PNG...".format(layoutName))
    exporter.exportToImage('../mapas/concelho_continente_{}.png'.format( altdate.strftime("%Y%m%d") ), QgsLayoutExporter.ImageExportSettings()) 

layoutName = 'madeira'
layout = manager.layoutByName(layoutName)
if layout:
    titulo = layout.itemById('titulo');
    titulo.setText("Casos de COVID-19 confirmados na RAM\n{}".format( altdate.strftime("%A, %d de %B de %Y") ))
    exporter = QgsLayoutExporter(layout)
    # print("A exportar a composição {} em PDF...".format(layoutName))
    # exporter.exportToPdf('distrito_continente_{}.pdf'.format(args.date), QgsLayoutExporter.PdfExportSettings())
    print("A exportar a composição {} em PNG...".format(layoutName))
    exporter.exportToImage('../mapas/madeira_{}.png'.format( altdate.strftime("%Y%m%d") ), QgsLayoutExporter.ImageExportSettings()) 

qgs.exitQgis()
