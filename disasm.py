#!/usr/bin/env python3
# SPDX-License-Identifier: 0BSD

# Copyright (C) 2021, 2023 by Forest Crossman <cyrozap@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for
# any purpose with or without fee is hereby granted.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
# PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.


import argparse
import struct


def dis(instr : int, index : int = 0):
    # Instructions are all 28 bits wide.
    assert (instr >> 28) == 0

    bits = "{:028b}".format(instr)
    op2724 = (instr >> 24) & 0xf
    op2723 = (instr >> 23) & 0x1f
    op2722 = (instr >> 22) & 0x3f

    #disassembled = ' '.join((bits[:5], bits[5:9], bits[9:]))
    disassembled = ' '.join((bits[:6], bits[6:9], bits[9:22], bits[22:]))
    if instr == 0:
        disassembled += "  nop?"
    elif op2723 == 0xc << 1:
        jump_target = (instr >> 6) & 0x1fff
        if jump_target & 0x1000:
            jump_target ^= 0x1fff
            jump_target += 1
            jump_target *= -1
        disassembled += "  relative branch/call/jump to {:+} ({})".format(jump_target, index + jump_target)

    return "0x{:07x}: {}".format(instr, disassembled)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--line-number", action="store_true", help="Print line numbers.")
    parser.add_argument("firmware", type=str, help="The firmware binary.")
    args = parser.parse_args()

    fw = open(args.firmware, 'rb').read()

    for i, (instr,) in enumerate(struct.iter_unpack('<I', fw)):
        dis_str = dis(instr, i)
        if args.line_number:
            dis_str = "{:>5d}: ".format(i) + dis_str
        print(dis_str)


if __name__ == "__main__":
    main()
