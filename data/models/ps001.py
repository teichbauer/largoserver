from tools.gen_id import generate_id
from data.models.cs001 import CS001

class PS001:
    def __init__(self, nickName, properties):
        self.dic = {
            'cat': 'PS001',
            'nick-name': nickName,
            'properties': properties,
            'relationships': {}
            }
        self.dic['_id'] = generate_id('PS')

        cs001_nick_name = f'{nickName}/R003:largo-acct'
        cs001_props = CS001.default_properties(nickName)
        self.cs001 = CS001(cs001_nick_name, cs001_props)
        self.cs001.dic['_id'] = generate_id('CS')
        self.cs001.dic['relationships']['R005'] = [self.dic['_id']]

        self.dic['relationships']['R003'] = [
            {
               'LS_info': {
                    'en': f"{nickName}'s Largo account",
                    'zh': '我的宝箱登录账号',
                },
                'id': self.cs001.dic['_id']
            }
        ]

    def save(self, db, save_cs001=False):
        db.insert1(self.dic, 'PS')
        if save_cs001:
            self.cs001.save(db)
    
