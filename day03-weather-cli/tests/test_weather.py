import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from weather import parse_weather, convert_temperature

class TestWeather:
    """Basic test structure for Weather CLI."""

    def test_parse_weather_valid(self):
        """Test parse_weather with valid data."""
        pass

    def test_parse_weather_invalid(self):
        """Test parse_weather with invalid data."""
        pass

    def test_convert_temperature(self):
        """Test temperature conversion."""
        pass