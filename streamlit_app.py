import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. Set up the wide webpage layout
st.set_page_config(layout="wide", page_title="SG Healthcare Accessibility")

st.title("🗺️ Singapore Healthcare Accessibility & Regional Planning")
st.caption("A data-driven evaluation of healthcare distribution across demographics.")

# 2. Sidebar Filter for Regions
st.sidebar.header("Map Filters")
region = st.sidebar.selectbox("Select Target Region:", ["All", "West", "East", "North", "South"])

# 3. Create the Base Map centered on Singapore
sg_center = [1.3521, 103.8198]
m = folium.Map(location=sg_center, zoom_start=11, tiles="OpenStreetMap")

# 4. Clickable Regional Boundaries (GeoJSON Overlay)
regions_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"name": "West", "description": "West Region: Focus on industrial hubs and aging estates."},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[103.60, 1.34], [103.76, 1.34], [103.76, 1.22], [103.60, 1.22], [103.60, 1.34]]]
            }
        },
        {
            "type": "Feature",
            "properties": {"name": "East", "description": "East Region: High residential density and aviation hubs."},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[103.90, 1.40], [104.03, 1.40], [104.03, 1.30], [103.90, 1.30], [103.90, 1.40]]]
            }
        },
        {
            "type": "Feature",
            "properties": {"name": "North", "description": "North Region: Developing residential zones and green spaces."},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[103.75, 1.47], [103.90, 1.47], [103.90, 1.35], [103.75, 1.35], [103.75, 1.47]]]
            }
        },
        {
            "type": "Feature",
            "properties": {"name": "South", "description": "South/Central Region: Core Central Business District and mature estates."},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[103.78, 1.32], [103.90, 1.32], [103.90, 1.24], [103.78, 1.24], [103.78, 1.32]]]
            }
        }
    ]
}

def style_function(feature):
    return {'fillColor': '#ffaf00', 'color': 'blue', 'weight': 1.5, 'fillOpacity': 0.1}

def highlight_function(feature):
    return {'fillColor': '#00ff00', 'color': 'green', 'weight': 2, 'fillOpacity': 0.3}

folium.GeoJson(
    regions_geojson,
    style_function=style_function,
    highlight_function=highlight_function,
    popup=folium.GeoJsonPopup(fields=['name', 'description'], labels=False)
).add_to(m)

# 5. Full Dataset of West, East, North, and South Healthcare Facilities
healthcare_facilities = [
    # --- WEST ---
    {"name": "National University Hospital", "lat": 1.2937083, "lon": 103.7831445, "address": "5 Lower Kent Ridge Rd, Singapore 119074", "region": "West", "type": "Hospital"},
    {"name": "Ng Teng Fong General Hospital", "lat": 1.3337448, "lon": 103.7453915, "address": "1 Jurong East Street 21, Singapore 609606", "region": "West", "type": "Hospital"},
    {"name": "Bukit Batok Polyclinic", "lat": 1.3519711, "lon": 103.7479248, "address": "50 Bukit Batok West Ave 3, Singapore 659164", "region": "West", "type": "Polyclinic"},
    {"name": "Chua Chu Kang Polyclinic", "lat": 1.3821900, "lon": 103.7509283, "address": "2 Teck Whye Cres, Singapore 688846", "region": "West", "type": "Polyclinic"},
    {"name": "Jurong Polyclinic", "lat": 1.3497921, "lon": 103.7306190, "address": "190 Jurong East Ave 1, Singapore 609788", "region": "West", "type": "Polyclinic"},
    {"name": "Clementi Polyclinic", "lat": 1.3128033, "lon": 103.7657387, "address": "451 Clementi Ave 3, #02-307, Singapore 120451", "region": "West", "type": "Polyclinic"},
    {"name": "Pioneer Polyclinic", "lat": 1.3386362, "lon": 103.6989744, "address": "26 Jurong West Street 61, Singapore 648201", "region": "West", "type": "Polyclinic"},
    
    # --- EAST ---
    {"name": "Changi General Hospital", "lat": 1.3405556, "lon": 103.9491667, "address": "2 Simei Street 3, Singapore 529889", "region": "East", "type": "Hospital"},
    {"name": "St Andrew’s Community Hospital", "lat": 1.3417531, "lon": 103.9499874, "address": "8 Simei Street 3, Singapore 529895", "region": "East", "type": "Hospital"},
    {"name": "Bedok Polyclinic", "lat": 1.3268481, "lon": 103.9321458, "address": "11 Bedok North Street 1, #03-147 Heartbeat@Bedok, Singapore 469662", "region": "East", "type": "Polyclinic"},
    {"name": "Tampines Polyclinic", "lat": 1.3551571, "lon": 103.9526703, "address": "1 Tampines Street 41, Singapore 529391", "region": "East", "type": "Polyclinic"},
    {"name": "Pasir Ris Polyclinic", "lat": 1.3676595, "lon": 103.9587711, "address": "1 Pasir Ris Drive 4, #01-11, Singapore 519457", "region": "East", "type": "Polyclinic"},
    {"name": "Marine Parade Polyclinic", "lat": 1.3031021, "lon": 103.9094034, "address": "80 Marine Parade Central, #01-792, Singapore 440080", "region": "East", "type": "Polyclinic"},
    
    # --- NORTH ---
    {"name": "Khoo Teck Puat Hospital (KTPH)", "lat": 1.424536, "lon": 103.838380, "address": "90 Yishun Central, Singapore 768828", "region": "North", "type": "Hospital"},
    {"name": "Yishun Community Hospital (YCH)", "lat": 1.425121, "lon": 103.837335, "address": "2 Yishun Central 2, Singapore 768024", "region": "North", "type": "Hospital"},
    {"name": "Woodlands Health", "lat": 1.425203, "lon": 103.794691, "address": "17 Woodlands Drive 17, Singapore 737628", "region": "North", "type": "Hospital"},
    {"name": "Yishun Polyclinic", "lat": 1.429452, "lon": 103.840243, "address": "2 Yishun Avenue 9, Singapore 768898", "region": "North", "type": "Polyclinic"},
    {"name": "Woodlands Polyclinic", "lat": 1.436735, "lon": 103.778262, "address": "10 Woodlands Street 31, Singapore 738579", "region": "North", "type": "Polyclinic"},
    {"name": "Sembawang Polyclinic", "lat": 1.453288, "lon": 103.824151, "address": "12 Sembawang Crescent, Singapore 757091", "region": "North", "type": "Polyclinic"},
    
    # --- SOUTH ---
    {"name": "Singapore General Hospital", "lat": 1.279449, "lon": 103.836274, "address": "Outram Rd, Singapore 169608", "region": "South", "type": "Hospital"},
    {"name": "Outram Community Hospital", "lat": 1.278480, "lon": 103.833950, "address": "10 Hospital Blvd, Singapore 169611", "region": "South", "type": "Hospital"},
    {"name": "Alexandra Hospital", "lat": 1.286824, "lon": 103.801232, "address": "378 Alexandra Rd, Singapore 159964", "region": "South", "type": "Hospital"},
    {"name": "Queenstown Polyclinic", "lat": 1.299580, "lon": 103.801550, "address": "580 Stirling Rd, Singapore 148958", "region": "South", "type": "Polyclinic"},
    {"name": "Bukit Merah Polyclinic", "lat": 1.284250, "lon": 103.821290, "address": "162 Bukit Merah Central, Singapore 150162", "region": "South", "type": "Polyclinic"},
    {"name": "Outram Polyclinic", "lat": 1.278820, "lon": 103.834310, "address": "3 Hospital Dr, Singapore 169609", "region": "South", "type": "Polyclinic"}
]

