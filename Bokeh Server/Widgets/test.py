import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.models.widgets import CheckboxGroup
from bokeh.plotting import figure

# create the color palettes (from https://github.com/bokeh/bokeh/blob/master/bokeh/palettes.py)
Category20_20 = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a',
                '#d62728', '#ff9896', '#9467bd', '#c5b0d5','#8c564b', '#c49c94', 
                '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d', 
                '#17becf', '#9edae5']
Category20_12 = Category20_20[:12]




def create_claims_by_desc_hbar(main_df):
    """
    Create a horizontal bar graph showing which type of claims are handled most often
    """

    claim_type_series = main_df['Short Desc.'].groupby(main_df['Short Desc.']).count()
    claim_type_df = pd.Series(claim_type_series).reset_index(name = 'Count').rename(columns={'Short Desc.': 'Type'})
    claim_type_df = claim_type_df.sort_values(by='Count',ascending=True)

    shorten_types_names(claim_type_df)

    # create a data source
    claim_type_source = ColumnDataSource(data = dict(types = list(claim_type_df['Type']),
                                                counts = list(claim_type_df['Count']),
                                                color = Category20_12))
    claim_type_hover = [("Type" , "@types"), ("Count", "@counts Claims")]

    # create the figure for the 
    claim_type_chart = figure(y_range = list(claim_type_df['Type']), plot_width = 650, plot_height = 650,x_range=(0, 1200),
                          tooltips = claim_type_hover, title = 'Number Of Claims Handled Per Type',
                          tools = ["pan,wheel_zoom,box_zoom,reset"])

    # create the vertical bar glyphs
    claim_type_chart.hbar(y = 'types',
                     right = 'counts',
                     height = 0.9,
                     source = claim_type_source)

    def update_data_source(types_list, counts_list, colours_list):
        return ColumnDataSource(data = dict(
            types = types_list,
            counts = counts_list,
            color = colours_list
        ))

    def create_check_boxes(types_list):
        return CheckboxGroup(
            labels = types_list,
            active = [0, 3])
    
    


    claim_type_chart.ygrid.grid_line_color = None
    claim_type_chart.toolbar.logo = None
    claim_type_chart.outline_line_color = None

    return claim_type_chart

def shorten_types_names(df):
    """
    Shorten the names of some of the claim types :

    * Injury Claim (WCA, PA, STATED BENEFITS ETC) \n
    * Liability (Professional Indemnity, general liability) \n
    * Money and Fedility Claim (money, airtime,cheques ets) \n
    """
    if df.loc[7, 'Type'] == 'Injury Claim (WCA, PA, STATED BENEFITS ETC)':
        df.loc[7, 'Type'] = 'Injury Claim'
    
    if df.loc[8, 'Type'] == 'Liability (Professional Indemnity, general liability)':
        df.loc[8, 'Type'] = 'Liability Claim'
    
    if df.loc[9, 'Type'] == 'Money and Fedility Claim (money, airtime,cheques ets)':
        df.loc[9, 'Type'] = 'Money and Fedility Claim'
    
    return df