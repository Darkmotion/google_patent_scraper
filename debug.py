from example.readme_example.readme import patent_1
from google_patent_scraper import scraper_class

def main():
    scraper = scraper_class()
    patent_1 = 'US10918145'
    err_1, soup_1, url_1 = scraper.request_single_patent(patent_1)

    patent_1_parsed = scraper.get_scraped_data(soup_1, patent_1, url_1)

    # ~ Print abstract text ~ #
    print(patent_1_parsed)


if __name__ == '__main__':
    main()