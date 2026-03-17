from jobspy import scrape_jobs
import pandas as pd

# This setup pulls all possible data points
jobs = scrape_jobs(
    site_name=["linkedin", "indeed", "glassdoor", "zip_recruiter"],
    search_term="software engineer",
    location="Remote",
    results_wanted=2000,
    
    # CRITICAL: These flags fetch the 'extra' data
    linkedin_fetch_description=True, # Gets full description & direct URL
    enforce_annual_salary=True,      # Normalizes all salary data to annual
    description_format="markdown",   # Makes description text readable
)

# Show ALL columns (prevents Pandas from hiding data with "...")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Print a list of all data fields you just captured
print("All available data fields:", jobs.columns.tolist())

# Save EVERYTHING to a file
jobs.to_csv("all_job_data.csv", index=False)