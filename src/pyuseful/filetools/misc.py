def escape_re(inp: str):
    char_list = [".", "(", ")", "{", "}", "[", "]", "?", "\\", "^", "$", "*", "+",
                "|", r"\A", r"\B", r"\b", r"\D", r"\d", r"\s", r"\S", r"\w", r"\Z"]
            
    for c in char_list:
        inp = inp.replace(c, fr"\{c}")
    return inp

def mod_name_with_ext(filename: str, mod: str):
    split_line = filename.split(".")
    ext = split_line[-1]
    base = ".".join(split_line[:-1])

    return f"{base}.{ext}"