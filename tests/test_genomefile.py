import sys
import os
import pprint
import unittest
from dbgetreader import *
from genomefile.genomefile import GenomeFile 
import re


class TestGenomeFile( unittest.TestCase):

    def setUp( self ):

        dbget = DBGET(file_to_read='./tests/fixtures/genome')
        reader = DBGETReader(reader=dbget)

        self.genome = GenomeFile(reader=reader)

    def test_load_genome_data( self ):

        self.genome.load_genome_data()

        self.assertEqual(len(self.genome.organism_entries), 3553)

    def test_all_internal_kegg_organism_ids( self ):

        all_internal_ids = self.genome.all_internal_kegg_organism_ids()

        self.assertTrue( len( all_internal_ids ) > 1 )
        self.assertTrue( type( all_internal_ids ) is dict )

        self.assertTrue( all_internal_ids['hsa'] == 'T01001')

    def test_organism_code_by_internal_kegg_id( self ):

        org = self.genome.organism_code_by_internal_kegg_id( 'T01001' )

        self.assertTrue( org == 'hsa' )


    def test_all_genome_data( self ):


        data = self.genome.all_genome_data()

        self.assertTrue( data['hsa']['complete_genome'] == True )
        self.assertTrue( data['hsa']['kegg_organism_id'] == 'T01001' )
        self.assertTrue( data['hsa']['organism_code'] == 'hsa' )
        self.assertTrue( data['hsa']['taxonomy_id'] == '9606' )


    def test_dictionary_keys( self ):

        data = self.genome.all_genome_data()

        for a_single_record,values in data.items():
            break

        expected_keys = [ 'complete_genome', 'kegg_definition_name', 'kegg_organism_id', 'organism_code', 'taxonomy_id' ]

        read_keys = values.keys() 

        if len(set(expected_keys) - set(read_keys)) > 0 or len(set(read_keys) - set(expected_keys)) > 0:
            keys_changed = True
        else:
            keys_changed = False

        self.assertFalse( keys_changed )


    def test_genome_dat_by_genome_code( self ):

        human = self.genome.genome_data_by_genome_code( 'hsa' )

        expected_keys = [ 'complete_genome', 'kegg_definition_name', 'kegg_organism_id', 'organism_code', 'taxonomy_id' ]

        read_keys = human.keys() 

        if len(set(expected_keys) - set(read_keys)) > 0 or len(set(read_keys) - set(expected_keys)) > 0:
            keys_changed = True
        else:
            keys_changed = False

        self.assertFalse( keys_changed )


    def test_genome_dat_by_taxonomy_id( self ):


        human = self.genome.genome_data_by_taxonomy_id( '9606' )
        
        # result is supposed to be a list.
        # In the case of 'hsa' is fact that there's only a single result.
        human = human[0]

        expected_keys = [ 'complete_genome', 'kegg_definition_name', 'kegg_organism_id', 'organism_code', 'taxonomy_id' ]

        read_keys = human.keys() 

        if len(set(expected_keys) - set(read_keys)) > 0 or len(set(read_keys) - set(expected_keys)) > 0:
            keys_changed = True
        else:
            keys_changed = False

        self.assertFalse( keys_changed )


    def test_all_organism_codes( self ):

        codes = self.genome.all_organism_codes()

        self.assertTrue( type( codes ) is list )
        self.assertTrue( 'hsa' in codes )


    def test_all_taxonomy_ids( self ):

        ids = self.genome.all_taxonomy_ids()

        self.assertTrue( type( ids ) is list )
        self.assertTrue( '9606' in ids )

    def test_taxonomy_id_by_organism_code( self ):

        data = self.genome.taxonomy_id_by_organism_code( 'hsa' )

        self.assertTrue( data == '9606' )


    def test_organism_code_by_taxonomy_id( self ):

        data = self.genome.organism_code_by_taxonomy_id( '9606' )

        # Because there's more then a single result for an specific taxonomy id, 
        # it's supposed that the result is a list.
        # In the case of 'Homo sapien' (case of this test - 9606), we know there's only a single result.
        data = data[0]

        self.assertTrue( data == 'hsa' )


if __name__ == "__main__":
    unittest.main()
