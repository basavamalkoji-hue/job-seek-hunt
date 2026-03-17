from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter"],
    search_term="software engineer",
    location="San Francisco, CA",
    results_wanted=20,
    hours_old=72,  # Only get jobs posted in the last 3 days
)

# See the results
print(f"Found {len(jobs)} jobs")
print(jobs.head())

# Save to a file
jobs.to_csv("jobs.csv", index=False)