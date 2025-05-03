import os


def write_count_ward(counter, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    out_path = os.path.join(output_folder, "results.tsv")
    with open(out_path, "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")
