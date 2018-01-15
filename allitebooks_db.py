#!/usr/bin/python3
# Author : Mrinal Sinha

"""
    Python Script to download all the ebooks from 
    'allitebooks.com' into a mysqlite database.
"""

from lxml.html import fromstring
from requests  import get
from sqlite3   import connect
from tqdm      import tqdm
from os        import path, makedirs

# Helper Function
def create_path(location):
    dirname = path.dirname(path.abspath(location))
    if not path.exists(dirname):
        makedirs(dirname)
    elif not path.isdir(dirname):
        raise RuntimeError('Invalid Path "%s"' % location)

html = get('http://www.allitebooks.com/')
html = fromstring(html.text)

db_schema = """
    CREATE TABLE IF NOT EXIST ebooks_index (
        category      CHAR,
        book_name     CHAR,
        cover_img     CHAR,
        authors       CHAR,
        isbn          CHAR,
        year          CHAR,
        pages         CHAR,
        description   CHAR,
        language      CHAR,
        file_size     CHAR,
        file_format   CHAR,
        categories    CHAR,
        download_link CHAR );
"""



# def index():
#     with open(FILE_NAME, 'w') as csvfile:
#         write = writer(csvfile)
#         write.writerow(['Category', 'Title', 'Author(s)', 'ISBN', 'Year', 'Cover_Image', 'Description',
#                         'Pages', 'Categories', 'Language', 'File_Size', 'File_Format', 'Download_Link'])

#         categories_title = html.xpath('//*[@id="side-content"]/ul/li/a/text()')
#         categories_link  = html.xpath('//*[@id="side-content"]/ul/li/a/@href')
#         category         = dict(zip(categories_title, categories_link))

#         for c_title, link in tqdm(category.items(), 'Categories'):
#             category_html = get(link)
#             category_html = fromstring(category_html.text)
#             pages = int(category_html.xpath('//*[@id="main-content"]/div/div/a[last()]/text()')[0])
            
#             for page in tqdm(range(pages), c_title):
#                 books = get(link + 'page/{}/'.format(page+1))
#                 books = fromstring(books.text)
#                 books_link = books.xpath('//*[@id="main-content"]//header/h2/a/@href')
                
#                 for each_book in tqdm(books_link, 'Page - {}'.format(page+1)):
#                     book = get(each_book)
#                     book = fromstring(book.text)

#                     def get_value(name, link = None):
#                         header_details = book.xpath('//*[@id="main-content"]/div/article/header')[0]
#                         if name is 'title': return (header_details.xpath('./h1/text()') or [''])[0]
#                         if name is 'dlink': return (book.xpath('//span[@class="download-links"]/a[contains\
#                                                     (@href, "file.allitebooks.com")]/@href') or [''])[0]
#                         if name is 'cover': return (header_details.xpath('.//div/a/img/@src') or [''])[0]
#                         if name is 'descr':
#                             desc = book.xpath('//div[@class="entry-content"]//text()')
#                             return ' '.join([x for x in [x.strip() for x in desc]])
#                         if link: return ', '.join([x for x in (header_details.xpath('.//*[text() = "{}"]\
#                                             /following-sibling::dd[1]/a/text()'.format(name)) or [''])])
#                         return (header_details.xpath('.//*[text() = "{}"]/following-sibling::dd[1]//text()'.format(name)) or [''])[0]

#                     category      = c_title
#                     book_name     = get_value('title')
#                     cover_img     = get_value('cover')
#                     authors       = get_value('Author:', link = True)
#                     isbn          = get_value('ISBN-10:')
#                     year          = get_value('Year:')
#                     pages         = get_value('Pages:')
#                     description   = get_value('descr')
#                     language      = get_value('Language:')
#                     file_size     = get_value('File size:')
#                     file_format   = get_value('File format:')
#                     categories    = get_value('Category:', link = True)
#                     download_link = get_value('dlink')

#                     write.writerow([category, book_name, authors, isbn, year, cover_img, description,
#                                     pages, categories, language, file_size, file_format, download_link])