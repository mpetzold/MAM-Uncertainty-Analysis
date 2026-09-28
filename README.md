# MAM-Uncertainty-Analysis

Python workflow for processing passive seismic surface-wave dispersion peaks using the **Microtremor Array Method (MAM)**.

The workflow uses **Geopsy** for FK and HRFK processing and [`swprocess`](https://github.com/jpvantassel/swprocess) for Python-based extraction, JSON export, and visualization.

## Workflow

```text
Passive seismic data
        ↓
      Geopsy
        ↓
   FK / HRFK
        ↓
      .max
        ↓
   swprocess
        ↓
   JSON + Figure
```

## Dataset

* 23-channel passive seismic array
* 3 m sensor spacing
* 66 m array length
* Sampling interval: 0.004 s
* Wave type: Rayleigh
* Instrument: PASI Gea24

## Results

The workflow preserves the complete set of dispersion maxima identified by FK and HRFK processing.

### FK vs HRFK dispersion

![FK vs HRFK dispersion](figures/tome_fk_vs_hfk_dispersion.png)

The figure compares phase velocity as a function of frequency and wavelength for the FK and HRFK results.

## Project structure

```text
MAM-Uncertainty-Analysis/
├── data/
│   ├── ReMi_Tome_1.dat
│   ├── tome_fk_vt.max
│   └── tome_hfk_vt.max
├── figures/
│   └── tome_fk_vs_hfk_dispersion.png
├── results/
│   ├── tome_rayleigh_fk.json
│   └── tome_rayleigh_hfk.json
├── mam_processing.py
├── .gitignore
└── README.md
```

## Requirements

```bash
pip install swprocess matplotlib
```

Run the processing with:

```bash
python mam_processing.py
```

## References

* Geopsy
* Vantassel, J. P. — `swprocess`

**Author:** Matías Petzold — Civil Geological Engineer
