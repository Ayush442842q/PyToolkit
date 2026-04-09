import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from weather import parse_weather, convert_temperature

class TestWeather:
    """Tests for Weather CLI."""

    def test_parse_weather_valid(self):
        """Test parse_weather with valid data."""
        mock_data = {
            "cod": 200,
            "name": "London",
            "sys": {"country": "GB"},
            "main": {
                "temp": 15.0,
                "feels_like": 13.0,
                "humidity": 80
            },
            "weather": [{"description": "clear sky"}],
            "wind": {"speed": 3.5}
        }
        result = parse_weather(mock_data)
        assert result is not None
        assert result["city"] == "London"
        assert result["country"] == "GB"
        assert result["temp"] == 15.0
        assert result["humidity"] == 80
        print("✅ test_parse_weather_valid passed!")

    def test_convert_temperature(self):
        """Test temperature conversion."""
        result = convert_temperature(0, "f")
        assert result == 32.0
        result = convert_temperature(100, "f")
        assert result == 212.0
        print("✅ test_convert_temperature passed!")

if __name__ == "__main__":
    t = TestWeather()
    t.test_parse_weather_valid()
    t.test_convert_temperature()
    print("\n✅ All tests passed!")