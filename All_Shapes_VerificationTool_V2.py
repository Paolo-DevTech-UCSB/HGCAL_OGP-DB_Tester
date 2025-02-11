# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:53:57 2025

@author: Admin
"""
import VerificationTool_ALL
import subprocess

def Tests(Type, details, Angle, XOffset, YOffset, PositionID):
    #print("details", details)
    #details = True;
    comp_type = 'protomodule'
    #PositionID = 1; Angle = -0.5; XOffset = 0.5; YOffset = 0.5; 
    
    if 'HD' in Type:
        Density = 'HD';
    elif 'LD' in Type:
        Density = 'LD';
        
    if Type[2] == 'F':
        Shape = 'Full';
    elif Type[2] == '5':
        Shape = 'Five';
    elif Type[2] == 'L':
        Shape = 'Left';
    elif Type[2] == 'R':
        Shape = 'Right';
    elif Type[2] == 'T':
        Shape = 'Top';
    elif Type[2] == 'B':
        Shape = 'Bottom';
        
    Inputs = [Angle, XOffset, YOffset]
    print(Density, Shape, 'Pos', PositionID, 'Protomodule')
    proto_name_list = []; ReportList = []; PMPassing = []; MPassing = [];
    
    
    proto_name_list, List, run, Review = VerificationTool_ALL.Generate_Spoof_Components(comp_type, Density, Shape, PositionID, proto_name_list, Inputs)
    # Define the PowerShell commands
    commands = """
    cd C:\\Users\\Admin\\HGC_OGP_DB
    python .\\rwOGP\\main.py
    """
    pmstart = True;
    if pmstart:
        process = subprocess.Popen(["powershell", "-Command", commands], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            output, error = process.communicate(input="y\n", timeout=10)
            #print("y")
            if details:
                print(output)
           #lines = output.split('\n')

            # Search for the specific line containing "Hole Vs FDCenter"
            #for line in lines:
            #    if "Hole Vs FDCenter" in line:
            #        print(line)
        except subprocess.TimeoutExpired:
            process.kill()
            output, error = process.communicate()
            print("Process timed out")
        
        
        
        
        ReportList, PMPassing = VerificationTool_ALL.compare_data(proto_name_list, List, run, Review, comp_type, PositionID)
        for Item in ReportList:
            print(Item)

        if details:
            print(proto_name_list)
        comp_type = 'module';
        
        #print(Density, Shape, 'In Pos:', PositionID, 'Module')
        proto_name_list, List, run, Review = VerificationTool_ALL.Generate_Spoof_Components(comp_type, Density, Shape, PositionID, proto_name_list, Inputs)
        # Define the PowerShell commands
        commands = """
        cd C:\\Users\\Admin\\HGC_OGP_DB
        python .\\rwOGP\\main.py
        """
        print(Density, Shape, 'Pos', PositionID, 'Module')
        contin = True;
        if contin:
            process = subprocess.Popen(["powershell", "-Command", commands], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            try:
                output, error = process.communicate(input="y\n", timeout=10)
                #print("y")
                if details:
                    print(output)
                """lines = output.split('\n')
    
                # Search for the specific line containing "Hole Vs FDCenter"
                for line in lines:
                    if "Hole Vs FDCenter" in line:
                        print(line)"""
            except subprocess.TimeoutExpired:
                process.kill()
                output, error = process.communicate()
                print("Process timed out")
            
            ReportList, MPassing = VerificationTool_ALL.compare_data(proto_name_list, List, run, Review, comp_type, PositionID)
            
            for Item in ReportList:
                print(Item)
        

    return PMPassing, MPassing;
Tests('LDF', True, 0.0010, -0.05, 0.05, 1)
    


