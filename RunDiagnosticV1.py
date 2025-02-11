# -*- coding: utf-8 -*-
"""
AutoDB Run Diagnostic
    -By Paolo



#Don't forget the functions being called at the end of Programs. 


Created on Mon Feb  3 13:42:26 2025

@author: Admin
"""

import All_Shapes_VerificationTool_V2

def error_handling(Results, PMPassing, MPassing, name):
    if PMPassing[0] == [True]: 
        Results.append(f"{name} PM PASS")
        #Results.append(str(name))
    else: 
        Results.append('PM'+str(name))
        for error in PMPassing:
            Results.append(error)
    
    if MPassing[0] == [True]:
        Results.append(f"{name} M PASS")
        
    else: 
        Results.append('M'+str(name))
        for error in PMPassing:
            Results.append(error)
            
    return Results






def TestV1(T, X, Y):
    Results = [];
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LDF', False, T, X, Y, 1)
    Results = error_handling(Results, PMPassing, MPassing, 'LDF');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LDF', False, T, X, Y, 2)
    Results = error_handling(Results, PMPassing, MPassing, 'LDF');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('HDF', False, T, X, Y, 1)
    Results = error_handling(Results, PMPassing, MPassing, 'HDF');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('HDF', False, T, X, Y, 2)
    Results = error_handling(Results, PMPassing, MPassing, 'HDF');
    #PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('HDB', False, T, X, Y, 1)
    #Results = error_handling(Results, PMPassing, MPassing, 'HDB');
    #PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('HDB', False, T, X, Y, 2)
    #Results = error_handling(Results, PMPassing, MPassing, 'HDB');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LDL', False, T, X, Y, 1)
    Results = error_handling(Results, PMPassing, MPassing, 'LDL');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LDL', False, T, X, Y, 2)
    Results = error_handling(Results, PMPassing, MPassing, 'LDL');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LDR', False, T, X, Y, 1)
    Results = error_handling(Results, PMPassing, MPassing, 'LDR');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LDR', False, T, X, Y, 2)
    Results = error_handling(Results, PMPassing, MPassing, 'LDR');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LDT', False, T, X, Y, 1)
    Results = error_handling(Results, PMPassing, MPassing, 'LDT');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LDT', False, T, X, Y, 2)
    Results = error_handling(Results, PMPassing, MPassing, 'LDT');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LDB', False, T, X, Y, 1)
    Results = error_handling(Results, PMPassing, MPassing, 'LDB');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LDB', False, T, X, Y, 2)
    Results = error_handling(Results, PMPassing, MPassing, 'LDB');
    #PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('HDL', False, T, X, Y, 1)
    #Results = error_handling(Results, PMPassing, MPassing, 'HDL');
    #PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('HDL', False, T, X, Y, 2)
    #Results = error_handling(Results, PMPassing, MPassing, 'HDL');
    #PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('HDR', False, T, X, Y, 1)
    #Results = error_handling(Results, PMPassing, MPassing, 'HDR');
    #PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('HDR', False, T, X, Y, 2)
    #Results = error_handling(Results, PMPassing, MPassing, 'HDR');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('HDT', False, T, X, Y, 1)
    Results = error_handling(Results, PMPassing, MPassing, 'HDT');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('HDT', False, T, X, Y, 2)
    Results = error_handling(Results, PMPassing, MPassing, 'HDT');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LD5', False, T, X, Y, 1)
    Results = error_handling(Results, PMPassing, MPassing, 'LD5');
    PMPassing, MPassing = All_Shapes_VerificationTool_V2.Tests('LD5', False, T, X, Y, 2)
    Results = error_handling(Results, PMPassing, MPassing, 'LD5');


    #print(Results) 
    for result in Results:
        if result != [False]:
            print(result)
        

TestV1(0.5, -0.5, 0.75)





