import pandas as pd
import Levenshtein
from geopy.distance import geodesic

df = pd.read_csv('data.csv')

df['is_similar'] = 0
    
for i in range(len(df)-1):
    levenshtein = Levenshtein.distance(df.loc[i, "name"], df.loc[i+1, "name"])

    location1 = (df.loc[i, "latitude"], df.loc[i, "longitude"])
    location2 = (df.loc[i+1, "latitude"], df.loc[i+1, "longitude"])
    
    distance = geodesic(location1, location2).meters 
    
    if levenshtein < 5 and distance <= 200:  
        df.loc[i, "is_similar"] = 1
        df.loc[i+1, "is_similar"] = 1
            
df.to_csv('output.csv')