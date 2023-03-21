import pytest
from Linkedin_Scrapper import scrape_linkedin_jobs


def test_scrape_linkedin_jobs_returns_list():
    """
    Test that the scrape_linkedin_jobs function returns a list.
    """
    results = scrape_linkedin_jobs("software engineer", "san francisco")
    assert isinstance(results, list)


def test_scrape_linkedin_jobs_returns_jobs():
    """
    Test that the scrape_linkedin_jobs function returns a list of job dictionaries.
    """
    results = scrape_linkedin_jobs("software engineer", "san francisco")
    assert all(isinstance(job, dict) for job in results)


def test_scrape_linkedin_jobs_job_details():
    """
    Test that each job dictionary returned by scrape_linkedin_jobs contains
    the keys "title", "company", "location", "link", and "description".
    """
    job_keys = ["title", "company", "location", "link", "description"]
    results = scrape_linkedin_jobs("software engineer", "san francisco")
    for job in results:
        assert all(key in job for key in job_keys)


def test_scrape_linkedin_jobs_pages():
    """
    Test that the scrape_linkedin_jobs function returns at least one job
    when passed the "pages" argument.
    """
    results = scrape_linkedin_jobs("software engineer", "san francisco", pages=2)
    assert len(results) > 0


def test_scrape_linkedin_jobs_job_titles():
    """
    Test that the titles of all jobs returned by scrape_linkedin_jobs contain the
    search query passed in the "job_title" argument.
    """
    job_title = "software engineer"
    results = scrape_linkedin_jobs(job_title, "san francisco")
    assert all(job_title.lower() in job["title"].lower() for job in results)


def test_scrape_linkedin_jobs_job_locations():
    """
    Test that the locations of all jobs returned by scrape_linkedin_jobs contain the
    search query passed in the "location" argument.
    """
    location = "san francisco"
    results = scrape_linkedin_jobs("software engineer", location)
    assert all(location.lower() in job["location"].lower() for job in results)
