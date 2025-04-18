import uvicorn
from fastapi import FastAPI
from api.rotues import router as gameMer_roter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

app = FastAPI(description='Maks Plaksin')
app.include_router(gameMer_roter)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)

