# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 19:40:36 2016

@author: shikh
"""
total_rows = 12
total_columns = 22
total_generations = 10
init_generation = 0

def make_grid():  
    """Extracts the original configuration of life and death from the given file and puts it on a list"""      
    grid = []
    for i in range(total_rows):
        grid.append([' ' for c in range(total_columns)])
    f = open("life.txt")
    file_row_number = 1    
    for line in f:  
        for elem_num in range(len(line)):
            if line[elem_num] != '\n':
                 grid[file_row_number][elem_num+1] = line[elem_num]
            else:
                 grid[file_row_number][elem_num+1] = ' '
        file_row_number += 1
    f.close()
    return grid
            
def print_grid(grid):
    """Formats the grid before printing it so it looks more clean"""
    for row in grid:
        print(row)
    print('\n')
    
def check_neighbors(grid, row_num, element_num):
    """Checks neighbors if live or dead"""
    count = 0
    if grid[row_num-1][element_num] == '*':
        count +=1
    if grid[row_num][element_num-1] == '*':
        count +=1
    if grid[row_num-1][element_num-1] == '*':
        count +=1
    if grid[row_num+1][element_num-1] == '*':
        count +=1
    if grid[row_num-1][element_num+1] == '*':
        count +=1
    if grid[row_num+1][element_num+1] == '*':
        count +=1
    if grid[row_num+1][element_num] == '*':
        count +=1
    if grid[row_num][element_num+1] == '*':
        count +=1
    return count
    
def change_grid(grid):
    """Kills or revives elements depending on number of neighbors recieved from check_neighbors()"""
    temp_grid = [row[:] for row in grid] 
    for row_num in range(1,len(grid) - 1): #to skip the extra blank gird elements 
        for element_num in range(1, len(grid[row_num]) - 1):
            live_neighbors = check_neighbors(grid, row_num, element_num)
            if live_neighbors < 2:
                temp_grid[row_num][element_num] = ' '
            elif live_neighbors >3:
                temp_grid[row_num][element_num] = ' '
            elif live_neighbors == 3:
                temp_grid[row_num][element_num] = '*'
    return temp_grid
    
def write_grid(grid, generation_num):
    """Writes the grid to a file after formatting it in the required format"""
    try:
        f = open("Output_HW01_Shikhar.txt", 'a')
    except:
        f = open("Output_HW01_Shikhar.txt", 'w')
    f.write('='*20 + '\n' + "Generation " + str(generation_num)+'\n')
    for row_num in range(1, len(grid)-1): #To skip the extra row at the beginning and end of the grids
        for c in range(1, len(grid[row_num])-1): #To skip the extra column at the beginning and end of the grids
            if grid[row_num][c]!='*':
                f.write('-') #To swap the spaces (' ') with '-'
            else:
                f.write(grid[row_num][c])
        f.write('\n')
    f.write('\n')
    f.close()
    
    
def main():
    """Calling all the functions in the required order. 
       Uncomment the comments to see the grids print on the output screen"""
    grid = make_grid() 
    #print_grid(grid)
    write_grid(grid, init_generation) 
    for i in range(total_generations):
        #print_grid(grid)
        grid = change_grid(grid)
        write_grid(grid, i+1)
        
        
if __name__ == "__main__":
    main()
        
        
    
            
                    
                
                
    