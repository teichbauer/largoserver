from pymongo import MongoClient
from tools.gen_id import generate_id

class DB:
    def __init__(self, host, port, db_name):
        self.db_name = db_name
        self.db_client = MongoClient()
        self.db = self.db_client[db_name]

    def drop_collection(self, collection_name):
        self.db.drop_collection(collection_name)


    def meta_insert1(self, dic, cname):
        try:
            ret = self.db[cname].insert_one(dic)
            return bool(ret.acknowledged)
        except Exception as e:
            print(str(e))
            return False

    def fill_id(dic, cname):
        if '_id' not in dic:
            dic['_id'] = generate_id(cname)
        return dic

    def insert1(self, dic, cname):
        try:
            # ret = self.db[cname].insert_one(dic)
            ret = self.db[cname].insert_one(dic)
            if bool(ret.acknowledged):
                return dic
        except Exception as e:
            print(str(e))
            return False

    def insert_many(self, dics, cname):
        # -----------------------------------------------------
        # dics is a list of Python/dicts.
        # every dict in this list must have _id in it
        # all dicts inserted into a collection named cname
        # -----------------------------------------------------
        try:
            ret = self.db[cname].insert_many(dics)
            if ret.acknowledged:
                return 'all inserted'
            else:
                return 'not inserted'
        except:
            return 'failed'

    def find(self, cname, q):
        results = []
        coll = self.db[cname] 
        lst = list(coll.find(q))
        for e in lst:
            results.append(e)
            # print(e)
        return results

    def delete1(self, cname, the_id):
        self.db[cname].delete_many({'_id': the_id})
