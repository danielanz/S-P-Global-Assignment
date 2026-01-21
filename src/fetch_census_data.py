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

data = []
for county in nyc_counties:
    result = c.acs5.state_county_tract(
        fields=['B01003_001E',  # Total population
                'B19013_001E',  # Median household income
                'B08201_001E',  # Total households
                'B08201_002E'], # Households with no vehicle
        state_fips='36',
        county_fips=county,
        tract='*',
        year=2023
    )
    data.extend(result)

# Convert to DataFrame
df = pd.DataFrame(data)

# Rename columns to be readable
df = df.rename(columns={
    'B01003_001E': 'total_population',
    'B19013_001E': 'median_household_income',
    'B08201_001E': 'total_households',
    'B08201_002E': 'households_no_vehicle'
})

# Create GEOID for tract (state + county + tract)
df['geoid'] = df['state'] + df['county'] + df['tract']

# Add borough name
df['borough'] = df['county'].map(county_names)

# Save to CSV
df.to_csv(CENSUS_DIR / 'nyc_census_tracts.csv', index=False)

print(f"Saved {len(df)} census tracts to {CENSUS_DIR / 'nyc_census_tracts.csv'}")