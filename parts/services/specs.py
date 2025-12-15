PART_SPECS = {
    "cpu": {
        "required": {
            "socket": str,
            "tdp": int,
        },
        "optional": {
            "cores": int,
            "threads": int,
            "base_clock": float,
            "boost_clock": float,
        }
    },

    "motherboard": {
        "required": {
            "socket": str,
            "ram_type": str,
        },
        "optional": {
            "max_ram": int,
            "form_factor": str,
        }
    },

    "ram": {
        "required": {
            "ram_type": str,
            "capacity": int,
        },
        "optional": {
            "speed": int,
        }
    },

    "psu": {
        "required": {
            "wattage": int,
        },
        "optional": {
            "certification": str,
        }
    }
}
