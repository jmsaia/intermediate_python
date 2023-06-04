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

        # get rid of the toolbar for graph

        plt.rcParams['toolbar'] = 'None'
        
        # create line graph
        
        data_set.plot(kind ='line',figsize = (7,3), grid = True,
                      title = "John Saia", 
                      ylabel = "PRICE")
        
        plt.locator_params(axis='x', nbins=5)

        # for better figure representation

        plt.tight_layout()

        # save file as a .jpg
        
        plt.savefig('Proj09.jpg')

        # show graph in a window

        plt.show()

    #end run function
#end class Runner