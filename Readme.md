# Kanji Osint
A open-source tool for asset discovery and attack surface management.

## Features
- Worker architecture which allows parrallel workers for resolution and enrichment
- Uses cutting edge tools which enable fast and reliable resolution
- Tools for enumeration, resolution and enrichment
  - Subfinder - https://github.com/projectdiscovery/Subfinder
  - DNSX - https://github.com/projectdiscovery/dnsx
  - TLSX - https://github.com/projectdiscovery/tlsx
  - Httpx - https://github.com/projectdiscovery/httpx

## Installation
### Backend
The backend uses the following frameworks
- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [redis](https://redis.io/)
- [docker](https://www.docker.com/)o

To start the backend
- Install docker on your machine
- clone the repository and enter the kanji-backend folder
- run `docker-compose up`

This will start
- redis
- fastapi
- subfinder worker
- dnsx worker
- tlsx worker
- httpx worker

### Frontend
The frontend uses the following frameworks
- [Shadcn UI](https://ui.shadcn.com/)
- [Vite](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Electron](https://www.electronjs.org/)
- [React](https://reactjs.org/)

To start the Frontend
- Clone the repository and enter the kanji-ui folder
- Create a .env file in the kanji-ui folder and add the following `VITE_BACKEND_URL:{BACKEND_URL}`
- run `npm install`
- run `npm run build`
- run `npm run electron`

This will start the frontend in an electron window
