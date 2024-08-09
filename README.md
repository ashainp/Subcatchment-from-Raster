# Subcatchments-from-Raster
A Python script for automating catchment delineation in QGIS from a raster layer using WhiteboxTools. The script fills depressions, generates isobasins, and vectorizes them for integration into geospatial workflows.

## Features

1. **Fill Depressions**: Uses the Wang and Liu method to fill depressions in a DEM, ensuring hydrological correctness.
2. **Generate Isobasins**: Automatically generates isobasins based on a user-defined target size.
3. **Vectorize Isobasins**: Converts the isobasins raster to vector polygons for integration into other GIS applications.

## Prerequisites

- **QGIS**: Ensure QGIS is installed with Python support.
- **WhiteboxTools**: This tool is required for the script to run successfully.

### Installing WhiteboxTools

Before running the script, you need to install WhiteboxTools. Open your Command Line Interface (CLI) and run the following command:
pip install whitebox

# After installing, you can verify the installation using the following code:

# Verify WhiteboxTools Installation
try:
    from whitebox.whitebox_tools import WhiteboxTools
    print("WhiteboxTools imported successfully.")
except ImportError as e:
    print(f"Error importing WhiteboxTools: {e}")
    print("Make sure you have installed the whitebox package using pip.")

**Running the Script**
1.Open QGIS.
2.Load your DEM file into QGIS or ensure you have the path to the DEM file you want to process.
3.Open the Python Console in QGIS (Plugins > Python Console).
4.Copy and paste the script into the console or use a .py file that contains the script.

****Script Overview****
The script performs the following steps:

**Fill Depressions:**
Takes the input DEM and fills depressions using the Wang and Liu method.
Outputs a raster layer with filled depressions.

**Generate Isobasins:**
Creates isobasins based on the filled DEM.
The target basin size can be specified by the user.

**Vectorize Isobasins:**
Converts the isobasins raster into vector polygons.
The resulting vector layer is then loaded into QGIS for further analysis.

**Example Usage******
Below is an example of how to use the script in the QGIS Python console. Specifiy input DEM path accurately. Specify output result layer path accurately as desired.

# Define the paths for your DEM and output files
input_dem_path = 'C:/path/to/your/DEM.tif'
filled_sinks_path = 'C:/path/to/output/filled_sinks.tif'
isobasins_path = 'C:/path/to/output/isobasins.tif'
vectorized_isobasins_path = 'C:/path/to/output/vectorized_isobasins.shp'

Run the script (details are provided in the main script file)
