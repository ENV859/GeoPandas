---
Title: Introduction to GeoPandas
Author: John Fay
Date: Fall 2017
---

# Introduction to GeoPandas

http://geopandas.org/

### What is GeoPandas

Briefly, GeoPandas is a Python package that enables geospatial analysis with Pandas dataFrames. It combines the geoprocessing engine of **GDAL** (which is interfaced with the **Fiona** package), the geospatial objects of **Shapely**, and of course the data manipulation power of **Pandas** to enable spatial analysis in Python - no ArcGIS license required!

### Installing Geopandas

With so many dependencies, GeoPandas cannot be installed with a simple `pip` command. Instead, it requires some specific wheels to be downloaded (from [Cristoph Gohlke's repository](https://www.lfd.uci.edu/~gohlke/pythonlibs/)) and installed in a particular sequence, and also requires the path the the GDAL binaries to be included in the system's environment PATH variable. Geoff Boeing has a nice page describing the process here: http://geoffboeing.com/2014/09/using-geopandas-windows/. However, included in this repository, in the `installation` folder, are the necessary wheels as well as a DOS batch file that handles the installation for you. This script also installs the Jupyter package, as it also used in these exercises. 

### Diving in with some example notebooks

In the `notebooks` folder are a set of Jupyter notebooks to familiarize yourself with the objects and functions of the GeoPandas package. While these by no means cover all there is to know about GeoPandas, they do bring you up to speed on some ways to construct a GeoPandas dataFrame and the basic properties and methods of it and other GeoPandas classes. 

#### The notebooks

* **0-Intro-to-Geopandas** - a super quick introduction to what GeoPandas is and what it's generally capable of doing: reading and writing shapefiles, analysis as a dataFrame object, plotting, and geospatial analysis. 
* **1-GetCounties-Documented** - using GeoPandas along with the Requests package to download geospatial data served on an ArcGIS Map Service so that we can use these data in analysis. 


* **2-Create-County-Annual-Runoff-Tables** - a "deep dive" into GeoPandas showing how it, and other packages, is used to accomplish a real-world task. This script:
  * Pulls monthly runoff data for the year 2000, stored as 1/8th degree points, from a server 
  * Convert the data from a netCDF object into a mulit-dimensional NumPy array
  * Sums the monthly values into annual values using NumPy functions
  * Converts the annual data into a GeoPandas dataFrame
  * Uses spatial analysis functions of GeoPandas to overlay the 1/8th degree point features with a feature class of US Counties to assign the county in which each point falls. 
  * Summarize runoff values by county and write the values to a table. 

### 

