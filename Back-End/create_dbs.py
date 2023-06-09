import csv, sqlite3
import os

def create_comments_sqlite_database():
  print(os.listdir("."))
  if "wikir.db" in os.listdir("."):
    return
  cur = sqlite3.connect( "wikir.db" )
  cur.text_factory = str
  cur.execute('CREATE TABLE IF NOT EXISTS wikir (doc_id VARCHAR, text VARCHAR)')
  reader = csv.reader(open("wikir.csv", "r"))
  for id, doc_id, test in reader:
    print('.', end="")
    cur.execute('INSERT OR IGNORE INTO wikir (doc_id, text) VALUES (?,?)', (doc_id, test))
  cur.commit()
  cur.close()

def create_documents_sqlite_database():
  print(os.listdir("."))
  if "wikir-French.db" in os.listdir("."):
    return
  cur = sqlite3.connect( "wikir-French.db" )
  cur.text_factory = str  #bugger 8-bit bytestrings
  cur.execute('CREATE TABLE IF NOT EXISTS wikir-French (doc_id VARCHAR ,title VARCHAR ,text VARCHAR)')
  reader = csv.reader(open("wikir-French.csv", "r"))
  for id, doc_id, title, text in reader:
    print(".", end="")
    cur.execute('INSERT OR IGNORE INTO wikir-French (doc_id, title, text) VALUES (?,?, ?)', (doc_id, title, text))
  cur.commit()
  cur.close()

