from pydantic import BaseModel
Database_Name = 'LARGODB'


class PS_Object(BaseModel):
    collection_name: str = 'PS'
    category_name: str
    nick_name: str
    properties: dict
    relationships: dict

#################################################

class ES_Object(BaseModel):
    collection_name: str = 'ES'
    category_name: str
    nick_name: str
    properties: dict
    relationships: dict

class CS_Object(BaseModel):
    collection_name: str = 'CS'
    category_name: str
    nick_name: str
    properties: dict
    relationships: dict

class DS_Object(BaseModel):
    collection_name: str = 'DS'
    category_name: str
    nick_name: str
    properties: dict
    relationships: dict