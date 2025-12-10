# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, conint, confloat
from fastapi.middleware.cors import CORSMiddleware
from .utils import calc_needed, calc_max_skip, simulate_upcoming

app = FastAPI(title="Attendance Helper API")

# allow local JS to call APIs during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# serve static frontend (index.html) from ../static
app.mount("/", StaticFiles(directory="static", html=True), name="static")


class CalcRequest(BaseModel):
    total: conint(ge=0)
    attended: conint(ge=0)
    target: confloat(gt=0, lt=100)  # percent, between 0 and 100 exclusive


class SimRequest(CalcRequest):
    upcoming: conint(ge=0)


@app.post("/api/calc")
def api_calc(payload: CalcRequest):
    total = payload.total
    attended = payload.attended
    target = float(payload.target)

    if attended > total:
        raise HTTPException(status_code=400, detail="attended cannot exceed total")

    curPct = 0.0
    if total == 0:
        curPct = 0.0 if attended == 0 else 100.0
    else:
        curPct = (attended / total) * 100.0

    needed = calc_needed(total, attended, target)
    max_skip = calc_max_skip(total, attended, target)

    return {
        "currentPct": round(curPct, 6),
        "needed": needed,
        "maxSkip": max_skip,
    }


@app.post("/api/simulate")
def api_simulate(payload: SimRequest):
    total = payload.total
    attended = payload.attended
    target = float(payload.target)
    upcoming = payload.upcoming

    if attended > total:
        raise HTTPException(status_code=400, detail="attended cannot exceed total")

    result = simulate_upcoming(total, attended, target, upcoming)
    return result
