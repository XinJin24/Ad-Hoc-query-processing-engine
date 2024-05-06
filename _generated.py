
import os
import psycopg2
import psycopg2.extras
import tabulate
from prettytable import PrettyTable
from _H_class_generated import H
import collections
from dotenv import load_dotenv

# DO NOT EDIT THIS FILE, IT IS GENERATED BY generator.py

def query():
    load_dotenv()

    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    dbname = os.getenv('DBNAME')

    conn = psycopg2.connect("dbname="+dbname+" user="+user+" password="+password,
                            cursor_factory=psycopg2.extras.DictCursor)

    cur = conn.cursor()
    cur.execute("SELECT * FROM sales")
    rows = cur.fetchall()
    
    mf_structure = collections.defaultdict(H)
    for row in rows:
        group_cust = row[0]
        if row[4] == 2018:
            if not (mf_structure[(group_cust)]['cust']):
                mf_structure[(group_cust)]['cust'] = group_cust
            if '1_max_quant' not in mf_structure[(group_cust)] or row[6] > mf_structure[(group_cust)]['1_max_quant']:
                mf_structure[(group_cust)]['1_max_quant'] = row[6]
            mf_structure[(group_cust)]['1.prod'] = row[1]
        if row[4] != 2018:
            if not (mf_structure[(group_cust)]['cust']):
                mf_structure[(group_cust)]['cust'] = group_cust
            if '2_max_quant' not in mf_structure[(group_cust)] or row[6] > mf_structure[(group_cust)]['2_max_quant']:
                mf_structure[(group_cust)]['2_max_quant'] = row[6]
            mf_structure[(group_cust)]['2.prod'] = row[1]
    x = PrettyTable()
    x.field_names = ['cust','1.prod','2.prod']
    for val in mf_structure.values():
            row = [val[key] for key in x.field_names if key in val]
            x.add_row(row)
    print(x)


    _global = []
    return tabulate.tabulate(_global,
                        headers="keys", tablefmt="psql")

def main():
    print(query())

if "__main__" == __name__:
    main()
    