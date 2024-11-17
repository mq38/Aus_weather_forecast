if __name__ == "__main__":
    print("Script started")
    
    import numpy as np # linear algebra
    import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
    import geopandas as gpd    
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt # data visualization
    import seaborn as sns # data visualization
    sns.reset_defaults()
    import geoplot as gplt
    from geopy.geocoders import Nominatim
    from shapely.geometry import Point
    import matplotlib.colors as mcolors
    from scipy.interpolate import griddata
    ##read data

    data = "C:\projekt\Andmed\weatherAUS.csv"
    df = pd.read_csv(data)
    #df.info()


    ##find categorical variables

    categorical = [var for var in df.columns if df[var].dtype=='O']

    print('There are {} categorical variables\n'.format(len(categorical)))

    print('Categorical variables are :', categorical)

    ## find missing values in categorical variables

    #print(df[categorical].isnull().sum())


    ##frequency of categorical variables

    #for var in categorical: 
        
    #    print(df[var].value_counts())

    ##check for cardinality in categorical variables

    #for var in categorical:
        
    #    print(var, ' contains ', len(df[var].unique()), ' labels')


    ## date variable contains 3436 labels so needs to be split into year/month/day

    #print(df["Date"].dtypes)

    df['Date']= pd.to_datetime(df['Date'])

    df['Year'] = df['Date'].dt.year

    df['Month'] = df['Date'].dt.month

    df['Day'] = df['Date'].dt.day

    df.drop('Date', axis=1, inplace = True)

    #start looking into other categorical variables

    #print('Location contains', len(df.Location.unique()), 'labels')

    #print(df.Location.unique())

    #one-hot encoding for location variables

    pd.get_dummies(df.Location, drop_first=True).astype(int).head()

    #one-hot encoding for wind gust direction variables, also add dummy for nan values

    pd.get_dummies(df.WindGustDir, drop_first=True, dummy_na=True).astype(int).head()

    #one-hot encoding for wind dir 9am variables, also add dummy for nan values

    pd.get_dummies(df.WindDir9am, drop_first=True, dummy_na=True).astype(int).head()

    #one-hot encoding for wind dir 9am variables, also add dummy for nan values

    pd.get_dummies(df.WindDir3pm, drop_first=True, dummy_na=True).astype(int).head()

    #one-hot encoding for raintoday variable, add dummy for nan values

    pd.get_dummies(df.RainToday, drop_first=True, dummy_na=True).astype(int).head()


    #explore numerical variables

    numerical = [var for var in df.columns if df[var].dtype!='O']

    #print('There are {} numerical variables\n'.format(len(numerical)))

    #print('The numerical variables are :', numerical)

    #19 numerical variables, all continuous type
    #check for missing values

    print(df[numerical].isnull().sum())

    print(round(df[numerical].describe()),2)

    # rainfall, evaporation, windspeed9am and windspeed 3pm might contain extreme outliers
    '''
    plt.figure(figsize=(15,10))


    plt.subplot(2, 2, 1)
    fig = df.boxplot(column='Rainfall')
    fig.set_title('')
    fig.set_ylabel('Rainfall')


    plt.subplot(2, 2, 2)
    fig = df.boxplot(column='Evaporation')
    fig.set_title('')
    fig.set_ylabel('Evaporation')


    plt.subplot(2, 2, 3)
    fig = df.boxplot(column='WindSpeed9am')
    fig.set_title('')
    fig.set_ylabel('WindSpeed9am')


    plt.subplot(2, 2, 4)
    fig = df.boxplot(column='WindSpeed3pm')
    fig.set_title('')
    fig.set_ylabel('WindSpeed3pm')


    plt.show()
    '''
    import geopandas as gpd
    import geoplot as gplt
    import matplotlib.pyplot as plt
    from geopy.geocoders import Nominatim
    from shapely.geometry import Point
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature


    df_filtered = df[(df['Year'] == 2012) & (df['Month'] == 4) & (df['Day'] == 30)].copy()

    # 2. Geocode the locations to get latitude and longitude
    geolocator = Nominatim(user_agent="geo_plotting")

    # Create lists to store latitudes and longitudes
    lons = []
    lats = []

    for location in df_filtered['Location']:
        location_info = geolocator.geocode(location + ", Australia")
        if location_info:
            lons.append(location_info.longitude)
            lats.append(location_info.latitude)
        else:
            lons.append(np.nan)
            lats.append(np.nan)

    # 3. Add latitude and longitude to the filtered dataframe using .loc
    df_filtered.loc[:, 'Longitude'] = lons
    df_filtered.loc[:, 'Latitude'] = lats

    # 4. Drop rows with NaN coordinates (e.g., missing longitude/latitude) or missing MaxTemp values
    df_filtered = df_filtered.dropna(subset=['Longitude', 'Latitude', 'MaxTemp'])

    # 5. Ensure lengths of coordinates and MaxTemp are the same
    lons = df_filtered['Longitude']
    lats = df_filtered['Latitude']
    temps = df_filtered['MaxTemp']

    # 6. Plot the locations with temperature labels
    plt.figure(figsize=(10, 8))

    # Create a Cartopy map with PlateCarree projection (for global lat-lon coordinates)
    ax = plt.axes(projection=ccrs.PlateCarree())

    # Add a natural coastline feature (cartopy feature)
    ax.add_feature(cfeature.COASTLINE, edgecolor='black')
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    # Add state boundaries for Australia
    ax.add_feature(cfeature.STATES, linestyle=':', edgecolor='gray')

    # Plot the location points on the map
    sc = ax.scatter(lons, lats, c=temps, cmap='coolwarm', edgecolors='k', s=100)

    # Add temperature labels at each location
    for idx, row in df_filtered.iterrows():
        ax.text(row['Longitude'], row['Latitude'], f"{row['MaxTemp']}°C", fontsize=12, ha='center', color='black')

    # Add a colorbar for the temperature scale
    cbar = plt.colorbar(sc, ax=ax, label='Max Temperature (°C)')

    # Add labels and title
    plt.title("Max Temperature across Australia on 30 April 2012")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    # Show the plot
    plt.show()
