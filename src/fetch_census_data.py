from dotenv import load_dotenv
import os
from census import Census
import pandas as pd
from pathlib import Path

load_dotenv()

RAW_DIR = Path("input/raw")
CENSUS_DIR = RAW_DIR / "census"

api_key = os.getenv('CENSUS_API_KEY')
c = Census(api_key)

# NYC county FIPS codes
nyc_counties = ['061', '047', '081', '005', '085']

# County FIPS to borough name mapping
county_names = {
    '061': 'Manhattan',
    '047': 'Brooklyn',
    '081': 'Queens',
    '005': 'Bronx',
    '085': 'Staten Island'
}

# Fields to fetch for analysis
fields = [
    # Population / poverty
    "B01003_001E",
    "B17001_002E",

    # Income brackets
    "B19001_002E","B19001_003E","B19001_004E","B19001_005E","B19001_006E",
    "B19001_007E","B19001_008E","B19001_009E","B19001_010E","B19001_011E","B19001_012E",
    "B19001_013E","B19001_014E","B19001_015E","B19001_016E","B19001_017E",

    # Households & vehicles
    "B08201_001E",
    "B08201_002E",

    # Means of transportation to work
    "B08301_001E","B08301_002E","B08301_003E","B08301_004E","B08301_010E",
    "B08301_016E","B08301_017E","B08301_018E","B08301_019E","B08301_020E","B08301_021E",

    # Travel time to work
    "B08303_001E","B08303_002E","B08303_003E","B08303_004E","B08303_005E","B08303_006E",
    "B08303_007E","B08303_008E","B08303_009E","B08303_010E","B08303_011E","B08303_012E","B08303_013E",

    # Employment status
    "B23025_001E","B23025_002E","B23025_003E","B23025_004E","B23025_005E","B23025_006E","B23025_007E",

    # Race/Ethnicity
    "B03002_001E","B03002_003E","B03002_004E","B03002_005E","B03002_006E",
    "B03002_007E","B03002_008E","B03002_009E","B03002_012E",

    # Disability
    "C18108_001E"
]

# Taking data from acs5
data = []
for county in nyc_counties:
    result = c.acs5.state_county_tract(
        fields=fields,
        state_fips='36', # New York
        county_fips=county,
        tract='*', # All Tracts
        year=2023 # Latest year for acs5
    )
    data.extend(result)

# Convert to DataFrame
df = pd.DataFrame(data)

# Rename columns to be readable
df = df.rename(columns={
    # Population
    'B01003_001E': 'total_population',
    'B17001_002E': 'population_below_poverty',

    # Income brackets
    'B19001_002E': 'hh_income_under_10k',
    'B19001_003E': 'hh_income_10k_to_15k',
    'B19001_004E': 'hh_income_15k_to_20k',
    'B19001_005E': 'hh_income_20k_to_25k',
    'B19001_006E': 'hh_income_25k_to_30k',
    'B19001_007E': 'hh_income_30k_to_35k',
    'B19001_008E': 'hh_income_35k_to_40k',
    'B19001_009E': 'hh_income_40k_to_45k',
    'B19001_010E': 'hh_income_45k_to_50k',
    'B19001_011E': 'hh_income_50k_to_60k',
    'B19001_012E': 'hh_income_60k_to_75k',
    'B19001_013E': 'hh_income_75k_to_100k',
    'B19001_014E': 'hh_income_100k_to_125k',
    'B19001_015E': 'hh_income_125k_to_150k',
    'B19001_016E': 'hh_income_150k_to_200k',
    'B19001_017E': 'hh_income_200k_plus',

    # Households & Vehicles
    'B08201_001E': 'total_households',
    'B08201_002E': 'households_no_vehicle',

    # Means of transportation to work
    'B08301_001E': 'commuters_total',
    'B08301_002E': 'commute_car_truck_van',
    'B08301_003E': 'commute_drove_alone',
    'B08301_004E': 'commute_carpooled',
    'B08301_010E': 'commute_public_transit',
    'B08301_016E': 'commute_taxi',
    'B08301_017E': 'commute_motorcycle',
    'B08301_018E': 'commute_bicycle',
    'B08301_019E': 'commute_walked',
    'B08301_020E': 'commute_other',
    'B08301_021E': 'commute_work_from_home',

    # Travel time to work
    'B08303_001E': 'travel_time_total',
    'B08303_002E': 'travel_time_under_5min',
    'B08303_003E': 'travel_time_5_to_9min',
    'B08303_004E': 'travel_time_10_to_14min',
    'B08303_005E': 'travel_time_15_to_19min',
    'B08303_006E': 'travel_time_20_to_24min',
    'B08303_007E': 'travel_time_25_to_29min',
    'B08303_008E': 'travel_time_30_to_34min',
    'B08303_009E': 'travel_time_35_to_39min',
    'B08303_010E': 'travel_time_40_to_44min',
    'B08303_011E': 'travel_time_45_to_59min',
    'B08303_012E': 'travel_time_60_to_89min',
    'B08303_013E': 'travel_time_90min_plus',

    # Employment status
    'B23025_001E': 'pop_16_plus',
    'B23025_002E': 'in_labor_force',
    'B23025_003E': 'civilian_labor_force',
    'B23025_004E': 'employed',
    'B23025_005E': 'unemployed',
    'B23025_006E': 'armed_forces',
    'B23025_007E': 'not_in_labor_force',

    # Race/Ethnicity
    'B03002_001E': 'race_total',
    'B03002_003E': 'race_white_alone',
    'B03002_004E': 'race_black_alone',
    'B03002_005E': 'race_american_indian_alone',
    'B03002_006E': 'race_asian_alone',
    'B03002_007E': 'race_pacific_islander_alone',
    'B03002_008E': 'race_other_alone',
    'B03002_009E': 'race_two_or_more',
    'B03002_012E': 'ethnicity_hispanic_latino',

    # Disability
    'C18108_001E': 'population_with_disability',
})

# Create GEOID
df['geoid'] = '36' + df['county'] + df['tract']

# Add borough name
df['borough'] = df['county'].map(county_names)

# Save to parquet
df.to_parquet(CENSUS_DIR / 'nyc_census_tracts.parquet', engine="pyarrow", index=False)

print(f"Saved {len(df)} census tracts to {CENSUS_DIR / 'nyc_census_tracts.parquet'}")