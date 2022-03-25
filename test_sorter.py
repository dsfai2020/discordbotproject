from copy import error
from numpy import int32, int64
import pandas
import json
import pytest

#getcsv is a df object.  You don't need to put getcsv into another dataframe.
getcsv=pandas.read_csv("my_csv.csv")

def test_dftype():
    assert type(getcsv)==pandas.core.frame.DataFrame, f"{type(getcsv)} Wasnt a pandas.core.frame.DataFrame"
    
def test_contents():
    #This will show all the types within the dataframe
    print(getcsv.dtypes)

    #visually verify. Int64 won't work correctly with sort_values.
    print(f"Here are the values.. {getcsv['Kills'].values.dtype}")
    assert str(getcsv['Kills'].values.dtype)!= 'int32', 'The data types are already int32'
    
    #convert the column from getcsv['Kills'] into an int.  Int32 is what your looking for.
    getcsv['Kills']=getcsv['Kills'].astype(int)
    print(getcsv.dtypes)
    #This is what the bot will output to the discord channel.  A sorted kill chart.
    print(f"Sorting...{getcsv['Kills'].sort_values()}")
    
    #Since we can reference the dtypes.  Let's just make sure that int32 is in there.  Just viewing the str makes the test easier since I just want to verify that the field is entered.
    assert str(getcsv['Kills'].dtypes)== 'int32', "Did not equal int32"


   
