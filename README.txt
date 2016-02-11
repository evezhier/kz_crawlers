
Hi!
This is a Scrapy project (http://scrapy.org/)

It includes two crawlers for scraping articles from:

http://prodengi.kz/lenta/ (crawler_name: dengispider)
http://investfunds.kz/markes/ (crawler_name: investspider)

Before you run the crawlers ensure that Scrapy is installed in your system 
(follow the link above for installation instructions)

Run in terminal:
$ scrapy crawl <crawler_name> -t csv -o <output_file_path>