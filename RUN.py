def RUN(x): #Run safely for LLMs
    try:
        return(x)
    except: 
        print("server overload")
        RUN(x)