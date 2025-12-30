import numpy as np
import pandas as pd

def calculate_psi(expected, actual, buckets=10):
    breakpoints = np.linspace(0, 100, buckets + 1)
    expected_perc = np.percentile(expected, breakpoints)
    actual_perc = np.percentile(actual, breakpoints)

    psi = 0
    for i in range(buckets):
        e_pct = (
            (expected >= expected_perc[i]) &
            (expected < expected_perc[i + 1])
        ).mean()
        a_pct = (
            (actual >= actual_perc[i]) &
            (actual < actual_perc[i + 1])
        ).mean()

        e_pct = max(e_pct, 0.0001)
        a_pct = max(a_pct, 0.0001)

        psi += (a_pct - e_pct) * np.log(a_pct / e_pct)

    return psi
