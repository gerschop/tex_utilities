# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 18:02:25 2022

@author: Patrick
"""

from typing import List

PATH = r"G:\My Drive\Documents\Projects\2022_tex_figure_grabber"
FILE = "\\influence_inhomogeneity.tex"

def is_commented(line:str) -> bool:
    """Checks if line is commented or not"""
    if line[0] == "%":
        return True
    else:
        return False
    
def get_figure_name_from_line(line:str) -> str:
    '''Grabs the figure name between { and } from a long string'''
    return line[line.find("{") + 1 : line.rfind("}")]
    
def get_figure_name_from_tex(path:str) -> List[str]:
    '''Grabs a list of all figure names in a tex document'''
    figure_list = []
    with open(PATH+FILE, "r") as file:
        for line in file:
            line = line.strip() # remove spaces
            if len(line) == 0:
                continue
            if is_commented(line=line):
                continue
            if "\\input" in line or "\\includegraphics" in line:
                figure_name = get_figure_name_from_line(line=line)
                figure_list.append(figure_name)
    print(figure_list)
        
def main():
    get_figure_name_from_tex(PATH + FILE)
    
    
if __name__ == "__main__":
    main()
