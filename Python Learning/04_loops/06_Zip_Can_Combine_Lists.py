# Zip ka matlab hai do (ya zyada) lists ko parallel me combine karke tuples banana.

names = ["Govind", "NAGORI", "Aaman", "Ronak"]
bills = [50, 70, 100, 55]

# zip(names, bills) => ('Govind', 50), ('NAGORI', 70) ...
for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")

