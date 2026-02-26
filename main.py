from fastapi import FastAPI
from routers import auth, drive   # 👈 import drive also

app = FastAPI(title="Google Drive Sync API")

@app.get("/")
def home():
    return {"message": "Drive Sync API Running"}

# Register Auth Router
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# ✅ Register Drive Router
app.include_router(drive.router, prefix="/drive", tags=["Drive"])