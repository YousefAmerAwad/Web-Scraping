# Web-Scraping
## Introduction
Imagine you have to pull a large amount of data from websites and you want to do it as quickly as possible. How would you do it without manually going to each website and getting the data? Well, “Web Scraping” is the answer. Web Scraping just makes this job easier and faster. 

Web scraping is an automated method used to extract large amounts of data from websites. The data on the websites are unstructured. Web scraping helps collect these unstructured data and store it in a structured form. There are different ways to scrape websites such as online Services, APIs or writing your own code. In this article, we’ll see how to implement web scraping with python. 

There is no universal solution for web scraping because the way data is stored on each website is usually specific to that site. In fact, if you want to scrape the data, you need to understand the website’s structure.

This website will give you more information about web scraping https://realpython.com/beautiful-soup-web-scraper-python/ <br>



## Project Description
In this project we will scrape data from two websites.
- Wuzzuf: It's an online employment platform that helps people to find Jobs in Egypt and Middle East. We will search for available data science jobs. For each job we will find job title, company name, location, skills, requirements and salary. Then we put these information in a csv file. <br>
The URL of the page: https://wuzzuf.net/search/jobs/?a=hpb&q=data%20science

- Oasis Cars: A trusted name among locals and expats communities in Qatar founded in (1997) in buying and selling new and used cars. For each car, we will find Model, Year, Show_Room, Mileage, Specs and Price. <br>
URL: https://oasiscars.com/Cars/List

In this project, we will use Python for scraping because of its ease. It has a library known as 'Beautiful Soup' which assists this task.
## Libraries used for Web Scraping 
- <b> BeautifulSoup</b>:  Beautiful Soup is a Python package for parsing HTML and XML documents. It creates parse trees that is helpful to extract the data easily.
- <b> requests</b>: With Python's requests library we're getting a web page by using get() on the URL, using page.content will give us the HTML. Once we have the HTML we can then parse it for the data we're interested in analyzing.
- <b> xlml</b>: A feature-rich library for processing XML and HTML
- <b> itertools</b>: From this module, we need to import zip_longest function. This function makes an iterator that aggregates elements from each of the iterables. The iteration continues until the longest iterable is not exhausted.

