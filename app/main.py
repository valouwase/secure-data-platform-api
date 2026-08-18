from fastapi import FastAPI

app = FastAPI(
    title="Secure Data Platform API",
    description="A secure REST API for managing and serving structured data.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Secure Data Platform API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
