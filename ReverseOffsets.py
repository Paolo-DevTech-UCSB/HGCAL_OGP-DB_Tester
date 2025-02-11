# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:08:53 2025

@author: hep
"""

import numpy as np

def reverse_offsets(OffsetX, OffsetY, AngleOffset, PositionID, Shape, Density, comp_type):
    #print(PositionID)
    #print("PositionID", PositionID)
    #print(Density, Shape, comp_type)
    if Density == 'HD':
        if Shape == 'Full':
            if comp_type == 'protomodule':
                if PositionID == 1:
                    FD1 = [56.8430, 265.8737]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [227.8285, 329.8903]
                    FD4 = [227.8285, 265.8737]
                    FD5 = [142.333, 298.179] ###
                    FD6 = [142.333, 298.179]#### BY  setting non needed FDS to the Expected FDC, Thier contributions are negated
                if PositionID == 2:
                    FD1 = [173.347, 137.951]
                    FD2 = [173.347, 77.957]
                    FD3 = [10.370, 77.957]
                    FD4 = [10.370, 137.957]
                    FD5 = [0,0]
                    FD6 = [0,0]
                FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1])/4]
                #print('THIS FDC', FDC)
                if PositionID == 1:
                    AdjustmentsX = -0.003;
                    AdjustmentsY = 0.297;
                if PositionID == 2:
                    AdjustmentsX = -0.327 + 0.0005;
                    AdjustmentsY = -0.246 + 0.005;
            if comp_type == 'module':
                if PositionID == 1:
                    FD1 = [56.8430, 265.8737]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [227.8285, 329.8903]
                    FD4 = [227.8285, 265.8737]
                    FD5 = [142.333, 298.179] ###
                    FD6 = [142.333, 298.179]#### BY  setting non needed FDS to the Expected FDC, Thier contributions are negated
                if PositionID == 2:
                    FD1 = [173.347, 137.951]
                    FD2 = [173.347, 77.957]
                    FD3 = [10.370, 77.957]
                    FD4 = [10.370, 137.957]
                    FD5 = [0,0]
                    FD6 = [0,0]
                FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1])/4]
                #print('THIS FDC', FDC)
                if PositionID == 1:
                    AdjustmentsX = -0.003;
                    AdjustmentsY = 0.297;
                if PositionID == 2:
                    AdjustmentsX = -0.327 + 0.0005;
                    AdjustmentsY = -0.246 + 0.005;
                
        elif Shape == 'Bottom':
            if comp_type == 'protomodule':
                if PositionID == 1:
                    FD1 = (126.333, 214.179)
                    FD2 = (217.334, 298.161)
                    FD3 = (126.333, 382.179)
                    FD4 = (158.333, 298.179)
                    FD5 = [0,0]
                    FD6 = [0,0]
                if PositionID == 2:
                    FD1 = (107.532, 191.714)
                    FD2 = (16.542, 107.73)
                    FD3 = (107.532, 23.714)
                    FD4 = (107.532, 107.714)
                    FD5 = [0,0]
                    FD6 = [0,0]
                FDC = [(FD1[0]+FD3[0])/2,(FD1[1]+FD3[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
            if comp_type == 'module':
                if PositionID == 1:
                    FD1 = (127.333, 215.179)
                    FD2 = (217.334, 298.161)
                    FD3 = (127.333, 381.179)
                    FD4 = (158.333, 298.179)
                    FD5 = [0,0]
                    FD6 = [0,0]
                if PositionID == 2:
                    FD1 = (106.532, 191.714)
                    FD2 = (16.542, 106.73)
                    FD3 = (106.532, 23.714)
                    FD4 = (106.532, 106.714)
                    FD5 = [0,0]
                    FD6 = [0,0]
                FDC = [(FD1[0]+FD3[0])/2,(FD1[1]+FD3[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                    
        elif Shape == 'Top':
            if comp_type == 'protomodule':
                if PositionID == 1:
                    FD1 = (108.893, 214.187)
                    FD2 = (217.334, 298.161)
                    FD3 = (108.893, 382.187)
                    FD4 = (158.333, 298.187)
                    FD5 = [0,0]
                    FD6 = [0,0]
                if PositionID == 2:
                    FD1 = (124.972, 191.714)
                    FD2 = (16.542, 107.73)
                    FD3 = (124.972, 23.714)
                    FD4 = (124.972, 107.714)
                    FD5 = [0,0]
                    FD6 = [0,0]
                FDC = [(FD1[0]+FD3[0])/2,(FD1[1]+FD3[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
            elif comp_type == 'module':
                if PositionID == 1:
                    FD1 = (113.333, 215.187)
                    FD2 = (217.334, 298.161)
                    FD3 = (113.333, 381.187)
                    FD4 = (158.333, 298.187)
                    FD5 = [0,0]
                    FD6 = [0,0]
                if PositionID == 2:
                    FD1 = (120.532, 147.714)
                    FD2 = (16.542, 106.73)
                    FD3 = (120.532, 67.714)
                    FD4 = (120.532, 106.714)
                    FD5 = [0,0]
                    FD6 = [0,0]
                FDC = [(FD1[0]+FD3[0])/2,(FD1[1]+FD3[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
        
        elif Shape == 'Left':
            if comp_type == 'protomodule':
                if PositionID == 1:
                    FD1 = (126.333, 214.179)
                    FD2 = (217.334, 298.161)
                    FD3 = (126.333, 382.179)
                    FD4 = (158.333, 298.179)
                    FD5 = [0,0]
                    FD6 = [0,0]
                if PositionID == 2:
                    FD1 = (107.532, 191.714)
                    FD2 = (16.542, 107.73)
                    FD3 = (107.532, 23.714)
                    FD4 = (107.532, 107.714)
                    FD5 = [0,0]
                    FD6 = [0,0]
                FDC = [(FD1[0]+FD3[0])/2,(FD1[1]+FD3[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
            if comp_type == 'module':
                if PositionID == 1:
                    FD1 = (127.333, 215.179)
                    FD2 = (217.334, 298.161)
                    FD3 = (127.333, 381.179)
                    FD4 = (158.333, 298.179)
                    FD5 = [0,0]
                    FD6 = [0,0]
                if PositionID == 2:
                    FD1 = (106.532, 191.714)
                    FD2 = (16.542, 106.73)
                    FD3 = (106.532, 23.714)
                    FD4 = (106.532, 106.714)
                    FD5 = [0,0]
                    FD6 = [0,0]
                FDC = [(FD1[0]+FD3[0])/2,(FD1[1]+FD3[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;            
   
        elif Shape == 'Right':
            if comp_type == 'protomodule':
                if PositionID == 1:
                    FD1 = (126.333, 214.179)
                    FD2 = (217.334, 298.161)
                    FD3 = (126.333, 382.179)
                    FD4 = (158.333, 298.179)
                    FD5 = [0,0]
                    FD6 = [0,0]
                if PositionID == 2:
                    FD1 = (107.532, 191.714)
                    FD2 = (16.542, 107.73)
                    FD3 = (107.532, 23.714)
                    FD4 = (107.532, 107.714)
                    FD5 = [0,0]
                    FD6 = [0,0]
                FDC = [(FD1[0]+FD3[0])/2,(FD1[1]+FD3[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
            if comp_type == 'module':
                if PositionID == 1:
                    FD1 = (127.333, 215.179)
                    FD2 = (217.334, 298.161)
                    FD3 = (127.333, 381.179)
                    FD4 = (158.333, 298.179)
                    FD5 = [0,0]
                    FD6 = [0,0]
                if PositionID == 2:
                    FD1 = (106.532, 191.714)
                    FD2 = (16.542, 106.73)
                    FD3 = (106.532, 23.714)
                    FD4 = (106.532, 106.714)
                    FD5 = [0,0]
                    FD6 = [0,0]
                FDC = [(FD1[0]+FD3[0])/2,(FD1[1]+FD3[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
            
    elif Density == 'LD':
        if Shape == 'Full':
            if comp_type == 'protomodule':
                if PositionID == 1:
                    FD1 = [56.8430, 265.8737]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [142.333, 360.89]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                if PositionID == 2:
                    FD1 = [173.347, 137.951]
                    FD2 = [173.347, 77.957]
                    FD3 = [91.532, 40]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD6[0])/2,(FD3[1]+FD6[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 2.286 +0.013;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = -2.299 +0.013; 
                    
            if comp_type == 'module':
                if PositionID == 1:
                    FD1 = [56.8430, 265.8737]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [142.333, 360.89]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                if PositionID == 2:
                    FD1 = [173.347, 137.951]
                    FD2 = [173.347, 77.957]
                    FD3 = [91.532, 40]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD6[0])/2,(FD3[1]+FD6[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 2.286 +0.013;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = -2.299 +0.013; 
                
        elif Shape == 'Left':
            #print("PositionID", PositionID)
            if comp_type == 'protomodule':
                if PositionID == 1:
                    FD1 = [99.328, 278.465]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [185.328,  278.465]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                elif PositionID == 2:
                    FD1 = [131.526, 127.442]
                    FD2 = [173.347, 77.957]
                    FD3 = [51.526, 127.442]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD1[0])/2,(FD3[1]+FD1[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0; 
            if comp_type == 'module':
                if PositionID == 1:
                    FD1 = [99.328, 270.185]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [185.328,  270.185]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                elif PositionID == 2:
                    FD1 = [131.526, 135.722]
                    FD2 = [173.347, 77.957]
                    FD3 = [51.526, 135.722]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD1[0])/2,(FD3[1]+FD1[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0; 
                
                
        elif Shape == 'Top':
            if comp_type == 'protomodule':
            #print("PositionID", PositionID)
                if PositionID == 1:
                    FD1 = [122.615, 338.187]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [122.615,  258.187]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                elif PositionID == 2:
                    FD1 = [111.238, 147.713]
                    FD2 = [173.347, 77.957]
                    FD3 = [111.238, 67.713]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD1[0])/2,(FD3[1]+FD1[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0; 
            if comp_type == 'module':
            #print("PositionID", PositionID)
                if PositionID == 1:
                    FD1 = [124.335, 338.187]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [124.335,  258.187]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                elif PositionID == 2:
                    FD1 = [109.518, 147.713]
                    FD2 = [173.347, 77.957]
                    FD3 = [109.518, 67.713]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD1[0])/2,(FD3[1]+FD1[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0; 
                
        elif Shape == 'Bottom':
            if comp_type == 'protomodule':
            #print("PositionID", PositionID)
                if PositionID == 1:
                    FD1 = [162.059, 338.188]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [162.059,  258.188]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                elif PositionID == 2:
                    FD1 = [71.815, 147.712]
                    FD2 = [173.347, 77.957]
                    FD3 = [71.815, 67.712]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD1[0])/2,(FD3[1]+FD1[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0; 
            if comp_type == 'module':
            #print("PositionID", PositionID)
                if PositionID == 1:
                    FD1 = [161.339, 338.188]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [161.339,  258.188]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                elif PositionID == 2:
                    FD1 = [72.535, 147.712]
                    FD2 = [173.347, 77.957]
                    FD3 = [72.535, 67.712]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD1[0])/2,(FD3[1]+FD1[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0; 
                
                
        elif Shape == 'Right':
            if comp_type == 'protomodule':
            #print("PositionID", PositionID)
                if PositionID == 1:
                    FD1 = [99.343, 317.905]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [185.343,  317.905]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                elif PositionID == 2:
                    FD1 = [51.535, 87.989]
                    FD2 = [173.347, 77.957]
                    FD3 = [131.535, 87.989]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD1[0])/2,(FD3[1]+FD1[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0; 
            if comp_type == 'module':
            #print("PositionID", PositionID)
                if PositionID == 1:
                    FD1 = [99.343, 326.185]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [185.343,  326.185]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                elif PositionID == 2:
                    FD1 = [51.535, 79.709]
                    FD2 = [173.347, 77.957]
                    FD3 = [131.535, 79.709]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD1[0])/2,(FD3[1]+FD1[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0; 
                
                
        elif Shape == 'Five':
            #print("PositionID", PositionID)
            if comp_type == 'module':
                if PositionID == 1:
                    FD1 = [99.333, 298.179]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [185.333,  298.179]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                elif PositionID == 2:
                    FD1 = [131.532, 107.714]
                    FD2 = [173.347, 77.957]
                    FD3 = [51.532, 107.714]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD1[0])/2,(FD3[1]+FD1[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0; 
            if comp_type == 'protomodule':
                if PositionID == 1:
                    FD1 = [99.333, 298.179]
                    FD2 = [56.8430, 329.8903]
                    FD3 = [185.333,  298.179]
                    FD4 = [227.8285, 329.8903]
                    FD5 = [227.8285, 265.8737]
                    FD6 = [142.333, 230.87]
                elif PositionID == 2:
                    FD1 = [131.532, 107.714]
                    FD2 = [173.347, 77.957]
                    FD3 = [51.532, 107.714]
                    FD4 = [10.370, 77.957]
                    FD5 = [10.370, 137.957]
                    FD6 = [91.532, 180]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/4,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/4]
                #FDC = [(FD1[0]+FD2[0]+FD3[0]+FD4[0]+FD5[0]+FD6[0])/6,(FD1[1]+FD2[1]+FD3[1]+FD4[1]+FD5[1]+FD6[1])/6]
                FDC = [(FD3[0]+FD1[0])/2,(FD3[1]+FD1[1])/2]
                if PositionID == 1:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0;
                if PositionID == 2:
                    AdjustmentsX = 0;
                    AdjustmentsY = 0; 
                
                
                
                
    #print(FDC)
    
    #print(FD3, FD6)

    #Apply X&Y Offsets
    FDC_A = [FDC[0] + OffsetX + AdjustmentsX, FDC[1] + OffsetY + AdjustmentsY]
    FD1_A = [FD1[0] + OffsetX + AdjustmentsX, FD1[1] + OffsetY + AdjustmentsY]
    FD2_A = [FD2[0] + OffsetX + AdjustmentsX, FD2[1] + OffsetY + AdjustmentsY]
    FD3_A = [FD3[0] + OffsetX + AdjustmentsX, FD3[1] + OffsetY + AdjustmentsY]
    FD4_A = [FD4[0] + OffsetX + AdjustmentsX, FD4[1] + OffsetY + AdjustmentsY]
    FD5_A = [FD5[0] + OffsetX + AdjustmentsX, FD5[1] + OffsetY + AdjustmentsY]
    FD6_A = [FD6[0] + OffsetX + AdjustmentsX, FD6[1] + OffsetY + AdjustmentsY]
    
    #Apply Theta Offset
    
    FD1_B = [FD1_A[0] - FDC_A[0], FD1_A[1] - FDC_A[1]]
    FD2_B = [FD2_A[0] - FDC_A[0], FD2_A[1] - FDC_A[1]]
    FD3_B = [FD3_A[0] - FDC_A[0], FD3_A[1] - FDC_A[1]]
    FD4_B = [FD4_A[0] - FDC_A[0], FD4_A[1] - FDC_A[1]]
    FD5_B = [FD5_A[0] - FDC_A[0], FD5_A[1] - FDC_A[1]]
    FD6_B = [FD6_A[0] - FDC_A[0], FD6_A[1] - FDC_A[1]]
    
    #print("STEP2: HD Bottom", FD1_B, FD3_B)
    
    FD1_C = np.arctan2(FD1_B[1], FD1_B[0])
    FD2_C = np.arctan2(FD2_B[1], FD2_B[0])
    FD3_C = np.arctan2(FD3_B[1], FD3_B[0])
    FD4_C = np.arctan2(FD4_B[1], FD4_B[0])
    FD5_C = np.arctan2(FD5_B[1], FD5_B[0])
    FD6_C = np.arctan2(FD6_B[1], FD6_B[0])
    
    FD1_D = np.sqrt((FD1_B[1]**2 + FD1_B[0]**2))
    FD2_D = np.sqrt((FD2_B[1]**2 + FD2_B[0]**2))
    FD3_D = np.sqrt((FD3_B[1]**2 + FD3_B[0]**2))
    FD4_D = np.sqrt((FD4_B[1]**2 + FD4_B[0]**2))
    FD5_D = np.sqrt((FD5_B[1]**2 + FD5_B[0]**2))
    FD6_D = np.sqrt((FD6_B[1]**2 + FD6_B[0]**2))
    
    FD1_E = (180/np.pi)*FD1_C
    FD2_E = (180/np.pi)*FD2_C
    FD3_E = (180/np.pi)*FD3_C
    FD4_E = (180/np.pi)*FD4_C
    FD5_E = (180/np.pi)*FD5_C
    FD6_E = (180/np.pi)*FD6_C
    
    FD1_F = AngleOffset + FD1_E
    FD2_F = AngleOffset + FD2_E
    FD3_F = AngleOffset + FD3_E
    FD4_F = AngleOffset + FD4_E
    FD5_F = AngleOffset + FD5_E
    FD6_F = AngleOffset + FD6_E
    
    FD1_G = FD1_F*(np.pi/180)
    FD2_G = FD2_F*(np.pi/180)
    FD3_G = FD3_F*(np.pi/180)
    FD4_G = FD4_F*(np.pi/180)
    FD5_G = FD5_F*(np.pi/180)
    FD6_G = FD6_F*(np.pi/180)
    
    
    
    FD1_H = [np.cos(FD1_G)*FD1_D, np.sin(FD1_G)*FD1_D]
    FD2_H = [np.cos(FD2_G)*FD2_D, np.sin(FD2_G)*FD2_D]
    FD3_H = [np.cos(FD3_G)*FD3_D, np.sin(FD3_G)*FD3_D]
    FD4_H = [np.cos(FD4_G)*FD4_D, np.sin(FD4_G)*FD4_D]
    FD5_H = [np.cos(FD5_G)*FD5_D, np.sin(FD5_G)*FD5_D]
    FD6_H = [np.cos(FD6_G)*FD6_D, np.sin(FD6_G)*FD6_D]
    
   
    """
    print(FD1_B)#, FD2_B, FD3_B, FD4_B)
    print(FD1_H)#, FD2_H, FD3_H, FD4_H)
    print()
    print(FD2_B)#, FD2_B, FD3_B, FD4_B)
    print(FD2_H)#, FD2_H, FD3_H, FD4_H)
    print()
    print(FD3_B)#, FD2_B, FD3_B, FD4_B)
    print(FD3_H)#, FD2_H, FD3_H, FD4_H)
    print()
    print(FD4_B)#, FD2_B, FD3_B, FD4_B)
    print(FD4_H)#, FD2_H, FD3_H, FD4_H)
    print()
    """
    
    FD1_I = [FD1_H[0] + FDC_A[0], FD1_H[1] + FDC_A[1]]
    FD2_I = [FD2_H[0] + FDC_A[0], FD2_H[1] + FDC_A[1]] 
    FD3_I = [FD3_H[0] + FDC_A[0], FD3_H[1] + FDC_A[1]]
    FD4_I = [FD4_H[0] + FDC_A[0], FD4_H[1] + FDC_A[1]]
    FD5_I = [FD5_H[0] + FDC_A[0], FD5_H[1] + FDC_A[1]]
    FD6_I = [FD6_H[0] + FDC_A[0], FD6_H[1] + FDC_A[1]]
    
    #print("STEP3: HD Bottom", FD1_I , FD3_I)
    
    #print()
    #print("FDC vs FDC after translation:")
    #print(FDC, [(FD3_I[0]+FD1_I[0])/2,(FD3_I[1]+FD1_I[1])/2])
    #print(
    #print("trasnlated FDC vs translated FDC after rotation:")
    #print([(FD3_B[0]+FD1_B[0])/2,(FD3_B[1]+FD1_B[1])/2], [(FD3_H[0]+FD1_H[0])/2,(FD3_H[1]+FD1_H[1])/2])
    #print()
    
    FD1X, FD1Y = FD1_I
    FD2X, FD2Y = FD2_I
    FD3X, FD3Y = FD3_I
    FD4X, FD4Y = FD4_I
    FD5X, FD5Y = FD5_I
    FD6X, FD6Y = FD6_I
    
    #print("This is OG FDC: ", FDC)
    #print(FD3_I, FD6_I)
    return FD1X, FD2X, FD3X, FD4X, FD5X, FD6X, FD1Y, FD2Y, FD3Y, FD4Y, FD5Y, FD6Y
    #print('OG: ', FD1X, FD2X, FD3X, FD4X, FD1Y, FD2Y, FD3Y, FD4Y)
    
    
    
    
#reverse_offsets(0, 0, 0, 1, 1)