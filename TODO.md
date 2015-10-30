TODO
====
- [ ] Figure out a better way to get list of x-values than
        ax.get_lines()[0].get_xydata()
- [ ] Some of the conditionals in tick_formatter are probably redundant.
- [ ] Consider moving ax.set_xlim out of the function. It solves an unrelated
problem.
- [ ] Allow step_size in set_smart_ticks to be iterable to generate ticks at
more than one base fraction. Sort out duplicates (e.g., 1*pi) with np.unique.
- [ ] Replace ax.set_xlim with a function for a generic axis specified by the
axis keyword.
