import plotly.graph_objects as go

# Define the skills and their scores
skills = ['Creativity', 'Organization']
scores = [3, 4]

# Create a polar bar chart figure
fig = go.Figure()

# Add a trace for each skill
fig.add_trace(go.Barpolar(
    r=scores,
    theta=skills,
    width=[0.4, 0.4],
    marker=dict(
        line=dict(
            width=1)
    ),
    name='Skills'
))

# Set the layout of the chart
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 5]
        )),
    showlegend=False
)

# Show the chart
fig.show()