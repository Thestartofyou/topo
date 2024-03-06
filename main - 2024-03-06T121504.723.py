import requests
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_elevation(lat, lon):
    """
    Get elevation data from USGS National Map API
    """
    url = f"https://nationalmap.gov/epqs/pqs.php?x={lon}&y={lat}&units=Meters&output=json"
    response = requests.get(url)
    data = response.json()
    elevation = data["USGS_Elevation_Point_Query_Service"]["Elevation_Query"]["Elevation"]
    return elevation

def plot_topography(lat, lon):
    """
    Plot topography using elevation data
    """
    elevation = get_elevation(lat, lon)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = lon
    y = lat
    z = elevation

    ax.scatter(x, y, z)

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Elevation (m)')
    ax.set_title('Topography')

    plt.show()

if __name__ == "__main__":
    # Example coordinates (San Francisco)
    latitude = 37.7749
    longitude = -122.4194

    plot_topography(latitude, longitude)
