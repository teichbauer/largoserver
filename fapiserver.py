# -----------------------------------------------------------------------------
# imports for running fastAPI
# -----------------------------------------------------------------------------
from fastapi import FastAPI
import uvicorn
from glob import glob
from os import path
import pdb

# -----------------------------------------------------------------------------
# imports for python-mongo lib api, database/object-models
# -----------------------------------------------------------------------------
from dal.dal import DB
from data.models.ps001 import PS001

import toml

from data.models.ps001 import PS001
CONF = toml.load('data/config.toml')

meta_db = DB(
        CONF['mongo-db']['host'], 
        CONF['mongo-db']['port'],
        CONF['mongo-db']['meta_db_name']
    )
db = DB(
    CONF['mongo-db']['host'],
    CONF['mongo-db']['port'],
    CONF['mongo-db']['app_db_name']
)
# -----------------------------------------------------------------------------
# set ups for running FastAPI server
# -----------------------------------------------------------------------------
app = FastAPI()
fapi_port = CONF['fastapi']['port']

@app.get("/")
async def index():
    return {'hello': "World!"}

@app.get('/load_db')
async def load_db():
    from tools.db_loader import load_db
    gdic = {}
    if path.exists('data/dbdata/PS'):
        lst = glob('data/dbdata/PS/*')
        for fn in lst:
            with open(fn) as file:
                ps = eval(file.read())
                for p in ps:
                    ps001 = PS001(p['nick-name'], p['properties'])
                    ps001.save(db, True)
        x = 1

@app.get("/load_meta")
async def load_meta():
    from data.cats import data as cats
    from data.rels import data as rels
    from tools.db_loader import load_meta

    ret = load_meta(meta_db, [('CS', cats),('RS', rels)])
    if ret:
        return {'result': "ok"}
    else:
        return {'result': "failed"}

if __name__ == '__main__':
    # -----------------------

    print(f"FastAPI server running on prt {fapi_port}")
    uvicorn.run(app, host='0.0.0.0', port=fapi_port)

