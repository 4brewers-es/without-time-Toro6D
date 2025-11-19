import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Configuración estilo "Paper Científico"
plt.rcParams.update({
    "text.usetex": False, # Cambiar a True si tienes LaTeX instalado en el sistema
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "font.size": 12,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.figsize": (6, 4),
    "savefig.dpi": 300
})

def plot_lemniscate():
    """Genera la Figura 1: Topología de Lemniscata de Bernoulli"""
    t = np.linspace(0, 2*np.pi, 1000)
    # Ecuación paramétrica de la Lemniscata (a=1)
    # x = a * cos(t) / (1 + sin^2(t))
    # y = a * sin(t) * cos(t) / (1 + sin^2(t))
    a = 1
    x = (a * np.cos(t)) / (1 + np.sin(t)**2)
    y = (a * np.sin(t) * np.cos(t)) / (1 + np.sin(t)**2)

    fig, ax = plt.subplots()
    
    # Dibujar curva
    ax.plot(x, y, color='black', linewidth=2, label=r'Entropic Bulk ($M_9$)')
    
    # Anotaciones de los loops
    ax.text(0.5, 0.1, 'Universe\n(Matter)', ha='center', fontsize=10)
    ax.text(-0.5, 0.1, 'Mirror\n(Anti-Matter)', ha='center', fontsize=10)
    
    # Punto de cruce (Singularidad/Tensión)
    ax.plot(0, 0, 'ro', markersize=5, label=r'Nucleation Point ($S_0$)')

    ax.set_title('Bernoulli Lemniscate Topology ($b_1=2$)')
    ax.axis('equal')
    ax.axis('off') # Ocultar ejes para diagrama topológico
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('lemniscate_topology_placeholder.pdf')
    print("Generada: lemniscate_topology_placeholder.pdf")
    plt.close()

def plot_shadow():
    """Genera la Figura 2: Comparación de Sombra de Agujero Negro"""
    fig, ax = plt.subplots()

    # Radio de Schwarzschild (normalizado a 1 para visualización)
    rs = 1.0 
    
    # Radio Sombra GR (Standard) ~ 2.6 * Rs
    r_shadow_gr = 2.6 * rs
    
    # Radio Sombra TORO6 (+4.2%)
    r_shadow_toro = r_shadow_gr * 1.042

    # Dibujar Discos
    # 1. Sombra TORO6 (Borde exterior visible)
    circle_toro = Circle((0, 0), r_shadow_toro, color='red', alpha=0.3, label='TORO6 Prediction (+4.2%)')
    ax.add_patch(circle_toro)
    
    # 2. Sombra GR (Borde interior estándar)
    circle_gr = Circle((0, 0), r_shadow_gr, fill=False, edgecolor='black', linestyle='--', linewidth=2, label='GR Prediction')
    ax.add_patch(circle_gr)
    
    # 3. El "Agujero" negro central (Event Horizon visual aproximado)
    circle_bh = Circle((0, 0), rs, color='black')
    ax.add_patch(circle_bh)

    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)
    ax.set_aspect('equal')
    
    ax.set_xlabel(r'Impact Parameter ($b/M$)')
    ax.set_ylabel(r'Impact Parameter ($b/M$)')
    ax.set_title('Sgr A* Shadow Diameter Prediction')
    ax.legend(loc='upper right')
    
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig('shadow_simulation_placeholder.pdf')
    print("Generada: shadow_simulation_placeholder.pdf")
    plt.close()

if __name__ == "__main__":
    plot_lemniscate()
    plot_shadow()
