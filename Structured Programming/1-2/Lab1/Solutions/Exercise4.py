#Exercise4.py

#This program reads in the tube radius, cross-sectional radius and mass of a
#torus and uses them to determine its moments of inertia

tubeRadius = input("Please enter the tube radius of the torus: ")
tubeRadius = float(tubeRadius)


xsectionalRadius = input("Please enter the cross-sectional radius of the torus: ")
xsectionalRadius = float(xsectionalRadius)

mass = input("Please enter the mass of the torus: ")
mass = float(mass)

momentOfInertiaAboutDiameter = (1/8)*(4*tubeRadius**2 +
                                      5*xsectionalRadius**2)*mass
        
momentOfInertiaAboutVerticalAxis = (tubeRadius**2 +
                                    0.75*xsectionalRadius**2)*mass;


print("\n=======Results========\n\nMoment of inertia about a diameter is : " + 
      "%.3f" % momentOfInertiaAboutDiameter + "kg sq m" +
      "\nMoment of inertia about a vertical axis is : " + 
      "%.3f" % momentOfInertiaAboutVerticalAxis + "kg sq m");
                        
 

