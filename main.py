rom medical_data_visualizer import draw_cat_plot, draw_heat_map

# Generate plots
cat_fig = draw_cat_plot()
heat_fig = draw_heat_map()

# Display plots
cat_fig.savefig('catplot.png')
heat_fig.savefig('heatmap.png')
