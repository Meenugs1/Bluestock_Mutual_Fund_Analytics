import requests
import pandas as pd

# Mutual fund scheme codes
scheme_codes = {
    "SBI Large Cap Fund - Direct Growth": 119598,
    "ICICI Prudential Large Cap Fund - Direct Growth": 120586,
    "Nippon India Large Cap Fund - Direct Growth": 118632,
    "Axis Large Cap Fund - Direct Growth": 120465,
    "Kotak Large Cap Fund - Direct Growth": 120152
}

# Fetch NAV data for each mutual fund
for scheme_name, scheme_code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        actual_scheme_name = data["meta"]["scheme_name"]

        print("\nRequested:", scheme_name)
        print("API returned:", actual_scheme_name)

        # Convert NAV data into a DataFrame
        nav_df = pd.DataFrame(data["data"])

        # Save NAV data to CSV
        output_file = f"data/raw/live_nav_{scheme_code}.csv"
        nav_df.to_csv(output_file, index=False)

        print("NAV data saved successfully!")
        print("File location:", output_file)
        print("Total records:", len(nav_df))

    else:
        print(f"Failed to fetch {scheme_name}: {response.status_code}")