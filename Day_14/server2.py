import imp
from fastapi import FastAPI
from scrape import run as scrape_runner
from logger import trigger_log_save

app = FastAPI()

@app.get("/")
def hell0_world():
    return {"Hello": "World"}

@app.get("/fast_api")
def fastapi_view():
    return {"fastapi": "Hello World"}

@app.post("/box_office_mojo_scraper")
def box_office_scraper_view():
    trigger_log_save()
    scrape_runner()
    return {"fastapi": "Movie_scraping"}