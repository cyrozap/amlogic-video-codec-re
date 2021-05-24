# Amlogic Video Codec RE

Reverse engineering Amlogic's video decoder/encoder hardware and its integrated
AMRISC CPU.


## Quick start


### Software dependencies

* [GNU Make](https://www.gnu.org/software/make/)
* [curl](https://curl.se/)


### Procedure

1. Run `make download` to download the firmware/microcode binaries from the
   linux-firmware repo.
2. The firmware files will now be in the [firmware](firmware) directory.


## Reverse engineering notes

See [Notes.md](Notes.md).
