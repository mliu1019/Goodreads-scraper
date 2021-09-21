# Goodreads Scraper

The project implements a scraper for Goodreads.com. The current version is implemented in Python 3.7.3.

## Tool
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  >=4.9.0

## Run
* `python3 main.py -h`
  * The command brings up usage information and a list of options you can use with the scraper.
* `python3 main.py [-h] --url  [--nbook] [--nauthor]`
  * `--url`       URL to begin, required.
  * `--nbook`     Number of books to scrape, optional. Default to 200.
  * `--nauthor`   Number of authors to scrape, optional. Default to 50.
* `python3 extra.py`
  * The command generates a graph based on scraping results.
* `python3 app.py`
  * The command runs the web app for HTML rendering.
* `python3 visualization.py`
  * The command runs the visualizations.

## Test 
* `python3 test.py`
  * The command runs unit tests. Because the database is hosted on Cloud, to test locally, please set up the database locally.

### Resources:
- [Repo](https://github.com/mliu1019/Goodreads-scraper)
