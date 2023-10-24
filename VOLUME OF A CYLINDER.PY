import math

def calculate_cylinder_volume(radius, height):
    """
    Calculates the volume of a cylinder.

    Args:
        radius (float): The radius of the base of the cylinder.
        height (float): The height of the cylinder.

    Returns:
        float: The volume of the cylinder.
    """
    return math.pi * radius**2 * height
