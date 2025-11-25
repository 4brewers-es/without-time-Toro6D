import numpy as np
import matplotlib.pyplot as plt

def plot_lusion_style_torus():
    print("--- TORO6: PARTICLE FLOW VISUALIZATION (Lusion Style) ---")
    
    # 1. CONFIGURACIÓN: Nube de Puntos Masiva
    num_particles = 50000 
    
    # 2. GEOMETRÍA BASE (Toroide)
    R = 4.0 # Radio mayor
    r = 1.5 # Radio menor
    
    # Generamos partículas aleatorias en el dominio (u, v)
    # Esto simula la "espuma cuántica" antes de organizarse
    u = np.random.uniform(0, 2*np.pi, num_particles)
    v = np.random.uniform(0, 2*np.pi, num_particles)
    
    # 3. LA FÍSICA (Tensión y Fuga)
    leakage = 0.01379
    # El ruido no es uniforme, sigue patrones de interferencia (Cimática)
    noise = (r * leakage * 8.0) * np.sin(3*u) * np.cos(5*v)
    
    # 4. POSICIONAMIENTO (Mapeo al Espacio 3D)
    r_dynamic = r + noise
    
    x = (R + r_dynamic * np.cos(v)) * np.cos(u)
    y = (R + r_dynamic * np.cos(v)) * np.sin(u)
    z = r_dynamic * np.sin(v)
    
    # 5. COLORIZACIÓN POR ENERGÍA (El toque Lusion)
    # Las partículas más "tensas" (mayor ruido) brillan más
    # Usamos la distancia al centro del tubo como métrica de energía
    energy = np.abs(noise)
    
    # 6. RENDERIZADO
    fig = plt.figure(figsize=(12, 12), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')
    
    # Scatter plot con transparencia (alpha) para efecto "volumétrico"
    # cmap='cool' da ese toque cian/magenta de sci-fi
    ax.scatter(x, y, z, c=energy, cmap='cool', s=0.5, alpha=0.6, linewidth=0)
    
    # Limpieza
    ax.axis('off')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_zlim(-4, 4)
    
    plt.title("TORO6 Particle Emergence\n(Entropy Flow Visualization)", color='white', fontsize=10)
    
    # Guardar en alta calidad
    plt.savefig("toro6_particle_cloud.png", dpi=300, bbox_inches='tight', facecolor='black')
    print("[SUCCESS] Imagen generada: 'toro6_particle_cloud.png'")
    print("Parece sólido, pero es polvo atrapado en la geometría.")
    plt.show()

if __name__ == "__main__":
    plot_lusion_style_torus()
