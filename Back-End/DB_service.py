import csv, sqlite3
# on server intialize
wikir = sqlite3.connect( "Back-End/wikir.db" )
wikirFr = sqlite3.connect( "Back-End/wikir-French.db" )

def get_docs_english(id_, cur=wikir):
  args = (id_,)
  wikir = cur.execute("SELECT * FROM wikir WHERE doc_id = ?", args).fetchall()
  if len(wikir) > 0:
    wikir = dict({'doc_id': wikir[0][0], 'text': wikir[0][1]})
    return wikir
  return -1
 

def get_all_docs_english(cur=wikir):
  return cur.execute("SELECT * FROM wikir").fetchall()

def get_document_french(id_, cur=wikirFr):
  args = (id_,)
  Frwikir = cur.execute("SELECT * FROM wikir-French WHERE doc_id = ?", args).fetchall()
  print(Frwikir)
  print(len(Frwikir))
  if len(Frwikir) > 0:
    Frwikir = dict({'doc_id': Frwikir[0][0], 'text': Frwikir[0][1]})
    return Frwikir
  return -1
 

def get_all_documents_french(cur=Frwikir):
  return cur.execute("SELECT * FROM wikir-French").fetchall()
