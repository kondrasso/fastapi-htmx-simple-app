from os.path import dirname, join

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter()

current_dir = dirname(__file__)
templates = Jinja2Templates(directory=join(current_dir, 'templates'))

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("shared/_base.html", {"request": request})