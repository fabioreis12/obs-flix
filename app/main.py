import time
import random
import logging
from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

# Easter egg que você pediu (importante: ele tenta abrir o browser, 
# mas no Docker ele apenas registra o módulo com sucesso)
try:
    import antigravity
except ImportError:
    pass

# Logs estruturados para Observabilidade
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="Obs-Flix API", version="1.0.0")

# Instrumentação automática: Cria o endpoint /metrics para o Prometheus
Instrumentator().instrument(app).expose(app)

MOVIES = {
    1: {"title": "The Matrix", "genre": "Sci-Fi"},
    2: {"title": "Inception", "genre": "Sci-Fi"},
    3: {"title": "The Godfather", "genre": "Drama"}
}

@app.get("/")
def read_root():
    return {"status": "🚀 Flying with Antigravity", "docs": "/docs"}

@app.get("/watch/{movie_id}")
async def watch_movie(movie_id: int):
    # Simula latência (essencial para mostrar variabilidade nas métricas)
    delay = random.uniform(0.1, 0.8)
    time.sleep(delay)
    
    if movie_id not in MOVIES:
        logger.error(f"Movie ID {movie_id} not found!")
        raise HTTPException(status_code=404, detail="Filme não disponível")
    
    logger.info(f"Streaming movie: {MOVIES[movie_id]['title']}")
    return {"data": MOVIES[movie_id], "latency": f"{delay:.2f}s"}

@app.get("/gravity-check")
def gravity():
        return {"gravity": "Zero", "module": "antigravity", "status": "Stable"}