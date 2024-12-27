# %%
import ultraplot as plt, numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib import patheffects  as pe

font = FontProperties(fname='./PermanentMarker-Regular.ttf')


fs = 38
left = 0.575
sw = 3
fig, ax = plt.subplots(figsize = (3, 1.25))
ax.text(left, 0.5, "Ultra",
    fontsize = fs,
    fontproperties = font,
    va = "center",
    ha = "right",
    color = "steelblue",
    path_effects = [
        pe.Stroke(linewidth = sw, foreground = "white"),
        pe.Normal(),
    ],
    transform = ax.transAxes)
ax.text(left, 0.5, "Plot",
    fontsize = fs,
    # fontproperties = font,
    va = "center",
    ha = "left",
    color = "white",
    path_effects = [
    pe.Stroke(linewidth = sw, foreground = "steelblue"),
    pe.Normal(),
    ],
    transform = ax.transAxes)

shift = 0.033
import colorengine as ce

colors = np.linspace(0, 1, 4, 0)
# colors = plt.colormaps.get_cmap("viko")(colors)
colors = ce.vivid(colors)
for idx, color in enumerate(colors):
    s = idx * shift
    ax.axhline(0.275 - 2.3 * s, 0.59 + s, 0.9 - s, color = color,
        ls = '-',
        lw = 3)
ax.axis(False)
fig.set_facecolor("lightgray")
fig.savefig(
    "UltraPlotLogo.svg",
    transparent = True,
    bbox_inches = "tight",
    )
fig.show()
