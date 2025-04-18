import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

app = FastAPI(description='Maks Plaksin')

@app.get('/')
def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/stitu')
def stitu(request: Request):
    return templates.TemplateResponse('stitu.html', {'request': request})

@app.get('/stitu2')
def stitu2(request: Request):
    return templates.TemplateResponse('stitu2.html', {'request': request})

@app.get('/babka')
def babka(request: Request):
    return templates.TemplateResponse('babka.html', {'request': request})

@app.get('/ded')
def ded(request: Request):
    return templates.TemplateResponse('ded.html', {'request': request})

@app.get('/gameover')
def gameover(request: Request):
    return templates.TemplateResponse('gameover.html', {'request': request})

if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)

