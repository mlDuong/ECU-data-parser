# -*- coding: utf-8 -*-
import tkinter as tk
import string 
import datetime
from tkinter import filedialog
  
def convert_dat_to_hex(filepath):
    with open(filepath, 'rb') as f:
        content = f.readlines()
    hex_content = []
    for line in content:
        hex_line = line.encode('hex').upper()
        hex_content.append(hex_line)
    return '\n'.join(hex_content)
    
def browse_file():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

def browse_output_location():
    output_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="Output.txt")
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, output_path)
    
def convert_file():
    filepath = file_path_entry.get()
    try:
        with open(filepath, 'rb') as f:

            hex_content = convert_dat_to_hex(filepath)
            
            # Read the entire file into memory and concatenate all lines into one continuous hex string
            hex_string = ''.join(line.strip() for line in hex_content)

            # Splitting the hex string into pairs of bytes
            byte_pairs = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
            print(byte_pairs)
            # Initialize counter and increment it by the number of pairs
            
            total_pairs = len(byte_pairs)
            # Clear the text box
            output_text.delete(1.0, tk.END)

            # Write the output to the text box
            output_text.insert(tk.END, hex_content)
            
            # Extracting the fields from the byte pairs
            vin = ''.join(byte_pairs[0:17])
            odometer = ''.join(byte_pairs[17:20])
            latitude = ''.join(byte_pairs[20:24])
            longitude = ''.join(byte_pairs[24:28])
            timestamp = ''.join(byte_pairs[28:36])
                       
            # <-- Start HPCM Module Information --> 
            HPCM = ''.join(byte_pairs[36:37])
            HPCM_ROM_ID_Length = ''.join(byte_pairs[37:38])
                     
            # Based on the ROMID Length. Read ROMID 
            # Convert ROMID Length hex value to decimal values
            HPCMRomIDLengthInDecimal = int(HPCM_ROM_ID_Length, 16)
            if HPCMRomIDLengthInDecimal == 0:
                HPCM_ROM_ID = ' '.join(byte_pairs[38:70])
                HPCM_SID_HEX = ' '.join(byte_pairs[70:71])
                HPCM_SID_DEC = int(HPCM_SID_HEX,16)
                 ################## DMCM ########################
                DMCM = ''.join(byte_pairs[71:72])
                DMCM_ROM_ID_Length = ''.join(byte_pairs[72:73])
                                    
                # Based on the ROMID Length. Read ROMID 
                # Convert ROMID Length hex value to decimal values
                DMCMRomIDLengthInDecimal = int(DMCM_ROM_ID_Length, 16)
                DMCM_ROM_ID = ' '.join(byte_pairs[73:74])
                DMCM_SID_HEX = ' '.join(byte_pairs[74:75])
                DMCM_SID_DEC = int(DMCM_SID_HEX,16)
                tempIncre = 75
                
                # BCU Module Information 
                BCU = ''.join(byte_pairs[tempIncre:tempIncre + 1])
                BCU_ROM_ID_Length = ''.join(byte_pairs[tempIncre + 1:tempIncre + 2])
                        
                # Based on the ROMID Length. Read ROMID 
                # Convert ROMID Length hex value to decimal values
                BCURomIDLengthInDecimal = int(BCU_ROM_ID_Length, 16)
                if BCURomIDLengthInDecimal == 0: #0xFF
                    print("Hello")
                    BCU_ROM_ID = ' '.join(byte_pairs[tempIncre + 2:tempIncre + 34])
                    BCU_SID_HEX = ' '.join(byte_pairs[tempIncre + 34:tempIncre + 35])
                    BCU_SID_DEC = int(HPCM_SID_HEX,16)
                    # <-- End HPCM Module Information --> 
                    
                    ################## BCCM ########################
                    BCCM = ''.join(byte_pairs[tempIncre + 35:tempIncre + 36])
                    BCCM_ROM_ID_Length = ''.join(byte_pairs[tempIncre + 36:tempIncre + 37])                          
                    # Based on the ROMID Length. Read ROMID 
                    # Convert ROMID Length hex value to decimal values
                    BCCMRomIDLengthInDecimal = int(BCCM_ROM_ID_Length, 16)
                    BCCM_ROM_ID = ' '.join(byte_pairs[tempIncre + 37:tempIncre + 38])
                    BCCM_SID_HEX = ' '.join(byte_pairs[tempIncre + 38:tempIncre + 39])
                    BCCM_SID_DEC = int(BCCM_SID_HEX,16)
                    tempIncre = tempIncre + 39
                else: 
                    BCU_ROM_ID = ' '.join(byte_pairs[tempIncre + 2:tempIncre + 2 + BCURomIDLengthInDecimal])
                    BCU_SID_HEX = ' '.join(byte_pairs[tempIncre + 2 + BCURomIDLengthInDecimal:tempIncre + 3 + BCURomIDLengthInDecimal])
                    BCU_SID_DEC = int(HPCM_SID_HEX,16)
                    # <-- End HPCM Module Information --> 
                    
                    ################## BCCM ########################
                    BCCM = ''.join(byte_pairs[tempIncre + 3 + BCURomIDLengthInDecimal:tempIncre + 4 + BCURomIDLengthInDecimal])
                    BCCM_ROM_ID_Length = ''.join(byte_pairs[tempIncre + 4 + BCURomIDLengthInDecimal:tempIncre + 5 + BCURomIDLengthInDecimal])                          
                    # Based on the ROMID Length. Read ROMID 
                    # Convert ROMID Length hex value to decimal values
                    BCCMRomIDLengthInDecimal = int(BCCM_ROM_ID_Length, 16)
                    BCCM_ROM_ID = ' '.join(byte_pairs[tempIncre + 5 + BCURomIDLengthInDecimal:tempIncre + 6 + BCURomIDLengthInDecimal])
                    BCCM_SID_HEX = ' '.join(byte_pairs[tempIncre + 6 + BCURomIDLengthInDecimal:tempIncre + 7 + BCURomIDLengthInDecimal])
                    BCCM_SID_DEC = int(BCCM_SID_HEX,16)
                    tempIncre = tempIncre + 7 + BCURomIDLengthInDecimal
            else: 
                HPCM_ROM_ID = ' '.join(byte_pairs[38:38 + HPCMRomIDLengthInDecimal])
                HPCM_SID_HEX = ' '.join(byte_pairs[38 + HPCMRomIDLengthInDecimal:39 + HPCMRomIDLengthInDecimal])
                HPCM_SID_DEC = int(HPCM_SID_HEX,16)
                
                ################## DMCM ########################
                DMCM = ''.join(byte_pairs[39 + HPCMRomIDLengthInDecimal:40 + HPCMRomIDLengthInDecimal])
                DMCM_ROM_ID_Length = ''.join(byte_pairs[40 + HPCMRomIDLengthInDecimal:41 + HPCMRomIDLengthInDecimal])
                                    
                # Based on the ROMID Length. Read ROMID 
                # Convert ROMID Length hex value to decimal values
                DMCMRomIDLengthInDecimal = int(DMCM_ROM_ID_Length, 16)
                DMCM_ROM_ID = ' '.join(byte_pairs[41 + HPCMRomIDLengthInDecimal:42 + HPCMRomIDLengthInDecimal])
                DMCM_SID_HEX = ' '.join(byte_pairs[42 + HPCMRomIDLengthInDecimal:43 + HPCMRomIDLengthInDecimal])
                DMCM_SID_DEC = int(DMCM_SID_HEX,16)
                tempIncre = 43 + HPCMRomIDLengthInDecimal
                
                # BCU Module Information 
                BCU = ''.join(byte_pairs[tempIncre:tempIncre + 1])
                BCU_ROM_ID_Length = ''.join(byte_pairs[tempIncre + 1:tempIncre + 2])
                        
                # Based on the ROMID Length. Read ROMID 
                # Convert ROMID Length hex value to decimal values
                BCURomIDLengthInDecimal = int(BCU_ROM_ID_Length, 16)
                if BCURomIDLengthInDecimal ==0: 
                    BCU_ROM_ID = ' '.join(byte_pairs[tempIncre + 2:tempIncre + 34])
                    BCU_SID_HEX = ' '.join(byte_pairs[tempIncre + 34:tempIncre + 35])
                    BCU_SID_DEC = int(HPCM_SID_HEX,16)
                
                    ################## BCCM ########################
                    BCCM = ''.join(byte_pairs[tempIncre + 35:tempIncre + 36])
                    BCCM_ROM_ID_Length = ''.join(byte_pairs[tempIncre + 36:tempIncre + 37])                          
                    # Based on the ROMID Length. Read ROMID 
                    # Convert ROMID Length hex value to decimal values
                    BCCMRomIDLengthInDecimal = int(BCCM_ROM_ID_Length, 16)
                    BCCM_ROM_ID = ' '.join(byte_pairs[tempIncre + 37:tempIncre + 38])
                    BCCM_SID_HEX = ' '.join(byte_pairs[tempIncre + 38:tempIncre + 39])
                    BCCM_SID_DEC = int(BCCM_SID_HEX,16)
                    tempIncre = tempIncre + 39
                else: 
                    BCU_ROM_ID = ' '.join(byte_pairs[tempIncre + 2:tempIncre + 2 + BCURomIDLengthInDecimal])
                    BCU_SID_HEX = ' '.join(byte_pairs[tempIncre + 2 + BCURomIDLengthInDecimal:tempIncre + 3 + BCURomIDLengthInDecimal])
                    BCU_SID_DEC = int(HPCM_SID_HEX,16)
                    # <-- End HPCM Module Information --> 
                    
                    ################## BCCM ########################
                    BCCM = ''.join(byte_pairs[tempIncre + 3 + BCURomIDLengthInDecimal:tempIncre + 4 + BCURomIDLengthInDecimal])
                    BCCM_ROM_ID_Length = ''.join(byte_pairs[tempIncre + 4 + BCURomIDLengthInDecimal:tempIncre + 5 + BCURomIDLengthInDecimal])                          
                    # Based on the ROMID Length. Read ROMID 
                    # Convert ROMID Length hex value to decimal values
                    BCCMRomIDLengthInDecimal = int(BCCM_ROM_ID_Length, 16)
                    BCCM_ROM_ID = ' '.join(byte_pairs[tempIncre + 5 + BCURomIDLengthInDecimal:tempIncre + 6 + BCURomIDLengthInDecimal])
                    BCCM_SID_HEX = ' '.join(byte_pairs[tempIncre + 6 + BCURomIDLengthInDecimal:tempIncre + 7 + BCURomIDLengthInDecimal])
                    BCCM_SID_DEC = int(BCCM_SID_HEX,16)
                    tempIncre = tempIncre + 7 + BCURomIDLengthInDecimal
            
            print(vin)
            print(odometer)
            print(latitude)
            print(longitude)
            print(timestamp)
            
            print(HPCM)
            print(HPCMRomIDLengthInDecimal)
            print(HPCM_ROM_ID)
            print(HPCM_SID_DEC)
                    
            print(DMCM)
            print(DMCMRomIDLengthInDecimal)
            print(DMCM_ROM_ID)
            print(DMCM_SID_DEC)
                    
            print(BCU)
            print(BCURomIDLengthInDecimal)
            print(BCU_ROM_ID)
            print(BCU_SID_DEC)
                    
            print(BCCM)
            print(BCCMRomIDLengthInDecimal)
            print(BCCM_ROM_ID)
            print(BCCM_SID_DEC)
                    
            # <-- Start Data Collection - Invalid Case--> 
            HPCM_DC =  ''.join(byte_pairs[tempIncre: tempIncre + 1])
            print(HPCM_DC)
            if HPCM_DC == '':
                Origin_BCU_NumberOfDataBlock = 0
                Origin_HPCM_NumberOfDataBlock = 0
                print("No Data Record") 
                
            
            # <-- End Data Collection - Invalid Case--> 
                    
            # <-- Start Data Collection - Normal Case--> 
            elif HPCM_DC != '0A': 
                Origin_HPCM_NumberOfDataBlock = 0
                print("NO data collection for HPCM")
                
                #BCU handling
                BCU_DC = HPCM_DC
                
                BCU_NumberOfDataBlock = ''.join(byte_pairs[tempIncre + 1:tempIncre + 5])
                countBCU = tempIncre + 5
                Origin_BCU_NumberOfDataBlock = int((BCU_NumberOfDataBlock[6:8] + BCU_NumberOfDataBlock[4:6] + BCU_NumberOfDataBlock[2:4] + BCU_NumberOfDataBlock[0:2]),16)
                print(BCU_NumberOfDataBlock)
                print(Origin_BCU_NumberOfDataBlock)    
                print(countBCU)
                        
                if Origin_BCU_NumberOfDataBlock > 1: #case BCU multiple data block 
                    print("BCU Multiple Handling")
                    tempNext = 0
                    i = 0
                    # accumulate the output in variables
                    BCUoutput = ""
                    for i in range(Origin_BCU_NumberOfDataBlock):
                    #while i < Origin_BCU_NumberOfDataBlock:
                        BCU_DID = ''.join(byte_pairs[countBCU + tempNext:countBCU + tempNext + 2]) #35: 35+2
                        Origin_BCU_DID = BCU_DID[2:4] + BCU_DID[0:2]
                        BCU_DataSize = ''.join(byte_pairs[countBCU + tempNext + 2 :countBCU + tempNext + 3])
                        temp = countBCU + tempNext
                        BCU_DataSizeInDec = int(BCU_DataSize, 16)
                        bs = BCU_DataSizeInDec
                        BCU_DataRecord = ' '.join(byte_pairs[temp + 3:temp + 3 + bs])
                        i += 1
                        tempNextTemp = temp + 3 + bs
                        tempNext = tempNextTemp - countBCU
                                
                        BCUoutput += "\nData Identifier: {}\n".format(Origin_BCU_DID)
                        BCUoutput += "Data Size: {}\n".format(BCU_DataSizeInDec)
                        BCUoutput += "Data Record: {}\n".format(BCU_DataRecord)
                                
                                #print("BCU_DID:", Origin_BCU_DID)
                                #print("BCU_DataSize:", BCU_DataSizeInDec)
                                #print("BCU_DataRecord:", BCU_DataRecord)
                                #print(tempNextTemp)
                                #print(tempNext)

                elif Origin_BCU_NumberOfDataBlock == 0:  #case BCU 0 data block  
                    print("BCU Invalid Data Collection")
                    Origin_HPCM_NumberOfDataBlock = 0
                else: #case BCU 1 data block 
                    print("BCU normal handling")
                    BCU_DID = ''.join(byte_pairs[countBCU:countBCU + 2])
                    Origin_BCU_DID = BCU_DID[2:4] + BCU_DID[0:2]
                    BCU_DataSize = ''.join(byte_pairs[countBCU + 2 :countBCU + 3])
                    temp = countBCU + 3              
                    BCU_DataSizeInDec = int(BCU_DataSize,16)
                    bs = BCU_DataSizeInDec
                    BCU_DataRecord = ' '.join(byte_pairs[temp: temp + bs]) 
                        #end 1DB BCU
            else:     
                HPCM_DC =  ''.join(byte_pairs[tempIncre: tempIncre + 1])
                HPCM_NumberOfDataBlock = ''.join(byte_pairs[tempIncre + 1: tempIncre + 5]) 
                countHpcm = tempIncre + 5
                Origin_HPCM_NumberOfDataBlock = int((HPCM_NumberOfDataBlock[6:8] + HPCM_NumberOfDataBlock[4:6] + HPCM_NumberOfDataBlock[2:4] + HPCM_NumberOfDataBlock[0:2]),16)
                print(Origin_HPCM_NumberOfDataBlock)    
                
                if Origin_HPCM_NumberOfDataBlock > 1: # HPCM case multiple data block
                    print("HPCM Multiple handling")
                    #HPCM Multiple DB handling
                    tempNext = 0
                    i = 0
                    # accumulate the output in variables
                    Hpcmoutput = ""
                    for i in range(Origin_HPCM_NumberOfDataBlock):
                    #while i < Origin_HPCM_NumberOfDataBlock:
                        HPCM_DID = ''.join(byte_pairs[countHpcm + tempNext:countHpcm + tempNext + 2]) #35: 35+2
                        Origin_HPCM_DID = HPCM_DID[2:4] + HPCM_DID[0:2]
                        HPCM_DataSize = ''.join(byte_pairs[countHpcm + tempNext + 2 :countHpcm + tempNext + 3])
                        temp = countHpcm + tempNext
                        HPCM_DataSizeInDec = int(HPCM_DataSize, 16)
                        bs = HPCM_DataSizeInDec
                        HPCM_DataRecord = ' '.join(byte_pairs[temp + 3:temp + 3 + bs])
                        i += 1
                        tempNextTemp = temp + 3 + bs
                        tempNext = tempNextTemp - countHpcm
                            
                        Hpcmoutput += "\nData Identifier: {}\n".format(Origin_HPCM_DID)
                        Hpcmoutput += "Data Size: {}\n".format(HPCM_DataSizeInDec)
                        Hpcmoutput += "Data Record: {}\n".format(HPCM_DataRecord)
                        #output += "{}\n".format(tempNext)
                            
                        print("HPCM_DID:", Origin_HPCM_DID)
                        print("HPCM_DataSize:", HPCM_DataSizeInDec)
                        print("HPCM_DataRecord:", HPCM_DataRecord)
                        print(tempNextTemp)
                        print(tempNext)
                    
                    continueBCU = tempNextTemp # next position BCU for data collection 
                    
                    #BCU handling
                    BCU_DC =  ''.join(byte_pairs[continueBCU: continueBCU + 1])
                    print(BCU_DC)
                    if BCU_DC == '': 
                        print("NO data collection for BCU")
                        Origin_BCU_NumberOfDataBlock = 0
                    else:
                        BCU_NumberOfDataBlock = ''.join(byte_pairs[continueBCU + 1: continueBCU + 5])
                        countBCU = continueBCU + 5
                        print(BCU_NumberOfDataBlock)
                        Origin_BCU_NumberOfDataBlock = int((BCU_NumberOfDataBlock[6:8] + BCU_NumberOfDataBlock[4:6] + BCU_NumberOfDataBlock[2:4] + BCU_NumberOfDataBlock[0:2]),16)  
                        
                        if Origin_BCU_NumberOfDataBlock > 1: #case BCU multiple data block 
                            print("BCU Multiple Handling")
                            tempNext = 0
                            i = 0
                            # accumulate the output in variables
                            BCUoutput = ""
                            for i in range(Origin_BCU_NumberOfDataBlock):
                            #while i < Origin_BCU_NumberOfDataBlock:
                                BCU_DID = ''.join(byte_pairs[countBCU + tempNext:countBCU + tempNext + 2]) #35: 35+2
                                Origin_BCU_DID = BCU_DID[2:4] + BCU_DID[0:2]
                                BCU_DataSize = ''.join(byte_pairs[countBCU + tempNext + 2 :countBCU + tempNext + 3])
                                temp = countBCU + tempNext
                                BCU_DataSizeInDec = int(BCU_DataSize, 16)
                                bs = BCU_DataSizeInDec
                                BCU_DataRecord = ' '.join(byte_pairs[temp + 3:temp + 3 + bs])
                                i += 1
                                tempNextTemp = temp + 3 + bs
                                tempNext = tempNextTemp - countBCU
                                
                                BCUoutput += "\nData Identifier: {}\n".format(Origin_BCU_DID)
                                BCUoutput += "Data Size: {}\n".format(BCU_DataSizeInDec)
                                BCUoutput += "Data Record: {}\n".format(BCU_DataRecord)
                                #output += "{}\n".format(tempNext)
                                
                                print("BCU_DID:", Origin_BCU_DID)
                                print("BCU_DataSize:", BCU_DataSizeInDec)
                                print("BCU_DataRecord:", BCU_DataRecord)
                                print(tempNextTemp)
                                print(tempNext)
                                
                        elif Origin_BCU_NumberOfDataBlock == 0:  #case BCU 0 data block 
                            print("BCU Invalid Data Collection")
                        else: #case BCU 1 data block 
                            print("BCU normal handling")
                            BCU_DID = ''.join(byte_pairs[continueBCU + 5:continueBCU + 7])
                            Origin_BCU_DID = BCU_DID[2:4] + BCU_DID[0:2]
                            BCU_DataSize = ''.join(byte_pairs[continueBCU + 7 :continueBCU + 8])
                            print(BCU_DataSize)
                            temp = continueBCU + 8              
                            BCU_DataSizeInDec = int(BCU_DataSize,16)
                            bs = BCU_DataSizeInDec
                            BCU_DataRecord = ' '.join(byte_pairs[temp: temp + bs])
                        
                elif Origin_HPCM_NumberOfDataBlock == 0: # case HPCM 0 data block
                    print("HPCM Invalid Data Collection")
                        
                else: # case HPCM 1 data block 
                    #HPCM Handling 
                    print("HPCM Normal Handling")
                    HPCM_DID = ''.join(byte_pairs[countHpcm:countHpcm + 2])
                    Origin_HPCM_DID = HPCM_DID[2:4] + HPCM_DID[0:2]
                    HPCM_DataSize = ''.join(byte_pairs[countHpcm + 2:countHpcm + 3]) 
                    HPCM_DataSizeInDec = int(HPCM_DataSize,16)
                    hs = HPCM_DataSizeInDec
                    HPCM_DataRecord = ' '.join(byte_pairs[countHpcm + 3: countHpcm + 3 + hs]) 
                    #end 1DB HPCM
                    print(HPCM_DataRecord)
                    
                    #BCU handling
                    BCU_DC =  ''.join(byte_pairs[countHpcm + 3 + hs: countHpcm + 4 + hs])
                    print(BCU_DC)
                    if BCU_DC == '': 
                        print("NO data collection for BCU")
                        Origin_BCU_NumberOfDataBlock = 0
                    else:
                        BCU_NumberOfDataBlock = ''.join(byte_pairs[countHpcm + 4 + hs: countHpcm + 8 + hs])
                        countBCU = countHpcm + 8 + hs
                        Origin_BCU_NumberOfDataBlock = int((BCU_NumberOfDataBlock[6:8] + BCU_NumberOfDataBlock[4:6] + BCU_NumberOfDataBlock[2:4] + BCU_NumberOfDataBlock[0:2]),16)
                        print(BCU_NumberOfDataBlock)
                        print(Origin_BCU_NumberOfDataBlock)    
                        print(countBCU)
                        
                        if Origin_BCU_NumberOfDataBlock > 1: #case BCU multiple data block 
                            
                            print("BCU Multiple Handling")
                            tempNext = 0
                            i = 0
                            # accumulate the output in variables
                            BCUoutput = ""
                            for i in range(Origin_BCU_NumberOfDataBlock):
                            #while i < Origin_BCU_NumberOfDataBlock:
                                BCU_DID = ''.join(byte_pairs[countBCU + tempNext:countBCU + tempNext + 2]) #35: 35+2
                                Origin_BCU_DID = BCU_DID[2:4] + BCU_DID[0:2]
                                BCU_DataSize = ''.join(byte_pairs[countBCU + tempNext + 2 :countBCU + tempNext + 3])
                                temp = countBCU + tempNext
                                BCU_DataSizeInDec = int(BCU_DataSize, 16)
                                bs = BCU_DataSizeInDec
                                BCU_DataRecord = ' '.join(byte_pairs[temp + 3:temp + 3 + bs])
                                i += 1
                                tempNextTemp = temp + 3 + bs
                                tempNext = tempNextTemp - countBCU
                                
                                BCUoutput += "\nData Identifier: {}\n".format(Origin_BCU_DID)
                                BCUoutput += "Data Size: {}\n".format(BCU_DataSizeInDec)
                                BCUoutput += "Data Record: {}\n".format(BCU_DataRecord)
                                
                                #print("BCU_DID:", Origin_BCU_DID)
                                #print("BCU_DataSize:", BCU_DataSizeInDec)
                                #print("BCU_DataRecord:", BCU_DataRecord)
                                #print(tempNextTemp)
                                #print(tempNext)
                                

                        elif Origin_BCU_NumberOfDataBlock == 0:  #case BCU 0 data block  
                            print("BCU Invalid Data Collection")
                        else: #case BCU 1 data block 
                            print("BCU normal handling")
                            BCU_DID = ''.join(byte_pairs[countBCU:countBCU + 2])
                            Origin_BCU_DID = BCU_DID[2:4] + BCU_DID[0:2]
                            BCU_DataSize = ''.join(byte_pairs[countBCU + 2 :countBCU + 3])
                            temp = countBCU + 3              
                            BCU_DataSizeInDec = int(BCU_DataSize,16)
                            bs = BCU_DataSizeInDec
                            BCU_DataRecord = ' '.join(byte_pairs[temp: temp + bs]) 
                            #end 1DB BCU
                
                #<-- End Data Collection -Normal Case--> 
                    
                    
            #<-- Start Conversion Section -->
                    
            #VIN
            VIN_InAscii= ""
            for i in range(0, len(vin), 2):
                VIN_InAscii += chr(int(vin[i:i+2], 16))
                    
            #Latitude and Longtitude
            latitude = ''.join(byte_pairs[20:24])
            longitude = ''.join(byte_pairs[24:28])        
            # Convert hexadecimal to decimal
            decimal_value_lat = int(latitude, 16)
            decimal_value_lon = int(longitude, 16)
            
            # Convert decimal to degrees
            degrees_lat = decimal_value_lat / 3600000.0
            degrees_lon = decimal_value_lon / 3600000.0
            result_lat = "{:6f}".format(degrees_lat)
            result_lon = "{:6f}".format(degrees_lon)
            
            # Calculate minutes and seconds
            minutes_lat = (degrees_lat - int(degrees_lat)) * 60.0
            seconds_lat = (minutes_lat - int(minutes_lat)) * 60.0
            minutes_lon = (degrees_lon - int(degrees_lon)) * 60.0
            seconds_lon = (minutes_lon - int(minutes_lon)) * 60.0    
            
            #Odometer
            Odometer = int(odometer, 16)
                    
            #Timestamp
            # Convert hex value to decimal values
            year = int(timestamp[0:4], 16)
            month = int(timestamp[4:6], 16)
            day = int(timestamp[6:8], 16)
            hour = int(timestamp[8:10], 16)
            minute = int(timestamp[10:12], 16)
            second = int(timestamp[12:14], 16)
            tz = timestamp[14:16]

            try: # Create timestamp object
                Timestamp = datetime.datetime(year, month, day, hour, minute, second)
            except ValueError as e:
                print("Error: ", e)
            else: # Print the Timestamp
                Timestamp = Timestamp.strftime("%d/%m/%Y %H:%M:%S TZ:{}".format(tz))
         
            # Open file in "w" mode to clear its contents
            output_path = output_path_entry.get()        
            # Open file in "w" mode to clear its contents
            with open(output_path, "w") as f:
                pass
       
            # Writing the formatted fields to file
            with open(output_path, 'a') as file2:
                file2.write("......................................................................................................................................................... " + "\n")
                file2.write("                                                         ECU data Parser Tool                                         " + "\n")       
                file2.write("Revision History:" + "\n")     
                file2.write("Date             Author                 Description" + "\n")
                file2.write("28-07-2023       mduong                 This ECU data record parser that decodes what data has ben collected from ECU as requirement requests " + "\n\n")

                file2.write("......................................................................................................................................................... " + "\n")
                file2.write("                                                            Header Information                                                 " + "\n")       
                file2.write("......................................................................................................................................................... " + "\n\n")        
                file2.write("VIN: " + VIN_InAscii + "\n" + "Odometer: " + str(Odometer) + "\n" + "Latitude: {}° {}' {:.3f}\" N".format(int(degrees_lat), int(minutes_lat), seconds_lat) + " (" +(result_lat) + ")" + "\n" + "Longtitude: {}° {}' {:.3f}\" N".format(int(degrees_lon), int(minutes_lon), seconds_lon) + " (" +(result_lon) + ")" + "\n" + "Timestamp: " + Timestamp + "\n\n")
                        
                file2.write("......................................................................................................................................................... " + "\n")
                file2.write("                                                            Module Information                                                 " + "\n")       
                file2.write("......................................................................................................................................................... " + "\n\n")
                
                file2.write("HPCM: " + HPCM + "\n" + "ROM_ID_Length: " + str(HPCMRomIDLengthInDecimal) + "\n" + "ROM_ID: " + HPCM_ROM_ID + "\n" + "SID: " + HPCM_SID_HEX + "\n\n")
                file2.write("DMCM: " + DMCM + "\n" + "ROM_ID_Length: " + str(DMCMRomIDLengthInDecimal) + "\n" + "ROM_ID: " + DMCM_ROM_ID + "\n" + "SID: " + str(DMCM_SID_DEC) + "\n\n")
                file2.write("BCU: " + BCU + "\n" + "ROM_ID_Length: " + str(BCURomIDLengthInDecimal) + "\n" + "ROM_ID: " + BCU_ROM_ID + "\n" + "SID: " + BCU_SID_HEX + "\n\n")
                file2.write("BCCM: " + BCCM + "\n" + "ROM_ID_Length: " + str(BCCMRomIDLengthInDecimal) + "\n" + "ROM_ID: " + BCCM_ROM_ID + "\n" + "SID: " + str(BCCM_SID_DEC) + "\n\n")
                
                file2.write("......................................................................................................................................................... " + "\n")
                file2.write("                                                            Data Collection                                                    " + "\n")       
                file2.write("......................................................................................................................................................... " + "\n\n")
                
                # case No Data Collection 
                if HPCM_DC == '': 
                    file2.write("No Data Collection - Invalid Data Collection")
                    
                # case: 0DC_HPCM_1DB_BCU passed
                if HPCM_DC != '0A' and Origin_BCU_NumberOfDataBlock == 1:
                    file2.write("BCU: " + BCU_DC + "\n" + "Number Of Data Block: " + str(Origin_BCU_NumberOfDataBlock) + "\n" + "Data Identifier: " + Origin_BCU_DID + "\n" + "Data Size: " + str(BCU_DataSizeInDec) + "\n" + "Data Record: " + BCU_DataRecord + "\n")
                
                # case: 0DC_HPCM_NDB_BCU passed
                if HPCM_DC != '0A' and Origin_BCU_NumberOfDataBlock > 1:
                    file2.write("BCU: " + BCU_DC + "\n" + "Number Of Data Block: " + str(Origin_BCU_NumberOfDataBlock) + "\n" + BCUoutput)
                    
                # case: 1DB_HPCM_0DC_BCU
                if HPCM_DC == '0A' and Origin_HPCM_NumberOfDataBlock == 1:
                    file2.write("HPCM: " + HPCM_DC + "\n" + "Number Of Data Block: " + str(Origin_HPCM_NumberOfDataBlock) + "\n" + "Data Identifier: " + Origin_HPCM_DID + "\n" + "Data Size: " + str(HPCM_DataSizeInDec) + "\n" + "Data Record: " + HPCM_DataRecord + "\n")
                    file2.write("......................................................................................................................................................... " + "\n")
                    
                # case: 1DB_HPCM_1DB_BCU passed
                if HPCM_DC == '0A' and Origin_HPCM_NumberOfDataBlock == 1 and Origin_BCU_NumberOfDataBlock == 1:
                    file2.write("BCU: " + BCU_DC + "\n" + "Number Of Data Block: " + str(Origin_BCU_NumberOfDataBlock) + "\n" + "Data Identifier: " + Origin_BCU_DID + "\n" + "Data Size: " + str(BCU_DataSizeInDec) + "\n" + "Data Record: " + BCU_DataRecord + "\n")
                    
                # case: 1DB_HPCM_NDB_BCU passed
                if HPCM_DC == '0A' and Origin_HPCM_NumberOfDataBlock == 1 and Origin_BCU_NumberOfDataBlock > 1:
                    file2.write("BCU: " + BCU_DC + "\n" + "Number Of Data Block: " + str(Origin_BCU_NumberOfDataBlock) + "\n" + BCUoutput)
                    
                # case: NDB_HPCM_0DB_BCU 
                if HPCM_DC == '0A' and Origin_HPCM_NumberOfDataBlock > 1:
                    file2.write("HPCM: " + HPCM_DC + "\n" + "Number Of Data Block: " + str(Origin_HPCM_NumberOfDataBlock) + "\n" + Hpcmoutput + "\n")
                    file2.write("......................................................................................................................................................... " + "\n")
                
                # case: NDB_HPCM_1DB_BCU 
                if HPCM_DC == '0A' and Origin_HPCM_NumberOfDataBlock > 1 and Origin_BCU_NumberOfDataBlock == 1:    
                    file2.write("BCU: " + BCU_DC + "\n" + "Number Of Data Block: " + str(Origin_BCU_NumberOfDataBlock) + "\n" + "Data Identifier: " + Origin_BCU_DID + "\n" + "Data Size: " + str(BCU_DataSizeInDec) + "\n" + "Data Record: " + BCU_DataRecord + "\n")
                # case: NDB_HPCM_NDB_BCU
                if HPCM_DC == '0A' and Origin_HPCM_NumberOfDataBlock > 1 and Origin_BCU_NumberOfDataBlock > 1:
                    file2.write("BCU: " + BCU_DC + "\n" + "Number Of Data Block: " + str(Origin_BCU_NumberOfDataBlock) + "\n" + BCUoutput)
                
                # Error Case Have Data Collection but Data Block 0
                if (HPCM_DC == '0A' and Origin_HPCM_NumberOfDataBlock == 0) or (HPCM_DC == '0C' and Origin_BCU_NumberOfDataBlock == 0):
                    file2.write("ECU ID: " + HPCM_DC + "\n")
                    file2.write("Error/Unexpected Case - Have Data Collection but Data Block 0")

            print("Total number of pairs:", total_pairs)
            
            # Remove any existing notification labels
            for widget in window.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget('text') == "File Saved Successfully":
                    widget.destroy()
            # Remove any existing notification labels
            for widget in window.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget('text') == "File not found!":
                    widget.destroy()
                    
            # Create a new notification label
            save_notification = tk.Label(window, text="File Saved Successfully", fg="green", font=("TkDefaultFont", 10, "bold"))
            save_notification.pack(side=tk.LEFT, padx=5)

    except IOError:
        # Remove any existing notification labels
        for widget in window.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget('text') == "File not found!":
                widget.destroy()
        for widget in window.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget('text') == "File Saved Successfully":
                    widget.destroy()
                    
        # Display error message if file is not found
        error_notification = tk.Label(window, text="File not found!", fg="red", font=("TkDefaultFont", 10, "bold"))
        error_notification.pack(side=tk.LEFT, padx=5)
        output_text.delete(1.0, tk.END)

    except:
        # Display generic error message
        error_notification = tk.Label(window, text="An error occurred!", fg="red", font=("TkDefaultFont", 10, "bold"))
        error_notification.pack(side=tk.LEFT, padx=5)
        output_text.delete(1.0, tk.END)
        
