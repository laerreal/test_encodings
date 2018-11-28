from os.path import split, isdir, join, isfile
from os import listdir
from codecs import CodecInfo
from sys import version
from time import time
from collections import defaultdict

from encodings import __file__ as enc_file, search_function

print("Python version: " + version)

enc_dir = split(enc_file)[0]

print("Looking for codecs in %s" % enc_dir)

# According to `encodings.search_function`, a codec is a Python module.

possible_encs = []

for p in listdir(enc_dir):
    if p.endswith(".py"):
        possible_encs.append(p[:-3])
    elif isdir(p):
        init = join(p, "__init__.py")
        if isfile(init):
            possible_encs.append(p[:-3])

print("Possible encodings: " + ", ".join(possible_encs))

encs = []

for e in possible_encs:
    try:
        assert isinstance(search_function(e), CodecInfo)
    except:
        continue
    encs.append(e)

print("Encodings: " + ", ".join(encs))

# Now select encodings those can decode and encode all byte values [0; 255]
# identically.

test_bytes = b''.join(eval(c) for c in ("b'\\x%02x'" % i for i in range(256)))

universal_encs = []

for e in encs:
    try:
        assert test_bytes == test_bytes.decode(e).encode(e)
    except Exception as e:
        # print(e)
        continue
    universal_encs.append(e)

print("Universal encodings: " + ", ".join(universal_encs))

# Find out fastest codec

big_test = test_bytes * (1 << 15)

cell_width = max(len(e) for e in universal_encs + ["Encoder"])

print("Test data length %uB" % len(big_test))

table = defaultdict(lambda : defaultdict(lambda : "-"))
table[0].update(enumerate((
    "Codec", "Decoding time", "Encoding time", "Total"
)))

for row, e in enumerate(universal_encs, 1):
    print("measuring " + e)
    t0 = time()
    _str = big_test.decode(e)
    t1 = time()
    _str.encode(e)
    t2 = time()

    table[row].update(enumerate((e, t1 - t0, t2 - t1, t2 - t0)))

columns = max(len(row) for row in table.values())
# print(columns)

col_widhts = [0] * columns
for col in range(columns):
    for row in table.values():
        col_widhts[col] = max(col_widhts[col], len(str(row[col])))

row_fmt = " ; ".join("%%-%us" % w for w in col_widhts)

for _, row in [(0, table[0])] + sorted(list(table.items())[1:],
    key = lambda e : e[1][3] # sort by total time
):
    print((row_fmt % tuple(v for r, v in sorted(row.items()))).rstrip())
