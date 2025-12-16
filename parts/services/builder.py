from parts.models import Part
from parts.services.budget import allocate_budget
from parts.services.compatibility import validate_build


class BuildError(Exception):
    pass


def pick_part(part_type, budget, filters=None):
    qs = Part.objects.filter(
        part_type=part_type,
        msrp__lte=budget,
        is_active=True,
    )

    if filters:
        qs = qs.filter(**filters)

    part = qs.order_by("-msrp").first()

    if not part:
        raise BuildError(
            f"No {part_type} found under budget {budget}"
        )

    return part


def generate_build(total_budget, use_case):
    allocation = allocate_budget(total_budget, use_case)

    build_parts = []

    # 1. CPU
    cpu = pick_part("cpu", allocation["cpu"])
    build_parts.append(cpu)

    # 2. Motherboard (must match CPU socket)
    mb = pick_part(
        "motherboard",
        allocation["cpu"],  # OK for MVP
        filters={"specs__socket": cpu.specs["socket"]},
    )
    build_parts.append(mb)

    # 3. RAM (must match motherboard)
    ram = pick_part(
        "ram",
        allocation["ram"],
        filters={"specs__ram_type": mb.specs["ram_type"]},
    )
    build_parts.append(ram)

    # 4. Storage
    storage = pick_part("storage", allocation["storage"])
    build_parts.append(storage)

    # 5. PSU
    psu_budget = allocation["psu"] + allocation.get("remaining", 0) + 300_000

    psu = pick_part("psu", psu_budget)

    build_parts.append(psu)

    # 6. Case
    case = pick_part("case", allocation["case"] + 400_000)

    build_parts.append(case)

    # Final compatibility check
    validate_build(build_parts)

    total_price = sum(p.msrp for p in build_parts)

    return {
        "total_budget": total_budget,
        "total_price": total_price,
        "parts": build_parts,
    }
