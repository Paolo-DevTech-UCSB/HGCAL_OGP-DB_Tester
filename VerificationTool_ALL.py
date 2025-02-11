# -*- coding: utf-8 -*-
"""
1/13/25
AutoDB Testing Tool: 
    by Paolo J
"""

import ReverseOffsets as RO
import PGConnect as PGC
import numpy as np


def Generate_Spoof_Components(comp_type, Density, Shape, PositionID, proto_name_list, Inputs):
    #PositionID = 2;
    PositionID_list = [PositionID]
    count = 0; 
    #Enter info here
    Angle, XOffset, YOffset = Inputs;
    Angles = [Angle]
    XOffsets = [XOffset]
    YOffsets = [YOffset]
    Geometry = Shape; 
    List = []
    
    if comp_type != 'module' and comp_type != 'protomodule':
        print('ERROR: Comp type NOT passed to spoof_componnents')
    if comp_type == 'modules':
        if proto_name_list == []:
            print('Error: Proto name list empty on module step')
    
    
    # Part 1 Reverse Calculations and Set Generation
    
    for PositionID in PositionID_list:
        for ang in Angles:
            for X in XOffsets:
                for Y in YOffsets:
                    
                    #print(PositionID)
                    #print(Density, Shape, PositionID)
                    if Density == 'LD':
                        if Shape == 'Left':
                            if PositionID == 1:
                                PinAngle = -0.007051
                            elif PositionID == 2:
                                PinAngle = 0.01410
                        elif Shape == 'Right':
                            if PositionID == 2:
                                PinAngle = 0.11287361544910751
                            elif PositionID == 1:
                                PinAngle = -0.003526
                        elif Shape == 'Top':
                            if PositionID == 1:
                                PinAngle = -0.01939
                            elif PositionID == 2:
                                PinAngle = -0.016744390127605584
                        elif Shape == 'Bottom':
                            if PositionID == 1:
                                PinAngle = -0.023801614860592415
                            elif PositionID == 2:
                                PinAngle = -0.015868232038327264
                        elif Shape == 'Five':
                            if PositionID == 1:
                                PinAngle = -0.002292045103521361
                            elif PositionID == 2:
                                PinAngle = 0.007640659728686245
                        else:  # Handle cases where Shape is not 'Left', 'Right', 'Top', 'Bottom', or 'Five'
                            if PositionID == 1:
                                PinAngle = -0.022919532957
                            elif PositionID == 2:
                                PinAngle = -0.01527887
                    else:
                        if Shape == 'Top':
                            if PositionID == 1:
                                PinAngle = -0.02521215833125812
                            elif PositionID == 2:
                                PinAngle = -0.022918310582918516
                        else:  # Handle cases where Shape is not 'Top'
                            if PositionID == 1:
                                PinAngle = -0.022919532957
                            elif PositionID == 2:
                                PinAngle = -0.01527887;
                    
                    count = count + 1;
                    FD1X, FD2X, FD3X, FD4X, FD5X, FD6X, FD1Y, FD2Y, FD3Y, FD4Y, FD5Y, FD6Y = RO.reverse_offsets(X, Y, ang, PositionID, Shape, Density, comp_type)
                    #print(FD3X, FD3Y, FD6X, FD6Y)
                    #print("-----")
                    List.append([count, X, Y, ang, FD1X, FD2X, FD3X, FD4X, FD5X, FD6X, FD1Y, FD2Y, FD3Y, FD4Y, FD5Y, FD6Y, PinAngle, PositionID, comp_type])
                    #print(count, X, Y, ang, FD1X, FD2X, FD3X, FD4X, FD1Y, FD2Y, FD3Y, FD4Y)
                    #print()
                
    # Part 2: The Review List
    
    Review = []; 
    if comp_type == 'protomodule': 
        proto_name_list = [];
    for data in List:
        count, X, Y, ang, FD1X, FD2X, FD3X, FD4X, FD5X, FD6X, FD1Y, FD2Y, FD3Y, FD4Y, FD5Y, FD6Y, PinAngle, PositionID, comp_type = data;
        if comp_type == 'protomodule':
            FirstPart = 'testcomponent_';
            SecondPart = str(np.random.randint(100000000));
            result = FirstPart + SecondPart;
            proto_name_list.append(result)
        elif comp_type == 'module': 
            result = proto_name_list[0];
        else:
            result = 'testcomponent_noname'
            print('ERROR: NO NAME GIVEN TO COMPONENT')
            
        Review.append([result, count, X, Y, ang, FD1X, FD2X, FD3X, FD4X, FD5X, FD6X, FD1Y, FD2Y, FD3Y, FD4Y, FD5Y, FD6Y, PinAngle, PositionID, comp_type])
        #c = c + 1; 
        
    #for data in Review:
    #    print(data)
    #    print()
    
    # Part 2.5 print and Run AutoDB
    
    def spoof_ogp_file(output_file, output_name, FD1X, FD2X, FD3X, FD4X, FD5X, FD6X, FD1Y, FD2Y, FD3Y, FD4Y, FD5Y, FD6Y, PinAngle, PositionID):
        new_component_id = output_name
        new_points = [
            (FD1X, FD1Y, 300.0),  # Values for FD1
            (FD2X, FD2Y, 300.0),  # Values for FD2
            (FD3X, FD3Y, 300.0),  # Values for FD3
            (FD4X, FD4Y, 300.0),   # Values for FD4
            (FD5X, FD5Y, 300.0),   # Values for FD4
            (FD6X, FD6Y, 300.0)   # Values for FD4
        ]
    
        content = """UCSB_Constrained_Survey
LastModified: 12:09:24 10:17:07     
Runtime: 12:09:24 10:02:26
Component ID: {component_id}
Operator: pjordano   
Geometry: {Geometry}
Density: {Density}
Sensor size: 8
Flatness: 0.60000
Position ID: {PositionID}
TrayNo: 2
---
Plane Pos1_MThickness1
Point        17.77073316596        6.90350428330        3.16473251921
direction cosine: 1                                                              
Plane Pos1_MThickness2
Point        33.72585204537        7.17783287632        3.19282005876
direction cosine: 1                                                              
Plane Pos1_MThickness3
Point        62.77487258271       26.55899628233        3.15597759339
direction cosine: 1                                                              
Plane Pos1_MThickness4
Point        94.47774810933       46.74824888254        3.31242670683
direction cosine: 1                                                              
Plane Pos1_MThickness5
Point       104.94941217380       57.02638897771        3.37166747775
direction cosine: 1                                                             
Plane Pos1_MThickness6
Point       102.46027670706       92.94659078119        2.40073467719
direction cosine: 1                                                             
Plane Pos1_MThickness7
Point       104.02764374148      134.02984549567        3.08507820465
direction cosine: 1                                                              
Plane Pos1_MThickness8
Point        95.53091553819      147.72922431542        3.04251796412
direction cosine: 1                                                              
Plane Pos1_MThickness9
Point        62.92969814321      166.09547962250        3.05235562127
direction cosine: 1                                                              
Plane Pos1_MThickness10
Point        32.28882874757      184.37847425380        3.15968842459
direction cosine: 1                                                              
Plane Pos1_MThickness11
Point        17.61972107835      183.47625628857        3.22594996088
direction cosine: 1                                                              
Plane Pos1_MThickness12
Point       -15.80958412499      163.73659437760        3.26247523562
direction cosine: 1                                                              
Plane Pos1_MThickness13
Point       -43.77459727289      147.02537331144        3.18129690436
direction cosine: 1                                                              
Plane Pos1_MThickness14
Point       -53.86957964706      132.70572061566        3.11334269469
direction cosine: 1                                                              
Plane Pos1_MThickness15
Point       -53.85783429331       96.86755001449        3.05242713906
direction cosine: 1                                                              
Plane Pos1_MThickness16
Point       -53.84676654256       55.77226798572        3.05915589156
direction cosine: 1                                                              
Plane Pos1_MThickness17
Point       -50.42919073974       61.45580480825        3.07229826471
direction cosine: 1                                                              
Plane Pos1_MThickness18
Point       -14.44814247962       28.67973344255        3.11052104867
direction cosine: 1                                                              
Plane Pos1_MThickness19
Point         0.92441039452       61.58648403887        3.06437562418
direction cosine: 1                                                              
Plane Pos1_MThickness20
Point        44.51656142316       61.59784486002        3.86174212197
direction cosine: 1                                                              
Plane Pos1_MThickness21
Point        62.63357063070       94.24203870912        3.07369920082
direction cosine: 1                                                              
Plane Pos1_MThickness22
Point        47.17133839966      129.07102102206        3.89896875211
direction cosine: 1                                                              
Plane Pos1_MThickness23
Point         0.79115235648      129.05498455546        3.18439702543
direction cosine: 1                                                              
Plane Pos1_MThickness24
Point       -11.86993339182       97.45097191313        3.92235943628
direction cosine: 1                                                              
Plane Pos1_MThickness25
Point        28.68316404105       98.30691796865        3.08043899594
direction cosine: 1                                                               
Circle pos1_FD1
Point        {point1[0]}      {point1[1]}      {point1[2]}                
direction cosine: 1                                                               
Radius: 1                      
Circle pos1_FD2
Point        {point2[0]}      {point2[1]}      {point2[2]}                
direction cosine: 1                                                               
Radius: 1                      
Circle pos1_FD3
Point       {point3[0]}      {point3[1]}      {point3[2]}                      
direction cosine: 1                                                                
Radius: 1                      
Circle pos1_FD4
Point       {point4[0]}      {point4[1]}      {point4[2]}                       
direction cosine: 1     
Circle pos1_FD5
Point       {point5[0]}      {point5[1]}      {point5[2]}                       
direction cosine: 1   
Circle pos1_FD6
Point       {point6[0]}      {point6[1]}      {point6[2]}                       
direction cosine: 1                                                             
Radius: 1
        """
    
        content = content.format( component_id=new_component_id, Geometry = Geometry, Density = Density, 
                                 PositionID=PositionID, 
                                 point1=new_points[0], 
                                 point2=new_points[1], 
                                 point3=new_points[2], 
                                 point4=new_points[3], 
                                 point5=new_points[4], 
                                 point6=new_points[5])
    
        with open(output_file, 'w') as file:
            file.write(content)



    for run in Review:
        if comp_type == 'protomodule':
            temp = fr'C:\Users\Admin\Desktop\module_assembly_surveys\offsets\OGP_results\protomodules\{run[0]}.txt'
        elif comp_type == 'module':   
            temp = fr'C:\Users\Admin\Desktop\module_assembly_surveys\offsets\OGP_results\modules\{run[0]}.txt'
        else: 
            print('ERROR:  comp_type not passed to temp (location) in spoof_components')
            temp = fr'C:\Users\Admin\Desktop\module_assembly_surveys\offsets\OGP_results\protomodules\{run[0]}.txt'
        spoof_ogp_file(temp, run[0], run[5], run[6], run[7], run[8], run[9], run[10], run[11], run[12], run[13], run[14], run[15], run[16], run[17], run[18])
        
    

    # Part 3 
    return proto_name_list, List, run, Review
    

