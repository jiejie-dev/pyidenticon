import hashlib

import os
from PIL import Image, ImageDraw
from pyidenticon.blocks import blocks, centerBlocks


def md5(data):
    m = hashlib.md5()
    m.update(data.encode(encoding='utf-8'))
    return m.digest()


def make(data, size=128, fore_color='grey', bg_color='white'):
    id = md5(data)

    block_size = int(size / 3)
    im = Image.new('RGBA', (size, size), bg_color)
    draw = ImageDraw.ImageDraw(im)

    b1_index = (id[0] + id[1] + id[2] + id[3]) % len(blocks)

    b1 = blocks[b1_index]

    b2_index = (id[4] + id[5] + id[6] + id[7]) % len(blocks)
    b2 = blocks[b2_index]

    c_index = (id[8] + id[9] + id[10] + id[11]) % len(centerBlocks)
    c = centerBlocks[c_index]

    angle = (id[12] + id[13] + id[14] + id[15]) % 4

    def incr_angle(angle):
        # 增加angle的值，但不会大于3
        angle += 1
        if angle > 3:
            angle = 0
        return angle

    c(draw, block_size, block_size, block_size, fore_color, 0)

    b1(draw, 0, 0, block_size, fore_color, angle)
    b2(draw, block_size, 0, block_size, fore_color, angle)

    angle = incr_angle(angle)
    b1(draw, block_size * 2, 0, block_size, fore_color, angle)
    b2(draw, block_size * 2, block_size, block_size, fore_color, angle)

    angle = incr_angle(angle)
    b1(draw, block_size * 2, block_size * 2, block_size, fore_color, angle)
    b2(draw, block_size, block_size * 2, block_size, fore_color, angle)

    angle = incr_angle(angle)
    b1(draw, 0, block_size * 2, block_size, fore_color, angle)
    b2(draw, 0, block_size, block_size, fore_color, angle)

    return im


if __name__ == '__main__':
    if not os.path.exists('.data'):
        os.mkdir('.data')
    items = ['卢杰杰', '李大鹏', '蒋凯', "192.168.1.1"]
    for item in items:
        img = make(item, 256, (0, 255, 0))
        img.save('.data/{}.png'.format(item))
