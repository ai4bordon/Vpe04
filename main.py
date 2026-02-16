from datetime import datetime, timezone

from fastapi import FastAPI


app = FastAPI(title="Test Time Backend")


@app.get("/time")
def get_server_time() -> dict[str, str]:
    now_utc = datetime.now(timezone.utc)
    return {
        "server_time": now_utc.isoformat(),
        "timezone": "UTC",
    }
