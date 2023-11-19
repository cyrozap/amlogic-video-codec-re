# Reverse engineering notes


## AMRISC


### Observations

* Amlogic used to make dedicated video processors with the same name.
* Firmware binaries:
  * The upper 4 bits of every 4th (3rd, 0-indexed) byte in every binary are
    always zero, without exception.
  * Only one binary is ever loaded into the AMRISC, and that binary doesn't
    appear to contain any PC-relative constant data (like an ARM binary would).


### Inferences

* Custom ISA?
  * 28-bit little-endian instruction words.
    * Highest 6 bits are the opcode?
  * Constant data must be loaded using instruction immediates.
  * Separate code and data memories.
