## Capacitor Miniproject

import math
e_0 = 8.854E-12
units = ["m^2", "m", "V", "F", "C", "C/m^2", "V/m", "J"]

# Area and distance (A, d) = meters squared and meters
# Voltage (V) = volts
# Capacitance (C) = farads 
# Charge magnitude (Q) = coulombs
# Surface charge density (sigma) = coulombs per meters squared
# Electric field (E) = volts per meter
# Potential energy (U_E) = joules 
class capacitor:
    def __init__(self, plate_area, separation_distance, voltage):
        self.plate_area = plate_area
        self.separation_distance = separation_distance
        self.voltage = voltage
        # C = (A * e_0) / d 
        self.capacitance = (e_0 * self.plate_area) / self.separation_distance
        # Q = C * V
        self.charge_magnitude = self.capacitance * self.voltage
        # sigma = Q / A
        self.surface_charge_density = self.charge_magnitude / self.plate_area
        # E = V / d
        self.electric_field = self.voltage / self.separation_distance
        # U_E = 1/2 * Q * V 
        self.potential_energy = (1/2) * self.charge_magnitude * self.voltage

def capacitor_features(plate_area, separation_distance, voltage):
    capacitor_values = vars(capacitor(plate_area, separation_distance, voltage))
    n = 0
    for quantity in capacitor_values:
        print(quantity, "=", "{:.2E}".format(capacitor_values[quantity]), units[n])
        n += 1

print("A capacitor of circular plates with radii 11 mm, separation distance 6.3 mm, and a potential difference of 11 V across the plates has the following features:")
capacitor_features(math.pi * (0.011**2), 0.0063, 11.0)
print("\nIf we reduce the distance between the plates by half to 3.15 mm, then the values become:")
capacitor_features(math.pi * (0.011**2), 0.00315, 11.0)
print("\nWe can observe that decreasing the distance between the plates of a capacitor with the same plate areas and potential difference increases the capacitance, " +
      "the charge on the surface of each plate, the surface charge densities, and both the electric field and potential energy stored.")
print("\nA capacitor of square plates with side length 25 nm, separation distance 10 nm, and a potential difference of 12 V across the plates has the following features:")
capacitor_features(2.5E-8 ** 2, 1E-8, 12)
print("\nIf we triple the potential difference across the plates to 36 V, then the values become:")
capacitor_features(2.5E-8 ** 2, 1E-8, 36)
print("\nWe can observe that increasing the potential difference across the capacitor plates has no effect on its capacitance, but does increase the surface charge on each plate and surface charge density " +
      "for the plates, as well as increasing the electric field and potential energy stored between them.")     
print("\nA capacitor of rectangular plates with width 20 km, length 10 km, separation distance 50 mm, and a potential difference of 300 V across the plates has the following features:")
capacitor_features(20000 * 10000, 0.05, 300.0)
print("\nIf we scale the widths and lengths of the rectangular plates by a factor of 10 (to 200 and 100 km respectively), then the values become:")
capacitor_features(200000 * 100000, 0.05, 300.0)
print("\nBy increasing the size of the plates, we can see that the capacitance increases along with both the surface charge magnitude and densities for the plates, and the electric field " +
      "and potential energy between them. We can also notice that these values scale by a factor of 100 instead of 10 as a result of the area (10 * 10) used in their calculations. " +
      "Finally, we also notice that the required dimensions of a capacitor to have a capacitance of more than even 1 F is massive without the presence of a dielectric!")
print("\nFrom the values for each capacitor above, we can also ultimately conclude that the capacitance of a parallel plate capacitor is solely dependent on the separation distance of its plates " +
      "and the area of the plates (as well as any dielectric between them, using the permittivity of free space for these example capacitors).")
