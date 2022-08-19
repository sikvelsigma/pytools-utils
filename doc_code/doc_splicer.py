import sys
sys.path.insert(0, 'src/')

# splice@:splicer
from pyuseful.filetools.splicer import Splicer

splicer = Splicer()
#  find tag block in a file
splicer.parse_segments("./doc_code/splicer_source.md")
# make new file from with insert tags swapped with found block
splicer.splice_into("./doc_code/splicer_test.md", "./doc_code/splicer_test_res.md")
# can parse and splice multiple files, use 'parse_batch()' and 'splice_batch'
# /splice@:splicer