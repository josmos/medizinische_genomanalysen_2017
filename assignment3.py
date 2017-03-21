#! /usr/bin/env python2

import vcf
import hgvs

__author__ = 'Josef Moser'


class Assignment3:
    def __init__(self):
        self.mother = vcf.Reader(filename="AmpliseqExome.20141120.NA24143.vcf",)
        self.father = vcf.Reader(filename="AmpliseqExome.20141120.NA24149.vcf")
        self.son = vcf.Reader(filename="AmpliseqExome.20141120.NA24385.vcf")
        #self.mother_rec = list([i for i in self.mother])
        #self.father_rec = list([i for i in self.father])
        #self.son_rec = list([i for i in self.son])

    def get_total_number_of_variants_mother(self):
        '''
        Return the total number of identified variants in the mother
        :return: 
        '''
        print "Total number of variants in mother: %d" % (len(self.mother_rec))

    def get_total_number_of_variants_father(self):
        '''
        Return the total number of identified variants in the father
        :return: 
        '''
        print "Total number of variants in father: %d" % (len(self.father_rec))
       
        
    def get_variants_shared_by_father_and_son(self):
        '''
        Return the number of identified variants shared by father and son
        :return: 
        '''
        shared = []
        for f in self.father:
            for s in self.son:
                if f.CHROM == s.CHROM and f.POS == s.POS and f.ALT == s.ALT and f.REF == s.REF:
                    shared.append(s)

        print len(shared)
        print shared[0]
        return shared

    def get_variants_shared_by_mother_and_son(self):
        '''
        Return the number of identified variants shared by mother and son
        :return: 
        '''
        shared = []
        for m in self.mother:
            for s in self.son:
                if m.CHROM == s.CHROM and m.POS == s.POS:# and m.ALT == s.ALT and m.REF == s.REF:
                    shared.append(s)

        print(len(shared))
        return shared

    def get_variants_shared_by_trio(self, mother_and_son, father_and_son):
        '''
        Return the number of identified variants shared by father, mother and son
        :return: 
        '''
        shared = []
        for m in mother_and_son:
            for f in father_and_son:
                if m.CHROM == f.CHROM: #and m.POS == f.POS and m.ALT == f.ALT and m.REF == f.REF:
                    shared.append(m)

        print(len(shared))
        return shared

    def merge_mother_father_son_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of the trio (merge VCFs)
        :return: 
        '''
        # write_vcf = vcf.Writer('trio_merged.vcf')
        # write_vcf.write_record(##give me the read##)
        # write_vcf.close()


        
    def convert_first_variants_of_son_into_HGVS(self):
        '''
        Convert the first 100 variants identified in the son into the corresponding transcript HGVS.
        Each variant should be mapped to all corresponding transcripts. Pointer:
        - https://hgvs.readthedocs.io/en/master/examples/manuscript-example.html#project-genomic-variant-to-a-new-transcript
        :return: 
        '''
        print("TODO")

    def print_summary(self):
        #self.get_total_number_of_variants_mother()
        #self.get_total_number_of_variants_father()
        #father_and_son = self.get_variants_shared_by_father_and_son()
        mother_and_son = self.get_variants_shared_by_mother_and_son()

        
if __name__ == '__main__':
    print("Assignment 3")
    assignment3 = Assignment3()
    assignment3.print_summary()
    
    

