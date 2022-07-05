from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import date
import aiohttp
import asyncio



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/hora", response_class=HTMLResponse)
async def hora(request: Request):
    currentDate = date.today()
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "currentDate": currentDate
                                        }
                                      )


@app.get("/api/rickymorty")
async def say_hello():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://rickandmortyapi.com/api/character/17') as response:
            return (await response.json())


@app.post("/api/uploadfile/")
async def create_upload_file(file: UploadFile):
    content = await file.read()
    with open("uploads/imgw.png", "wb") as obj:
        obj.write(content)
    return {"filename": file.filename}