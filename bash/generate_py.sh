#!/bin/bash

for file in *.vasp; do
    filename=$(basename "$file")  
    filename_without_extension="${filename%.vasp}"
    destination_file="$filename_without_extension.py"
    cp dft_base_small.py "$destination_file"
    line_number=9
    file_to_add="'$file')"
    line_number_second=29
    chkfile_to_add="'$filename_without_extension.chk'"
    sed -i "${line_number}s|.*|& ${file_to_add}|" "$destination_file"
    sed -i "${line_number_second}s|.*|& ${chkfile_to_add}|" "$destination_file"
done
