import re
from pathlib import Path
from collections import defaultdict
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--include', nargs="*")
parser.add_argument('--exclude', nargs="*")

def create_regex(strings):
    if not strings:
        return None
    pattern = "|".join([inc for inc in strings])
    return re.compile(pattern)


def organize_files_by_type(root_dir=".", include=None, exclude=None):
    file_dict = defaultdict(list)

    root_path = Path(root_dir).resolve()

    include_list = None
    exclude_list = None

    if include is not None:
        include_list = [item.strip() for item in "".join(include).split(",")]
    if exclude is not None:
        exclude_list = [item.strip() for item in "".join(exclude).split(",")]

    include_regex = create_regex(include_list)
    exclude_regex = create_regex(exclude_list)

    for file_path in root_path.rglob('*'):
        if file_path.is_file():
            if include_regex is None or include_regex.search(str(file_path)):
                if exclude_regex is None or not exclude_regex.search(str(file_path)):
                    file_extension = file_path.suffix.lower()
                    file_dict[file_extension].append(str(file_path))
    
    for filetype, paths in file_dict.items():
        print()
        print(f"{filetype if filetype else 'No Extension'}:")
        for path in paths:
            print(f"code {path}")

    print()
    return file_dict

if __name__ == "__main__":
    args = parser.parse_args()
    organize_files_by_type(include=args.include, exclude=args.exclude)