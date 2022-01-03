import glob
from pymongo import MongoClient
import pandas as pd
import time
path='/home/souid/Desktop/evax/'
date=glob.glob(path+'*')
date=[i.split('/')[-1] for i in date]
print(date)


client=MongoClient()

for d in date:
    dbnames = client.list_database_names()
    print(dbnames)
    if d in dbnames:
        print('pass')
        print(d)
        pass
    else:
        db=client[d]
        print(db)
        gouvernorats = glob.glob(path+d+'/*')
        gouvernorats = [i.split('/')[-1] for i in gouvernorats]

        for gouv in gouvernorats:
            l=glob.glob(path+d+'/'+gouv+'/*.csv')
            m=[]
            print(gouv)
            for i in l:
                df=pd.read_csv(i,delimiter=';')
                m.append(df)

            f=pd.concat(m)
            print(gouv)
            coll=db[gouv]
            coll.insert_many(f.to_dict('records'))
            time.sleep(1)
print(client.list_database_names())