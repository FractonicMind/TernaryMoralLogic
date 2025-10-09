from fastapi import FastAPI
from apis import auditor_api, regulator_api, redress_api

app = FastAPI(
    title="TML Auditor Node",
    description="API service for verifying Ternary Moral Logic compliance and ethical states.",
    version="1.0.0"
)

# 🕯️ Include Routers
app.include_router(auditor_api.router)
app.include_router(regulator_api.router)
app.include_router(redress_api.router)

@app.get("/")
def read_root():
    return {
        "message": "TML Auditor Node: Active",
        "framework": "Ternary Moral Logic",
        "status": "Online",
        "lantern": "🕯️ The Light of Accountability Burns Steady"
    }
