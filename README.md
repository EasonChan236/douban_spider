# Douban_spider
Spider to obtain data from www.douban.com

# python get_link.py 
  Generate a file, containing links to all the books we could reach in the douban website: 
  
  Start from https://book.douban.com/tag/?view=type&icn=index-sorttags-all.
  Go into each tag pages.
  Obtain links to each book's information page. Mostly 50 pages for a tag.
  
  Store all the link we obtained in a file.
  
# python spider_main.py
  Read each line of file we created last step and get the link to information page.
  Parsed the page information using BeautifulSoup and regular expression.
  Output the information of each book to a file.
