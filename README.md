# HGCAL_OGP-DB_Tester

A test harness for validating HGCAL AutoDB offset calculations using spoofed OGP survey data.

This repository generates synthetic component measurements, writes OGP-style survey files, and compares expected offsets against database values returned by AutoDB.

## What it does

- Generates spoofed geometry for protomodules and modules
- Uses reverse offset logic to calculate fake feature point coordinates
- Writes temporary OGP survey files for each spoofed component
- Runs the AutoDB workflow via PowerShell and captures results
- Compares expected X/Y/angle offsets against values read from PostgreSQL

## Main files

- `RunDiagnosticV1.py`
  - Entry point for the verification workflow
  - Runs a batch of shape tests for different densities and positions

- `All_Shapes_VerificationTool_V2.py`
  - Orchestrates test sequences for protomodules and modules
  - Calls `VerificationTool_ALL.Generate_Spoof_Components`
  - Executes the AutoDB runner and compares results

- `VerificationTool_ALL.py`
  - Builds spoofed component data and writes OGP-style survey files
  - Uses `ReverseOffsets.reverse_offsets` to compute fake feature detector positions
  - Calls `PGConnect.Get_PG_Info_By_Name` to fetch offsets from the database

- `ReverseOffsets.py`
  - Encodes geometry-specific reverse offset calculations
  - Returns fake FD point coordinates based on shape, density, and component type

- `PGConnect.py`
  - Connects to PostgreSQL to fetch computed offsets for protomodules and modules
  - Uses `psycopg2`

## Requirements

- Python 3.x
- `numpy`
- `psycopg2`
- PowerShell (Windows)
- Access to the target AutoDB repository and runtime
- PostgreSQL database containing `proto_inspect` and `module_inspect`

## Setup

1. Install Python packages:

```powershell
pip install numpy psycopg2
```

2. Update database connection settings in `PGConnect.py`:

- `database`
- `host`
- `user`
- `password`
- `port`

3. Update AutoDB path in `All_Shapes_VerificationTool_V2.py` and `ReverseOffsets.py` if needed:

- `cd C:\Users\Admin\HGC_OGP_DB`
- `python .\rwOGP\main.py`

4. Update output paths in `VerificationTool_ALL.py` if the local OGP results folders differ from the hard-coded paths.

## Usage

From the repository root, run:

```powershell
python RunDiagnosticV1.py
```

This executes the default test set and prints any comparison results or offset mismatches.

## Notes

- The current code is written for a Windows environment and uses hard-coded paths.
- Components are generated with fixed test angles and offsets.
- Some shapes and positions are currently disabled in `RunDiagnosticV1.py` via comments.
- The database query logic assumes specific table schemas and result ordering.

## Recommended improvements

- Parameterize paths, database settings, and test inputs
- Add command-line arguments for shapes, positions, and offsets
- Replace hard-coded PowerShell commands with a configurable runner
- Add structured logging for easier diagnostics
