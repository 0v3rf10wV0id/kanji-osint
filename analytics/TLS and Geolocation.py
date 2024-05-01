import requests
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Sample data load (replace 'data.csv' with your actual data file)
data = pd.read_csv('iit.edu-tslx-resolved__1_.csv')

# Define your API key and the geolocation fetch function
API_KEY = '3d736f6dedc24e3ba6136bd3646d2b51'
def get_geolocation(ip):
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Fetch geolocation data for unique IPs
unique_ips = data['ip'].unique()
locations = [get_geolocation(ip) for ip in unique_ips if get_geolocation(ip) is not None]

# Convert locations into a DataFrame
location_df = pd.DataFrame(locations)

# Visualization: Plotting the geographical distribution
fig_geo = px.scatter_geo(location_df,
                         lat='latitude',
                         lon='longitude',
                         hover_name='city',
                         title='Geographical Distribution of IPs',
                         projection="natural earth")
fig_geo.show()

# TLS versions and ciphers analysis
tls_versions = data['tls_version'].value_counts()
cipher_suites = data['cipher'].value_counts()

# Visualization: TLS configurations
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
tls_versions.plot(kind='bar', color='teal')
plt.title('TLS Version Distribution')
plt.xlabel('TLS Version')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
cipher_suites.plot(kind='bar', color='orchid')
plt.title('Cipher Suite Distribution')
plt.xlabel('Cipher Suite')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
