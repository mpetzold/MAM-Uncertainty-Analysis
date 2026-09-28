from pathlib import Path
import swprocess
import matplotlib.pyplot as plt


# ============================================================
# 1. DIRECTORIOS DEL PROYECTO
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent

DATA_DIR = PROJECT_DIR / "data"
RESULTS_DIR = PROJECT_DIR / "results"
FIGURES_DIR = PROJECT_DIR / "figures"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. ARCHIVOS DE ENTRADA
# ============================================================

fk_file = DATA_DIR / "tome_fk_vt.max"
hfk_file = DATA_DIR / "tome_hfk_vt.max"


# ============================================================
# 3. LECTURA DE ARCHIVOS .MAX
# ============================================================

wavetype = "rayleigh"

fk_suite = swprocess.PeaksSuite.from_max(
    fnames=[str(fk_file)],
    wavetype=wavetype,
)

hfk_suite = swprocess.PeaksSuite.from_max(
    fnames=[str(hfk_file)],
    wavetype=wavetype,
)


print("\n========================================")
print("        LECTURA DE ARCHIVOS .MAX")
print("========================================")

print("\nFK")
print("Archivo:", fk_file.name)
print("Número de objetos Peaks:", len(fk_suite))

print("\nHRFK")
print("Archivo:", hfk_file.name)
print("Número de objetos Peaks:", len(hfk_suite))


# ============================================================
# 4. EXPORTACIÓN DE LOS PEAKS SUITE COMPLETOS
# ============================================================

labels = [
    "fk",
    "hfk",
]

suites = [
    fk_suite,
    hfk_suite,
]

output_fname_prefix = "tome"

for label, suite in zip(labels, suites):

    output_file = RESULTS_DIR / (
        f"{output_fname_prefix}_{wavetype}_{label}.json"
    )

    suite.to_json(fname=str(output_file))

    print("\nJSON guardado:")
    print(output_file)


# ============================================================
# 5. EXTRACCIÓN DE TODOS LOS MÁXIMOS
# ============================================================

def extract_peaks(peaks_suite):
    """
    Extrae todos los máximos contenidos en un PeaksSuite.

    No utiliza simplify_mpeaks(), por lo que conserva
    los múltiples máximos identificados por Geopsy.
    """

    frequencies = []
    velocities = []
    wavelengths = []

    for peak in peaks_suite:

        frequencies.extend(peak.frequency)
        velocities.extend(peak.velocity)
        wavelengths.extend(peak.wavelength)

    return frequencies, velocities, wavelengths


fk_frequency, fk_velocity, fk_wavelength = extract_peaks(
    fk_suite
)

hfk_frequency, hfk_velocity, hfk_wavelength = extract_peaks(
    hfk_suite
)


print("\n========================================")
print("        INFORMACIÓN EXTRAÍDA")
print("========================================")

print("\nFK")
print("Frecuencias:", len(fk_frequency))
print("Velocidades:", len(fk_velocity))
print("Longitudes de onda:", len(fk_wavelength))

print("\nHRFK")
print("Frecuencias:", len(hfk_frequency))
print("Velocidades:", len(hfk_velocity))
print("Longitudes de onda:", len(hfk_wavelength))


# ============================================================
# 6. FIGURA FK vs HRFK
# ============================================================

fig, axes = plt.subplots(
    1,
    2,
    figsize=(15, 6),
)


# ------------------------------------------------------------
# Panel izquierdo
# Velocidad vs frecuencia
# ------------------------------------------------------------

ax = axes[0]

ax.scatter(
    fk_frequency,
    fk_velocity,
    s=5,
    alpha=0.35,
    label="FK",
)

ax.scatter(
    hfk_frequency,
    hfk_velocity,
    s=5,
    alpha=0.35,
    label="HRFK",
)

ax.set_xlabel("Frecuencia (Hz)")
ax.set_ylabel("Velocidad de fase (m/s)")
ax.set_title("Velocidad vs frecuencia")

ax.grid(True, alpha=0.3)
ax.legend()


# ------------------------------------------------------------
# Panel derecho
# Velocidad vs longitud de onda
# ------------------------------------------------------------

ax = axes[1]

ax.scatter(
    fk_wavelength,
    fk_velocity,
    s=5,
    alpha=0.35,
    label="FK",
)

ax.scatter(
    hfk_wavelength,
    hfk_velocity,
    s=5,
    alpha=0.35,
    label="HRFK",
)

ax.set_xlabel("Longitud de onda (m)")
ax.set_ylabel("Velocidad de fase (m/s)")
ax.set_title("Velocidad vs longitud de onda")

ax.grid(True, alpha=0.3)
ax.legend()


# ============================================================
# 7. GUARDAR FIGURA
# ============================================================

fig.suptitle(
    "Análisis de máximos de dispersión: FK vs HRFK",
    fontsize=14,
)

fig.tight_layout()

figure_file = FIGURES_DIR / "tome_fk_vs_hfk_dispersion.png"

fig.savefig(
    figure_file,
    dpi=300,
    bbox_inches="tight",
)

print("\nFigura guardada:")
print(figure_file)

plt.show()