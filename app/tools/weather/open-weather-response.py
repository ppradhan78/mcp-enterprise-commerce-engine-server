from typing import List, Optional
from pydantic import BaseModel, Field


class Coord(BaseModel):
    lon: float
    lat: float


class WeatherItem(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class MainData(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: Optional[int] = None
    grnd_level: Optional[int] = None


class Wind(BaseModel):
    speed: float
    deg: int
    gust: Optional[float] = None


class Rain(BaseModel):
    one_hour: Optional[float] = Field(default=None, alias="1h")

    class Config:
        populate_by_name = True


class Clouds(BaseModel):
    all: int


class Sys(BaseModel):
    country: str
    sunrise: int
    sunset: int
    type: Optional[int] = None
    id: Optional[int] = None


class OpenWeatherResponse(BaseModel):
    coord: Coord
    weather: List[WeatherItem]
    base: str
    main: MainData
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int
    rain: Optional[Rain] = None

