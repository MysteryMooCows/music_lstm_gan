import itertools
import shutil
import os



def flatten_dir(dir):
    print("Flattening MusicData directory...")
    all_files = []
    dups = 0

    for root, _dirs, files in itertools.islice(os.walk(dir), 1, None):
        try:
            for filename in files:
                all_files.append(os.path.join(root, filename))
        except:
            dups += 1
    for filename in all_files:
        try:
            shutil.move(filename, dir)
        except:
            dups += 1

    print(f"{dups} duplicate files removed")

if __name__ == "__main__":
    flatten_dir("MIDIs")