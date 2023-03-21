# LinkedIn Job Scraper
This Python script allows you to scrape job listings from LinkedIn based on a job title and location. It uses the Selenium web driver and BeautifulSoup to scrape the job postings and store the results in a list of dictionaries, where each dictionary represents a job listing with the following keys: 'title', 'company', 'location', 'link', and 'description'.

# Prerequisites
Before using this script, you need to install the following Python packages:

- Selenium
- BeautifulSoup
- Pandas

You also need to download the Chrome web driver from the following link:

https://sites.google.com/a/chromium.org/chromedriver/downloads

> Make sure to choose the appropriate version for your operating system and Chrome browser.

# Usage
To use this script, you need to provide the following arguments:

job_title: the job title to search for on LinkedIn

location: the location to search for jobs in on LinkedIn


pages: the number of pages of job listings to scrape (optional, default is 1)

### Here's an example of how to use the script:

```python
job_title = "data scientist"
location = "New York City"
pages = 3

jobs = scrape_linkedin_jobs(job_title, location, pages)
```

This will scrape the first 3 pages of job listings for "data scientist" jobs in "New York City" and store the results in a list of dictionaries called "jobs".

# Output
The output of this script is a list of dictionaries, where each dictionary represents a job listing with the following keys:

| Field        | Description                                      |
|--------------|--------------------------------------------------|
| title        | the job title                                    |
| company      | the name of the company offering the job         |
| location     | the location of the job                          |
| link         | the URL to apply for the job                      |
| description  | the description of the job (if available)         |

# Run Tests
The project has a test_linked_scraper.py file that uses pytest to test the code. To run the tests, you need to install pytest using pip. Here are the steps:

1. Open a command prompt or terminal window.
2. Change the directory to the location of the project.
3. Install pytest by running the following command:

```bash
pip install pytest
```

4. Run the tests by running the following command:

```bash
pytest test_linked_scraper.py
```

This will run all the tests in the test_linked_scraper.py file and display the results in the command prompt or terminal window.

