class BudgetProfileError(Exception):
    pass


BUDGET_PROFILES = {
    "gaming": {
        "cpu": 0.25,
        "gpu": 0.40,
        "ram": 0.10,
        "storage": 0.10,
        "psu": 0.07,
        "case": 0.08,
    },
    "office": {
        "cpu": 0.35,
        "gpu": 0.10,
        "ram": 0.20,
        "storage": 0.15,
        "psu": 0.10,
        "case": 0.10,
    },
}
def allocate_budget(total_budget, use_case):
    profile = BUDGET_PROFILES.get(use_case)

    if not profile:
        raise BudgetProfileError(f"Unknown use case: {use_case}")

    allocation = {}
    for part_type, ratio in profile.items():
        allocation[part_type] = int(total_budget * ratio)

    return allocation
