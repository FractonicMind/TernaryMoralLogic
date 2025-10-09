
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import re
from datetime import datetime

router = APIRouter()

HEX64 = re.compile(r"^[A-Fa-f0-9]{64}$")

class RedressReport(BaseModel):
    sha256: str = Field(..., description="Hash of the Moral Trace Log or evidence bundle")
    contact: str | None = Field(None, description="Email or other contact (optional)")
    summary: str = Field(..., description="Short description of the harm or violation")
    consent_public: bool = Field(False, description="If true, you consent to public listing of this report hash.")

@router.post("/report")
def submit_redress(report: RedressReport):
    if not HEX64.match(report.sha256):
        raise HTTPException(status_code=400, detail="Invalid SHA-256 format.")
    # Public node: do not persist PII. Acknowledge receipt only.
    ticket_id = report.sha256[:12]
    ack = {
        "received": True,
        "ticket_id": ticket_id,
        "sha256": report.sha256,
        "consent_public": report.consent_public,
        "received_at": datetime.utcnow().isoformat() + "Z"
    }
    return ack
