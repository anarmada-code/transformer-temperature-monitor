# Transformer Temperature Monitor
# Simple Python Simulation

print("===================================")
print("     TRANSFORMER TEMPERATURE MONITOR")
print("===================================")

# Temperature limits in degree Celsius
NORMAL_LIMIT = 70
COOLING_LIMIT = 80
TRIP_LIMIT = 90

# Get temperature from the user
temperature = float(input("Enter transformer temperature (°C): "))

print("\nTemperature:", temperature, "°C")

# Check temperature condition
if temperature < NORMAL_LIMIT:
    print("Status: NORMAL")
    print("Cooling Fan: OFF")
    print("Alarm: OFF")

elif temperature < COOLING_LIMIT:
    print("Status: TEMPERATURE RISING")
    print("Cooling Fan: ON")
    print("Alarm: OFF")

elif temperature < TRIP_LIMIT:
    print("Status: HIGH TEMPERATURE")
    print("Cooling Fan: ON")
    print("Alarm: ON")
    print("Warning: Check transformer loading and cooling.")

else:
    print("Status: CRITICAL OVERHEATING")
    print("Cooling Fan: ON")
    print("Alarm: ON")
    print("Trip Protection: ACTIVE")
    print("Warning: Transformer should be disconnected safely.")

print("\nMonitoring completed.")
