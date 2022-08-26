import sqlite3
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')
list_counter = 0 

def add_item_to_list(item):
    try:
        conn  = sqlite3.connect("./list.db")
        iten_status = config['STATUS']['NOTSTARTED']
        item_number = list_counter + 1
        x = conn.cursor()
        x.execute('insert into items(number, item, status) values(?,?,?)', (item_number,item, iten_status))
        conn.commit()
        return {"number":item_number, "item":item, "status":iten_status}

    except Exception as e:
        print('Error:', e)
        return None

def return_items():
    """
        return 
    """
    conn = sqlite3.connect("list.db")
    x = conn.cursor()
    x.execute("SELECT * FROM items")
    items = x.fetchall()
    
    for item in items:
        print(item)
def main():
    add_item_to_list("make food")
    """return_items()"""
main()