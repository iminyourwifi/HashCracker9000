#Imports
import os
import hashlib
from optparse import OptionParser

#Hash Types
md5 = hashlib.md5()

def globalvars():
    globalvars.fName = os.path.basename(__file__)

def parse():
    usage = "Usage: " + globalvars.fName + " -H md5 -i md5.txt -o cracked_md5.txt -d rockyou.txt"
    parser = OptionParser(usage)
    parser.add_option("-H", "--hash-type", dest="hashtype",
                      help="Hash Type for cracking")
    parser.add_option("-i", "--input-file", dest="inputfile",
                      help="Input file containing the hashes.")
    parser.add_option("-o", "--output-file", dest="outputfile",
                      help="Where the cracked hashes shall be sent to.")
    parser.add_option("-d", "--dictionary", dest="dictionary",
                      help="Dictionary to compare on.")
    parser.add_option("-t", "--threads", dest="threads",
                      help="Ammount of threads to use for comparing.", default=4)
    (option, args) = parser.parse_args()
    if not option.hashtype:
        print "We require a hash type."
    if not option.inputfile:
        print "We require a input file."
    if not option.outputfile:
        print "We require a output file."
    if not option.dictionary:
        print "We require a dictionary."

if __name__ == '__main__':
    globalvars()
    parse()
