"""
ISSP Classifier - Information Self-Sufficiency Principle for galaxies

© 2026 Andrey Murdasov — All rights reserved for original research and visuals; 
all classification data and source code are publicly available on 
Zenodo under CC BY 4.0. Independent researcher.
"""

import numpy as np

# Пороги из основной статьи v4.2
K_THRESHOLD_LOW = 1e3    # K ≤ 1000 → Class III
K_THRESHOLD_HIGH = 3e4   # K > 30000 → Class I

def classify_peqs(sigma, R_eff_kpc, N_n):
    """
    ISSP v4.3.1 with PEQS environmental filter.
    
    Parameters
    ----------
    sigma : float
        Velocity dispersion [km/s]
    R_eff_kpc : float  
        Effective radius [kpc]
    N_n : int
        Number of neighbors within 500 kpc
        
    Returns
    -------
    dict with K, class_name, class_code, subclass
    """
    K = sigma**2 / R_eff_kpc
    
    # Базовая классификация ISSP (v4.3.1)
    if K > 30000:
        base_class = 'I_Self-Sufficient'
        base_code = 1
        # PEQS-уточнение
        if N_n == 0:
            subclass = 'Pure_Relic'
            full_name = 'I_Pure_Relic'
        else:
            subclass = 'Exogenous_Quasi-PI'
            full_name = 'I_Exogenous_Quasi-PI'
    elif K > 1000:
        base_class = 'II_Balanced'
        base_code = 2
        subclass = None
        full_name = base_class
    else:
        base_class = 'III_DM-Dependent'
        base_code = 3
        subclass = None
        full_name = base_class
    
    return {
        'K': K,
        'class': full_name,
        'class_code': base_code,
        'subclass': subclass,
        'N_n': N_n
    }