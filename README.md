🤖 Google Play Store App Analysis
This project is an Exploratory Data Analysis (EDA) study using a comprehensive Google Play Store dataset from Kaggle to explore relationships between app categories, 
popularity (number of installs), ratings, and key features.

🎯 Project Objectives
To clean the Google Play Store dataset and prepare it for analysis.

To visualize the key distributions of apps (rating, size, number of reviews).

To identify the most installed (popular) app categories.

To examine the distribution of high-rated apps (5.0).

📈 Exploratory Data Analysis (EDA) Results
1. Numerical Feature Distributions (KDE Plot)
The distributions of numerical features (Rating, Reviews, Size, Installs, Price, Day, Month, Year) in the dataset were examined using Kernel Density Estimation (KDE) plots.
These graphs show that the ratings, reviews, and installs of most apps in the dataset are stacked to the left (skewed to the right).

3. Categorical Feature Distributions (Count Plots)
The distributions of app type (Type) and content rating (Content Rating) were analyzed using Count Plots.

Most apps are seen to be "Free."

The vast majority have a content rating of "Everyone."

3. Most Popular App Categories (by Install Count)
App categories are ranked by total install count.

The Games, Communication, and Tools categories are the clear leaders in total install count.

4. Apps with Perfect Ratings (Rating = 5.0)
The dataset contains 271 apps with a perfect 5.0 rating and unique app names. These apps are typically niche or newer apps with lower install counts.

![figure_1](https://github.com/alcngns/GooglePlayDataEDA/blob/main/Figure_1.png)

![figure_2](https://github.com/alcngns/GooglePlayDataEDA/blob/main/Figure_2.png)
