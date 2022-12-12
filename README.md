# pyfucc

[BrainFuck](https://esolangs.org/wiki/Brainfuck) interpreter, implemented in Python.

![./pyfucc-repl-thumbnail-Dec-12-2022.png](pyfucc-repl-thumbnail-Dec-12-2022.png)

## BrainFuck


| Command | Description |
| ------- | ----------- |
| `>` | Move the pointer to the right |
| `<` | Move the pointer to the left |
| `+` | Increment the memory cell at the pointer
| `-` | Decrement the memory cell at the pointer
| `.` | Output the character signified by the cell at the pointer
| `,` | Input a character and store it in the cell at the pointer
| `[` | Jump past the matching `]` if the cell at the pointer is 0
| `]` | Jump back to the matching `[` if the cell at the pointer is nonzero
| `$` | Print debug

> I use `$` for debug instead of the usual `#` because I more frequently use "#" in comments when referring to cell number, but don't want to see the debug output


## Source File

Run files ending in `.bf`

```powershell
python .\pyfucc\main.py --src .\examples\helloworld.bf
```

## REPL

The same set of cells are used for a single session

Some convenience methods built into the REPL

```bash
:help   Help
:exit   Exit REPL
:about  More information about BrainFuck
:reset  Reset program state
:undo   Undo the last operation
```

-----

**Table of Contents**

- [pyfucc](#pyfucc)
  - [BrainFuck](#brainfuck)
  - [Source File](#source-file)
  - [REPL](#repl)
  - [Installation](#installation)
  - [License](#license)
  - [Development](#development)

## Installation

```console
python -m pip install pyfucc
```

## License

`pyfucc` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.


## Development

Python 3.11 and Pytest 7 on Windows 11

This project manages environments and dependencies using [Hatch](https://github.com/pypa/hatch). Install with `python -m pip install hatch` or using [pipx](https://pypa.github.io/pipx/)

To work on this project:

```powershell
# Clone rep
git clone https://github.com/ImAKappa/pyfucc.git
# Change directories 
cd pyfucc
# Create environment
hatch env create
# Spawn shell within virtual env
hatch shell
# Test the project
python '.\pyfucc\main.py'
```