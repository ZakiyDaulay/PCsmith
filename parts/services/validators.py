def validate_specs(part_type, specs):
    required = {
        "cpu": ["socket", "tdp"],
        "motherboard": ["socket", "ram_type"],
        "ram": ["ram_type", "capacity"],
        "psu": ["wattage"],
    }

    missing = [
        key for key in required.get(part_type, [])
        if key not in specs
    ]

    if missing:
        raise ValueError(f"Missing specs for {part_type}: {missing}")
