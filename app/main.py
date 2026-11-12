from fastapi import FastAPI

app = FastAPI(title="LoanLens")


@app.get("/health")
def health():
    return {"status": "ok"}