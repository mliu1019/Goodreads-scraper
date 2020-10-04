# FA20 CS242 Assignment 2

Assignment 2 of CS 242 Class Fall 2020. The assignment implements a scraper for Goodreads.com. The current version is implemented in Python 3.7.3.

## Tool
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  >=4.9.0

## Run
* `python3 main.py -h`
  * The command brings up usage information and a list of options you can use with the scraper.
* `python3 main.py [-h] --url  [--nbook] [--nauthor]`
  * `--url`       URL to begin, required.
  * `--nbook`     Number of books to scrape, optional. Default to 200.
  * `--nauthor`   Number of authors to scrape, optional. Default to 50.

## Test 
* `python3 test.py -h`
  * The command runs unit tests on the scraper.

### Resources:
- [Repo](https://gitlab.engr.illinois.edu/minerl2/fa20-cs242-assignment2)
