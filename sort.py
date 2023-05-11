import platform,string
ip="127.0.0.1 "
ip2="0.0.0.0 "
dvb="||"
s1=""
s2="^"
s3="^$important"
input_file="input.txt"
output_file="output.txt"
generated_lines=set()
def generate_suffixes(domain):
    suffixes=[]
    if not domain.endswith(s2):
        suffixes.append(ip+domain+s1)
        suffixes.append(ip+domain+s2)
        suffixes.append(ip+domain+s3)
        suffixes.append(ip2+domain+s1)
        suffixes.append(ip2+domain+s2)
        suffixes.append(ip2+domain+s3)
        suffixes.append(dvb+domain+s1)
        suffixes.append(dvb+domain+s2)
        suffixes.append(dvb+domain+s3)
    return suffixes
with open(input_file,"r")as f:
    for line in f:
        line=line.strip()
        if s2 in line or s3 in line or"^^"in line or"^$importent^"in line:
            continue
        if line.startswith(ip):
            domain=line[len(ip):]
            suffixes=generate_suffixes(domain)
            for suffix in suffixes:
                if suffix not in generated_lines:
                    generated_lines.add(suffix)
        elif line.startswith(dvb):
            domain=line[len(dvb):]
            suffixes=generate_suffixes(domain)
            for suffix in suffixes:
                if suffix not in generated_lines:
                    generated_lines.add(suffix)
sorted_lines=sorted(generated_lines,key=str.lower)
with open(output_file,"w")as f:
    f.write("\n".join(sorted_lines))
