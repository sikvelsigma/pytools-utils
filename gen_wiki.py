import sys
sys.path.insert(0, 'src/')

from pyuseful.filetools.splicer import Splicer

import os

splicer = Splicer()


soruce_path = "./doc_code"
for dir, _, filenames in os.walk(soruce_path):
    source_files = [os.path.join(dir, f) for f in filenames if f.endswith(".py") and f.startswith("doc_")]
    break


doc_path = "./wiki_base"
doc_res_path = "./pytools-utils.wiki"
for dir, _, filenames in os.walk(doc_path):
    doc_files = [os.path.join(dir, f) for f in filenames if f.endswith(".md")]
    docres_files = [os.path.join(doc_res_path, f) for f in filenames if f.endswith(".md")]
    break

doc_path_tuple = [(s,r) for s, r in zip(doc_files, docres_files)]

splicer.parse_batch(source_files)
splicer.splice_batch(doc_path_tuple)
