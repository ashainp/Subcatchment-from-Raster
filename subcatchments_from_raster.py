from qgis.core import QgsProject, QgsRasterLayer, QgsVectorLayer
from whitebox.whitebox_tools import WhiteboxTools
import os

# Initialize the WhiteboxTools instance
wbt = WhiteboxTools()

# Define the path to your DEM and the output paths
input_dem_path = 'C:/Users/enoks/Desktop/test qgis/a.tif'
filled_sinks_path = 'C:/Users/enoks/Desktop/test qgis/filled_sinks.tif'
isobasins_path = 'C:/Users/enoks/Desktop/test qgis/isobasins.tif'
vectorized_isobasins_path = 'C:/Users/enoks/Desktop/test qgis/vectorized_isobasins.shp'

# Set the working directory for WhiteboxTools
wbt.set_working_dir(os.path.dirname(input_dem_path))

# 1. Fill depressions using the Wang and Liu method
try:
    wbt.fill_depressions_wang_and_liu(
        dem=input_dem_path,
        output=filled_sinks_path,
        fix_flats=True,
        flat_increment=0.01
    )
    print("Sinks filled using Wang and Liu method, output saved at:", filled_sinks_path)

    # Load the filled sinks layer into QGIS
    filled_sinks_layer = QgsRasterLayer(filled_sinks_path, "Filled Sinks")
    if filled_sinks_layer.isValid():
        QgsProject.instance().addMapLayer(filled_sinks_layer)
        print("Filled Sinks layer added to QGIS project.")
    else:
        print("Failed to load the filled sinks raster.")
except Exception as e:
    print(f"An error occurred while filling depressions: {e}")

# 2. Generate Isobasins
try:
    wbt.isobasins(
        dem=filled_sinks_path,
        output=isobasins_path,
        size=300000  # Correct parameter for specifying target basin size
    )
    print("Isobasins generated, output saved at:", isobasins_path)

    # Load the isobasins layer into QGIS
    isobasins_layer = QgsRasterLayer(isobasins_path, "Isobasins")
    if isobasins_layer.isValid():
        QgsProject.instance().addMapLayer(isobasins_layer)
        print("Isobasins layer added to QGIS project.")
    else:
        print("Failed to load the isobasins raster.")
except Exception as e:
    print(f"An error occurred while generating isobasins: {e}")

# 3. Vectorize Isobasins
try:
    # Convert the isobasins raster to vector polygons
    wbt.raster_to_vector_polygons(
        i=isobasins_path,
        output=vectorized_isobasins_path,
    )
    print("Isobasins vectorized, output saved at:", vectorized_isobasins_path)

    # Load the vectorized isobasins into QGIS
    vectorized_isobasins_layer = QgsVectorLayer(vectorized_isobasins_path, "Vectorized Isobasins", "ogr")
    if vectorized_isobasins_layer.isValid():
        QgsProject.instance().addMapLayer(vectorized_isobasins_layer)
        print("Vectorized Isobasins layer added to QGIS project.")
    else:
        print("Failed to load the vectorized isobasins.")
except Exception as e:
    print(f"An error occurred while vectorizing isobasins: {e}")
