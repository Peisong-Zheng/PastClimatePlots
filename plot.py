import plotly.express as px

# Example data - replace with your own data source
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

# Save the plot as an HTML file
fig.write_html('templates/index.html')
