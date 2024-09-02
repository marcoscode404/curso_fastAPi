from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from http import HTTPStatus
from fast_zero.schemas import Message, UserSchema, UserPublic, UserDB, UserList

app = FastAPI()
database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'Hello': 'World'}


@app.put('/atualizar_gados')
def read_update():
    return {'Hello': 'Fala galera'}


@app.get('/buscar_gados')
def read_search():
    return {'Hello': 'Buscar gados'}


@app.delete('/deletar_gados')
def read_delete():
    return {'Hello': 'Apagar gados'}


@app.post('/alterar_gados')
def read_create():
    return {'Hello': 'Fala galera'}


@app.get('/html', response_class=HTMLResponse)
def read_html():
  return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>
    """


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    
    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1: 
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        ) 

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id 

    return user_with_id

@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    del database[user_id - 1]

    return {'message': 'User deleted' }