def save(self, *args, **kwargs):
    from .validators import validate_specs
    validate_specs(self.part_type, self.specs)
    super().save(*args, **kwargs)
