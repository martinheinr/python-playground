fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.units import inch

report = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
#report.build([report_title])

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

print(table_data)

report_table = Table(data=table_data)
report.build([report_title, report_table])

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
#report.build([report_title, report_table])

report_pie = Pie(width=5*inch, height=5*inch)

report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

drawing = Drawing()
drawing.add(report_pie)

print(report_pie.data)
# output: [2, 5, 8, 3, 1, 1, 13]
print(report_pie.labels)
# output: ['apples', 'bananas', 'cherries', 'durians', 'elderberries', 'figs', 'grapes']

report.build([report_title, report_table, drawing])