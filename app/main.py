from fastapi import FastAPI

app = FastAPI(
        title="LinuxProfile",
        description="Linux Profile Project",
        version="0.0.1",
        contact={
            "name": "Fernando Celmer",
            "url": "www.linuxprofile.com",
            "email": "email@fernandocelmer.com",
        }
        )

@app.get("/")
def get_status():
    """Get status of messaging server."""
    return ({"status":  "it's live"})

