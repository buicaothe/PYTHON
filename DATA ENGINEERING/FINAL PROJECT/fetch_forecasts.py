import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Tọa độ Sân bay Turku
LAT, LON = 60.5141, 22.2628

URLS = {
    "open_meteo": (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}"
        f"&hourly=temperature_2m&forecast_days=4",
        "json",
    ),
    "fmi_forecast": (
        f"https://opendata.fmi.fi/wfs?service=WFS&version=2.0.0"
        f"&request=getFeature"
        f"&storedquery_id=fmi::forecast::harmonie::surface::point::simple"
        f"&latlon={LAT},{LON}&parameters=Temperature&timestep=60",
        "xml",
    ),
}

def main():
    out_dir = Path("rawdata")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Gắn timestamp UTC vào tên file để lần chạy sau không ghi đè lần trước
    run_ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%MZ")

    for name, (url, ext) in URLS.items():
        filepath = out_dir / f"{name}_{run_ts}.{ext}"
        urllib.request.urlretrieve(url, filepath)
        print(f"Saved: {filepath}")

if __name__ == "__main__":
    main()