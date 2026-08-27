from datascience import *
import numpy as np

def correctness_check_1_1_a(a):
    try:
        return a == 2
    except Exception:
        return False

def correctness_check_1_1_b(b):
    try:
        return b == 5
    except Exception:
        return False

def correctness_check_1_1_c(c):
    try:
        return c == 3
    except Exception:
        return False

def correctness_check_2_1(characters_q1):
    try:
        return characters_q1 == 2
    except Exception:
        return False

def correctness_check_2_2(characters_q2):
    try:
        return characters_q2 == 1
    except Exception:
        return False    

def correctness_check_3_1(names_q1):
    try:
        return names_q1 == 2
    except Exception:
        return False     

def correctness_check_3_2(names_q2):
    try:
        return names_q2 == 4
    except Exception:
        return False     

def correctness_check_3_3(names_q3):
    try:
        return names_q3 == 2
    except Exception:
        return False     

def correctness_check_4_1(biggest_change):
    try:
        return biggest_change == (max(abs(17 - 28), abs(49 - 67), abs(113 - 56)))
    except Exception:
        return False     

def correctness_check_4_2(smallest_change_major):
    try:
        return smallest_change_major == 1
    except Exception:
        return False          

def correctness_check_4_3_a(gws_relative_change):
    try:
        return gws_relative_change >= 64 and gws_relative_change <= 66
    except Exception:
        return False

def correctness_check_4_3_b(linguistics_relative_change):
    try:
        return linguistics_relative_change >= 36 and linguistics_relative_change <= 38
    except Exception:
        return False 

def correctness_check_4_3_c(rhetoric_relative_change):
    try:
        return rhetoric_relative_change >= 50 and rhetoric_relative_change <= 52
    except Exception:
        return False   

def correctness_check_4_4(biggest_rel_change_major):
    try:
        return biggest_rel_change_major == 1
    except Exception:
        return False   

def correctness_check_5_1(study_type):
    try:
        return study_type == 1
    except Exception:
        return False 

def correctness_check_5_2(myopia_statement):
    try:
        return myopia_statement == 2
    except Exception:
        return False    

def correctness_check_5_3(causation_answer):
    try:
        return causation_answer == 2
    except Exception:
        return False    

def correctness_check_5_4(myopia_factors):
    try:
        return myopia_factors == (1,2,3)
    except Exception:
        return False                     

def correctness_check_6_1(survivor_answer):
    try:
        return survivor_answer == 1
    except Exception:
        return False 

def correctness_check_7_1(contact):
    try:
        return contact == 3
    except Exception:
        return False            

def correctness_check_7_2(extension):
    try:
        return extension == 2
    except Exception:
        return False            

def correctness_check_7_3(regrade):
    try:
        return regrade == 2
    except Exception:
        return False     

def correctness_check_7_5(acceptable):
    try:
        return acceptable == 2
    except Exception:
        return False   

def correctness_check_7_6(drops):
    try:
        return drops == 2
    except Exception:
        return False   

def correctness_check_7_7(exams):
    try:
        return exams == 1
    except Exception:
        return False 

def correctness_check_7_8(secret):
    try:
        return secret == 1
    except Exception:
        return False     