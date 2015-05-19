#! needed libraries
import matplotlib.pyplot as plt
import time
import csv
from components.classtools import AttrDisplay


# define two main classes this petit program will use later.
class Center_Village(AttrDisplay):
    '''
    This class defines center village which creates center village instance.
    '''
    def __init__(self, ID, admin, name:str, check, X, Y):
        '''
        Meaning of arguments:
        ID -- object id
        admin -- the administrative village where this very instance village belongs to
        name -- the name of village
        check -- mark whether a village is hollow or center
        X & Y -- geographical coordinates represented as a tuple type      
        '''
        self.ID = ID
        self.admin = admin
        self.name = name
        self.cord = (float(X), float(Y))
        self.check = check
        

    def mass_calculate(self):
        '''
        This method calculates the the mass factor of the center village
        k, p, q are weights. 
        '''
        k = 0.004
        p = 0.5
        q = 0.5
        # need more work here
        self.mass = 1
        return self.mass   
                
   
class Hollow_Village(Center_Village):
    '''
    This class defines hollow village which creates hollow village instance
    '''
    def mass_calculate(self):
        '''
        This method calculates the the mass factor of the hollow village
        k, p, q are weights. 
        '''
        k = 1
        p = 1
        q = 1
        self.mass = 1
        return self.mass
    
        

# module level functions
def opener():
    '''
    Control the outer file IO when the draw method starts: open file
    '''
    global data
    data = open(r'J:\VillageMerger\Data\villages.csv')
    

def closer():
    '''
    Control the outer file IO when the draw method ends: close file
    '''
    global data
    data.close()
    

def data_reader(data, choice: 'H or C'):
    '''
    This function read hollow and center village data out of certain file
    The choice filter can decide whether collect hollow or centers
    '''
    hollows = []
    centers = []
    flag = choice
    res = None
    collector = csv.reader(data, delimiter=',', skipinitialspace=True)
    for row in collector:
        if row[3] == '0':
            hollows.append(row)
        elif row[3] == '3':
            centers.append(row)
    if flag == 'H':
        res = hollows
    elif flag == 'C':
        res = centers
    return res



def distance(insH, insC):
    '''
    This function calculates phisical distance between two village points
    insH - class Hollow_Village object
    insC - class Center_Village object
    '''
    cordH = insH.cord
    cordC = insC.cord
    # This method might have some proble, check later before May 24th.
    H = complex(cordH[0], cordH[1])
    C = complex(cordC[0], cordC[1])
    return abs(H - C)



def gravity(insH, insC):# this algorithm would be replaced with more advanced aproach later
    '''
    This function calculates 
    insH - class Hollow_Village object
    insC - class Center_Village object
    '''
    mH = insH.mass_calculate()
    mC = insC.mass_calculate()
    gravity = mH * mC / (distance(insH, insC) ** 2)
    return gravity    


def drag_X(cord):
    return cord[0]

def drag_Y(cord):
    return cord[1]

# have to make clear the mechanism of opener and closer in this function
def draw_background():
    '''
    This function plots all those center villages and hollow villages as a background map
    Then the lines could be drawn between them
    '''
    opener()
    hollows = data_reader(data, 'H')
    hollow_list = []
    for vilas in hollows:        
        args = tuple(vilas)
        h = Hollow_Village(*args)
        h.mass_calculate() # this step will be replaced also, before June
        hollow_list.append(h.cord)
    closer()
        
    opener()
    centers = data_reader(data, 'C')
    center_list = []
    for vilas in centers:        
        args = tuple(vilas)
        c = Center_Village(*args)
        c.mass_calculate()
        center_list.append(c.cord)
    
    plt.plot(list(map(drag_X, center_list)), list(map(drag_Y, center_list)), 'ro')    
    plt.plot(list(map(drag_X, hollow_list)), list(map(drag_Y, hollow_list)), 'k.')     
    
    plt.axis('scaled');plt.axis('off')
    closer()



def pick_lines(keyword: 'H, C or L' = "L"):
    '''
    This function picks the connective lines that show how hollow villages shoulb be merged into
    center villages
    '''
    flag = keyword
    opener()
    hollow_ins = data_reader(data, 'H')
    hollow_assembly = []
    for obj in hollow_ins:        
        args = tuple(obj)
        hi = Hollow_Village(*args)
        hi.mass_calculate()
        hollow_assembly.append(hi)
    closer()
    # close the file and then reopen it for reading centers
    opener()
    center_ins = data_reader(data, 'C')
    center_assembly = []
    for obj in center_ins:        
        args = tuple(obj)
        ci = Center_Village(*args)
        ci.mass_calculate()
        center_assembly.append(ci)
    closer()
    
    # In the nested loop below, i for hollow villages and j for center villages.
    # Now compair in permutations: first decide if two(hollow and center) are in same administrative
    # village, if so, then calculate their general distance and save into a dictionary for further op-
    # -eration.
    # Pay attention to the additionaly created 'inversed' dict, it's for finding the min value's key
    # later to append the pair of shortest distance in linelist.
    
    linelist = []
    for i in hollow_assembly:
        record = {}
        inversed = {}
        for j in center_assembly:            
            if i.admin != '' and j.admin != '':
                if i.admin == j.admin:
                    record[i.ID + '->' + j.ID] = distance(i, j)
                    inversed[str(distance(i, j))+i.ID] = (i.ID + '->' + j.ID)
                             
        if record != {}:
            if max(record.values()) != 0:             
                temp = inversed[str(min(record.values()))+i.ID]
                linelist.append(temp)

    if flag == 'L':
        out = linelist
    elif flag == 'H':
        out = hollow_assembly
    elif flag == 'C':
        out = center_assembly
    return out
    


def draw_line(H, C, L):
    '''
    This function draw lines that indicates which village should be merged to which
    '''
    hollows = H
    centers = C
    goods = L
    for item in goods:
        # v0 represent hollow village point and v1 represent center village point
        v0_ID = item.split('->')[0]
        v1_ID = item.split('->')[1]
        
        # print(v0_ID, v1_ID)
        for h in hollows:
            if h.ID == v0_ID:
                v0 = h.cord
        for c in centers:
            if c.ID == v1_ID:
                v1 = c.cord
        plt.plot([v0[0], v1[0]], [v0[1], v1[1]], 'k-')          
            
            
# self test
if __name__ == '__main__':
    t1 = time.time()
    H = pick_lines(keyword='H')
    C = pick_lines(keyword='C')
    L = pick_lines(keyword='L')
    
    print('H', len(H))
    print('C', len(C))
    print('L', len(L))

    draw_line(H, C, L)
    draw_background()
    t2 = time.time()
    plt.show()
    
    t = t2-t1
    print(t)
    





