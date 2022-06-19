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


## License

Except where otherwise stated:

* All software in this repository (e.g., tools for downloading and disassembling
  firmware, etc.) is made available under the
  [Zero-Clause BSD (0BSD) license][license].
* All copyrightable content that is not software (e.g., reverse engineering
  notes, this README file, etc.) is licensed under the
  [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].


[license]: LICENSE.txt
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
