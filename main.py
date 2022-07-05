from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from routes import api
from datetime import date



app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)
app.include_router(api.router)


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