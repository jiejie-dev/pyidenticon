# Copied and translated from https://github.com/issue9/identicon/blob/master/block.go
# This project is under MIT License.

from PIL import ImageDraw

# 4个元素分别表示 cos(0),cos(90),cos(180),cos(270)
cos = [1, 0, -1, 0]

# 4个元素分别表示 sin(0),sin(90),sin(180),sin(270)
sin = [0, 1, 0, -1]


def rotate(points, x, y, angle):
    if 0 > angle > 3:
        raise Exception("rotate:参数angle必须0,1,2,3三值之一")
    for index, item in enumerate(points):
        i, j = item[0], item[1]
        px = i - x
        py = j - y
        new_x = px * cos[angle] - py * sin[angle] + x
        new_y = px * sin[angle] + py * cos[angle] + y
        points[index] = (new_x, new_y)
    return points


def draw_block(img: ImageDraw, points, x, y, block_size, color, angle):
    if angle > 0:
        # 0 角度不需要转换
        # 中心坐标与 x、y 的距离，方便下面指定中心坐标(x+m, y+m)，
        # 0.5 的偏移值不能少，否则坐标靠右，非正中央
        m = block_size / 2 - 0.5
        points = rotate(points, x + m, y + m, angle)

    img.polygon(points, fill=color)


# 全空白
#
#  --------
#  |      |
#  |      |
#  |      |
#  --------
def b0(img, x, y, size, color, angle):
    pass


# 全填充正方形
#
#  --------
#  |######|
#  |######|
#  |######|
#  --------
def b1(img: ImageDraw, x, y, size, color, angle):
    draw_block(img, [(x, y),
                     (x + size, y),
                     (x + size, y + size),
                     (x, y + size)], x, y, size, color, angle)


# 中间小方块
#  ----------
#  |        |
#  |  ####  |
#  |  ####  |
#  |        |
#  ----------
def b2(img, x, y, size, color, angle):
    l = size / 4
    x = x + l
    y = y + l
    draw_block(img, [(x, y),
                     (x + l * 2, y),
                     (x, y + l * 2),
                     (x + l * 2, y + l * 2)], x, y, size, color, angle)


# 菱形
#
#  ---------
#  |   #   |
#  |  ###  |
#  | ##### |
#  |#######|
#  | ##### |
#  |  ###  |
#  |   #   |
#  ---------
def b3(img, x, y, size, color, angle):
    m = size / 2

    draw_block(img, [(x + m, y),
                     (x + size, y + m),
                     (x + m, y + size),
                     (x, y + m),
                     (x + m, y)], x, y, size, color, angle)


# b4
#
#  -------
#  |#####|
#  |#### |
#  |###  |
#  |##   |
#  |#    |
#  |------
def b4(img, x, y, size, color, angle):
    draw_block(img, [
        (x, y),
        (x + size, y),
        (x, y + size),
        (x, y)], x, y, size, color, angle)


# b5
#
#  ---------
#  |   #   |
#  |  ###  |
#  | ##### |
#  |#######|
def b5(img, x, y, size, color, angle):
    m = size / 2
    draw_block(img, [(x + m, y),
                     (x + size, y + size),
                     (x, y + size),
                     (x + m, y)], x, y, size, color, angle)


# b6 矩形
#
#  --------
#  |###   |
#  |###   |
#  |###   |
#  --------
def b6(img, x, y, size, color, angle):
    m = size / 2
    draw_block(img, [
        (x, y),
        (x + m, y),
        (x + m, y + size),
        (x, y + size),
        (x, y)], x, y, size, color, angle)


# b7 斜放的锥形
#
#  ---------
#  | #     |
#  |  ##   |
#  |  #####|
#  |   ####|
#  |--------
def b7(img, x, y, size, color, angle):
    m = size / 2
    draw_block(img, [
        (x, y),
        (x + size, y + m),
        (x + size, y + size),
        (x + m, y + size),
        (x, y)], x, y, size, color, angle)


