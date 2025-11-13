import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.width", 500)
pd.set_option("display.max_columns", None)
df = pd.read_csv("googleplaystore.csv")

df.head()

df.columns
"""
Index(['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver'], dtype='object')
"""

df.info()
"""
Data columns (total 13 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   App             10841 non-null  object 
 1   Category        10841 non-null  object 
 2   Rating          9367 non-null   float64
 3   Reviews         10841 non-null  object 
 4   Size            10841 non-null  object 
 5   Installs        10841 non-null  object 
 6   Type            10840 non-null  object 
 7   Price           10841 non-null  object 
 8   Content Rating  10840 non-null  object 
 9   Genres          10841 non-null  object 
 10  Last Updated    10841 non-null  object 
 11  Current Ver     10833 non-null  object 
 12  Android Ver     10838 non-null  object 
dtypes: float64(1), object(12)
"""

df.describe()

##########################
# missing data
##########################

df.isnull().sum()
"""
App                  0
Category             0
Rating            1474
Reviews              0
Size                 0
Installs             0
Type                 1
Price                0
Content Rating       1
Genres               0
Last Updated         0
Current Ver          8
"""


#Reviews values are more suitable for int64, but the dataset is given as string. Let's do the conversion.

df["Reviews"].value_counts()
df["Reviews"].unique()

df[~df["Reviews"].str.isnumeric()]  # -> We found a value that is not suitable for numeric conversion.
"""
10472  Life Made WI-Fi Touchscreen Photo Frame      1.9    19.0    3.0M  1,000+     Free    0  Everyone            NaN  February 11, 2018       1.0.19  4.0 and up         NaN
"""

df_clean = df.copy()

df_clean = df_clean.drop(df_clean.index[10472])

df_clean["Reviews"] = df_clean["Reviews"].astype(int)

df_clean.info()
"""
0   App             10840 non-null  object 
 1   Category        10840 non-null  object 
 2   Rating          9366 non-null   float64
 3   Reviews         10840 non-null  int64  
 4   Size            10840 non-null  object 
 5   Installs        10840 non-null  object 
 6   Type            10839 non-null  object 
 7   Price           10840 non-null  object 
 8   Content Rating  10840 non-null  object 
 9   Genres          10840 non-null  object 
 10  Last Updated    10840 non-null  object 
 11  Current Ver     10832 non-null  object 
 12  Android Ver     10838 non-null  object 
dtypes: float64(1), int64(1), object(11)
"""

df_clean["Size"].unique()

df_clean["Size"] = df_clean["Size"].str.replace("M", "000")
df_clean["Size"] = df_clean["Size"].str.replace("k", "")

df_clean["Size"] = df_clean["Size"].replace("Varies with device", np.nan)

df_clean["Size"] = df_clean["Size"].astype(float)

df_clean["Installs"].value_counts()

df_clean["Price"].value_counts()

chars_to_remove = ["+", ",", "$"]
cols_to_clean = ["Installs", "Price"]

for item in chars_to_remove:
    for cols in cols_to_clean:
        df_clean[cols] = df_clean[cols].str.replace(item, "")

df_clean["Price"].unique()
"""
array(['0', '4.99', '3.99', '6.99', '1.49', '2.99', '7.99', '5.99',
       '3.49', '1.99', '9.99', '7.49', '0.99', '9.00', '5.49', '10.00',
       '24.99', '11.99', '79.99', '16.99', '14.99', '1.00', '29.99',
       '12.99', '2.49', '10.99', '1.50', '19.99', '15.99', '33.99',
       '74.99', '39.99', '3.95', '4.49', '1.70', '8.99', '2.00', '3.88',
       '25.99', '399.99', '17.99', '400.00', '3.02', '1.76', '4.84',
       '4.77', '1.61', '2.50', '1.59', '6.49', '1.29', '5.00', '13.99',
       '299.99', '379.99', '37.99', '18.99', '389.99', '19.90', '8.49',
       '1.75', '14.00', '4.85', '46.99', '109.99', '154.99', '3.08',
       '2.59', '4.80', '1.96', '19.40', '3.90', '4.59', '15.46', '3.04',
       '4.29', '2.60', '3.28', '4.60', '28.99', '2.95', '2.90', '1.97',
       '200.00', '89.99', '2.56', '30.99', '3.61', '394.99', '1.26',
       '1.20', '1.04'], dtype=object)
"""

df_clean["Price"] = df_clean["Price"].astype(float)
df_clean["Installs"] = df_clean["Installs"].astype(int)

df_clean.info()
"""
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   App             10840 non-null  object 
 1   Category        10840 non-null  object 
 2   Rating          9366 non-null   float64
 3   Reviews         10840 non-null  int64  
 4   Size            9145 non-null   float64
 5   Installs        10840 non-null  int64  
 6   Type            10839 non-null  object 
 7   Price           10840 non-null  float64
 8   Content Rating  10840 non-null  object 
 9   Genres          10840 non-null  object 
 10  Last Updated    10840 non-null  object 
 11  Current Ver     10832 non-null  object 
 12  Android Ver     10838 non-null  object 
dtypes: float64(3), int64(2), object(8)
"""


df_clean["Last Updated"] = pd.to_datetime(df_clean["Last Updated"])

