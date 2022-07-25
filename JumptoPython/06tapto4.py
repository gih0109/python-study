# 탭을 4개의 공백으로 바꾸기

import sys

src = sys.argv[1]
dst = sys.argv[2]

with open(src, 'r') as f:
    contents = f.read()

space_contents = contents.replace('\t', " "*4)

with open(dst, 'w') as f:
    f.write(space_contents)
