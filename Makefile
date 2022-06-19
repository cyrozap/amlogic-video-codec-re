# SPDX-License-Identifier: 0BSD

# Copyright (C) 2021 by Forest Crossman <cyrozap@gmail.com>
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


FW_NAMES_2019_05_13 := g12a_h264 g12a_vp9 gxbb_h264 gxl_h263 gxl_h264 gxl_hevc gxl_hevc_mmu gxl_mjpeg gxl_mpeg12 gxl_mpeg4_5 gxm_h264
FW_COMMIT_2019_05_13 := e04cc56d0e6b6ff05924ff88fdba1a438ee7d3c8
FW_FILES_2019_05_13 := $(FW_NAMES_2019_05_13:%=firmware/%.2019-05-13.bin)

FW_NAMES_2020_02_03 := g12a_hevc_mmu g12a_vp9 gxl_h264 gxl_hevc gxl_hevc_mmu gxl_mjpeg gxl_mpeg12 gxl_vp9 gxm_h264 sm1_hevc_mmu sm1_vp9_mmu
FW_COMMIT_2020_02_03 := fb505a691b2a37b9d1fc20617433dfd52fb6e27e
FW_FILES_2020_02_03 := $(FW_NAMES_2020_02_03:%=firmware/%.2020-02-03.bin)

FIRMWARE := $(FW_FILES_2019_05_13) $(FW_FILES_2020_02_03)


firmware/%.2019-05-13.bin:
	curl -o $@ https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/meson/vdec/$(@:firmware/%.2019-05-13.bin=%.bin)?id=$(FW_COMMIT_2019_05_13)

firmware/%.2020-02-03.bin:
	curl -o $@ https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/meson/vdec/$(@:firmware/%.2020-02-03.bin=%.bin)?id=$(FW_COMMIT_2020_02_03)

download: $(FIRMWARE)

clean:
	rm -f $(FIRMWARE)


.PHONY: download clean
