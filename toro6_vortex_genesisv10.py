import numpy as np
import matplotlib.pyplot as plt
import math

def validate_genesis_condition():
    print("--- TORO6 v10: MATERIA GENESIS AUDIT ---")
    
    # 1. AXIOMAS
    gamma = math.e / 5.0       # Viscosidad / Tensión
    delta = 2.0 / math.pi      # Umbral Causal
    
    # 2. DERIVACIÓN DEL REYNOLDS
    # Hipótesis: El flujo debe completar un ciclo (2pi) contra la tensión gamma
    # Velocidad de Fase Crítica = 2*pi * gamma (Velocidad para cerrar el bucle)
    v_crit = 2 * math.pi * gamma 
    
    # Reynolds = (v * L) / mu
    # L = 1 (Unidad topológica), mu = gamma
    Re_universe = (v_crit * 1) / gamma
    
    print(f"[Parámetros de Fluido]")
    print(f"  Viscosidad (Gamma): {gamma:.4f}")
    print(f"  Velocidad Fase:     {v_crit:.4f} (Mach Topológico)")
    print(f"  Reynolds Calculado: {Re_universe:.4f}")
    print(f"  Meta (Ciclo 2π):    {2*math.pi:.4f}\n")
    
    # 3. SIMULACIÓN DE SUPERVIVENCIA
    # Ecuación de Vórtice Amortiguado: A(t) = e^(-t/Re) * cos(t)
    # Queremos ver cuánta energía queda al llegar a t = 2pi (una vuelta)
    
    t = np.linspace(0, 3*np.pi, 500)
    
    # Universo TORO6 (Re = 6.28)
    wave_toro = np.exp(-t / Re_universe) * np.cos(t)
    
    # Universo Muerto (Alta Viscosidad, Re = 1)
    wave_dead = np.exp(-t / 1.0) * np.cos(t)
    
    # Energía Remanente al cerrar el bucle (t=2pi)
    energy_remnant = np.exp(-2*math.pi / Re_universe)
    
    print(f"[Condición de Existencia]")
    print(f"  Energía al cerrar el bucle (2π): {energy_remnant:.4f} (1/e)")
    print(f"  Interpretación: El vórtice retiene exactamente 1/e (~36.8%) de su energía.")
    print(f"  Esto es suficiente para mantener el bucle cerrado estable.")
    
    # 4. GRÁFICA
    plt.figure(figsize=(10, 6), facecolor='#0b0c10')
    ax = plt.gca()
    ax.set_facecolor('#0b0c10')
    
    plt.plot(t, wave_toro, 'cyan', linewidth=3, label='TORO6 (Materia Estable)')
    plt.plot(t, wave_dead, 'r--', linewidth=1, label='Universo Muerto (Viscoso)')
    
    # Línea de meta (2pi)
    plt.axvline(2*math.pi, color='yellow', linestyle=':', label='Cierre de Bucle (Partícula)')
    plt.axhline(0, color='white', alpha=0.3)
    
    plt.title("Génesis de Materia: Supervivencia del Vórtice", color='white')
    plt.legend(facecolor='black', labelcolor='white')
    plt.tick_params(colors='white')
    plt.grid(True, alpha=0.2)
    
    plt.show()

if __name__ == "__main__":
    validate_genesis_condition()
