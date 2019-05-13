import subprocess
beg_str=b'Non-authoritative answer:\n'
beg_beg_str=b'.in-addr.arpa'
end_str=b'.in-addr.arpa\tname = '
end_end_str=b'\n\nAuthoritative answers can be found from'
for i in range(1,255):
    s = subprocess.Popen('nslookup ' + '10.185.195.' + str(i) , stdout=subprocess.PIPE, shell=True)
    (output, err) = s.communicate()
    # output = output.decode('utf-8')
    #print(output)
    if( output.find(b'No answer') ==-1):
        ipaddress = output[ output.find(beg_str) + len(beg_str) : output.find(beg_beg_str)]
        #print(ipaddress[::-1])
        #print(ipaddress)
        [a, b, c, d] = ipaddress.split(b'.')
        real_ipaddress=(d+b'.'+c+b'.'+b+b'.'+a)
        hostname = output[ output.find(end_str) + len(end_str) : output.find(end_end_str) -1]
        print((real_ipaddress + b' '+ hostname).decode('utf-8'))
        #print((real_ipaddress + b' '+ hostname))
