


def generate_id(prefix: str, last_id: int) -> str:
    # increment last id
    new_id = last_id + 1
    # format with leading zeros (5 digits → 00001, 00002, etc.)
    return f"{prefix}-{new_id:05d}"