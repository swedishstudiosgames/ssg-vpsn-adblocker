import platform,string
ip="127.0.0.1 "
ip2="0.0.0.0 "
dvb="||"
s1=""
s2="^"
s3="^$important"
a1=""
b3=""
g6=""
generated_lines=set()
def generate_suffixes(domain):
    suffixes=[]
    if not domain.endswith(s2):
        suffixes.append(a1+s1)
        suffixes.append(a1+s2)
        suffixes.append(a1+s3)
        suffixes.append(b3+s1)
        suffixes.append(b3+s2)
        suffixes.append(b3+s3)
        suffixes.append(g6+s1)
        suffixes.append(g6+s2)
        suffixes.append(g6+s3)
    return suffixes
input_file="input.txt"
output_file="output.txt"
with open(input_file,"r")as f:
    for line in f:
        line=line.strip()
        if s2 in line or s3 in line or"^^"in line or"^$important^"in line:
            continue
        if line.startswith(ip):
            domain=line[len(ip):]
            a1=(ip+domain)
            suffixes=generate_suffixes(domain)
            for suffix in suffixes:
                if suffix not in generated_lines:
                    generated_lines.add(suffix)
        elif line.startswith(dvb):
            domain=line[len(dvb):]
            b3=(ip2+domain)
            g6=(dvb+domain)
            suffixes=generate_suffixes(domain)
            for suffix in suffixes:
                if suffix not in generated_lines:
                    generated_lines.add(suffix)
sorted_lines=sorted(generated_lines,ey=str.lower)
with open(output_file,"w")as f:
    f.write("\n".join(sorted_lines))
