radius = float(input("Please enter the tube radius of the torus: "))
cross_sec_radius = float(input("Please enter the cross-setional radius of the torus: "))
mass = float(input("Please enter the mass of the torus: "))

print("-" * 7, "Result", "-" * 7)

print(f"Moment of inertia about a diameter is : {(1/8*(4*radius**2 + 5*cross_sec_radius**2)*mass):.3f}kg sq m")
print(f"Moment of inertia about a vertical axis is : {((radius **2 + 3/4*cross_sec_radius**2)*mass):.3f}kg sq m")
