from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')
router = APIRouter(prefix='/merGame')

@router.get('/')
def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@router.get('/stitu')
def stitu(request: Request):
    return templates.TemplateResponse('stitu.html', {'request': request})

@router.get('/stitu2')
def stitu2(request: Request):
    return templates.TemplateResponse('stitu2.html', {'request': request})

@router.get('/babka')
def babka(request: Request):
    return templates.TemplateResponse('babka.html', {'request': request})

@router.get('/ded')
def ded(request: Request):
    return templates.TemplateResponse('ded.html', {'request': request})

@router.get('/gameover')
def gameover(request: Request):
    return templates.TemplateResponse('gameover.html', {'request': request})