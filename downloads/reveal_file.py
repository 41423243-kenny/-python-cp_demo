# pip install markdown requests plotly pandas altair matplotlib
import sys
import os
# For reveal_file.py located at downloads directory and generate reveal format file into reveal directory
# Add the ../cmsimde directory to sys.path
cmsimde_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../cmsimde'))
sys.path.append(cmsimde_path)

from respysive import Slide, Presentation
import markdown

# Create a new presentation
p = Presentation()

#
# slide1
#

# Create the first slide with a centered layout
slide1 = Slide(center=True)

# Content for the title page
logo_url = "https://upload.wikimedia.org/wikipedia/commons/4/4d/Fractal_canopy.svg"
title_page_content = {
    'title': '計算機程式 w3 簡報',
    'subtitle': '如何使用 Git',
    'authors': '學員一, 學員二',
    'logo': logo_url
}

# Styles for the title page content in the same order as content
styles = [
    {'color': '#e63946', 'class': 'r-fit-text border-top'},  # title
    {},  # subtitle style by default
    {},  # authors style by default
    {'filter': 'invert(100%) opacity(30%)'},  # logo
]

# Add the title page to the slide
slide1.add_title_page(title_page_content, styles)

#
# slide2
#

# Create the second slide
slide2 = Slide()

# Add a title to the slide with a fontawesome icon
slide2.add_title("Your title with a fontawesome icon", icon="fas fa-infinity fa-beat")

# Create some text in markdown format
txt = markdown.markdown("""
This is some dummy text 

- and it's easier to use Markdown
<ul><li>but it's ok to use HTML tag</li></ul>
""")

# Add the text to the slide in a new Bootstrap column with a width of 12 (default)
slide2.add_content([txt], columns=[12])

#
# slide3
#

# Create a new slide
slide3 = Slide()

text = markdown.markdown("""
En cosmologie, le modèle de l'univers fractal désigne un modèle cosmologique 
dont la structure et la répartition de la matière possèdent une dimension fractale, 
et ce, à plusieurs niveaux. 

De façon plus générale, il correspond à l'usage ou 
l'apparence de fractales dans l'étude de l'Univers et de la matière qui le compose.
Ce modèle présente certaines lacunes lorsqu'il est utilisé à de très grandes ou de 
très petites échelles.

""")

# Add image url
url = "./assets/img/Univers_Fractal_J.H..jpg"

# Add title to slide
slide3.add_title("Bootstrap powering")

# Add styles to slide
css_txt = [
   {'font-size': '70%', 'text-align': 'justify', 'class': 'bg-warning'},  # text style
   None  # url style is mandatory even it is None
]

# Add content to slide, where text and url are added to the slide with 7 and 5 columns respectively
# css_txt is added as styles
slide3.add_content([text, url], columns=[7, 5], styles=css_txt)

#
# slide4
#

slide4 = Slide()
slide4.add_title("Plotly")

# import plotly express for creating scatter plot
import plotly.express as px

# load iris data
df = px.data.iris()

# create scatter plot
fig = px.scatter(df, x="sepal_width", y="sepal_length",
                 color="species", size="petal_length", hover_data=["petal_width"])

# update layout
fig.update_layout(autosize=True)

# Export the figure to json format
j = fig.to_json()

# apply css to the figure
css_txt = [{'class': 'stretch'}]

# add the scatter plot to the slide
slide4.add_content([j], columns=[12], styles=css_txt)

#
# slide5
#

slide5 = Slide()
slide5.add_title("Altair")

# import altair for creating scatter plot
import altair as alt

source = px.data.iris()

# create scatter plot
chart = (
    alt.Chart(source)
    .mark_circle(size=60)
    .encode(
        x="sepal_width", y="sepal_length", color="species",
        tooltip=["species", "sepal_length", "sepal_width"],
    )
    .interactive()
    .properties(width=900, height=500)
)

# Export the figure to json format
j = chart.to_json()

# add the scatter plot to the slide
slide5.add_content([j], columns=[12])

#
# add fig to slide5
#

slide5_fig = Slide()
slide5_fig.add_title("Matplotlib")

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4*np.pi-1,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)

plt.rcParams["figure.figsize"] = (8, 5)
fig, ax = plt.subplots()
plt.plot(x,y,x,z)
plt.xlabel('x values')
plt.title('sin and cos ')
plt.legend(['sin(x)', 'cos(x)'])

# add the  plot to the slide
slide5_fig.add_content([fig], columns=[12])

#
# slide6
#

slide6 = Slide()
slide6.add_title("Mathematical Equations")

# Text with LaTeX expressions
math_content = """
The Gaussian function $f(x) = e^{-x^2}$ or in display mode:

$$f(x) = e^{-x^2}$$
"""
slide6.add_content([math_content], columns=[12])

#
# slide7
#

slide7 = Slide()

# card 1 content
txt_card1 = markdown.markdown("""
- list 1
- list 2

""")

# card 1 image
univ_url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Mandel_zoom_04_seehorse_tail.jpg"

# list of cards. These orders will be the same on the HTML page
cards = [{'text': txt_card1, 'image': univ_url},  # Only text and image
         {'image': logo_url, 'text': "Card text 2", 'title': "Card Title 2", },  # Image, text and title
         {'title': "Card Title 3", 'text': "Card text 3"}]  # Title and text

# styles for each cards
styles_list = [{'font-size': '20px', 'color': '#1d3557', 'class': 'bg-danger'},
               {'font-size': '20px', 'color': '#e63946', 'class': 'bg-warning'},
               {'font-size': '20px', 'color': '#f1faee', 'class': 'bg-info'}]

# add title and card to slide
slide7.add_title("Bootstrap cards can be added")
slide7.add_card(cards, styles_list)

#
# slide8
#

bckgnd_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Frost_patterns_2.jpg/1920px-Frost_patterns_2.jpg"

# Create a dictionary with slide kwargs
slide_kwargs = {
    'data-background-image': bckgnd_url,
    'data-background-size': 'cover',  # more options here : https://revealjs.com/backgrounds/
}

# Create a slide object with slide kwargs
slide8 = Slide(center=True, **slide_kwargs)

css_background = {"class": "text-center", "color": "#e63946", "background-color": "#f1faee"}
slide8.add_title("Image  background", **css_background)

#
# slide 9 and 10
#

slide9 = Slide()
text = markdown.markdown("""Press arrow down to show vertical slide""")
slide9.add_title("Horizontal and vertical slides")
slide9.add_content([text])

slide10 = Slide(center=True)
slide10.add_title("Horizontal and vertical slides")
text = markdown.markdown("""This is a vertical slide""")
slide10.add_content([text])

# Adding slide to the presentation
p.add_slide([slide1, slide2, slide3, slide4, slide5, slide5_fig, slide6, slide7, slide8, slide9, slide10])

# Saving the presentation in HTML format
p.save_html("./../reveal/index.html")