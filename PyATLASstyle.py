import os

def applyATLASstyle(mtp):
    font_dir = os.path.abspath(__file__).replace("PyATLASstyle.py", "fonts/")
    font_dirs = [font_dir,]

    import matplotlib.font_manager as font_manager
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
    font_list = font_manager.createFontList(font_files)
    font_manager.fontManager.ttflist.extend(font_list)
    mtp.rcParams['font.family'] = 'Arial'
    mtp.rcParams['font.size'] = 12.5
    mtp.rcParams['legend.frameon'] = False
    mtp.rcParams['legend.fontsize'] = 10.0
    mtp.rcParams['lines.antialiased'] = False
    mtp.rcParams['lines.linewidth'] = 2.5
    mtp.rcParams['xtick.direction'] = 'in'
    mtp.rcParams['xtick.top'] = True
    mtp.rcParams['xtick.minor.visible'] = True
    mtp.rcParams['ytick.direction'] = 'in'
    mtp.rcParams['ytick.right'] = True
    mtp.rcParams['ytick.minor.visible'] = True
    mtp.rcParams['mathtext.fontset'] = 'custom'
    mtp.rcParams['mathtext.it'] = 'Arial:italic'
    mtp.rcParams['mathtext.bf'] = 'Arial:bold'
    mtp.rcParams['mathtext.rm'] = 'Arial'
    mtp.rcParams['mathtext.sf'] = 'Arial'
    mtp.rcParams['mathtext.cal'] = 'Arial:italic'
    mtp.rcParams['mathtext.tt'] = 'Arial'

def makeATLAStag(ax, fig, first_tag='', second_tag=''):
    xmin = 0.03
    ymax = 0.97
    line_spacing = 0.2
    box0 = ax.text(xmin, ymax, "ATLAS", fontweight='bold', fontstyle='italic', verticalalignment='top', transform=ax.transAxes)
    box0_ext_tr = ax.transAxes.inverted().transform(box0.get_window_extent(renderer=fig.canvas.get_renderer()))
    box1 = ax.text(box0_ext_tr[1][0], ymax, " ", verticalalignment='top', transform=ax.transAxes)
    box1_ext_tr = ax.transAxes.inverted().transform(box1.get_window_extent(renderer=fig.canvas.get_renderer()))
    ax.text(box1_ext_tr[1][0], ymax, first_tag, verticalalignment='top', transform=ax.transAxes)
    ax.text(xmin, box0_ext_tr[0][1]-(box0_ext_tr[1][1]-box0_ext_tr[0][1])*line_spacing, second_tag, verticalalignment='top', transform=ax.transAxes)
