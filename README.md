# Active Self-Righting Buoy Project

An exploratory engineering project investigating whether event-triggered moving ballast can reduce buoy roll while using less energy than continuous control.

**Current stage: Week 1 — simplified roll simulation and reproducible parameter experiments.** Moving ballast, control and energy consumption are not yet implemented.

## Model and experiments

The educational model is θ(t) = θ₀ exp(−bt) cos(ωt), sampled at 1,000 points over 0–20 seconds. θ₀ is in degrees, b is an amplitude decay rate in s⁻¹, and ω is angular frequency in rad/s.

| Simulation | θ₀ (°) | b (s⁻¹) | ω (rad/s) |
|---|---:|---:|---:|
| Baseline | 10 | 0.15 | 2.0 |
| Experiment A | 20 | 0.15 | 2.0 |
| Experiment B | 10 | 0.40 | 2.0 |
| Experiment C | 10 | 0.15 | 3.0 |

## Week 1 results

| Simulation | Maximum roll (°) | RMS roll (°) | Settling time (s) | Oscillation estimate |
|---|---:|---:|---:|---:|
| Baseline | 10.00 | 2.90 | 14.41 | 6 |
| Experiment A | 20.00 | 5.80 | 19.12 | 6 |
| Experiment B | 10.00 | 1.81 | 5.09 | 6 |
| Experiment C | 10.00 | 2.89 | 14.81 | 9 |

Increasing initial angle scales the roll amplitude. Increasing amplitude decay rate reduces RMS roll and settling time for the tested cases. Increasing angular frequency shortens the period from 3.14 s to 2.09 s while leaving the exponential amplitude envelope unchanged.

Settling time is measured after the last sample outside ±1° in the recorded 20-second window; it is not an infinite-time guarantee. Oscillations are estimated by counting pairs of zero crossings.

## Files

- notebooks/01_buoy_simulation_basics.ipynb: Sessions 1–3, figures, observations and export code.
- results/week1_results.csv: verified results table.
- docs/VERIFICATION.md: execution and comparison record.
- docs/EXPLAIN_WEEK1_ZH.md: Chinese explanation for presenting the work.
- run_week1.py: standard-library numerical reproduction script.

## Reproduce

# Active Self-Righting Buoy Project

An exploratory engineering project investigating whether event-triggered moving ballast can reduce buoy roll while using less energy than continuous control.

**Current stage: Week 1 — simplified roll simulation and reproducible parameter experiments.** Moving ballast, control and energy consumption are not yet implemented.

## Model

The educational model is θ(t) = θ₀ exp(−bt) cos(ωt), sampled at 1,000 points over 0–20 seconds. θ₀ is in degrees, b is an amplitude decay rate in s⁻¹, and ω is angular frequency in rad/s.

## Week 1 results

| Simulation | Maximum roll (°) | RMS roll (°) | Settling time (s) | Oscillations |
|---|---:|---:|---:|---:|
| Baseline | 10.00 | 2.90 | 14.41 | 6 |
| Experiment A | 20.00 | 5.80 | 19.12 | 6 |
| Experiment B | 10.00 | 1.81 | 5.09 | 6 |
| Experiment C | 10.00 | 2.89 | 14.81 | 9 |

Increasing initial angle scales roll amplitude. Increasing amplitude decay rate reduces RMS roll and settling time for the tested cases. Increasing angular frequency shortens the period while leaving the exponential amplitude envelope unchanged.

## Project files

- notebooks/01_buoy_simulation_basics.ipynb — complete Sessions 1–3 notebook.
- results/week1_results.csv — verified results.
- docs/VERIFICATION.md — execution record.
- docs/EXPLAIN_WEEK1_ZH.md — Chinese presentation notes.
- run_week1.py — numerical reproduction script.

## Limits

This is a prescribed educational signal, not a validated hydrodynamic model. Week 1 does not simulate wave forcing, buoy geometry, ballast motion, actuator limits, power use, capsizing or large-angle recovery. It does not yet establish that event-triggered control saves energy or that a physical buoy will self-right.

The next stage will add physical roll and actuator equations, identical disturbances, and an explicit energy model.

The script regenerates the CSV and checks all 16 values against the original export. To run the complete notebook including plots, open it in Google Colab and select **Run all**.

## Limits and next stage

The damped cosine is a prescribed educational signal, not a validated hydrodynamic model. Week 1 does not simulate wave forcing, buoy geometry, ballast motion, actuator limits, sensor noise, power use, capsizing or large-angle recovery. It cannot establish that event-triggered control saves energy or that a physical buoy will self-right.

The next stage will specify the physical roll and actuator equations, apply identical disturbances to each control strategy, define an energy model and validate numerical convergence before drawing control-performance conclusions.
