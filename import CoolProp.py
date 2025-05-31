from iapws import IAPWS97

# Define operating pressure in MPa
pressure = 4.5

# Define the two liquid-phase temperatures in Kelvin
liquid_temperatures = [471.5, 530]

print("=== LIQUID WATER PROPERTIES ===")
print(
    f"{'T (K)':>10} | {'ρ (kg/m³)':>10} | {'Cp (J/kg·K)':>15} | {'k (W/m·K)':>15} | {'μ (Pa·s)':>10}"
)
print("-" * 70)

# Liquid water properties
for T in liquid_temperatures:
    water = IAPWS97(P=pressure, T=T)

    rho = water.rho  # Density [kg/m³]
    cp = water.cp * 1000  # Cp from kJ/kg·K to J/kg·K
    k = water.k  # Thermal conductivity [W/m·K]
    mu = water.mu  # Dynamic viscosity [Pa·s]

    print(f"{T:10.1f} | {rho:10.2f} | {cp:15.2f} | {k:15.5f} | {mu:10.2e}")

# Now get vapor properties at saturation (T=530K, x=1)
saturated_vapor = IAPWS97(T=530, x=1)

print("\n=== SATURATED WATER VAPOR PROPERTIES ===")
print(
    f"{'T (K)':>10} | {'ρ (kg/m³)':>10} | {'Cp (J/kg·K)':>15} | {'k (W/m·K)':>15} | {'μ (Pa·s)':>10}"
)
print("-" * 70)

rho_v = saturated_vapor.rho
cp_v = saturated_vapor.cp * 1000
k_v = saturated_vapor.k
mu_v = saturated_vapor.mu

print(f"{530:10.1f} | {rho_v:10.2f} | {cp_v:15.2f} | {k_v:15.5f} | {mu_v:10.2e}")
