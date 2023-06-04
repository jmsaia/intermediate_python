# create Runner class
class Runner():
    
    # create run definition in Runner class
    
    def run(args):

        # import needed libraries

        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        # certification print

        print('I certify that this program is my own work')
        print('and is not the work of others. I agree not')
        print('to share my solution with others.')
        print('John Saia')

        # read csv file into a Dataframe variable, covert date to datetime for sorting

        data = pd.read_csv(args[0])

        data['Date'] = pd.to_datetime(data['Date'])

        # rename column headers, Pulse should be renamed as well based on examples

        data_re = data.rename({'Systolic (mmHg)':'Syst', 'Diastolic (mmHg)':'Dias', 'Pulse (bpm)':'Pulse'}, axis = 1)

        # use groupby to get the mean of duplicate dates

        data_g = data_re.groupby(['Date']).mean()

        # get the mean of the dataset

        data_mean_uni = data_g.mean()

        # counts unique dates out of the data set.

        uni_rows = len(data_g)

        # sort index in descending order since groupby made it ascending

        data_g = data_g.sort_index(ascending = False)

        # limit to row count

        data_sp = data_g.iloc[0:int(args[1]),:]

        # get the mininum and maximum of all columns

        data_min = data_sp.min().min()
        data_max = data_sp.max().max()

        # get the mean of the spliced data

        data_sp_mean = data_sp.mean()

        # convert index into a string

        x_tl = [x.strftime("%Y-%m-%d") for x in data_sp.index]

        # reset index, add string date, set string index, sort based on datetime index, drop datetime date as it is not needed

        data_n = data_sp.reset_index()
        data_n['Date2'] = x_tl
        data_n = data_n.set_index('Date2')
        data_n = data_n.sort_values('Date')
        data_n = data_n.drop(columns=['Date'])

        # graph creation and formatting

        data_n.plot(grid = True,
            ylabel = 'Value',
            title = "John Saia",
            yticks = np.arange(data_min, data_max+1, 10),
            xticks = np.arange(0,int(args[1]),10))
        
        plt.xticks(rotation = 90)
        plt.legend(loc="center left")
        plt.xlabel('Date')
        plt.savefig(f'Proj12-{args[1]}.jpg', bbox_inches='tight')

        print('\nCollapse the data into unique rows')
        print(f'Number of unique rows: {uni_rows}')
        print('Mean values for columns of interest in unique rows')
        print(data_mean_uni,'\n')

        print(f'Number of rows to plot: {args[1]}')
        print(f'Minimum data value in rows to plot: {data_min}')
        print(f'Maximum data value in rows to plot: {data_max}\n')

        print('Mean values for columns of interest in rows to plot')
        print(data_sp_mean,'\n')

        print('Plot the data and write output image file.')
        print(f'Output file name: Proj12-{args[1]}.jpg')

    #end run function
#end class Runner