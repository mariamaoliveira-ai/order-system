from fastapi import FastAPI

app = FastAPI(title="Order System API", version="0.1.0")


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Report that the API process is running."""
    return {"status": "ok"}
