#!/usr/bin/env python3

bf = 'build/build.ninja'
out = []

with open(bf,'r') as rf:
    lines = rf.readlines()
    for line in lines:
        if 'LINK_LIBRARIES' in line and \
           '/opt/rocm/lib/libamdhip64.so' in line and \
           '/opt/rocm/lib/libamdhip64.so.' not in line and \
           '/opt/rocm/lib/libhsa-runtime64.so' not in line:
               line = line.replace('/opt/rocm/lib/libamdhip64.so', 
                                   '/opt/rocm/lib/libamdhip64.so /opt/rocm/lib/libhsa-runtime64.so')

        if 'LINK_LIBRARIES' in line and \
           'lib/libc10.so' in line and \
           '/opt/rocm/lib/libhsa-runtime64.so' not in line:
               line = line.replace('lib/libc10.so', 
                                   'lib/libc10.so /opt/rocm/lib/libhsa-runtime64.so')

        out.append(line)

with open(bf,'w') as wf:
    wf.write(''.join(out))
    
