# Import the required modules
import os
import urllib.request

# Define the input and output file names
iurl = "https://raw.githubusercontent.com/nickspaargaren/no-google/master/google-domains"
of1 = "ads.txt"
of2 = "noads.txt"

# Define the prefixes and suffixes for the output lines
pwa="||" # prefix with ads
pwo="@@||" # prefix without ads
s1="^" # suffix

# Define the keywords for advertising links
ak=["googleads","doubleclick","adsense"] # ads keywords

# Initialize two sets to store the lines with and without advertising links
ads=set()
noads=set()

# Open the input file from the given URL and loop through each line
with urllib.request.urlopen(iurl)as if1:
    for l1 in if1:
        # Decode the line from bytes to string and remove the newline character
        l1=l1.decode("utf-8").strip()
        # Check if the line contains any of the keywords for advertising links
        if any(k1 in l1 for k1 in ak):
            # Add the line to the set with advertising links, with the prefix and suffix
            ads.add(pwa+l1+s1)
        else:
            # Add the line to the set without advertising links, with the prefix and suffix
            noads.add(pwo+l1+s1)

# Sort the sets in alphabetical order and convert them to lists
ads=sorted(ads)
noads=sorted(noads)

# Write the sorted lines to the output files
with open(of1,"w")as of1:
    of1.write("\n".join(ads))
with open(of2,"w")as of1:
    of1.write("\n".join(noads))
