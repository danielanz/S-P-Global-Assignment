# NYC Rideshare Service Equity Analysis

An analysis of whether rideshare platforms systematically underserve lower-income and outer-borough neighborhoods in New York City during the post-subsidy era.

## Overview

This project investigates transportation equity in NYC's rideshare market using TLC Trip Record Data and U.S. Census Bureau demographic data. The central hypothesis was that the end of venture capital subsidies for Uber and Lyft (post-2020) may have exposed service inequities in lower-income neighborhoods that were previously masked by artificially low fares.

**Key Finding:** Contrary to initial concerns, we found no evidence of systematic rideshare underservice in lower-income NYC neighborhoods as of 2024. Service levels are well-predicted by vehicle ownership and transit access, with no residual correlation with poverty or race.

## Data Sources

- **TLC Trip Record Data:** HVFHV (Uber, Lyft) trip records for January, April, July, and October 2024
- **U.S. Census Bureau:** American Community Survey 5-year estimates (2020-2024) at the census tract level

## Methodology

### 1. Data Preparation
- Filtered to HVFHV trips (86.6% market share)
- Excluded airports, parks, and zones with near-zero residential population
- Spatial join of census tracts to taxi zones via centroid assignment
- Aggregated to zone-level metrics

### 2. Exploratory Data Analysis
- Choropleth maps of trips per capita, fare per mile, and wait times
- Pair plots examining relationships between service metrics and demographic variables
- Temporal analysis by hour and poverty level across boroughs

### 3. Machine Learning Pipeline
- **Target variable:** Trips per capita
- **Features:** Vehicle ownership, transit usage, labor force participation, commute patterns, population density
- **Models:** Ridge Regression and Random Forest
- **Equity analysis:** Correlation of residuals with poverty rate, low-income percentage, and minority percentage

## Key Visualizations

- Trip count choropleths by vehicle type
- Fare per mile by zone
- Pair plots of service metrics vs. demographic variables
- Hourly demand patterns by poverty bin and borough
- Residual analysis scatter plots

## Results

| Analysis | Finding |
|----------|---------|
| Bivariate EDA | No significant correlation between poverty and trips per capita (R² = 0.01) |
| ML Residuals | No systematic relationship between residuals and equity variables |
| Wait Times | No evidence of longer wait times in lower-income zones |

## Usage

1. Run `01_data_cleaning.ipynb` to process raw TLC and Census data
2. Run `02_data_exploration.ipynb` to generate EDA visualizations
3. Run `03_ml_underservice_detection.ipynb` to fit models and analyze residuals

## Author

Daniel Anzures Fernández