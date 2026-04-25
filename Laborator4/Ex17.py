import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

def convert_finante(valoare_text):
    if isinstance(valoare_text, str):
        valoare_text = valoare_text.replace('€', '')
        if 'M' in valoare_text:
            return float(valoare_text.replace('M', '')) * 1000000
        elif 'K' in valoare_text:
            return float(valoare_text.replace('K', '')) * 1000
    return 0.0

df = pd.read_csv('data.csv')

df_bokeh = df.head(500).copy()
df_bokeh['Wage_num'] = df_bokeh['Wage'].apply(convert_finante)
df_bokeh['Value_num'] = df_bokeh['Value'].apply(convert_finante)

source = ColumnDataSource(df_bokeh)

p = figure(title="Interactiune Cursor", x_axis_label='Wage', y_axis_label='Value')

p.circle('Wage_num', 'Value_num', size=10, source=source)

hover = HoverTool(tooltips=[("Jucator", "@Name"), ("Club", "@Club"), ("Overall", "@Overall")])
p.add_tools(hover)

output_file("interactiv.html")
show(p)