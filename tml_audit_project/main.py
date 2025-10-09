
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .apis import auditor_api, regulator_api, redress_api
import logging
import os

APP_NAME = "TML Lantern Auditor Node (Public)"
CREATOR = "Lev Goukassian (ORCID: 0009-0006-5966-1243)"
LANTERN = "🏮"

app = FastAPI(
    title=APP_NAME,
    description="Public verification service for Ternary Moral Logic (TML). No private data is stored or required. Proofs only.",
    version="1.0.0"
)

# CORS: open for read-only GETs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Routers
app.include_router(auditor_api.router, prefix="/auditor", tags=["auditor"])
app.include_router(regulator_api.router, prefix="/regulator", tags=["regulator"])
app.include_router(redress_api.router, prefix="/redress", tags=["redress"])

@app.get("/health")
def health():
    return {"status": "ok", "service": APP_NAME, "lantern": LANTERN}

@app.get("/lantern")
def lantern_info():
    return {
        "lantern": LANTERN,
        "creator": CREATOR,
        "mission": "Verify hashes, timestamps, and governance anchors per TML.",
        "public": True
    }

# Startup banner
@app.on_event("startup")
async def startup_event():
    logging.basicConfig(level=logging.INFO)
    logging.info(f"{LANTERN} {APP_NAME} started")
    logging.info(f"Creator: {CREATOR}")
    logging.info("Mode: Public Auditor Node — transparent, read-mostly, no private content.")
