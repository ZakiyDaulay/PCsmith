from django.db import models

class Part(models.Model):
    PART_TYPES = [
        ("cpu", "CPU"),
        ("gpu", "GPU"),
        ("motherboard", "Motherboard"),
        ("ram", "RAM"),
        ("storage", "Storage"),
        ("psu", "Power Supply"),
        ("case", "Case"),
    ]

    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)

    part_type = models.CharField(
        max_length=20,
        choices=PART_TYPES,
        db_index=True
    )

    # Flexible specs (socket, wattage, RAM type, etc.)
    specs = models.JSONField()

    # Reference price (not marketplace price)
    msrp = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        from .services.validators import validate_specs
        validate_specs(self.part_type, self.specs)
        super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=["part_type"]),
            models.Index(fields=["msrp"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.part_type})"
