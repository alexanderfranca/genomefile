# -*- coding: utf-8 -*-

import pprint

# Import essential modules
from dbgetreader import * 
from genomefile.genomefile import *

# Load the reader and load the dbgetreader
dbget = DBGET(file_to_read='./tests/fixtures/genome')
dbgetr = DBGETReader(reader=dbget)

genome_file = GenomeFile(reader=dbgetr)

human = genome_file.genome_data_by_taxonomy_id( '9606' )

pprint.pprint(human)
