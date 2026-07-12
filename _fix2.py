import nbformat as nbf
nb = nbf.read('ch01/ch01.ipynb', as_version=4)
md, code = nbf.v4.new_markdown_cell, nbf.v4.new_code_cell

dep_idx = None
for i, c in enumerate(nb.cells):
    if c.cell_type != 'code':
        continue
    # bare function reference in the sweep cell
    c.source = c.source.replace('best(vectorized,', 'best(vectorized_in_numpy,')
    if 'are_independent' in c.source or 'c3 adds nothing new' in c.source:
        dep_idx = i
    if 'combination, exhibited' in c.source:
        dep_idx = i

if dep_idx is None:
    for i, c in enumerate(nb.cells):
        if c.cell_type == 'code' and 'c3' in c.source:
            dep_idx = i
print('dep cell at', dep_idx)
print(repr(nb.cells[dep_idx].source[:120]))
nb.cells[dep_idx] = code(
    "c1 = np.array([1, -1, 0])\n"
    "c2 = np.array([0, 1, -1])\n"
    "c3 = np.array([-1, 0, 1])\n"
    "print('c1 + c2 + c3 =', c1 + c2 + c3)   # the combination, exhibited")
new_cells = [
    md("### The dependent triple, drawn"),
    code("fig = plt.figure(figsize=(6, 6))\n"
         "ax = fig.add_subplot(projection='3d')\n"
         "for v, c, name in [(c1, 'tab:blue', 'c1'), (c2, 'tab:red', 'c2'),\n"
         "                   (c3, 'tab:green', 'c3')]:\n"
         "    ax.quiver(0, 0, 0, *v, color=c, arrow_length_ratio=0.1)\n"
         "    ax.text(*(v * 1.15), name, color=c)\n"
         "xx, yy = np.meshgrid(np.linspace(-1, 1, 8), np.linspace(-1, 1, 8))\n"
         "zz = -xx - yy                       # the plane x + y + z = 0\n"
         "ax.plot_surface(xx, yy, zz, alpha=0.12, color='gray')\n"
         "ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)\n"
         "ax.set_title('Three vectors, one plane: the triple is dependent')\n"
         "plt.savefig('figures/fig_dependent_triple.png', dpi=150,\n"
         "            bbox_inches='tight')\n"
         "plt.show()"),
]
nb.cells = nb.cells[:dep_idx+1] + new_cells + nb.cells[dep_idx+1:]
nbf.write(nb, 'ch01/ch01.ipynb')
print('cells:', len(nb.cells))
