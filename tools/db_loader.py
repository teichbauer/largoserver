def load_meta(db, cn_dics):
    for cn, dics in cn_dics:
        db.drop_collection(cn)
        for k, d in dics.items():
            print(f'inserting {k}')
            ret = db.meta_insert1(d, cn)
            if not ret:
                return False
    return True
 
def load_db(db, cn_dics):
    return True

