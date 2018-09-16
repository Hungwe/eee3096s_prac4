#constructs the timer string
def timer_str(hr_1 ,hr ,mins_1 ,mins ,sec_1 ,sec):
    
    timer_string = "{hr_1}{hr}:{mins_1}{mins}:{sec_1}{sec}".format(hr_1=hr_1,hr=hr,mins_1=mins_1,mins=mins,sec_1=sec_1,sec=sec)

    return timer_string


# constructs the time string
def time_string():

    time_start = time.time()
    real_time = time.localtime()
    hours = str(real_time.tm_hour)
    minutes = str(real_time.tm_min)
    secs = str(real_time.tm_sec)
    current = datetime.now()            
    tstring = hours+":"+minutes+":"+secs
    

    return tstring

def data_print():

    #tstring = time_string()
    CH5 = 5
    CH6 = 6
    CH7 = 7
    CH5_Data = GetData(CH5)
    CH5_Temp = ConvertTemp(CH5_Data,2)
    CH6_Data = GetData(CH6)
    CH6_Light = LightPercent(CH6_Data,0)
    CH7_Data = GetData(CH7)
    CH7_Pot = PotVolts(CH7_Data,0)
    CH6_string = str(int(CH6_Light))+"%"
    sys.stdout.flush()
    
    data =("{CH7_Pot}V  {CH5_Temp}C    {CH6_string}".format(CH7_Pot=CH7_Pot,CH5_Temp=CH5_Temp,CH6_string=CH6_string))
    return data
