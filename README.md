# Amlogic Video Codec RE

Reverse engineering Amlogic's video decoder/encoder hardware and its integrated
AMRISC CPU.


## Quick start


### Software dependencies

* [GNU Make](https://www.gnu.org/software/make/)
* [curl](https://curl.se/)
* [Python 3](https://www.python.org/)


### Procedure

1. Run `make download` to download the firmware/microcode binaries from the
   linux-firmware repo into the [firmware](firmware) directory.
2. Disassemble the binaries using `disasm.py`.


## Reverse engineering notes

See [Notes.md](Notes.md).