# b8 三个堆叠的三角形
#
#  -----------
#  |    #    |
#  |   ###   |
#  |  #####  |
#  |  #   #  |
#  | ### ### |
#  |#########|
#  -----------
def b8(img, x, y, size, color, angle):
    m = size / 2
    mm = m / 2

    # 顶部三角形
    draw_block(img, [
        (x + m, y),
        (x + 3 * mm, y + m),
        (x + mm, y + m),
        (x + m, y)],
               x, y, size, color, angle
               )

    # 底下左边
    draw_block(img, [
        (x + mm, y + m),
        (x + m, y + size),
        (x, y + size),
        (x + mm, y + m)],
               x, y, size, color, angle
               )

    # 底下右边
    draw_block(img, [
        (x + 3 * mm, y + m),
        (x + size, y + size),
        (x + m, y + size),
        (x + 3 * mm, y + m)],
               x, y, size, color, angle
               )


# b9 斜靠的三角形
#
#  ---------
#  |#      |
#  | ####  |
#  |  #####|
#  |  #### |
#  |   #   |
#  ---------
def b9(img, x, y, size, color, angle):
    m = size / 2
    draw_block(img, [
        (x, y),
        (x + size, y + m),
        (x + m, y + size),
        (x, y)],
               x, y, size, color, angle
               )


# b10
#
#  ----------
#  |    ####|
#  |    ### |
#  |    ##  |
#  |    #   |
#  |####    |
#  |###     |
#  |##      |
#  |#       |
#  ----------
def b10(img, x, y, size, color, angle):
    m = size / 2
    draw_block(img, [
        (x + m, y),
        (x + size, y),
        (x + m, y + m),
        (x + m, y)],
               x, y, size, color, angle
               )

    draw_block(img, [
        (x, y + m),
        (x + m, y + m),
        (x, y + size),
        (x, y + m)],
               x, y, size, color, angle
               )


# b11 左上角1/4大小的方块
#
#  ----------
#  |####    |
#  |####    |
#  |####    |
#  |        |
#  |        |
#  ----------
def b11(img, x, y, size, color, angle):
    m = size / 2
    draw_block(img, [
        (x, y),
        (x + m, y),
        (x + m, y + m),
        (x, y + m),
        (x, y)],
               x, y, size, color, angle
               )


# b12
#
#  -----------
#  |         |
#  |         |
#  |#########|
#  |  #####  |
#  |    #    |
#  -----------
def b12(img, x, y, size, color, angle):
    m = size / 2
    draw_block(img, [
        (x, y + m),
        (x + size, y + m),
        (x + m, y + size),
        (x, y + m)],
               x, y, size, color, angle
               )


# b13
#
#  -----------
#  |         |
#  |         |
#  |    #    |
#  |  #####  |
#  |#########|
#  -----------
def b13(img, x, y, size, color, angle):
    m = size / 2
    draw_block(img, [
        (x + m, y + m),
        (x + size, y + size),
        (x, y + size),
        (x + m, y + m)],
               x, y, size, color, angle
               )


# b14
#
#  ---------
#  |   #   |
#  | ###   |
#  |####   |
#  |       |
#  |       |
#  ---------
def b14(img, x, y, size, color, angle):
    m = size / 2
    draw_block(img, [
        (x + m, y),
        (x + m, y + m),
        (x, y + m),
        (x + m, y)],
               x, y, size, color, angle
               )


# b15
#
#  ----------
#  |#####   |
#  |###     |
#  |#       |
#  |        |
#  |        |
#  ----------
def b15(img, x, y, size, color, angle):
    m = size / 2
    draw_block(img, [
        (x, y),
        (x + m, y),
        (x, y + m),
        (x, y)],
               x, y, size, color, angle
               )


# b16
#
#  ---------
#  |   #   |
#  | ##### |
#  |#######|
#  |   #   |
#  | ##### |
#  |#######|
#  ---------
def b16(img, x, y, size, color, angle):
    m = size / 2
    draw_block(img, [
        (x + m, y),
        (x + size, y + m),
        (x, y + m),
        (x + m, y)],
               x, y, size, color, angle
               )

    draw_block(img, [
        (x + m, y + m),
        (x + size, y + size),
        (x, y + size),
        (x + m, y + m)],
               x, y, size, color, angle
               )


# 可以出现在中间的方块，一般为了美观，都是对称图像。
centerBlocks = [b0, b1, b2, b3]

# 所有方块
blocks = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16]
