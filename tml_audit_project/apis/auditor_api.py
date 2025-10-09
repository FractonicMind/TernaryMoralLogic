
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import re
from datetime import datetime

router = APIRouter()

HEX64 = re.compile(r"^[A-Fa-f0-9]{64}$")

class VerifyResponse(BaseModel):
    sha256: str
    format_valid: bool
    ots_status: str
    evm_status: str
    polygon_status: str
    last_checked: str

@router.get("/verify/sha256/{digest}", response_model=VerifyResponse)
def verify_sha256(digest: str):
    if not HEX64.match(digest):
        raise HTTPException(status_code=400, detail="Invalid SHA-256 hex format (expect 64 hex chars).")
    # Placeholders: In a real deployment, call OTS and EVM explorers / local verifier here.
    resp = VerifyResponse(
        sha256=digest,
        format_valid=True,
        ots_status="unknown (connect OTS verifier)",
        evm_status="unknown (connect Ethereum AnchorLog)",
        polygon_status="unknown (connect Polygon AnchorLog)",
        last_checked=datetime.utcnow().isoformat() + "Z"
    )
    return resp

class HashSubmission(BaseModel):
    sha256: str
    note: str | None = None

@router.post("/submit")
def submit_hash(payload: HashSubmission):
    # This public node does not persist; it just acknowledges format.
    if not HEX64.match(payload.sha256):
        raise HTTPException(status_code=400, detail="Invalid SHA-256 hex format.")
    return {"accepted": True, "sha256": payload.sha256, "note": payload.note}
