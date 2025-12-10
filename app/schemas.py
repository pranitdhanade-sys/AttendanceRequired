from pydantic import BaseModel, Field

class CalcRequest(BaseModel):
    total: int = Field(..., ge=0)
    attended: int = Field(..., ge=0)
    target: float = Field(..., ge=0, le=100)

class SimulateRequest(CalcRequest):
    upcoming: int = Field(..., ge=0)
