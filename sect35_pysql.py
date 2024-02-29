""" 
    "import sqlite3" module
        - sqlite3.connect(filename.db) - creates a connection to sqlite3 and upserts similarly to sqlite3's .open filename.db, returning a connection object and cursor method
        - connect().cursor() - creates cursor object with access to all cursor methods that must be used sequentially like so (see example A):
            1) cursor.execute(query, tuple) - execute some sql
            2) connection.commit() - always used except when creating table
            3) connection.close() - closes connection to the connected db
        - cursor.executemany(query, list of tuples) - bulk inserts (see example C)
        - cursor.fetchall() - after executing a select, we can loop over the connetion object since its an iterator or use fetchall which returns a list of tuples
        - cursor.fetchone() - returns one tuple after executing a select
    
    SQL Injection
        -instead sql injection, we must pass in tuples and f-string should contain "?" instead (see example B)
        - this prevents mallicious sql injection into the query such as "WHERE name = '' OR 1=1 --'"
        - "OR 1=1" - makes everything true since OR only needs one condition to make the entire WHERE true
        - "--" - tricks SQL to comment our last quote in sql injection
"""
import sqlite3

# example A: create a databse within it, a friends tables with first_name, last_name, rate of friendship closeness
def create_db(db_name, table_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f'CREATE TABLE {table_name} (first_name TEXT, last_name TEXT, closeness INTEGER);')
    cursor.close()

# create_db('../friends_db.db', 'friends')

# example B: insert a row into table
def insert_row(db_name, table_name, first_name, last_name, closeness = 0):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    
    query = f'INSERT INTO {table_name} VALUES (?,?,?);'
    cursor.execute(query, (first_name, last_name, closeness))
    
    connection.commit()
    connection.close()

# insert_row('../friends_db.db', 'friends', 'Steve', 'Irwin')

# example C: bulk insert
def insert_rows(db_name, table_name, list_of_tuples):
    connection = sqlite3.connect(db_name)
    c = connection.cursor()
    
    # of course we can do for loop and execute() but we should reserve it for when calculations are needed
    query = f'INSERT INTO {table_name} VALUES (?,?,?);'
    c.executemany(query, list_of_tuples)
    
    connection.commit()
    connection.close()
    
""" 
insert_rows('../friends_db.db', 'friends',[
	("Roald","Amundsen", 5),
	("Rosa", "Parks", 8),
	("Henry", "Hudson", 7),
	("Neil","Armstrong", 7),
	("Daniel", "Boone", 3)
])
"""

# using requests and BeautifulSoup, scrape from https://books.toscrape.com/catalogue/category/books/history_32/index.html
def create_book_db(url, db_name): 
    import requests
    from bs4 import BeautifulSoup

    def scrape_books(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article')
        all_books = []
        
        for book in books:
            all_books.append((get_title(book), get_price(book), get_rating(book)))

        save_books(db_name, all_books)

    def save_books(db_name, all_books):
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute('CREATE TABLE books (title TEXT, price REAL, rating INTEGER)')
        c.executemany('INSERT INTO books VALUES (?,?,?)', all_books)
        conn.commit()
        conn.close()
    
    def get_title(book):
        return book.find('h3').find('a')['title']
    
    def get_price(book):
        price = book.select(".price_color")[0].get_text()
        return float(price.replace("£","").replace("Â",""))

    def get_rating(book):
        ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        paragraph = book.select(".star-rating")[0]
        word = paragraph.get_attribute_list("class")[-1]
        return ratings[word]
    
    scrape_books(url)

# create_book_db("http://books.toscrape.com/catalogue/category/books/history_32/index.html", '../scraped_books.db')

def get_scraped_books():
    conn = sqlite3.connect('../scraped_books.db')
    c = conn.cursor()
    
    query = f'SELECT * FROM books WHERE rating=? AND price<?'
    c.execute(query, (5, 50))
    books = c.fetchall()
    
    conn.commit()
    conn.close()

    print(books)

get_scraped_books()