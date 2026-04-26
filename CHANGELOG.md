## Day 13 - QR Code Generator
- Added check_dependencies function
- Added ensure_output_folder function
- Added generate_qr core function
- Added generate_qr_colored function
- Added generate_qr_bulk function
- Added _detect_data_type helper function
- Added get_qr_info function
- Added display_info function
- Added main interactive menu
- Added unit tests

## Day 12 - Text to Speech
- Added check_gtts function
- Added ensure_output_folder function
- Added text_to_speech core function
- Added text_to_speech_slow function
- Added file_to_speech function
- Added supported languages dictionary
- Added display_languages function
- Added main interactive menu
- Added unit tests

## Day 11 - YouTube Downloader
- Added check_ytdlp function
- Added is_valid_url function
- Added ensure_download_folder function
- Added download_video function
- Added download_audio function
- Added get_video_info function
- Added display_info function
- Added download_playlist function
- Added main function with interactive menu
- Added unit tests

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

## [Day 07] - Image Resizer
- Added get_image_info() to read image metadata
- Added display_info() for formatted output
- Added resize_image() for exact dimension resizing
- Added resize_by_percentage() for proportional resizing
- Added crop_image() to crop by coordinates
- Added convert_format() to change image format
- Added apply_grayscale() for grayscale filter
- Added apply_blur() for Gaussian blur filter
- Added rotate_image() to rotate by degrees
- Added flip_image() for horizontal/vertical flip
- Added main() CLI menu with 9 options
- Added full unit test suite

## [Day 08] - URL Shortener
- Added is_valid_url() for URL validation
- Added shorten_url() using TinyURL API
- Added load_history() to read JSON history
- Added save_history() to write JSON history
- Added add_to_history() to track shortened URLs
- Added display_history() for formatted output
- Added clear_history() to reset history
- Added get_history_count() helper
- Added shorten_bulk() for multiple URLs
- Added main() CLI menu with 5 options
- Added full unit test suite

## [Day 09] - Email Sender
- Added is_valid_email() for email validation
- Added create_message() to build email objects
- Added add_attachment() to attach files
- Added send_email() via Gmail SMTP
- Added log_email() for tracking sent emails
- Added send_bulk_emails() for multiple recipients
- Added view_log() to display email history
- Added main() CLI menu with 5 options
- Added full unit test suite

## [Day 10] - Todo CLI App
- Added load_todos() and save_todos() for JSON persistence
- Added add_todo() with priority support (high/medium/low)
- Added list_todos() with optional done filter
- Added mark_done() to complete todos by ID
- Added delete_todo() to remove todos by ID
- Added edit_todo() to update todo titles
- Added search_todos() to find todos by keyword
- Added get_stats() for todo statistics
- Added clear_done() to bulk remove completed todos
- Added main() CLI menu with 9 options
- Added full unit test suite with 9 test cases
