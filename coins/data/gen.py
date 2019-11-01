import random
import math

from PIL import Image

PATH = "../problem_statement/%s.png"
DIAM = 75

def whiteify(img):
    width, height = img.size
    pixdata = img.load()
    for y in range(height):
        for x in range(width):
            p = list(pixdata[x, y])
            if p[3] != 255:
                pixdata[x, y] = (255, 255, 255, 255)

def dist(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx*dx + dy*dy)

def ok(poses, overlap):
    for i in range(len(poses)):
        superduperclose = 0
        superclose = 0
        overlapping = 0
        for j in range(len(poses)):
            if i == j:
                continue
            d = dist(poses[i], poses[j])
            if d < DIAM / 20: superduperclose += 1
            if d < DIAM / 2.1: superclose += 1
            if d < DIAM: overlapping += 1
        if superclose > 0: return False
        if superclose > 1: return False
        if overlapping > 3: return False
        if not overlap and overlapping: return False
    return True


def tc(coins, overlap, rotate):
    ims = [(Image.open(PATH % str(c)), c) for c in coins]
    for img, _ in ims:
        img.thumbnail((DIAM, DIAM), Image.ANTIALIAS)
    im = Image.new(mode = "RGBA", size = (1000, 1000), color=(255,255,255,255))
    
    poses = []
    mx = (200 if overlap else 100) + random.randint(-10, 10)
    while len(poses) < mx:
        pos = (random.randint(0, 1000), random.randint(0, 1000))
        poses.append(pos)
        if not ok(poses, overlap):
            poses.pop()

    ans = 0
    for center in poses:
        w, c = random.choice(ims)
        if rotate:
            w = w.rotate(random.randint(0, 359))
        im.paste(w, (center[0] - DIAM // 2, center[1] - DIAM // 2), w)
        ans += c
    return im, ans

def writecase(group, name, case):
    inp, ans = case
    inp = inp.convert("RGB")
    inp.save("secret/%s/%s.in" % (group, name), "JPEG")
    with open("secret/%s/%s.ans" % (group, name), "wb") as f:
        f.write(str(ans).encode('ASCII'))

# g1
for i in range(3):
    writecase("g1", i, tc([1], False, False))
# g2
for i in range(3):
    writecase("g2", i, tc([1], False, True))
# g3
for i in range(3):
    writecase("g3", i, tc([1], True, True))
# g4
for i in range(3):
    writecase("g4", i, tc([1, 5, 10], False, False))
# g5
for i in range(3):
    writecase("g5", i, tc([1, 5, 10], False, True))
# g6
for i in range(3):
    writecase("g6", i, tc([1, 5, 10], True, True))

writecase("sample", "group-1", tc([1], False, False))
writecase("sample", "group-2", tc([1], False, True))
writecase("sample", "group-3", tc([1], True, True))
writecase("sample", "group-4", tc([1, 5, 10], False, False))
writecase("sample", "group-5", tc([1, 5, 10], False, True))
writecase("sample", "group-6", tc([1, 5, 10], True, True))