# Render pins dynamically based on sidebar choice
for place in healthcare_facilities:
    if region == "All" or place["region"] == region:
        # Construct clean HTML popup display
        popup_text = f"""
        <div style='font-family: Arial, sans-serif; width: 220px;'>
            <h4 style='margin:0 0 5px 0; color:#333;'>{place['name']}</h4>
            <p style='margin:0 0 5px 0; font-size:12px;'><b>Type:</b> {place['type']}</p>
            <p style='margin:0; font-size:11px; color:#555;'><b>Address:</b> {place['address']}</p>
        </div>
        """
        
        # Color coding: Red for Major Hospitals, Blue for Community Polyclinics
        marker_color = "red" if place["type"] == "Hospital" else "blue"
        marker_icon = "plus-sign" if place["type"] == "Hospital" else "info-sign"
        
        folium.Marker(
            location=[place["lat"], place["lon"]],
            popup=folium.Popup(popup_text, max_width=250),
            tooltip=place["name"],
            icon=folium.Icon(color=marker_color, icon=marker_icon)
        ).add_to(m)

# 6. Build the Tabbed Layout
tab1, tab2 = st.tabs(["Interactive GIS Dashboard", "Strategic Findings & Policy Proposals"])

with tab1:
    st.subheader(f"Geospatial Mapping: Showing {region} Facilities")
    st_folium(m, width=1100, height=500)

with tab2:
    st.subheader("📝 Strategic Analysis & Urban Infrastructure Planning")
    
    st.markdown("""
    ### 1. Key Spatial Discrepancies
    * **High Hospital Consolidation:** The Southern sector exhibits a massive concentration of acute and specialized medical infrastructure clustered closely around the Outram campus (SGH, Outram Community Hospital, Outram Polyclinic). This presents high local accessibility but poses emergency vulnerability gaps for newer fringe districts.
    * **Fringe Distribution Adjustments:** While the North and West are supported by strategic anchor points like Woodlands Health and Ng Teng Fong General Hospital, the massive residential population sprawl relies heavily on foundational Polyclinic nodes to offset acute facility congestion.
    
    ### 2. Strategic Policy Recommendations
    * **Data-Driven Infrastructure Placement:** Future polyclinics and satellite day-care units should be mathematically positioned within 1km walking radii of mature residential blocks to directly alleviate minor emergency bottlenecks from regional acute hospitals.
    * **Adaptive Capacity Scaling:** Using live geographic spatial tracking to balance hospital bed management and localized clinical deployments based on dynamic regional demographic developments rather than fixed territory limits.
    """)
