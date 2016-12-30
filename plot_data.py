import requests 
import simplejson as json
import pandas as pd

def get_data(ticker='GOOG',date_end = '20161229',date_begin = '20161129'):
    
    ## Define the parameters to be passed to the query
    quandl_params = {'ticker': ticker, 'date.gte': date_begin, 'date.lte': date_end, 'api_key' : 'ruZerKYm8E-LFEPjXM_8'}
    
    ## Send data query
    r = requests.get('https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json', params = quandl_params)
    
    ## Check if data query was successful
    assert r.status_code == requests.codes.ok

    ## Parse the JSON data and store it in dictionary data. n_row and n_col are num of rows and columns of the final data frame
    r_text = json.loads(r.text)
    n_col = len(r_text['datatable']['columns'])
    colnames = [str(r_text['datatable']['columns'][i]['name']) for i in range(n_col)]

    data = r_text['datatable']['data']
    n_row = len(data)

    ## Store the data in pandas data frame df

    df = pd.DataFrame(data, columns = colnames)
    
    return df

def plot_df(df, colnames):
    from bokeh.charts import TimeSeries, show, output_file
    output_file('stock_price.html')
    p = TimeSeries(df, x = 'date', y = colnames, color = colnames, dash = colnames, \
                   title = 'Stock Price plot' , ylabel = 'Stock Prices', legend = True)
    show(p)
    return ('stock_price.html')
    