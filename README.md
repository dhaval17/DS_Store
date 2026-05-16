# DS_Store Parser

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Python script to view and parse contents of macOS `.DS_Store` files.

## About .DS_Store

The `.DS_Store` file is a macOS system file that stores folder display preferences and metadata. This tool allows you to inspect and extract entries from these files programmatically.

**Before:**

![DS_Store](https://raw.githubusercontent.com/dhaval17/DS_Store/assets/logo.png)

**After:**

![DS_Store](https://pbs.twimg.com/media/BqalhBgCMAA1B5W.jpg)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/dhaval17/DS_Store.git
cd DS_Store
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python dsstore.py -p /path/to/.DS_Store -t Iloc
```

### Parameters

- `-p, --path` (required): Path to the `.DS_Store` file
- `-t, --type` (optional): Entry type to filter (default: `Iloc`)

### Supported Entry Types

- `Iloc` - Position information
- `bwsp` - Browser window position
- `lsvp` - List view properties
- `lsvP` - List view properties (alternate)
- `icvp` - Icon view properties

## Dependencies

The project requires the following Python packages:

- **ds_store** (>=1.3.0): Library for reading `.DS_Store` files
- **tqdm** (>=4.65.0): Progress bar library

Install with: `pip install -r requirements.txt`

## Example

```bash
# View all Iloc entries
python dsstore.py -p ~/.DS_Store -t Iloc

# View bwsp entries with progress bar
python dsstore.py -p /Volumes/External/.DS_Store -t bwsp
```

## Requirements

To manually install dependencies:

```bash
pip install ds_store>=1.3.0
pip install tqdm>=4.65.0
```

## License

This project is provided as-is for educational and utility purposes.

## Contributing

Contributions are welcome! Feel free to submit issues and enhancement requests.

## Disclaimer

This tool is meant for analyzing your own `.DS_Store` files. Ensure you have the necessary permissions before accessing `.DS_Store` files on systems or volumes you don't own.
