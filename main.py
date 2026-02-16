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


@app.get("/date")
def get_server_date_utc() -> dict[str, str]:
    today_utc = datetime.now(timezone.utc).date()
    return {
        "server_date": today_utc.isoformat(),
        "timezone": "UTC",
    }


@app.get("/date/local")
def get_server_date_local() -> dict[str, str]:
    local_now = datetime.now().astimezone()
    return {
        "server_date": local_now.date().isoformat(),
        "timezone": str(local_now.tzinfo),
    }
