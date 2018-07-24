from config import *
import os
from bs4 import BeautifulSoup

def main():
    
    delete_filelist = [file for file in os.listdir(OUTPUT_DIR) if file.endswith(".htm")]
    for file in delete_filelist:
        os.remove(os.path.join(OUTPUT_DIR, file))

    input_file_ptr = open(os.path.join(INPUT_DIR, "test1.htm"), "r+")
    output_file_ptr = open(os.path.join(OUTPUT_DIR, "test1.htm"), "w+")

    #print(input_file_ptr.readline())

    source_code_str = input_file_ptr.read()
    
    # Create HTML parser
    soup = BeautifulSoup(source_code_str, "html.parser")

    # Create a list of PDF documents in order
    for span_tag in soup.find_all("span"):
        #print("Span!")
        # Sanitize filename by removing directory names
        style_value = span_tag.get("style")

        # If PDF file is found, add it to list
        if "font-family: 'MS Mincho'" in style_value:

            target = span_tag.text

            # Exceptions
            if target[0] == "　" or target[0] == "(" or target[0] == "△" or \
               target[0] == "※" or target[0] == "－" or target[0] == "（":
                continue
            if target.isspace():
                continue
            if "," in target or "." in target:
                continue
            try:
                int(target)
                continue
            except:
                output_file_ptr.write(target + "\n")

    input_file_ptr.close()
    output_file_ptr.close()


if __name__ == "__main__":
    main()