def compare_data(proto_name_list, List, run, Review, comp_type, PositionID):
    #print("COMPARE DATA: ", comp_type)
    if comp_type == 'protomodule': 
        ReturningData = PGC.Get_PG_Info_By_Name(proto_name_list, 'protomodule')
    elif comp_type == 'module':
        ReturningData = PGC.Get_PG_Info_By_Name(proto_name_list, 'module')
    else:
        print('Error: Comp Type didnt Make to PGC from compare_data')
        
    
    #print(f"Returning Data: {ReturningData}")
    #print(ReturningData)
    #print(List)    
    ReportList = []; Passing = [];
    if 'No data found for the given module names' in ReturningData[0]:
        Passing.append(["no offsets received from pg"])
        #print(proto_name_list)
        #print('__________^proto_name_list due to to no offsets recived from pg^____________')
        
        
    for List in ReturningData:
        for run in Review:
            if run[0] == List[0]:
                PinAngle = run[17]
                #print(run[2], run[3], run[4], List[1], List[2], List[3])
                temp = f'########===--{comp_type}-results--====############'
                ReportList.append(temp)
                #print('############====--results--====############')
                temp = "Names: " + run[0] + List[0]
                ReportList.append(temp)
                #print("Names:", run[0], List[0])
                temp = "Pos " + str(run[18])
                ReportList.append(temp)
                #print("Pos:", run[18])
                if PositionID == 1:
                    temp = "X: yinput: " + str(run[2]) + " -->  X:" +  str(int(run[2]*1000)) + " <db>: " +  str(List[1])
                elif PositionID == 2:
                    temp = "X: yinput: " + str(run[2]) + "*(-1) -->  X:" +  str(int(run[2]*1000)*-1) + " <db>: " +  str(List[1])    
                ReportList.append(temp)
                #print("X values:", run[2],"--", List[1])
                if PositionID == 1:
                    temp = "Y: xinput: " + str(run[2]) + "*(-1) =  Y:" +  str(int(run[3]*1000)*-1) + " <db>: " +  str(List[2])
                if PositionID == 2:
                    temp = "Y: xinput: " + str(run[2]) + " -->  Y:" +  str(int(run[3]*1000)) + " <db>: " +  str(List[2])
                ReportList.append(temp)
                #print("Y Values:", run[3],"--", List[2])
                temp = "Angles: " + f"{(run[4] - PinAngle):.3f}" + ' --> ' + str(List[3])
                #print('Input Angle:', str(run[4]), 'PinAngle:', PinAngle, 'Input - Pin =', f"{(run[4] - PinAngle):.3f}")
                #print('--------------PIN ANGLE, ', PinAngle)
                #if int(run[4]) != int(List[3]):
                if int(run[4]- PinAngle) != int(List[3]): 
                    Passing.append(["Input Angle Offset: " + str(run[4] - PinAngle) + " Is Not Equal to db: " + str(List[3])])
                elif int(List[3]) > 1:
                    Passing.append(["Returned Angle Offset: " + str(List[3]) + " >> 1, offset too big"])
                ReportList.append(temp)
                #print("Angles:", run[4] - PinAngle, List[3])
                temp = "Angles (w/o pins): " + str(run[4]) +  ' --> '+ f"{(List[3] + PinAngle):.3f}"
                ReportList.append(temp)
                #print("Angles (w/o pins):", run[4], f"{(List[3] + PinAngle):.3f}")
                temp = f"Spoofed PinAngle: {PinAngle}"
                ReportList.append(temp)
                temp = f"Spoofed PinAngle: {PinAngle}"
                ReportList.append(temp)
                

                #print('-------=====################=====-------')
                #print('Input Data:', run[1], run[2], run[3] )
                #print('Returning Data:', List[1], List[2], List[3] )
                
                convertedX = int(run[2]*1000);
                convertedY = int(run[3]*1000);
                if PositionID == 1:
                    NEWX = convertedY;
                    NEWY = convertedX*-1;
                elif PositionID == 2: 
                    NEWX = convertedY*-1;
                    NEWY = convertedX;

                #print('Translated Input Data:', NEWX, NEWY, List[3] )

                if NEWX != int(List[1]): 
                    Passing.append(["Input X Offset (Rotated): " + str(NEWX/1000) + " Is Not Equal to db: " + str(List[1]/1000)])
                elif int(List[1]) > 5000:
                    Passing.append(["Returned X Offset: " + str(List[1]) + " >> 5000, offset too big"])

            
                if NEWY != int(List[2]): 
                    Passing.append(["Input Y Offset (Rotated): " + str(NEWY/1000) + " Is Not Equal to db: " + str(List[2]/1000)])
                elif int(List[2]) > 5000:
                    Passing.append(["Returned Y Offset: " + str(List[1]) + " >> 5000, offset too big"])
                temp = '-------=====################=====-------';
                ReportList.append(temp)
           
    #print("!!!!!!!!!!!!!!", len(Passing), Passing)            
    if len(Passing) == 0:
        Passing = [[True]];
                #print()
                #print("-Module Done-")
                #print()
    #part 4: compare inputs to outputs
    
    
    return ReportList, Passing
    
    
    
    
    
    
    
