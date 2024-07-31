from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from prisma import Prisma
from prisma.models import User
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="public"), name="static")    
templates = Jinja2Templates(directory="views")

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse(request, name='index.html', context= {"page":"home"})

@app.post('/')
def post():
    return {"message":"text uploaded successfully, conversion starting soon"}

@app.get('/createuser')
async def main():
    db = Prisma(auto_register=True)
    await db.connect()
    user = await db.user.create(
        data={
            'name': 'Robert',
            'email': 'robert@craigie.dev'
        },
    )
    await db.disconnect()
    
@app.get('/getusers')
async def get():
    db = Prisma(auto_register=True)
    await db.connect()
    u = await db.user.find_many()
    await db.disconnect()
    return {'users':u}