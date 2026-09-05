# Week 1 completion record

Status: complete and verified on 2026-09-05.

## Colab notebook

[Open the executed Week 1 notebook in Google Colab](https://colab.research.google.com/drive/1W9caYzYhrxdEa-GK4yepQ5FlxXigTtrk)

## Completed work

- Sessions 1-3 executed in Colab.
- Nine code cells completed without errors.
- Six result figures were generated.
- Four parameter cases were compared over 0-20 seconds with 1,000 samples.
- All 16 numerical outputs were reproduced independently by run_week1.py and matched the original export.
- README documents the model, assumptions, results, limits and next engineering stage.

## Main result

Experiment B increased the decay rate from 0.15 to 0.40 per second. In this educational signal model, RMS roll fell from 2.90 degrees to 1.81 degrees and settling time fell from 14.41 seconds to 5.09 seconds. This is a simulation result, not yet a physical buoy validation.

## Repository files

- run_week1.py reproduces and checks the result table with the Python standard library.
- requirements.txt lists the Colab analysis packages.
- week1_results.csv is the regenerated result table.
- week1_results_original.csv is the original Colab export used for verification.
