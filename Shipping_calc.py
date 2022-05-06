weight = int(input("What is your shipping weight? "))
print("What shipping method would you like?")
print("Ground Shipping (GS), Ground Shipping Premium (GSP), Drone Shipping (DS)")
shipping_type = input("GS, GSP, DS>>>")

if shipping_type == "GS":
  # Ground Shipping
  if weight <= 2.0:
    cost_ground = weight * 1.5 + 20
  elif weight > 2.0 and weight <= 6.0:
    cost_ground = weight * 3.0 + 20
  elif weight > 6.0 and weight <= 10:
    cost_ground = weight * 4.0 +20
  else:
    cost_ground = weight * 4.75 + 20
  print("Cost of Ground shipping is $"+str(cost_ground))
elif shipping_type == "GSP":
  # Ground Shipping Premium
  cost_ground_premium = 125
  print("Cost of Premium Ground is $"+str(cost_ground_premium))
else:
  # Drone Shipping
  if weight <= 2.0:
    drone_shipping = weight * 4.5
  elif weight > 2.0 and weight <= 6.0:
    drone_shipping = weight * 9.00
  elif weight > 6.0 and weight <= 10:
    drone_shipping = weight * 12
  else:
    drone_shipping = weight * 14.25
  print("Cost of Drone Shipping is $"+str(drone_shipping))