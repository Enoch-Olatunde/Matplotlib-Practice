#Matplotlib Practice - Enoch

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('default') # You can also use 'seaborn' , 'ggplot'

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

plt.figure(figsize=(10, 6))

plt.plot(x,y1, label='sin(x)')
plt.plot(x,y2, label='cos(x)')
plt.plot(x,y3, label='sin(x) * cos(x)' , color='darkgreen', linestyle='--', linewidth=2)

plt.xlabel('x')
plt.ylabel('y')

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Plots Practice", fontsize=14, fontweight='bold')
plt.legend() # Show Legend
plt.grid(True, alpha=0.3) # Alpha controls transparency

# Save the figure
# Common formats: PNG (raster), PDF (vector), SVG (vector), EPS (vector)
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
plt.savefig('my_plot.pdf', bbox_inches='tight') # Vector format

plt.show()
