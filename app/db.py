from peewee import PostgresqlDatabase

# Connect to a Postgres database.
database = PostgresqlDatabase(
    'railway', 
    user='postgres', 
    password='SWU4WDBLXQLX6iz0Mnmk',
    host='containers-us-west-118.railway.app', 
    port=7611
)

def conect_db()-> PostgresqlDatabase:
    if database.is_closed():
        database.connect()
    return database

def disconnect_db()->None:
    if not database.is_closed():
      database.close()
