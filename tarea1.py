import numpy as np
import matplotlib.pyplot as plt
import random

# --- Parte 1: Latencia ---
L0 = 3
k = 997
C = 1000

def latencia(n):
    return L0 + k / (C - n)

def derivada_latencia(n):
    return k / ((C - n) ** 2)

def simulacion_servidor():
    usuarios = list(range(1, C-50, 10))
    latencias_teoricas = [latencia(n) for n in usuarios]
    latencias_simuladas = []
    for n in usuarios:
        latencia_empirica = latencia(n) + random.gauss(0, 0.01)
        latencias_simuladas.append(latencia_empirica)
    return usuarios, latencias_teoricas, latencias_simuladas

def graficar_latencia():
    n_values = np.linspace(1, C-1, 1000)
    L_values = [latencia(n) for n in n_values]
    dL_values = [derivada_latencia(n) for n in n_values]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(n_values, L_values, 'b-', linewidth=2)
    ax1.set_xlabel('Número de usuarios (n)')
    ax1.set_ylabel('Latencia L(n)')
    ax1.set_title('Función de Latencia L(n)')
    ax1.grid(True, alpha=0.3)

    ax2.plot(n_values, dL_values, 'r-', linewidth=2)
    ax2.set_xlabel('Número de usuarios (n)')
    ax2.set_ylabel("Derivada L'(n)")
    ax2.set_title("Derivada de la Latencia L'(n)")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('latenciapython.png')
    plt.show()

# --- Parte 2: Rendimiento ---
B = 1000

def rendimiento_por_usuario(n):
    return B * (1 - n / C)

def rendimiento_total(n):
    return B * n * (1 - n / C)

def derivada_rendimiento(n):
    return B * (1 - 2 * n / C)

def derivada_rendimiento_por_usuario(n):
    return -B / C

def encontrar_maximo_rendimiento():
    n_optimo = C / 2
    R_maximo = rendimiento_total(n_optimo)
    return n_optimo, R_maximo

def simulacion_rendimiento():
    usuarios = list(range(1, C, 10))
    R_values = [rendimiento_total(n) for n in usuarios]
    T_values = [rendimiento_por_usuario(n) for n in usuarios]
    return usuarios, R_values, T_values

def graficar_rendimiento():
    n_values = np.linspace(1, C-1, 1000)
    R_values = [rendimiento_total(n) for n in n_values]
    T_values = [rendimiento_por_usuario(n) for n in n_values]
    dR_values = [derivada_rendimiento(n) for n in n_values]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(n_values, R_values, 'g-', linewidth=2, label='R(n) total')
    ax1.plot(n_values, T_values, 'm-', linewidth=2, label='T(n) usuario')
    ax1.set_xlabel('Número de usuarios (n)')
    ax1.set_ylabel('Rendimiento (Mbps)')
    ax1.set_title('Rendimiento Total y por Usuario')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(n_values, dR_values, linewidth=2, label="R'(n)")
    ax2.axhline(y=0, color='r', linestyle='--', alpha=0.7)
    ax2.axvline(x=C/2, color='r', linestyle='--', alpha=0.7, label=f'n óptimo = {C/2}')
    ax2.set_xlabel('Número de usuarios (n)')
    ax2.set_ylabel("Derivada R'(n)")
    ax2.set_title("Derivada del Rendimiento Total")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('rendimiento.png')
    plt.show()

# --- Análisis ---
def analisis_completo():
    print("=" * 60)
    print("ANÁLISIS DE OPTIMIZACIÓN DE REDES")
    print("=" * 60)

    print("\n--- Latencia ---")
    print(f"L'(n) > 1 cuando n > {C - np.sqrt(k):.2f}")

    print("\n--- Rendimiento ---")
    n_optimo, R_maximo = encontrar_maximo_rendimiento()
    print(f"Punto óptimo: n = {n_optimo}")
    print(f"Rendimiento máximo: R({n_optimo}) = {R_maximo:.2f}")

    B_aumentado = B * 1.5
    R_max_aumentado = B_aumentado * C / 4
    incremento = (R_max_aumentado - R_maximo) / R_maximo * 100

    print(f"\nAumento de B en 50% → Mejora de rendimiento: {incremento:.1f}%")

    usuarios, lat_teo, lat_sim = simulacion_servidor()
    error_latencia = np.mean(np.abs(np.array(lat_teo) - np.array(lat_sim)))
    print(f"\nError promedio de latencia simulada: {error_latencia:.4f}")

    usuarios_rend, R_sim, T_sim = simulacion_rendimiento()
    n_opt_sim = usuarios_rend[np.argmax(R_sim)]
    print(f"n óptimo simulado: {n_opt_sim}")

# --- Main ---
if __name__ == "__main__":
    analisis_completo()

    print("\nGenerando gráficas...")
    graficar_latencia()
    graficar_rendimiento()

    print("\n" + "=" * 60)
    print("RESUMEN")
    print("=" * 60)

    n_optimo, R_maximo = encontrar_maximo_rendimiento()
    print(f"Latencia mínima: L(1) = {latencia(1):.4f}")
    print(f"Latencia en n={C-1}: {latencia(C-1):.4f}")
    print(f"Rendimiento máximo: {R_maximo:.2f} Mbps con {n_optimo} usuarios")
    print(f"Rendimiento por usuario en óptimo: {rendimiento_por_usuario(n_optimo):.2f} Mbps")
