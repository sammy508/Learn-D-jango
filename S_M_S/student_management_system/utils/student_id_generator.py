

def generate_student_id(course_code: str, last_number: int) -> str:
    """
    Example: course_code='BCA', last_number=1
    Returns: 'BCA-00002'
    """
    new_number = last_number + 1
    return f"{course_code}-{new_number:05d}"
