[![Python package](https://github.com/ZipRecruiter/zr_murmur2/actions/workflows/python-package.yml/badge.svg)](https://github.com/ZipRecruiter/zr_murmur2/actions/workflows/python-package.yml)

# Murmur2
This is Murmur2 hash wrapper for Python.

This was forked and extended from https://github.com/gsmcwhirter/zr_murmur2.

## How to install

### PIP install

You can install from pip:
```bash
pip install git+git://github.com/gsmcwhirter/zr_murmur2.git
```

### Manual Install

If you want to install Murmur2 from a local download, execute the following script.
```bash
python setup.py install
```

## How to use

Functions:

- `hash_32` (MurmurHash2 32-bit)
- `hash_32a` (MurmurHash2A 32-bit -- Merkle-Damgard construction)
- `hash_32al` (MurmurHashAligned2 32-bit)
- `hash_32n` (MurmurHashNeutral2 32-bit)
- `hash_64a` (MurmurHash64A 64-bit for 64-bit architecture)
- `hash_64b` (MurmurHash64B 64-bit for 32-bit architecture)

Example:
```
import zr_murmur2

print zr_murmur2.hash_64a(key="test", seed=100)
```

The first argument, "test", is input to be hashed.
The second argument is a seed. The seed is optional and defaults to 0.

You can pass parameters by position or keyword.

