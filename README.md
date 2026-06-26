# clae-code

Companion code for *Computational Linear Algebra for Estimation* (CLAE).

Every figure and timing in the book is produced by the per-chapter Jupyter
notebooks here; the book renders these notebook cells (code + output) inline.

## Layout

    ch01/ch01.ipynb     Chapter 1 — Vectors and Linear Combinations
    ch01/figures/       figures the notebook writes

## Running

    jupyter nbconvert --to notebook --execute --inplace ch01/ch01.ipynb

Requires the scientific Python stack: numpy, scipy, matplotlib, pandas, scikit-learn.