# Create a new Tkinter window
window = tk.Tk()
window.title("ECU Data Parser Tool")

# Create a label for the file path input
file_path_label = tk.Label(window, text="Select the .dat file:")
file_path_label.pack()

# Create a frame for the file path input and the browse button
file_path_frame = tk.Frame(window)
file_path_frame.pack()

# Create an entry for the file path input
file_path_entry = tk.Entry(file_path_frame)
file_path_entry.pack(side=tk.LEFT)

# Create a button to browse for the file
browse_button = tk.Button(file_path_frame, text="Browse", command=browse_file)
browse_button.pack(side=tk.LEFT)

# Create a label for the output file location input
output_path_label = tk.Label(window, text="Select the output file location:")
output_path_label.pack()

# Create a frame for the output file location input and the browse button
output_path_frame = tk.Frame(window)
output_path_frame.pack()

# Create an entry for the output file location input
output_path_entry = tk.Entry(output_path_frame)
output_path_entry.pack(side=tk.LEFT)

# Create a button to browse for the output file location
output_browse_button = tk.Button(output_path_frame, text="Browse", command=browse_output_location)
output_browse_button.pack(side=tk.LEFT)

# Create a button to initiate the conversion
convert_button = tk.Button(window, text="Convert", command=convert_file)
convert_button.pack()

# Create a label for the output
output_label = tk.Label(window, text="Hex Content:")
output_label.pack()

# Create a text box for the output
output_text = tk.Text(window, height=10)
output_text.pack()

# Start the Tkinter event loop
window.mainloop()

#NOTE New Test Scenarios: DB: Data Block, DC: Data Collection
 
# Invalid case: 0DB_2ECU                No data collection - passed
# case:         0DC_HPCM_NDB_BCU               passed - OK
# case:         NDB_HPCM_0DC_BCU               passed - OK
# case:         0DC_HPCM_1DB_BCU               passed - OK
# case:         0DC_HPCM_NDC_BCU               passed - OK    
# case:         1DB_HPCM_0DC_BCU               passed - OK          
# case:         1DB_HPCM_1DB_BCU               passed - OK
# case:         1DB_HPCM_NDB_BCU               passed - OK      
# case:         NDB_HPCM_NDB_BCU               Passed - OK

# Error/Unexpected Case
# case: Have Data Collection but Data Block 0   Passed - OK
 