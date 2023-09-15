import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("climate.db")
cursor = conn.cursor()
cursor.execute("SELECT year, co2, temperature FROM climate_data")
data = cursor.fetchall()

years = [row[0] for row in data]
co2 = [row[1] for row in data]
temp = [row[2] for row in data]

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")
