from tools.gen_id import generate_id

class CS001:
    @classmethod
    def default_properties(cls, usrname):
        return {
            'user-name': usrname,
            'email': f'{usrname}@largo.com',
            'pwd': f'{usrname}123',
            'role': 0,
        }

    def __init__(self, nickName, properties):
        self.dic = {
            'cat': 'CS001',
            'nick-name': nickName,
            'properties': properties,
            'relationships': {

            }
        }

    def save(self, db):
        db.insert1(self.dic, 'CS')

    