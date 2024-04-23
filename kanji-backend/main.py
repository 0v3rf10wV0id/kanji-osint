from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pubsub import publish_message
from redishelper import add_domain_to_redis,get_domain_data
import json
import redis
import os

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DomainRequest(BaseModel):
    domain: str

redis_host = "redis"  # Replace with your Redis server hostname/IP
redis_port = 6379  # Replace with your Redis server port (default)

redis_client = redis.Redis(host=redis_host, port=redis_port)

@app.post("/sub-enum")
async def start_enumeration(request: DomainRequest):
    """
    Initiates subdomain enumeration for the provided domain name.

    Args:
        request (DomainRequest): Pydantic model containing the domain name.

    Returns:
        dict: JSON response indicating the start of enumeration.
    """

    print(f"Received request for domain: {request.domain}")
    job = {"domain" : request.domain, "status" : "Init"}
    publish_message("enum-jobs",json.dumps(job))
    add_domain_to_redis(request.domain,json.dumps(job))

    response = {
        "message": f"Subdomain enumeration for domain '{request.domain}' has started."
    }

    return response

@app.get("/get-domain-info")
async def get_domain_info(domain: str):
    domain_data = get_domain_data(domain)
    return domain_data

@app.get("/get-file/")
async def get_file(filename: str = Query(..., description="The name of the file to retrieve")):
    # Specify the directory where your files are stored
    file_directory = os.getcwd()+"/outputs"
    file_path = os.path.join(file_directory, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9000)

