# Kampala Weather Report

A small Python program that fetches live weather data from the
Open-Meteo API and prints a clean, easy-to-read summary.

## What it shows

- Temperature
- Humidity
- Wind speed
- Elevation
- Time of the report (East Africa Time)
- A simple "feeling" note (humid or comfortable)

## Requirements

- Python 3
- The `requests` library

## Setup

```
python -m pip install requests
```

## How to run

```
python weather.py
```

## Example output

```
==================================
  Current Weather Report: Kampala
==================================
Temperature:    20.5 °C
Humidity:       95 %
Wind speed:     8.6 km/h
Elevation:      1,224 metres above sea level
Reported at:    13 October 2026, 21:45 (East Africa Time)
Feeling:        Very humid
==================================
```

## Error handling

The program shows a clear message instead of crashing if the internet
is down, the server is slow, or the API returns an error code.

## Data source

Weather data from [Open-Meteo](https://open-meteo.com). No API key needed.