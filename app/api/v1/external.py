from fastapi import APIRouter, Depends
from app.services.external_service import get_weather_safe
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/external", tags=["External APIs"])

@router.get("/weather/{city}")
async def get_weather(
    city: str,
    current_user: User = Depends(get_current_user)
):
    """
    Get weather for any city.
    Uses OpenWeatherMap public API.
    Has retry logic and timeout built in.
    """
    return await get_weather_safe(city)