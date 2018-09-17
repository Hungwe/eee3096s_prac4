 if sec>9:
                sec_1+=1
                #if (frequ == 1):
                    #
                print("{tstring} {timer_string} {data} ".format(tstring=tstring,timer_string=timer_string , data = data))
            
                if(frequ == 1):
                    if (sec_1%2 == 0):
                        print("{tstring} {timer_string} {data} ".format(tstring=tstring,timer_string=timer_string , data = data))
                if (frequ == 2):
                    if (time_laps%4 ==0):
                        print("{tstring} {timer_string} {data} ".format(tstring=tstring,timer_string=timer_string , data = data))
                sec=0
