portugal_regions = ["Alentejo", "Algarve", "Centro", "Lisboa", "Norte", "Açores", "Madeira"]

print (portugal_regions[0])  # Alentejo
print (portugal_regions[1])  # Algarve
print (portugal_regions[2])  # Centro
print (portugal_regions[3])  # Lisboa
print (portugal_regions[4])  # Norte
print (portugal_regions[5])  # Açores
print (portugal_regions[6])  # Madeira
print (portugal_regions[-1]) # Madeira
print (portugal_regions[-2]) # Açores
portugal_regions[0] = "Alentejo Region"
print (portugal_regions[0])  # Alentejo Region
portugal_regions.append("Wonderland")
print (portugal_regions)
portugal_regions.extend(["Hogwarts", "Narnia"])
print (portugal_regions)