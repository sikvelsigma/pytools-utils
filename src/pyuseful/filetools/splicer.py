
from typing import List, Tuple
from collections import defaultdict
import re
from pprint import pprint

class Splicer:

    def __init__(self, parse_prefix="splice@:", splice_prefix="insert@:") -> None:
        self._parse_prefix = parse_prefix
        self._end_parse_prefix = f"/{self._parse_prefix}"
        self._splice_prefix = splice_prefix 
        self._segments = {}

    def parse_batch(self, files: List[str], encoding="utf-8"):
        for f in files:
            self.parse_segments(f, encoding=encoding)

    def splice_batch(self, files: List[Tuple[str, str]], encoding="utf-8"):
        for (f_in, f_out) in files:
            self.splice_into(f_in, f_out, encoding=encoding)

    def parse_segments(self, filename, encoding="utf-8"):
        new_segments = defaultdict(list)
        current_segments = set()
        with open(filename, "r", encoding=encoding) as f:
            for line in f:
                if self._parse_prefix in line and self._end_parse_prefix not in line:  
                    re_seg = rf"(?<={self._parse_prefix})(.*)"
                    new_seg = re.findall(re_seg, line)[0]  
                    if new_seg in current_segments:
                        raise RuntimeError(f"'{type(self).__name__}': key '{new_seg}' appeared twice")
                    current_segments.add(new_seg)
                    continue
                if self._end_parse_prefix in line:
                    re_seg = rf"(?<={self._end_parse_prefix})(.*)"
                    end_seg = re.findall(re_seg, line)[0]
                    if end_seg not in current_segments:
                        raise RuntimeError(f"'{type(self).__name__}': cannot close never started segment '{end_seg}'")
                    current_segments.remove(end_seg)
                    continue

                for key in current_segments:
                    new_segments[key].append(line)
            if len(current_segments) != 0:
                raise RuntimeError(f"'{type(self).__name__}': segments were never closed {current_segments}")

        self._segments = self._segments | new_segments
        
    def splice_into(self, filename: str, out_filename: str, encoding="utf-8"):
        result_text = []
        with open(filename, "r", encoding=encoding) as f:
            for line in f:
                if self._splice_prefix in line:
                    re_seg = rf"(?<={self._splice_prefix})(.*)"
                    seg_name = re.findall(re_seg, line)[0]
                    if seg_name not in self._segments:
                        raise KeyError(f"'{type(self).__name__}': no '{seg_name}' found")
                    result_text += self._segments[seg_name]
                    continue
                result_text.append(line)
                
        with open(out_filename, "w", encoding=encoding) as f:
            f.writelines(result_text)

    def clear_segments(self):
        self._segments = {}

    @staticmethod
    def escape_re(inp: str):
        char_list = [".", "(", ")", "{", "}", "[", "]", "?", "\\", "^", "$", "*", "+",
                    "|", r"\A", r"\B", r"\b", r"\D", r"\d", r"\s", r"\S", r"\w", r"\Z"]
                
        for c in char_list:
            inp = inp.replace(c, fr"\{c}")
        return inp