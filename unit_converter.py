# unit_converter.py
# Simple Engineering Unit Converter
# By Yamilet Rocha :)

def convert_current(value, unit):
    conversions = {
        "A": value,
        "mA": value * 1e3,
        "uA": value * 1e6
    }
    return conversions

def convert_voltage(value, unit):
    conversions = {
        "V": value,
        "kV": value / 1e3,
        "mV": value * 1e3
    }
    return conversions

def convert_resistance(value, unit):
    conversions = {
        "Ω": value,
        "kΩ": value / 1e3,
        "MΩ": value / 1e6
    }
    return conversions

def convert_frequency(value, unit):
    conversions = {
        "Hz": value,
        "kHz": value / 1e3,
        "MHz": value / 1e6,
        "GHz": value / 1e9
    }
    return conversions

def main():
    print("\n📏 Engineering Unit Converter 📏")
    print("Choose category:")
    print("1. Current (A, mA, uA)")
    print("2. Voltage (V, kV, mV)")
    print("3. Resistance (Ω, kΩ, MΩ)")
    print("4. Frequency (Hz, kHz, MHz, GHz)")

    choice = input("Enter choice (1-4): ")

    value = float(input("Enter value: "))
    unit = input("Enter unit: ")

    if choice == "1":
        result = convert_current(value, unit)
    elif choice == "2":
        result = convert_voltage(value, unit)
    elif choice == "3":
        result = convert_resistance(value, unit)
    elif choice == "4":
        result = convert_frequency(value, unit)
    else:
        print("❌ Invalid choice.")
        return

    print("\n✅ Conversions:")
    for k, v in result.items():
        print(f"{v:.6g} {k}")

if __name__ == "__main__":
    main()
