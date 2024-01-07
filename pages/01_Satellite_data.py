import streamlit as st 


st.title("Satellite data")

st.header("What is satellite data?")
st.markdown("Satellite data or satellite imagery is understood as information about Earth and other planets in the space, gathered by man-made satellites in their orbits.")

st.header("How is satellite data being used?")
st.markdown("""

* Agriculture: crop monitoring
* Forestry: forestry planning and prevention of illegal logging
* Fishing: prevention of illegal fishing
* Energy: pipeline and right-of-way monitoring
* Insurance: infrastructure integrity monitoring
* Land use: infrastructure planning and monitoring of building activity
* Sea traffic: iceberg monitoring, oil spills detection
* Security: coastal traffic monitoring
* Disaster response: fast response to natural catastrophes

""")

st.header("How is satellite data collected?")
st.markdown("""Satellite data is collected using remote sensing technologies and sensors. There are 2 types of remote sensing systems:
* passive remote sensing
* active remote sensing            
""")
st.image("https://www.earthdata.nasa.gov/s3fs-public/imported/passive.png?VersionId=WS26F.oPn0JhfTaB6AxZMEuIYzQrJAF2",width=300,caption="Passive remote sensing")

st.image("https://scied.ucar.edu/sites/default/files/styles/extra_large/public/images/solar-spectrum1.jpg.webp?itok=hmMksnbS",width=500,caption="Solar spectrum")
st.image("https://www.researchgate.net/publication/318843407/figure/fig4/AS:631662853488661@1527611568465/Spectral-signatures-as-functions-of-wavelength-for-five-typical-surfaces-The-central.png",width=500,caption="Spectral signature")
st.image("https://ece.montana.edu/seniordesign/archive/SP15/OpticalWeedMapping/uploads/4/9/2/7/49273335/1429843234.png",width=300,caption='NDVI')