# Weathercast

Weathercast is an open-source project for daily weather forecast posting to VK (a social network). It allows you to
automate the process of sharing weather updates with your VK community.

## Features

- Retrieves weather data from a reliable weather API.
- Formats the weather information into an aesthetically pleasing format.
- Publishes the daily weather forecast directly to your VK community messages.

## Installation

1. Make sure you have [Poetry](https://python-poetry.org/) installed.
2. Clone this repository:

```bash
git clone https://github.com/Sirius-Bell/Weathercast.git
```

3. Navigate to the project directory:

```bash
cd Weathercast
```   

4. Install the project dependencies using Poetry:

```bash
poetry install
```   

## Usage

1. Create a configuration file .env and specify the required environment variables:

```bash
# VK API credentials
VK_TOKEN=your_vk_token
VK_GROUP_ID=your_vk_group_id
   
# Weather API credentials
WEATHER_API_KEY=your_weather_api_key
```

2. Run the Weathercast script:

```bash
poetry run python main.py
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an
issue or submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0 License. See
the [LICENSE](https://github.com/Sirius-Bell/Weathercast/blob/main/LICENSE) file for details.