import math

AB = float(input("Enter AB (vertical side): "))
BC = float(input("Enter BC (horizontal side): "))

# Compute cos(θ) using geometry
cos_theta = BC / math.sqrt(AB**2 + BC**2)

# Compute angle in degrees
theta_rad = math.acos(cos_theta)
theta_deg = math.degrees(theta_rad)

print("Angle MBC =", round(theta_deg), "degrees")