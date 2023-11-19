from os.path import dirname, join

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter()

current_dir = dirname(__file__)
templates = Jinja2Templates(directory=join(current_dir, 'templates'))

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/astronaut")
async def astronaut(request: Request):
    return templates.TemplateResponse("astronaut.html", {"request": request})

@router.get("/about")
async def astronaut(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})