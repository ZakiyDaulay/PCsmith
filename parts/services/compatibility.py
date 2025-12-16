class CompatibilityError(Exception):
    pass

def check_cpu_motherboard(cpu, motherboard):

        cpu_socket = cpu.specs.get("socket")
        mb_socket = motherboard.specs.get("socket")

        if cpu_socket != mb_socket:
            raise CompatibilityError(
                f"CPU socket ({cpu_socket}) is incompatible with motherboard socket ({mb_socket})"
            )
def check_ram_motherboard(ram, motherboard):
        ram_type = ram.specs.get("ram_type")
        mb_ram_type = motherboard.specs.get("ram_type")

        if ram_type != mb_ram_type:
            raise CompatibilityError(
                f"RAM type ({ram_type}) is incompatible with motherboard RAM type ({mb_ram_type})"
            )

def check_psu_wattage(psu, parts):
        total_tdp = 0

        for part in parts:
            total_tdp += part.specs.get("tdp", 0)

        required_wattage = int(total_tdp * 1.3)
        psu_wattage = psu.specs.get("wattage")

        if psu_wattage < required_wattage:
            raise CompatibilityError(
                f"PSU wattage ({psu_wattage}W) is insufficient. Required: {required_wattage}W"
            )

def validate_build(parts):
        parts_by_type = {p.part_type: p for p in parts}

        cpu = parts_by_type.get("cpu")
        motherboard = parts_by_type.get("motherboard")
        ram = parts_by_type.get("ram")
        psu = parts_by_type.get("psu")

        if cpu and motherboard:
            check_cpu_motherboard(cpu, motherboard)

        if ram and motherboard:
            check_ram_motherboard(ram, motherboard)

        if psu:
            check_psu_wattage(psu, parts)

        return True




