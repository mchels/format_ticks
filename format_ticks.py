from fractions import Fraction
import numpy as np
d
def tick_formatter(tick):
    """
    Format tick into a nice ticklabel.
    Currently hard-coded for pi.
    """
    sign_str = ''
    if tick < 0:
        sign_str = '-'
    tick_normalized = np.abs(tick) / np.pi
    fraction = Fraction(tick_normalized).limit_denominator(10000)
    if fraction.numerator == 0:
        numerator_str = '0'
    elif fraction.numerator == 1:
        numerator_str = '\pi'
    else:
        numerator_str = str(fraction.numerator) + '\pi'
    if fraction.denominator == 1:
        denominator_str = ''
    else:
        denominator_str = '/' + str(fraction.denominator)
    return '$' + sign_str + numerator_str + denominator_str + '$'

def set_smart_ticks(ax, step_size=1, step_unit=None, axis=0):
    """
    Sets ticks and ticklabels on axis ax.
    Tick separation is given by step_size OR by step_size*<hard-coded number> if
    step_unit is specified as one of the hard-coded options.
    """
    if step_unit is 'pi':
        step_size_unit = step_size * np.pi
    else:
        step_size_unit = step_size
    xydata = ax.get_lines()[0].get_xydata()
    raw_data = xydata[:,axis]
    low = np.min(raw_data)
    high = np.max(raw_data)
    tick_range = high - low
    ticks = np.linspace(low, high, tick_range/step_size_unit+1)
    ticklabels = [tick_formatter(tick) for tick in ticks]
    ax.set_xticks(ticks)
    ax.set_xticklabels(ticklabels)
    ax.set_xlim(low, high)
    return ticks, ticklabels

if __name__=='__main__':
    import matplotlib.pyplot as plt
    angles = np.linspace(-2*np.pi, 2*np.pi, 91)
    y_data = np.sin(angles)
    fig, ax = plt.subplots(1,1)
    ax.plot(angles, y_data)
    set_smart_ticks(ax, step_size=1/3, step_unit='pi')
    plt.show()
