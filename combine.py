# this will store the final content
CombineContent = []

## First content is from the Structure Molden file
StructContent = []
with open('anthr_core_again_struc.molden', 'rt') as StructFile:
    for line in StructFile:
        StructContent.append(line.rstrip('\n'))

## Second content is from the Frequencies Molden file
FreqContent = []
with open('anthr_core_again_freq.molden_normal_modes', 'rt') as FreqFile:
    for line in FreqFile:
        FreqContent.append(line.rstrip('\n'))
        
## Third content is from the IR results
# Add a spacer and a new heading
IRContent = ['\n[INT]']
# and read the IR data
with open ('anthr_core_again.out', 'rt') as IRFile:
    for line in IRFile:
        if 'IR activ [km/mol]' in line:
            IRContent = IRContent + line.split()[3:len(line.split())]
            
CombineContent = StructContent + FreqContent[1:len(FreqContent)-1] + IRContent

with open('combined.molden', 'w') as CombineFile:
    for item in CombineContent:
        CombineFile.write("%s\n" % item)
        
with open('combined.molden', 'w') as CombineFile:
    for item in CombineContent:
        CombineFile.write("%s\n" % item)
