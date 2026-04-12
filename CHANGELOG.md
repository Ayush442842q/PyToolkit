# Changelog

All notable changes to PyToolkit will be documented here.

## Day 04 - Web Scraper
- Added base configuration and imports
- Added get_page function with error handling
- Added parse_headlines function
- Added display_headlines function
- Added main function
- Added save_headlines function
- Added get_scores function
- Added unit tests

---

## [Day 03] - Weather CLI 🌤️
### Added
- `get_weather(city)` — fetches real-time weather from OpenWeatherMap API
- `parse_weather(data)` — parses raw API response into clean dictionary
- `display_weather(weather)` — displays formatted current weather
- `get_forecast(city)` — fetches 5-day weather forecast
- `display_forecast(data)` — displays formatted 5-day forecast
- `compare_cities(cities)` — compares weather across multiple cities
- `convert_temperature(temp, unit)` — converts between Celsius and Fahrenheit
- `get_weather_with_unit(city, unit)` — fetches weather with unit preference
- Error handling for network errors and timeouts
- Unit tests for parse_weather and invalid city handling

---

## [Day 02] - Password Generator 🔐
### Added
- `generate_password()` — generates secure random password
- `validate_length()` — validates password length
- `check_password_strength()` — returns Weak/Medium/Strong rating
- `generate_multiple_passwords()` — generates multiple passwords at once

---

## [Day 01] - File Organizer 📁
### Added
- `get_file_category()` — returns category from file extension
- `get_files()` — scans folder and returns list of files
- `organize_files()` — moves files into subfolders
- `get_file_count()` — counts files before organizing
## Day 05 - Expense Tracker
- Added imports and configuration
- Added initialize_file function
- Added add_expense function
- Added get_all_expenses function
- Added get_total function
- Added get_by_category function
- Added display_expenses function
- Added get_summary and display_summary functions
- Added main function with menu
- Added unit tests

## [Day 06] - PDF Merger/Splitter
- Added merge_pdfs() to combine multiple PDFs
- Added split_pdf() to split into individual pages
- Added get_pdf_info() to view PDF metadata
- Added extract_pages() to extract specific pages
- Added display_info() for formatted output
- Added rotate_pages() to rotate PDF pages
- Added add_watermark() to stamp watermark on pages
- Added get_page_count() utility function
- Added main() CLI menu
- Added unit tests for all edge cases
