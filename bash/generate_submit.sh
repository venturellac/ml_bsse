#!/bin/bash

for file in *.py; do
    filename=$(basename "$file")
    filename_without_extension="${filename%.py}"
    destination_file="${filename_without_extension}_submit"

    # Copy the template file
    cp run_dft_edit "$destination_file"

    # Line number where the first text should be added
    line_number=3
    file_to_add="${file}.out"

    # Line number where the second text should be added
    line_number_second=30
    chkfile_to_add="$file"

    # Use a different delimiter for sed to avoid issues with slashes in file paths
    sed -i "${line_number}s|\(.*\)|\1${file_to_add}|" "$destination_file"
    sed -i "${line_number_second}s|\(.*\)|\1${chkfile_to_add}|" "$destination_file"
done
