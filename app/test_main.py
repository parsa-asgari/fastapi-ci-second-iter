import pytest
from httpx import ASGITransport, AsyncClient

from .main import app


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


@pytest.mark.anyio
async def test_status():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.anyio
async def test_metrics():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/metrics")
    assert response.status_code == 200
    assert response.json() == {
        "os": "5.15.167.4-microsoft-standard-WSL2",
        "runtime": "Docker",
        "framework": "FastAPI",
        "language": "Python",
        "version": "0.1.0",
        "release": "2024-06-01",
    }


@pytest.mark.anyio
async def ping():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"output": "pong"}


@pytest.mark.anyio
async def pong():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/pong")
    assert response.status_code == 200
    assert response.json() == {"output": "ping"}


@pytest.mark.anyio
async def test_items_positive():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": 0}


@pytest.mark.anyio
async def test_items_negative():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/items/42")
    assert response.status_code == 404
