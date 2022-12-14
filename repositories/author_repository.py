from db.run_sql import run_sql

from models.author import Author

def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    return results

def select_all():
    authors = []
    
    sql = "SELECT * FROM authors"
    results = run_sql(sql)
    return(results)
    
def select(id):
    sql = "SELECT * FROM authors WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)[0]
    
    return(results)
    
        
