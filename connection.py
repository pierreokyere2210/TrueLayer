import json

with open('config.json') as config_file:
    data = json.load(config_file)

# database connection details

def connection():

    db = {}
    db['host'] = data['postgres']['host']
    db['database'] = data['postgres']['dbname']
    db['user'] = data['postgres']['user']
    db['password'] = data['postgres']['password']
    db['port']=data['postgres']['port']
    print(db)
    return db