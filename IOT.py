class Machine:
    def __init__(self, mid, plant, operating_hours, downtime,
                 energy, units, maintenance):
        self.mid = mid
        self.plant = plant
        self.operating_hours = operating_hours
        self.downtime = downtime
        self.energy = energy
        self.units = units
        self.maintenance = maintenance

    def efficiency(self):
        if self.operating_hours - self.downtime == 0:
            return 0
        return self.units / (self.operating_hours - self.downtime)

    def production_cost(self):
        if self.units == 0:
            return 0
        return (self.energy + self.maintenance) / self.units


machines = [
    Machine("M101", "Plant A", 100, 10, 5000, 1000, 1200),
    Machine("M102", "Plant A", 120, 20, 6000, 900, 2500),
    Machine("M103", "Plant B", 90, 15, 4500, 700, 3000),
    Machine("M104", "Plant B", 110, 5, 5500, 1200, 1500)
]

print("\nIndustrial IoT Machine Performance Monitoring\n")

for m in machines:
    print("Machine ID:", m.mid)
    print("Plant:", m.plant)
    print("Efficiency:", round(m.efficiency(), 2))
    print("Production Cost per Unit:", round(m.production_cost(), 2))
    print()

print("Inefficient Machines (Efficiency < 10)")
for m in machines:
    if m.efficiency() < 10:
        print(m.mid)

highest = max(machines, key=lambda x: x.maintenance)
print("\nHighest Maintenance Cost")
print(highest.mid, "-", highest.maintenance)

print("\nPlant Wise Efficiency")
plants = {}

for m in machines:
    plants.setdefault(m.plant, []).append(m.efficiency())

for p in plants:
    avg = sum(plants[p]) / len(plants[p])
    print(p, ":", round(avg, 2))

print("\nPreventive Maintenance Required")
for m in machines:
    if m.maintenance > 2000:
        print(m.mid)

machines.sort(key=lambda x: x.efficiency(), reverse=True)

print("\nMachines Sorted by Efficiency")
for m in machines:
    print(m.mid, round(m.efficiency(), 2))

report = open("maintenance_report.txt", "w")

report.write("Maintenance Report\n\n")

for m in machines:
    report.write(f"{m.mid}\n")
    report.write(f"Plant : {m.plant}\n")
    report.write(f"Efficiency : {m.efficiency():.2f}\n")
    report.write(f"Production Cost : {m.production_cost():.2f}\n")
    report.write(f"Maintenance Cost : {m.maintenance}\n\n")

report.close()

print("\nReport Saved Successfully")

print("\nReading Report\n")

report = open("maintenance_report.txt", "r")
print(report.read())
report.close()
