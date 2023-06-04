# create Runner class
class Runner():
    
    # create run definition in Runner class
    
    def run(args):
        print('I certify that this program is my own work')
        print('and is not the work of others. I agree not')
        print('to share my solution with others.')
        print('John Saia')
        
        # import needed libraries

        import pandas as pd
        import matplotlib.pyplot as plt

        # read in csv file
        data = pd.read_csv(args[0], index_col = args[1])
        
        # access needed rows and columns
        
        data_set = data.loc[args[2]:args[3], args[4]:args[5]]
        
        # transpose to swap axes from Proj09 code starter
        
        data_set = data_set.transpose()
        
        # create line graph
        
        data_set.plot(kind ='line',figsize = (7,3),
                      title = "John Saia",
                      xticks = range(0,len(data_set.index)),
                      ylabel = "Value",
                      xlabel = "Category")

        # for better figure representation

        plt.tight_layout()

        # show graph in a window

        plt.show()

    #end run function
#end class Runner