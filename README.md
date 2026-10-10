# Google Maps Lead Generation Scraper

A lightweight and efficient Python script built with **Playwright** to automate local business data collection from Google Maps. 

Designed to help with lead generation by extracting structured contact information based on custom search queries and locations.

## Features

- **Automated Browser Navigation:** Uses Playwright to interact with Google Maps dynamically (searching, scrolling through results, and clicking individual listings)[cite: 1].
- **Data Extraction:** Automatically pulls key business details:
  - Business Name[cite: 1]
  - Google Maps Profile URL[cite: 1]
  - Address[cite: 1]
  - Phone Number[cite: 1]
- **Structured Export:** Cleans the extracted text and outputs it directly into a formatted CSV file (`leads.csv`) using a semicolon delimiter for easy Excel/Google Sheets compatibility[cite: 1].

## Tech Stack

- **Python 3.x**
- **Playwright** (Python sync API)[cite: 1]
- **Built-in CSV module**[cite: 1]

## Prerequisites & Installation

1. Make sure you have Python installed.
2. Install the required dependencies:
   ```bash
   pip install playwright
   Install the browser binaries for Playwright:
    Bash

    playwright install

How to Run

    Open the script (gmap_job.py) and modify the search query if needed (default is set to local coffee shops as an example)[cite: 1]:
    Python

    page.fill("input.UGojuc", "Your Search Query Here")

    Run the script:
    Bash

    python gmap_job.py

    Once finished, the results will be saved locally in leads.csv[cite: 1].
