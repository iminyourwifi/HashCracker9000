#Imports
import re
import os
import sys
import hashlib
from optparse import OptionParser

def globalvars():
    globalvars.fName = os.path.basename(__file__)

def parse():
    try:
        usage = "Usage: " + globalvars.fName + " -m md5 -i md5.txt -o cracked_md5.txt -d rockyou.txt"
        parser = OptionParser(usage)
        parser.add_option("-m", "--mode", dest="hashtype",
                          help="Hash Type for cracking")
        parser.add_option("-i", "--input-file", dest="inputfile",
                          help="Input file containing the hashes.")
        parser.add_option("-o", "--output-file", dest="outputfile",
                          help="Where the cracked hashes shall be sent to.")
        parser.add_option("-d", "--dictionary", dest="dictionary",
                          help="Dictionary to compare on.")
        (option, args) = parser.parse_args()
        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(1)
        hashtype = option.hashtype
        inputfile = option.inputfile
        outputfile = option.outputfile
        dictionary = option.dictionary
        if not hashtype:
            print "We require a hash type."
        if not inputfile:
            print "We require a input file."
        if not outputfile:
            print "We require a output file."
        if not dictionary:
            print "We require a dictionary."

        if (hashtype > 0) and (inputfile > 0) and (outputfile > 0) and (dictionary > 0):
            #Checking Regex

            if hashtype.lower() == "md5":
                pattern = "(^[0-9a-fA-F]{32}$)"
                hasher = hashlib.md5()
            elif hashtype.lower() == "sha1":
                pattern = "(^[0-9a-fA-F]{40}$)"
                hasher = hashlib.sha1()
            else:
                print "Invalid Hash Type"

            valid_hash = 0
            invalid_hash = 0
            with open(inputfile) as f:
                for line in f:
                    if re.search(pattern, line):
                        valid_hash = valid_hash + 1
                    else:
                        invalid_hash = invalid_hash + 1

                if invalid_hash > 0:
                    print str(invalid_hash) + " invalid hashes found. Please check " + inputfile + " and run again!"
                    sys.exit(1)

            if os.path.isfile(inputfile + "_temp"):
                os.remove(inputfile + "_temp")

            file = open(outputfile, 'w')
            with open(dictionary) as f:
                for line in f:
                    hasher.update(line)
                    hash = hasher.hexdigest()
                    if hash in open(inputfile).read():
                        file.write(hash + ":" + line + "\n")
            file.close()
    except KeyboardInterrupt:
        print "Ctrl+C Detected. Closing"
        if os.path.isfile(inputfile + "_temp"):
            os.remove(inputfile + "_temp")
        sys.exit()

if __name__ == '__main__':
    globalvars()
    parse()
