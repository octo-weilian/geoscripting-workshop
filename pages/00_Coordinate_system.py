import streamlit as st

st.header("Coordinate systems and projections")
st.markdown("""
Geodata has a coordinate reference system (CRS) that defines its location on the earth's surface. 
""")
st.image("https://help.arcgis.com/en/geodatabase/10.0/sdk/arcsde/images/coordsys_blockdiag1.jpg",width=500,caption="Coordinate system")
st.image("https://www.esri.com/arcgis-blog/wp-content/uploads/2022/02/grid2.png",width=500,caption="Geographic and Projected")

st.markdown("""
* A geographic coordinate system (GCS) is used to define locations on a spherical model of the surface of the earth
* A projected coordinate system (PCS) is a GCS that has been flattened using a map projection
* Reprojection is converting geodata in one CRS to another. CRS are often defines using EPSG codes, e.g. EPSG:4326 (GCS), EPSG:28992 (PCS).
* Each region and country has its own PCS
* A geodata must be projected for spatial analysis and visualization (!)
""")