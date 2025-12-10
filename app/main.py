from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.schemas import CalcRequest, SimulateRequest
from app.utils import calc_attendance, simulate_upcoming  # <-- correct names


app = FastAPI(title="Attendance Helper")

# Serve HTML
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("app/static/index.html", "r", encoding="utf-8") as f:
        return f.read()

# API endpoints
@app.post("/api/calc")
async def calc_attendance_endpoint(req: CalcRequest):
    return calc_attendance(req.total, req.attended, req.target)

@app.post("/api/simulate")
async def simulate_upcoming_endpoint(req: SimulateRequest):
    return simulate_upcoming(req.total, req.attended, req.target, req.upcoming)
