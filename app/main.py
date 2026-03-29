from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logging_setup import logger
from app.db.init_db import init_db
from app.api.v1 import auth, tasks, external

# ── Create the FastAPI app ────────────────────────────────────────
app = FastAPI(
    title=settings.APP_NAME,
    description="Secure Task Manager API with JWT Auth & RBAC",
    version="1.0.0",
    docs_url="/docs"       # Swagger UI at http://localhost:8000/docs
)

# ── CORS — allows frontend to talk to backend ─────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],   # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Runs when server STARTS ───────────────────────────────────────
@app.on_event("startup")
def on_startup():
    logger.info("Server starting...")
    init_db()              # create DB tables
    logger.info("Server ready ✅")

# ── Register all routers ──────────────────────────────────────────
app.include_router(auth.router,     prefix=settings.API_V1_PREFIX)
app.include_router(tasks.router,    prefix=settings.API_V1_PREFIX)
app.include_router(external.router, prefix=settings.API_V1_PREFIX)

# ── Health check routes ───────────────────────────────────────────
@app.get("/", tags=["Health"])
def root():
    return {"status": "running ✅", "docs": "/docs"}

@app.get("/health", tags=["Health"])
def health():
    return {"status": "healthy ✅"}