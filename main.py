from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from colagem import gerador
from manutencao.controle import *

descricao = """Api para a geração de colagem apartir de um texto \n
EM CONSTRUÇÃO
"""
app = FastAPI(
    title="Gerador de Colagem",
    description=descricao,
    version='0.0.1'
)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5500"
    ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/', response_class=HTMLResponse)
def home():
    html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de Colagem API</title>
</head>
<body>
<h1> API Gerador de Colagem <h1>
<div>Para acessar a documentação acesse /docs</div>
</body>
</html>"""
    return html

@app.get('/colagem')
def criar_colagem(texto: Union[str, None] = None, tipo: Union[str, None] = 'png'):
    tipo = tipo.upper()
    if tipo == 'PNG':
        imagem = gerador.png(texto)
    elif tipo == 'GIF':
        imagem = gerador.gif(texto=texto)
    Somar() ## Controle de imagens geradas
    return FileResponse(imagem)

@app.get('/status')
def status():
    return Ler_dados()


@app.delete('/manutencao')
def limpar(senha: Union[str, None]= None):
    ## provisorio para facilitar minha vida8
    if senha == "senha":
        Apagar()
        return {"apagar": "realizado"}