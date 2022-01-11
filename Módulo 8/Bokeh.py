import bokeh
from bokeh.io import show, output_notebook
from bokeh.palettes import Spectral6
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
# from bokeh.palettes import Spectra16

output_notebook()

# output_file("Bokeh-Grafico-Interativo.html")
# p = figure()

# print(type(p))
# p.line([1,2,3,4,5], [6,7,2,4,5], line_width = 2)
# show(p)

# output_file("Bokeh-Frafico-Barras.html")
# fruits = ['Maça', 'Peras', 'Tangerinas', 'Uvas', 'Melancias', 'Morangos']
# counts = [5,3,4,2,4,6]

# source = ColumnDataSource(data = dict(fruits=fruits, counts=counts))

# p = figure(x_range=fruits, plot_height=350, toolbar_location=None, title="Contagem de Frutas")
# p.vbar(x='fruits', top='counts', source=source, legend='fruits', line_color='white', fill_color=factor_cmap('fruits', palette=Spectral6, factors=fruits))
# p.xgrid.grid_line_color = None
# p.y_range.start = 0
# p.y_range.end = 9
# p.legend.orientation = 'horizontal'
# p.legend.location = 'top_center'

# show(p)

from bokeh.sampledata.iris import flowers

# colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
# colors = [colormap[x] for x in flowers['species']]

# p = figure(title='Iris Morphology')
# p.xaxis.axis_label = 'Petal Lenght'
# p.yaxis.axis_label = 'Petal Width'
# p.circle(flowers['petal_length'], flowers['petal_width'], color=colors, fill_alpha=0.2, size=10)

# output_file('Bokeh_grafico_iris.html', title='iris.py example')
# show(p)

output_file('Bokeh-Grafico-CIrculos.html')
p = figure(plot_width = 400, plot_height = 400)
p.circle([1,2,3,4,5], [6,7,2,4,5], size = 20, color = 'navy', alpha = 0.5)

show(p)
