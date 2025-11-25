import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_stormy_torus():
    print("--- TORO6: 3D GEOMETRY VISUALIZATION ---")
    
    # 1. CONFIGURACIÓN DEL TORO (R, r)
    R = 4.0 # Radio mayor (El ciclo del universo)
    r = 1.5 # Radio menor (La dimensión compacta)
    
    # 2. MALLA DE COORDENADAS
    u = np.linspace(0, 2 * np.pi, 100) # Ángulo toroidal
    v = np.linspace(0, 2 * np.pi, 100) # Ángulo poloidal
    u, v = np.meshgrid(u, v)
    
    # 3. PERTURBACIÓN ENTRÓPICA (El Ruido Gamma)
    # Añadimos rugosidad a la superficie proporcional a la Fuga (1.37%)
    leakage = 0.01379
    noise_amplitude = r * leakage * 5.0 # Exagerado para verlo
    
    # Ruido determinista (basado en seno/coseno para suavidad)
    # Simula los modos de vibración del Bulk
    noise = noise_amplitude * np.sin(3*u) * np.cos(5*v)
    
    # 4. ECUACIONES PARAMÉTRICAS (Toro Deformado)
    # x = (R + (r + noise) * cos(v)) * cos(u)
    # y = (R + (r + noise) * cos(v)) * sin(u)
    # z = (r + noise) * sin(v)
    
    r_effective = r + noise
    x = (R + r_effective * np.cos(v)) * np.cos(u)
    y = (R + r_effective * np.cos(v)) * np.sin(u)
    z = r_effective * np.sin(v)
    
    # 5. RENDERIZADO
    fig = plt.figure(figsize=(12, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')
    
    # Plotear la superficie
    surf = ax.plot_surface(x, y, z, cmap='ocean', edgecolor='cyan', lw=0.2, alpha=0.8)
    
    # Ajustes de cámara
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-3, 3)
    ax.axis('off') # Quitar ejes para que parezca flotar
    
    plt.title(f"TORO6 Vacuum Geometry\n(Perturbation $\\Gamma \\approx$ {leakage*100:.2f}%)", color='white', fontsize=15)
    
    # Guardar
    plt.savefig("toro6_stormy_wireframe.png", dpi=300, bbox_inches='tight', facecolor='black')
    print("[SUCCESS] Imagen generada: 'toro6_stormy_wireframe.png'")
    plt.show()

if __name__ == "__main__":
    plot_stormy_torus()