df_clean["Day"] = df_clean["Last Updated"].dt.day
df_clean["Month"] = df_clean["Last Updated"].dt.month
df_clean["Year"] = df_clean["Last Updated"].dt.year
"""
                                                App        Category  Rating  Reviews     Size  Installs  Type  Price Content Rating                     Genres Last Updated         Current Ver   Android Ver  Day  Month  Year
0     Photo Editor & Candy Camera & Grid & ScrapBook  ART_AND_DESIGN     4.1      159  19000.0     10000  Free    0.0       Everyone               Art & Design   2018-01-07               1.0.0  4.0.3 and up    7      1  2018
1                                Coloring book moana  ART_AND_DESIGN     3.9      967  14000.0    500000  Free    0.0       Everyone  Art & Design;Pretend Play   2018-01-15               2.0.0  4.0.3 and up   15      1  2018
2  U Launcher Lite – FREE Live Cool Themes, Hide ...  ART_AND_DESIGN     4.7    87510      8.7   5000000  Free    0.0       Everyone               Art & Design   2018-08-01               1.2.4  4.0.3 and up    1      8  2018
3                              Sketch - Draw & Paint  ART_AND_DESIGN     4.5   215644  25000.0  50000000  Free    0.0           Teen               Art & Design   2018-06-08  Varies with device    4.2 and up    8      6  2018
4              Pixel Draw - Number Art Coloring Book  ART_AND_DESIGN     4.3      967      2.8    100000  Free    0.0       Everyone    Art & Design;Creativity   2018-06-20                 1.1    4.4 and up   20      6  2018

"""

df_clean.info()

###############################
# EDA
###############################

df_clean[df_clean.duplicated("App")].shape
"""
(1181, 16)
"""

df_clean = df_clean.drop_duplicates(subset = ["App"], keep= "first")

df_clean.info()
"""
 #   Column          Non-Null Count  Dtype         
---  ------          --------------  -----         
 0   App             9659 non-null   object        
 1   Category        9659 non-null   object        
 2   Rating          8196 non-null   float64       
 3   Reviews         9659 non-null   int64         
 4   Size            8432 non-null   float64       
 5   Installs        9659 non-null   int64         
 6   Type            9658 non-null   object        
 7   Price           9659 non-null   float64       
 8   Content Rating  9659 non-null   object        
 9   Genres          9659 non-null   object        
 10  Last Updated    9659 non-null   datetime64[ns]
 11  Current Ver     9651 non-null   object        
 12  Android Ver     9657 non-null   object        
 13  Day             9659 non-null   int32         
 14  Month           9659 non-null   int32         
 15  Year            9659 non-null   int32         
dtypes: datetime64[ns](1), float64(3), int32(3), int64(2), object(7)
"""

numeric_features = [feature for feature in df_clean.columns if df_clean[feature].dtype != "O"]
categorical_features = [feature for feature in df_clean.columns if df_clean[feature].dtype == "O"]

print(numeric_features)
print(categorical_features)

plt.figure(figsize=(15, 10))

for i in range(0, len(numeric_features)):
    plt.subplot(5, 3, i+1)
    sns.kdeplot(x = df_clean[numeric_features[i]], color= "b", fill= True)
    plt.xlabel(numeric_features[i])
    plt.tight_layout()
plt.show()


plt.figure(figsize=(15, 5))

categories = ["Type", "Content Rating"]

for i in range(0, len(categories)):
    plt.subplot(1, 2, i+1)
    sns.countplot(x = df_clean[categories[i]], color= "r", fill= True)
    plt.xlabel(categories[i])
    plt.tight_layout()
plt.show()


# top app categories by installment
df_clean.groupby(["Category"])["Installs"].sum().sort_values(ascending=False)
"""
Category
GAME                   13878924415
COMMUNICATION          11038276251
TOOLS                   8001771915
PRODUCTIVITY            5793091369
SOCIAL                  5487867902
PHOTOGRAPHY             4649147655
FAMILY                  4427941505
VIDEO_PLAYERS           3926902720
TRAVEL_AND_LOCAL        2894887146
NEWS_AND_MAGAZINES      2369217760
ENTERTAINMENT           2113660000
BOOKS_AND_REFERENCE     1665969576
PERSONALIZATION         1532494782
SHOPPING                1400348785
HEALTH_AND_FITNESS      1144022512
SPORTS                  1096474498
BUSINESS                 697164865
LIFESTYLE                503823539
MAPS_AND_NAVIGATION      503281890
FINANCE                  455348734
WEATHER                  361100520
EDUCATION                352952000
FOOD_AND_DRINK           211798751
DATING                   140926107
ART_AND_DESIGN           114338100
HOUSE_AND_HOME            97212461
AUTO_AND_VEHICLES         53130211
LIBRARIES_AND_DEMO        52995910
COMICS                    44981150
MEDICAL                   38193177
PARENTING                 31521110
BEAUTY                    27197050
EVENTS                    15973161
"""

# 5 rating apps

rating_df = df_clean.groupby(["Category", "Installs", "App"])["Rating"].sum().sort_values(ascending= False).reset_index()

top_rated_apps = rating_df[rating_df["Rating"] == 5.0]
"""
               Category  Installs                                 App  Rating
0                FAMILY        10                         DN Employee     5.0
1                FAMILY        10                       Chronolink DX     5.0
2               MEDICAL       500                      FHR 5-Tier 2.0     5.0
3    HEALTH_AND_FITNESS        10                              CB Fit     5.0
4               MEDICAL       100                            Zen Leaf     5.0
..                  ...       ...                                 ...     ...
266              FAMILY        10                       Story Time FD     5.0
267              FAMILY        50                             DYPSOET     5.0
268  LIBRARIES_AND_DEMO      1000               Nur təfsiri 1-ci cild     5.0
269  LIBRARIES_AND_DEMO      1000                        Eternal life     5.0
270            BUSINESS      1000  Jobs in Canada - Emplois au Canada     5.0
"""

top_rated_apps.shape
"""
(271, 4)
"""














