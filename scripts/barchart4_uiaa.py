import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as tck
# 
# IV ,IV+,V-,V ,V+ ,VI-,VI,VI+,VII-,VII,VII+,VIII-,VIII,VIII+,IX-,IX ,IX+,X- ,X  ,X+
# 

colors=['#ddc8db', '#d6bcd4', '#cfb1cd', '#c9a6c5', '#c29bbe', '#bb90b7', '#ad7aa9', '#a0649a', '#924d8c', '#85377d', '#77216f', '#5e2750', '#6e3d62', '#7e5273', '#8e6885', '#9e7d96', '#af93a8', '#b79eb0', '#bfa9b9']
x = np.array(["IV", "IV+", "V-", "V", "V+", "VI-", "VI", "VI+", "VII-", "VII", "VII+", "VIII-", "VIII", "VIII+", "IX-", "IX", "IX+", "X-", "X", "X+"])
plt.style.use('ggplot')
cm = 1/2.54  # centimeters in inches
figsize=(17*cm, 2.5*cm)
plt.rcParams["figure.figsize"] = figsize
# plt.figure(facecolor='yellow')
margins = {  #     vvv margin in inches
    "left"   :     0.3  / figsize[0],
    "bottom" :     0.25 / figsize[1],
    "right"  : 1 - 0.01 / figsize[0],
    "top"    : 1 - 0.2  / figsize[1]
}
plt.subplots_adjust(**margins)

ax = plt.axes()
ax.set_facecolor("#F4FAF4")
plt.grid(c='#dfdfdf')

ax.yaxis.set_tick_params(which='minor', color='#dfdfdf')
# ax.yaxis.set_minor_locator(tck.AutoMinorLocator(3))


# Turn minor gridlines on and make them thinner.
ax.grid(which='minor', linewidth=0.6, color='#efefef', linestyle='--')