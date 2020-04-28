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

## This also creates a very basic multiuse geometry.xyz file with just coordinates
# reopen and read geometry content
GeometryContent = []
line_after_trigger = -1
trigger_line = []
trigger_flag = False
start_record = False
stop_record = False
with open ('h2o.out', 'rt') as IRFile:
    for line in IRFile:
        if 'Final (previous) structure:' in line:
            trigger_flag = True
        if trigger_flag == True:
            line_after_trigger = line_after_trigger + 1
            if line_after_trigger == 2:
                start_record = True
            if start_record == True:
                if 'Saving final (previous) structure.' in line:
                    stop_record == True
                    break
                if stop_record == False:
                    GeometryContent.append(line.rstrip('\n'))
                    
## Write new Geomety file
with open('geometry.xyz', 'w') as GeometryFile:
    GeometryFile.write("%s\n\n" % len(GeometryContent))
    for item in GeometryContent:
        GeometryFile.write("%s\n" % item)
