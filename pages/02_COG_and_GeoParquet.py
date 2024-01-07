import streamlit as st

st.title("COG and GeoParquet")

st.header("What is a Cloud Optimized GeoTIFF (COG)?")
st.markdown("""
* A TIF/TIFF file is just a file format to store raster graphic images
* A GeoTIFF is TIFF + georeference
* A Cloud Optimizedf GeoTIFF is a GeoTIFF + internal tiling + overviews
""")

st.image("https://maxar-blog-assets.s3.amazonaws.com/uploads/blogImages/2018/01/FLAME-animation-COGEO.gif")


st.header("What is a GeoParquet file?")
st.markdown("""
* Parquet is a column-oriented data file format designed for efficient data storage and retrieval
* GeoParquet is a Parquet file + geometry column
""")

st.image("https://insightsoftware.com/wp-content/uploads/2022/02/what_is_a_column-oriented_database.png")