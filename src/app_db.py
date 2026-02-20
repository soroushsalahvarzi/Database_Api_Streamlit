import sqlite3

DB_NAME = 'MoviesInfo2.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.commit()
    conn.close()

#init_db()
def create_table():
    query = '''
            CREATE TABLE IF NOT EXISTS Movie
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            year TEXT,
            country TEXT,
            imdb_rate TEXT,
            genres TEXT
            )
            '''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

create_table()
def insert_movie(title, year, country, imdb_rate, genres):
    query = '''INSERT INTO Movie (title, year, country, imdb_rate, genres)
    VALUES(?, ?, ?, ?, ?)
    '''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, (title, year, country, imdb_rate, genres))
    conn.commit()
    conn.close()
insert_movie('The Godfather', '1972', 'USA', '9.2', 'Dram')
def select_all_records():
    query = 'SELECT * FROM Movie'
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    result = cursor.execute(query).fetchall()
    conn.close()
    return result
def select_record_by_id(id):
    query = 'SELECT * FROM Movie WHERE id=?'
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    result = cursor.execute(query, (id,)).fetchone()
    conn.close()
    return result
# # print(select_all_records())
# # print(select_record_by_id(1))
def delete_record_by_id(id):
    query = 'delete FROM Movie WHERE id=?'
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()
    # return 'DONE'
def update_record_by_id(id, imdb_rate, year):
    query = 'UPDATE Movie SET imdb_rate=?, year=? WHERE id = ?'
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, (imdb_rate, year, id))
    conn.commit()
    conn.close()

# update_record_by_id(2, '8.5', '2003')
# print(select_all_records())