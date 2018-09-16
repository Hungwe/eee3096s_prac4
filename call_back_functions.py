
#CALL BACK FUNCTIONS
##################################################################################
def my_callback(push1): #Reset
    print("reset1")
    #set timer to zero
    global clear_reset

    clear_reset = True

    #clear screne
    print("\n"*50)
 

def my_callback1(push2): # frequency
    print("reset2")
    global count
    global frequ
    
    count+=1
    
    if count > 3:
        count = 1

    if count ==1: # default frequency 
        frequ = 0.5

    elif count ==2: #frequecy
        frequ =1

    elif count ==3:
        frequ = 2

    
        

def my_callback2(push3): #stop swich
    print("stop switch pressed")
    global stop_pressed
    global play
    if stop_pressed == True:
        #print the latest 5 readings
        play = True
        stop_pressed = False
        
    else:
        #stop srinting
        play = False
        stop_pressed = True 

        
        
    
def my_callback3(push4): # display switch
    # check if stop swich was pressed
    print(" button 4 was pressed")

    #END OF CALL BACK FUNCTIONS
############################################################################################
