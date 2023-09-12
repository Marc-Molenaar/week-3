from datetime import datetime

maximum_snelheid = 100

auto_historie = {
    "21-RB-XX": {
        "merk": "Toyota",
        "metingen": [
            {
                "tijd": "12/09/2023 08:55:00",
                "snelheid": 102
            },
        ]
    },
    "12-AB-ZL": {
        "merk": "Nissan",
        "metingen": [
            {
                "tijd": "12/09/2023 08:12:51",
                "snelheid": 95
            },
            {
                "tijd": "12/09/2023 08:13:45",
                "snelheid": 110
            }
        ]
    }
}


def nieuwe_meting(historie, kenteken, snelheid):
    # If kenteken is not in historie, add it
    if kenteken not in historie:
        historie[kenteken] = {
            "metingen": []
        }

    # Add new measurement to historie
    historie[kenteken]["metingen"].append({
        "tijd": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "snelheid": snelheid
    })

    return historie

def snelste_auto(historie):
    hoogste_snelheid = {"snelheid": 0}

    # Voor elke auto in historie
    for kenteken in historie:

        # Voor elke meting in historie
        for meting in historie[kenteken]["metingen"]:

            if meting["snelheid"] > hoogste_snelheid["snelheid"]:
                hoogste_snelheid["kenteken"] = kenteken
                hoogste_snelheid["snelheid"] = meting["snelheid"]

    return hoogste_snelheid


if __name__ == '__main__':
    historie = nieuwe_meting(auto_historie, "21-RB-XX", 100)
    hoogste_snelheid = snelste_auto(auto_historie)

    # Snelste auto
    print(f"Snelste auto: {hoogste_snelheid['kenteken']}")
    print(f"Hoogste snelheid: {hoogste_snelheid['snelheid']} km/h")
    print(f"Sneller dan maximum: {(hoogste_snelheid['snelheid'] - maximum_snelheid)} km/h")
