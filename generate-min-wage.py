import pandas as pd

# Creating a list of dictionaries for each state with relevant info
minimum_wages = [
    {"State": "Alaska", "Minimum Wage": 11.91, "Premium Pay": "Daily - 8, Weekly - 40"},
    {"State": "American Samoa", "Minimum Wage": "Special rates", "Premium Pay": ""},
    {"State": "Arizona", "Minimum Wage": 14.70, "Premium Pay": ""},
    {"State": "Arkansas", "Minimum Wage": 11.00, "Premium Pay": "Weekly - 40"},
    {"State": "California", "Minimum Wage": 16.50, "Premium Pay": "Daily - 8 (1.5x), 12 (2x); Weekly - 40; 7th day"},
    {"State": "Colorado", "Minimum Wage": 14.81, "Premium Pay": "Daily - 12, Weekly - 40"},
    {"State": "Connecticut", "Minimum Wage": 16.35, "Premium Pay": "Weekly - 40"},
    {"State": "Delaware", "Minimum Wage": 15.00, "Premium Pay": ""},
    {"State": "District of Columbia", "Minimum Wage": 17.50, "Premium Pay": "Weekly - 40"},
    {"State": "Florida", "Minimum Wage": 13.00, "Premium Pay": ""},
    {"State": "Georgia", "Minimum Wage": 5.15, "Premium Pay": ""},
    {"State": "Guam", "Minimum Wage": 9.25, "Premium Pay": "Weekly - 40"},
    {"State": "Hawaii", "Minimum Wage": 14.00, "Premium Pay": "Weekly - 40"},
    {"State": "Idaho", "Minimum Wage": 7.25, "Premium Pay": ""},
    {"State": "Illinois", "Minimum Wage": 15.00, "Premium Pay": "Weekly - 40"},
    {"State": "Indiana", "Minimum Wage": 7.25, "Premium Pay": "Weekly - 40"},
    {"State": "Iowa", "Minimum Wage": 7.25, "Premium Pay": ""},
    {"State": "Kansas", "Minimum Wage": 7.25, "Premium Pay": ""},
    {"State": "Kentucky", "Minimum Wage": 7.25, "Premium Pay": "Weekly - 40, 7th day"},
    {"State": "Louisiana", "Minimum Wage": "No state law", "Premium Pay": ""},
    {"State": "Maine", "Minimum Wage": 14.65, "Premium Pay": "Weekly - 40"},
    {"State": "Maryland", "Minimum Wage": 15.00, "Premium Pay": "Weekly - 40"},
    {"State": "Massachusetts", "Minimum Wage": 15.00, "Premium Pay": "Weekly - 40"},
    {"State": "Michigan", "Minimum Wage": 10.56, "Premium Pay": "Weekly - 40"},
    {"State": "Minnesota", "Minimum Wage": 11.13, "Premium Pay": "Weekly - 48"},
    {"State": "Mississippi", "Minimum Wage": "No state law", "Premium Pay": ""},
    {"State": "Missouri", "Minimum Wage": 13.75, "Premium Pay": "Weekly - 40"},
    {"State": "Montana", "Minimum Wage": "10.55 (> $110k); $4.00 (≤ $110k)", "Premium Pay": "Weekly - 40"},
    {"State": "Nebraska", "Minimum Wage": 13.50, "Premium Pay": ""},
    {"State": "Nevada", "Minimum Wage": 12.00, "Premium Pay": "Daily - 8 (if <1.5x), Weekly - 40"},
    {"State": "New Hampshire", "Minimum Wage": 7.25, "Premium Pay": "Weekly - 40"},
    {"State": "New Jersey", "Minimum Wage": 15.49, "Premium Pay": "Weekly - 40"},
    {"State": "New Mexico", "Minimum Wage": 12.00, "Premium Pay": "Weekly - 40"},
    {"State": "New York", "Minimum Wage": "16.50 (NYC/Metro); 15.50 (elsewhere)", "Premium Pay": "Weekly - 40"},
    {"State": "North Carolina", "Minimum Wage": 7.25, "Premium Pay": "Weekly - 40"},
    {"State": "North Dakota", "Minimum Wage": 7.25, "Premium Pay": "Weekly - 40"},
    {"State": "Northern Mariana Islands", "Minimum Wage": 7.25, "Premium Pay": ""},
    {"State": "Ohio", "Minimum Wage": "10.70 (≥ $394k); $7.25 (< $394k)", "Premium Pay": "Weekly - 40"},
    {"State": "Oklahoma", "Minimum Wage": "7.25 (≥ $100k or 10+ FT); $2.00 (others)", "Premium Pay": ""},
    {"State": "Oregon", "Minimum Wage": "13.70–15.95", "Premium Pay": "Weekly - 40, Daily - 10 (some industries)"},
    {"State": "Pennsylvania", "Minimum Wage": 7.25, "Premium Pay": "Weekly - 40"},
    {"State": "Puerto Rico", "Minimum Wage": 10.50, "Premium Pay": "Daily - 8, Weekly - 40"},
    {"State": "Rhode Island", "Minimum Wage": 15.00, "Premium Pay": "Weekly - 40"},
    {"State": "South Carolina", "Minimum Wage": "No state law", "Premium Pay": ""},
    {"State": "South Dakota", "Minimum Wage": 11.50, "Premium Pay": ""},
    {"State": "Tennessee", "Minimum Wage": "No state law", "Premium Pay": ""},
    {"State": "Texas", "Minimum Wage": 7.25, "Premium Pay": ""},
    {"State": "Utah", "Minimum Wage": 7.25, "Premium Pay": ""},
    {"State": "Vermont", "Minimum Wage": 14.01, "Premium Pay": "Weekly - 40"},
    {"State": "Virgin Islands", "Minimum Wage": 10.50, "Premium Pay": "Daily - 8, Weekly - 40"},
    {"State": "Virginia", "Minimum Wage": 12.41, "Premium Pay": ""},
    {"State": "Washington", "Minimum Wage": 16.66, "Premium Pay": "Weekly - 40"},
    {"State": "West Virginia", "Minimum Wage": 8.75, "Premium Pay": "Weekly - 40"},
    {"State": "Wisconsin", "Minimum Wage": 7.25, "Premium Pay": "Weekly - 40"},
    {"State": "Wyoming", "Minimum Wage": 5.15, "Premium Pay": ""},
]

# Convert to DataFrame
df = pd.DataFrame(minimum_wages)

# Save as spreadsheet
file_path = "./Minimum_Wage_By_State.xlsx"
df.to_excel(file_path, index=False)

file_path

