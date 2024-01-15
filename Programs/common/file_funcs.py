def write_line_to_file(line, file):
    f = open(file, "w")
    f.write(line)
    f.close()
