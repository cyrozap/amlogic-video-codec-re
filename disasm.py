#!/usr/bin/env python3

import argparse
import struct


def dis(instr : int):
    # Instructions are all 28 bits wide.
    assert (instr >> 28) == 0

    bits = "{:028b}".format(instr)

    return bits

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("firmware", type=str, help="The firmware binary.")
    args = parser.parse_args()

    fw = open(args.firmware, 'rb').read()

    for (instr,) in struct.iter_unpack('<I', fw):
        print("0x{:07x}: {}".format(instr, dis(instr)))


if __name__ == "__main__":
    main()
