from difflib import SequenceMatcher
import sys

domain_name = sys.argv[1]
fuz = SequenceMatcher(None, "google", domain_name) # Change "google" to a NB domain. Results above 90% and below 100% are suspect
print 'Fuzzy Ratio is %.2f%%' % (fuz.ratio()*100)

