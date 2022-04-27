def do_log(the_func):

    def wrapper(*values):
        print("log avant",values[-1])
        
        the_func(*values)
        print("log aprés")
    
    return wrapper