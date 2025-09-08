# RDKit UGM 2025 scikit-fingerprints workshop

Workshop for RDKit UGM 2025 on scikit-fingerprints. We cover various capabilities
of scikit-fingerprints and compare it to RDKit.

Warning: this is an advanced tutorial, assuming knowledge of RDKit and chemoinformatics.

If you are looking for a totally introductory materials, see our
[workshop on molecular ML](https://github.com/j-adamczyk/molecular_ml_workshops)
or [scikit-fingerprints tutorials](https://scikit-fingerprints.readthedocs.io/latest/examples.html).

## Setup

Preferred way is to use [uv dependency manager](https://docs.astral.sh/uv/).

On Linux and macOS, run:
```commandline
uv venv && source .venv/bin/activate && uv sync
```

On Windows CMD, run:
```commandline
uv venv && .venv\Scripts\activate && uv sync
```

On Windows PowerShell, run:
```commandline
uv venv; .venv\Scripts\Activate.ps1; uv sync
```

If you prefer plain `venv` or to use Conda, use `requirements.txt`:
```commandline
pip install -r requirements.txt
```
