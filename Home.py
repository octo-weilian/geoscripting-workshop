import streamlit as st 

st.title("Geoscripting workshop")

st.header("What is geoscripting?")
st.markdown("""Programming and scripting to solve geographical or spatial applied problems""")

st.header("What are examples of spatial problems?")
st.markdown("Spatial problems are issues that relate to the location or distribution of objects and phenomena in space (and time)")

st.image("https://gisgeography.com/wp-content/uploads/2020/10/Least-Cost-Path-Analysis-1265x439.jpg",width=500,caption="Routing")
st.image("https://imgs.mongabay.com/wp-content/uploads/sites/30/2019/10/10102500/Assam_Guwahati_Flood.gif",width=500,caption="Flood areas")

st.header("What is geodata?")
st.markdown("Geodata is information about geographic locations that is stored in a format that can be used with a geographic information system (GIS) and geospatial tools. Two types of geodata: vector and raster")

st.image("https://seos-project.eu/agriculture/images/gis_layers.gif",caption="GIS layers")

st.header("How to store geodata?")
st.markdown("Vector files: .shp, .geojson (.json), .gml, .kml, .gpkg, .parquet, .gdb")
st.markdown("Raster files: .tiff, .img, .ecw, .jp2, .gdb")
st.markdown("And many more...")

st.header("How is information stored in a vector file?")

st.text("A .geojson file stores geometry as key-value pairs")
st.code("""#geojson string
{"type":"Polygon",
"coordinates":[[[30,10],[40,40],[20,40],[10,20],[30,10]]]
        }
""")

st.markdown("Binary vector file stores geometry as well-known binary (WKB). Geospatial tools often display them as well-known text (WKT).")
st.code("""#WKT
POLYGON((30 10,40 40,20 40,10 20,30 10))
""")
st.code("""#WKB
010300000001000000050000000000000000003e4000000000000024400000000000004440000000000000444000000000000034400000000000004440000000000000244000000000000034400000000000003e400000000000002440
        """)

st.header("How is information stored in a raster file?")

st.image("https://miro.medium.com/v2/resize:fit:1400/1*jsPHpueq_PAPRH5KVA2VMw.png",width=300,caption='Image array')

st.header("How to work with geodata?")
st.image("https://geopandas.org/en/stable/_images/geopandas_logo.png",width=500,caption="Geoopandas: vector data manipulation, spatial operations, and map visualization on dataframes")
st.image("https://numfocus.org/wp-content/uploads/2018/09/xarray-logo-square.png",width=300,caption="rioxarray: geospatial xarray extension powered by rasterio for working with raster data")
st.markdown("And many more...")
