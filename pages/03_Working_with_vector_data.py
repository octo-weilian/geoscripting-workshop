import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.title("Working with vector data")

st.code("""# import modules
import streamlit as st
import geopandas as gpd
import leafmap.foliumap as leafmap
""")

st.markdown("Load Argentina from GeoPandas dataset")

gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf = gdf[gdf["name"]=='Argentina'].reset_index(drop=True)


st.code("""
gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf = gdf[gdf["name"]=='Argentina'].reset_index(drop=True)
gdf.T
""")

st.text(gdf.T)

st.markdown("Print datasource CRS")
st.code("""
gdf.crs
""")

st.text(gdf.crs)

st.markdown("Reproject to Web Mercator projection (EPSG:3857)")
gdf = gdf.to_crs(3857)
st.code("""
gdf = gdf.to_crs(3857)
gdf.crs
""")

st.text(gdf.crs)

st.markdown("Show on an interactive map")


st.code("""

m = leafmap.Map(
    center=(-31.417, -64.183), 
    zoom=4,
    draw_control=False,
    measure_control=False,
    fullscreen_control=False,
    attribution_control=True
)
m.add_gdf(gdf,style={"Fill":True})
m.to_streamlit()
""")

m= leafmap.Map(
    center=(-31.417, -64.183), 
    zoom=4,
    draw_control=True,
    measure_control=False,
    fullscreen_control=False,
    attribution_control=True
)

m.add_gdf(gdf,style={"Fill":True})
m.to_streamlit()