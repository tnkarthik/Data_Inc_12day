def plot_df(df):
    
    from bokeh.charts import TimeSeries
    from bokeh.io import save, output_file
    output_file('templates/stock_price.html')
    
    colnames = list(df.columns)
    colnames.remove('date')
    #colnames.remove('ticker')
    
    p = TimeSeries(df, x = 'date', y = colnames, color = colnames, dash = colnames, title = 'Stock Price plot' , ylabel = 'Stock Prices', legend = True)
    save(p)
    #return ('stock_price.html')