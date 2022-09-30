import gzip
from multiprocessing import Pool


def create_blocklist(size):
    message = f"Writing blocklist of size {size:_}..."
    print(message)
    with gzip.open(f"blocklist_{size}.txt.gz", "ab") as f:
        for i in range(size):
            f.write(f"{i}.sg\n".encode())
    print(message, "DONE")


if __name__ == "__main__":
    p = Pool(4)
    sizes = (1000_000, 10_000_000, 20_000_000, 30_000_000)
    p.map(create_blocklist, sizes)
