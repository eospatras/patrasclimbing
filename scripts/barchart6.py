import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as tck

colors=['#0FA1D3', '#079DD0', '#E2F0B6', '#C5E26D', '#A8D324', '#A8D324', '#83B600', '#83B600', '#FFECC0', '#FFD980', '#FFC641', '#FFB61C', '#FFA00E', '#FF9105', '#FFCACA', '#FF9494', '#FF5F5F', '#F83A3A', '#E21D1D', '#D30A0A']
x = np.array(["~5b", "5c", "6a", "6a+", "6b", "6b+", "6c", "6c+", "7a", "7a+", "7b", "7b+", "7c", "7c+", "8a", "8a+", "8b", "8b+", "8c", "8c+"])
plt.style.use('ggplot')
cm = 1/2.54  # centimeters in inches
figsize=(17*cm, 3*cm)
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
ax.yaxis.set_minor_locator(tck.AutoMinorLocator(2))


# Turn minor gridlines on and make them thinner.
ax.grid(which='minor', linewidth=0.6, color='#efefef', linestyle='--')