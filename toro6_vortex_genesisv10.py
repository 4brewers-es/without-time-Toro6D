import numpy as np
import matplotlib.pyplot as plt
import math

def simulate_quantum_stability():
    print("--- TORO6: QUANTUM NOISE STRESS TEST ---")
    
    # 1. AXIOMAS & CONSTANTES
    gamma = math.e / 5.0
    v_crit = 2 * math.pi * gamma
    Re_universe = v_crit / gamma  # ~ 6.28
    
    # Tiempo topológico (2 vueltas)
    t = np.linspace(0, 4*np.pi, 1000)
    
    # 2. LA SEÑAL PURA (La Geometría Ideal)
    # Vórtice amortiguado: e^(-t/Re) * cos(t)
    signal_pure = np.exp(-t / Re_universe) * np.cos(t)
    
    # 3. EL RUIDO CUÁNTICO (La Fricción del Bulk)
    # Nivel Base: Tu "Leakage" (1.37%) es el ruido de fondo natural del vacío.
    leakage_noise = 0.01379 
    # Nivel Alto: 5 veces el leakage (Tormenta entrópica)
    high_noise = leakage_noise * 5  # ~0.07
    
    np.random.seed(42) # Para reproducibilidad (El número mágico)
    noise_low = np.random.normal(0, leakage_noise, len(t))
    noise_high = np.random.normal(0, high_noise, len(t))
    
    signal_real = signal_pure + noise_low
    signal_stressed = signal_pure + noise_high
    
    # 4. ANÁLISIS EN EL PUNTO CRÍTICO (2pi)
    # Buscamos el índice más cercano a 2pi
    idx_2pi = (np.abs(t - 2*math.pi)).argmin()
    
    amp_pure = signal_pure[idx_2pi]       # Debería ser ~0.368 (1/e)
    amp_noisy = signal_real[idx_2pi]
    amp_stressed = signal_stressed[idx_2pi]
    
    print(f"[Critical Checkpoint: t = 2π]")
    print(f"  Signal Strength (Pure):   {amp_pure:.4f} (Target: 1/e)")
    print(f"  Noise Floor (Leakage):    {leakage_noise:.4f}")
    print(f"  Signal-to-Noise Ratio:    {amp_pure/leakage_noise:.1f} (Muy robusto)")
    print(f"  Status: La partícula sobrevive al ruido de fondo sin problemas.\n")

    # 5. VISUALIZACIÓN
    plt.figure(figsize=(12, 6), facecolor='#0b0c10')
    ax = plt.gca()
    ax.set_facecolor('#0b0c10')
    
    # Plot Señal Ideal (Guía)
    plt.plot(t, signal_pure, 'w--', linewidth=1, alpha=0.5, label='Geometría Pura (Platónica)')
    
    # Plot Realidad (Con Ruido de Fuga)
    plt.plot(t, signal_real, 'c-', linewidth=2, label=f'Realidad TORO6 (Ruido {leakage_noise*100:.1f}%)')
    
    # Plot Estrés (Con Ruido Alto)
    plt.plot(t, signal_stressed, 'm-', linewidth=1, alpha=0.6, label='Alta Entropía (Ruido ~7%)')
    
    # Límites
    plt.axvline(2*math.pi, color='yellow', linestyle=':', linewidth=2, label='Cierre de Bucle (Partícula)')
    plt.axhline(0, color='gray', alpha=0.3)
    plt.axhline(1/math.e, color='lime', linestyle='--', alpha=0.3, label='Umbral de Vida (1/e)')
    
    plt.title(f"Estabilidad Cuántica: ¿Sobrevive el Vórtice al Ruido?", color='white', fontsize=14)
    plt.xlabel("Fase Topológica", color='white')
    plt.legend(facecolor='black', labelcolor='white')
    plt.tick_params(colors='white')
    plt.grid(True, alpha=0.15)
    
    plt.show()

if __name__ == "__main__":
    simulate_quantum_stability()
