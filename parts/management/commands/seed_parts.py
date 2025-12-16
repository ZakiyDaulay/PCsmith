from django.core.management.base import BaseCommand
from parts.models import Part

class Command(BaseCommand):
    help = "Seed initial PC parts dataset"

    def handle(self, *args, **options):
        self.stdout.write("Seeding PC parts...")
        self.seed_cpus()
        self.seed_motherboards()
        self.seed_gpus()
        self.seed_ram()
        self.seed_storage()
        self.seed_psu()
        self.seed_cases()
        self.stdout.write(self.style.SUCCESS("Seeding complete."))
    def seed_storage(self):
        storages = [
            {
                "name": "Samsung 970 EVO Plus 1TB",
                "brand": "Samsung",
                "msrp": 1500000,
                "specs": {"type": "SSD", "capacity": 1000, "interface": "NVMe"},
            },
            {
                "name": "Western Digital Blue 2TB",
                "brand": "Western Digital",
                "msrp": 800000,
                "specs": {"type": "HDD", "capacity": 2000, "interface": "SATA"},
            },
        ]

        for storage in storages:
            Part.objects.update_or_create(
                name=storage["name"],
                defaults={
                    "brand": storage["brand"],
                    "part_type": "storage",
                    "msrp": storage["msrp"],
                    "specs": storage["specs"],
                },
            )
    def seed_cases(self):
        cases = [
            {
                "name": "NZXT H510",
                "brand": "NZXT",
                "msrp": 1200000,
                "specs": {"form_factor": "ATX", "color": "White"},
            },
            {
                "name": "Corsair 4000D Airflow",
                "brand": "Corsair",
                "msrp": 1300000,
                "specs": {"form_factor": "ATX", "color": "Black"},
            },
        ]

        for case in cases:
            Part.objects.update_or_create(
                name=case["name"],
                defaults={
                    "brand": case["brand"],
                    "part_type": "case",
                    "msrp": case["msrp"],
                    "specs": case["specs"],
                },
            )
    def seed_gpus(self):
        gpus = [
            {
                "name": "NVIDIA GeForce RTX 3060",
                "brand": "NVIDIA",
                "msrp": 4000000,
                "specs": {"vram": 12, "base_clock": 1320, "boost_clock": 1777},
            },
            {
                "name": "AMD Radeon RX 6600 XT",
                "brand": "AMD",
                "msrp": 3500000,
                "specs": {"vram": 8, "base_clock": 1968, "boost_clock": 2589},
            },
        ]

        for gpu in gpus:
            Part.objects.update_or_create(
                name=gpu["name"],
                defaults={
                    "brand": gpu["brand"],
                    "part_type": "gpu",
                    "msrp": gpu["msrp"],
                    "specs": gpu["specs"],
                },
            )

    def seed_motherboards(self):
        boards = [
            {
                "name": "B550M DS3H",
                "brand": "Gigabyte",
                "msrp": 1600000,
                "specs": {
                    "socket": "AM4",
                    "ram_type": "DDR4",
                    "max_ram": 128,
                    "form_factor": "mATX",
                },
            },
            {
                "name": "B660M Pro RS",
                "brand": "ASRock",
                "msrp": 1900000,
                "specs": {
                    "socket": "LGA1700",
                    "ram_type": "DDR4",
                    "max_ram": 128,
                    "form_factor": "mATX",
                },
            },
        ]

        for board in boards:
            Part.objects.update_or_create(
                name=board["name"],
                defaults={
                    "brand": board["brand"],
                    "part_type": "motherboard",
                    "msrp": board["msrp"],
                    "specs": board["specs"],
                },
            )

    def seed_cpus(self):
        cpus = [
            {
                "name": "Ryzen 5 5600",
                "brand": "AMD",
                "msrp": 1800000,
                "specs": {"socket": "AM4", "tdp": 65, "cores": 6, "threads": 12},
            },
            {
                "name": "Ryzen 7 5700X",
                "brand": "AMD",
                "msrp": 3000000,
                "specs": {"socket": "AM4", "tdp": 65, "cores": 8, "threads": 16},
            },
            {
                "name": "Core i5-12400F",
                "brand": "Intel",
                "msrp": 2300000,
                "specs": {"socket": "LGA1700", "tdp": 65, "cores": 6, "threads": 12},
            },
        ]

        for cpu in cpus:
            Part.objects.update_or_create(
                name=cpu["name"],
                defaults={
                    "brand": cpu["brand"],
                    "part_type": "cpu",
                    "msrp": cpu["msrp"],
                    "specs": cpu["specs"],
                },
            )

    def seed_ram(self):
        kits = [
            {
                "name": "Corsair Vengeance LPX 16GB",
                "brand": "Corsair",
                "msrp": 700000,
                "specs": {"ram_type": "DDR4", "speed": 3200, "capacity": 16},
            },
            {
                "name": "Kingston Fury Beast 32GB",
                "brand": "Kingston",
                "msrp": 1300000,
                "specs": {"ram_type": "DDR4", "speed": 3200, "capacity": 32},
            },
        ]

        for ram in kits:
            Part.objects.update_or_create(
                name=ram["name"],
                defaults={
                    "brand": ram["brand"],
                    "part_type": "ram",
                    "msrp": ram["msrp"],
                    "specs": ram["specs"],
                },
            )

    def seed_psu(self):
        psus = [
            {
                "name": "Cooler Master MWE 650 Bronze",
                "brand": "Cooler Master",
                "msrp": 950000,
                "specs": {"wattage": 650, "certification": "80+ Bronze"},
            },
            {
                "name": "Corsair CV550",
                "brand": "Corsair",
                "msrp": 850000,
                "specs": {"wattage": 550, "certification": "80+ Bronze"},
            },
        ]

        for psu in psus:
            Part.objects.update_or_create(
                name=psu["name"],
                defaults={
                    "brand": psu["brand"],
                    "part_type": "psu",
                    "msrp": psu["msrp"],
                    "specs": psu["specs"],
                },
            )
