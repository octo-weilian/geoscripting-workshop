import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

# geom = {"type":"Polygon",
#         "coordinates":[[[-63.403816,-31.171611]
#                         ,[-63.403816,-31.161623]
#                         ,[-63.392229,-31.161623]
#                         ,[-63.392229,-31.171611]
#                         ,[-63.403816,-31.171611]]]
#         }


st.title("Working with raster data")

st.markdown("Open COG directly from S3 bucket")
st.code("""
import rioxarray as rio
import xarray as xr

# sentinel-2 data
red = "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/20/J/ML/2024/1/S2A_20JML_20240104_0_L2A/B04.tif"
green = "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/20/J/ML/2024/1/S2A_20JML_20240104_0_L2A/B03.tif"
blue = "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/20/J/ML/2024/1/S2A_20JML_20240104_0_L2A/B02.tif"
nir = "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/20/J/ML/2024/1/S2A_20JML_20240104_0_L2A/B08.tif"
       
#open as DataArray
red_img = rio.open_rasterio(red, overview_level=2)
green_img = rio.open_rasterio(green, overview_level=2)
blue_img = rio.open_rasterio(blue, overview_level=2)
nir_img = rio.open_rasterio(nir, overview_level=2)
""")

st.markdown("Create and export RGB and NDVI images")
st.code("""
ndvi_img = ((nir_img-red_img)/(nir_img+red_img)).to_dataset(name='ndvi')
ndvi_img = ndvi_img.where(ndvi_img<1,other=nir_img.rio.nodata)
rgb_img = xr.combine_by_coords([red_img.to_dataset(name='red'),
                                green_img.to_dataset(name='green'),
                                blue_img.to_dataset(name='blue')
                                ])

rgb_img.rio.to_raster("rgb_img.tif", driver='COG')
ndvi_img.rio.to_raster("ndvi_img.tif", driver='COG')
""")

st.markdown("Show local geotiffs on map")
st.code("""
m= leafmap.Map(
    center=(-31.417, -64.183), 
    zoom=8,
    draw_control=False,
    measure_control=False,
    fullscreen_control=False,
    attribution_control=True
)
m.add_raster("ndvi_img.tif",bands=[1],palette='RdYlGn',layer_name='ndvi')
m.add_raster("rgb_img.tif",bands=[3,2,1],layer_name='rgb')
m
""")

m= leafmap.Map(
    center=(-31.417, -64.183), 
    zoom=8,
    draw_control=False,
    measure_control=False,
    fullscreen_control=False,
    attribution_control=True
)
m.add_raster("ndvi_img.tif",bands=[1],palette='RdYlGn',layer_name='ndvi')
m.add_raster("rgb_img.tif",bands=[3,2,1],layer_name='rgb')
m.to_streamlit()


