from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from app.db import test_db_connection

app = FastAPI(title="Kingdom Health Services Management System")

# Set templates directory
templates = Jinja2Templates(directory="app/templates")

# get, post, put and delete = CRUD                            

# Homepage route
@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request},)

# Health check route
@app.get("/health", response_class=JSONResponse)
def health():
    return {"status": "ok","db_connected": test_db_connection()}

# Extra route test for localhost
@app.get("/patient-data")
def patient_data():
    return {"Status": "This is a future page for accessing patient data."}

