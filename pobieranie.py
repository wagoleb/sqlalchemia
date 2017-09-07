from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql://bonowg:P@$sw0rd001@localhost/classicmodels')

engine.echo=False

metadata = MetaData(engine)

# customersObj = Table('customers', metadata, autoload=True)

def LoadAllTables(dbTables, metadata):
    object = list()

    for table in dbTables:
        object.append(Table(table, metadata, autoload=True))
    return object

pobrane = LoadAllTables(engine.table_names(), metadata)

import pdb; pdb.set_trace()