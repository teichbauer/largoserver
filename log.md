### 2022-06-23a
---
- aded:
  ```
  @app.get("/login")
  async def index(email:str, pwd:str):
      print(f'email: {email}, pwd: {pwd}')
      return {'hello': "World!", "email": email, "pwd": pwd}
  ```
  So when the flutter app send the url:
  ```dart
  String email = 'wei@outlook.com';
  String pwd = 'secret';
  String url = 'http://172.25.248.31:5002/login/?email=$email&  pwd=$pwd';
  final uri = Uri.parse(url);
  ...
  Response response = await get(uri);
  ```
  it will responds back the json: 
  ```
  {email: 'wei@outlook.com', pwd: 'secret'}
  ```

### 2022-06-23
---
- added:
  ```
  from fastapi.middleware.cors import CORSMiddleware
  ...
  app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )
  ```
  so the fastAPI server can accept request from
  different origin (like a http-request sent from a
  flutter mobile app)

- find out the local ip-address: my here: 172.25.248.31
  and use this in flutter app http:
  uri = Uri.parse('http://172.25.248.31:5002')
  resp = get(uri)



### 2022-06-21
---
- added howto.md

### 2022-06-20
---
- fast-api works with mongo-db
- mongo.sh to run mongo-db in a container, on a persistent volume