import requests

def get_current_weather(lat: float, lon: float, units: str = "metric") -> dict:
    """
    Retrieve current weather data from the Open-Meteo public API.

    Args:
        lat (float): Latitude of the location (e.g. 52.37 for Amsterdam).
        lon (float): Longitude of the location (e.g. 4.89 for Amsterdam).
        units (str, optional): Unit system to use. Only "metric" is supported for now.

    Returns:
        dict: Dictionary with current temperature (°C), windspeed (km/h), and weather code.

    Raises:
        requests.exceptions.RequestException: If the HTTP request fails.

    Example:
        ```python
        data = get_current_weather(52.37, 4.89)
        print(data["temperature"])  # e.g., 17.2
        ```
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("current_weather", {})