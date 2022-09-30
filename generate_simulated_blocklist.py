import lzma

for size in (1000_000, 10_000_000, 100_000_000):
    with lzma.open(f"blocklist_{size}.txt.xz", "ab") as f:
        for i in range(size):
            f.write(f"{i}.sg\n".encode())
