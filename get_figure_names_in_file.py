# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 18:02:25 2022

@author: Patrick
"""

from typing import List

PATH = r"FILEPATH"

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
    with open(path, "r") as file:
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
    return figure_list
    
def save_figure_list_to_txt(figure_list:List[str]) -> None:
    '''Takes a list of figures and and saves them as a txt file'''
    with open('list_of_figures.txt', "w") as f:
        for line in figure_list:
            f.write(f"{line}\n")
    
        
def main():
    figure_list = []
    filenames = ["file1",
                 'file2']
    tex_list =  [f'\\{name}.tex' for name in filenames]
    for file in tex_list:
        figure_list.extend(get_figure_name_from_tex(PATH + file))
    save_figure_list_to_txt(figure_list)
    
if __name__ == "__main__":
    main()
