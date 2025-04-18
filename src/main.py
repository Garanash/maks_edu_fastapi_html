import uvicorn
from fastapi import FastAPI, Request
from api.rotues import router as gameMer_roter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

app = FastAPI(description='Maks Plaksin')
app.include_router(gameMer_roter)


@app.get('/')
def root(request: Request):
    return templates.TemplateResponse('Root.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)
