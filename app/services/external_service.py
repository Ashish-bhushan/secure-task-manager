import httpx
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)
from app.core.config import settings
from app.core.logging_setup import logger

# ── RETRY DECORATOR ───────────────────────────────────────────────
# This decorator adds automatic retry logic to any function
# stop_after_attempt(3)     = try maximum 3 times
# wait_exponential(...)     = wait 1s, then 2s, then 4s between tries
# retry_if_exception_type   = only retry on HTTP errors
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=4),
    retry=retry_if_exception_type(httpx.HTTPError),
    reraise=True
)
async def fetch_weather(city: str) -> dict:
    """
    Fetches weather from OpenWeatherMap API.
    Has automatic retry and 10 second timeout.
    """
    logger.info(f"Fetching weather for: {city}")

    # httpx.AsyncClient = async HTTP client (like requests library)
    # timeout=10.0 = give up after 10 seconds
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{settings.WEATHER_BASE_URL}/weather",
            params={
                "q":     city,
                "appid": settings.WEATHER_API_KEY,
                "units": "metric"
            }
        )
        response.raise_for_status()    # throw error if 4xx or 5xx
        data = response.json()

        return {
            "city":        data["name"],
            "temperature": data["main"]["temp"],
            "humidity":    data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed":  data["wind"]["speed"]
        }

async def get_weather_safe(city: str) -> dict:
    """Safe version — returns error dict instead of crashing."""
    try:
        return await fetch_weather(city)
    except httpx.HTTPStatusError as e:
        logger.error(f"Weather API error {e.response.status_code}")
        return {"error": f"City '{city}' not found"}
    except httpx.TimeoutException:
        logger.error("Weather API timed out")
        return {"error": "Service timed out, try again"}
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {"error": "Weather service unavailable"}