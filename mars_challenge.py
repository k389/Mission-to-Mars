
# In[15]:
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

# In[16]:
# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)

# In[20]:

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# In[21]:

# St-up HTML parser
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

# In[22]:

# assign the title and summary text to variables
slide_elem.find("div", class_='content_title')

# In[23]:

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# In[24]:

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

# In[25]:
"### Featured Images"
"Markdown."
# In[9]:
# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
# In[27]:
# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# In[28]:
# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()

# In[29]:
# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

# In[30]:
# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# In[31]:
# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url

# In[32]:
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

# In[33]:
df.to_html()

# In[110]:
# Visit  Cerberus URL
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# In[111]:
# Find and click the Cerberus image button
cerb_image_elem = browser.find_by_text('Cerberus Hemisphere Enhanced')
cerb_image_elem.click()

# In[112]:
# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')
cerb_soup = BeautifulSoup(html, 'html.parser')

# In[113]:
cerberus_title = cerb_soup.find("h2", class_='title').get_text()
cerberus_title

# In[114]:
# access the full resolution image
#cerberus = browser.links.find_by_partial_text('cerberus_enhanced.tif')
cerberus = browser.links.find_by_partial_text('Sample')
cerberus.click()

# In[115]:
# Find the relative image url
cerb_url_rel = img_soup.select_one('img.wide-image').get('src')
cerb_url_rel

# In[116]:
# Use the base URL to create an absolute URL
cerb_img_url = f'https://astrogeology.usgs.gov{cerb_url_rel}'
cerb_img_url

# In[117]:
# Cerberus dictionary
#cerb_dict = {"img_url": cerb_img_url, "title": cerberus_title}
#cerb_dict
sidebar_soup = BeautifulSoup(html, 'html.parser')
side_bar = browser.select_one('div.sidebar a href')
test = side_bar.find_by_text('Syrtis Major Hemisphere Enhanced')
test.click()

# In[22]:

# assign the title and summary text to variables
slide_elem.find("div", class_='content_title')

# In[23]:

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title
test = browser.find_by_text('Schiaparelli Hemisphere Enhanced')
test.click()
#%%
# Visit schiaparelli URL
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# In[111]:
# Find and click the Schiaparelli image button
schiap_image_elem = browser.find_by_text('Schiaparelli Hemisphere Enhanced')
schiap_image_elem.click()

# In[112]:
# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')
schiap_soup = BeautifulSoup(html, 'html.parser')

# In[113]:
schiap_title = schiap_soup.find("h2", class_='title').get_text()
schiap_title

# In[114]:
# access the full resolution image
#schiaparelli = browser.links.find_by_partial_text('schiap_enhanced.tif')
schiaparelli = browser.links.find_by_partial_text('Sample')
schiaparelli.click()

# In[115]:
# Find the relative image url
schiap_url_rel = img_soup.select_one('img.wide-image').get('src')
schiap_url_rel

# In[116]:
# Use the base URL to create an absolute URL
schiap_img_url = f'https://astrogeology.usgs.gov{schiap_url_rel}'
schiap_img_url

# In[117]:
# Cerberus dictionary
#schiap_dict = {"img_url": schiap_img_url, "title": schiap_title}
#schiap_dict

#%%
# Visit Syrtis major URL
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# In[111]:
# Find and click the Schiaparelli image button
syrtis_image_elem = browser.find_by_text('Syrtis Major Hemisphere Enhanced')
syrtis_image_elem.click()

# In[112]:
# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')
syrtis_soup = BeautifulSoup(html, 'html.parser')

# In[113]:
syrtis_title = syrtis_soup.find("h2", class_='title').get_text()
syrtis_title

# In[114]:
# access the full resolution image
#schiaparelli = browser.links.find_by_partial_text('schiap_enhanced.tif')
syrtis = browser.links.find_by_partial_text('Sample')
syrtis.click()

# In[115]:
# Find the relative image url
syrtis_url_rel = img_soup.select_one('img.wide-image').get('src')
syrtis_url_rel

# In[116]:
# Use the base URL to create an absolute URL
syrtis_img_url = f'https://astrogeology.usgs.gov{syrtis_url_rel}'
syrtis_img_url

# In[117]:
# Cerberus dictionary
#syrtis_dict = {"img_url": syrtis_img_url, "title": syrtis_title}
#syrtis_dict

#%%
# Visit Valles Marineris URL
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# In[111]:
# Find and click the Schiaparelli image button
valles_image_elem = browser.find_by_text('Valles Marineris Hemisphere Enhanced')
valles_image_elem.click()

# In[112]:
# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')
valles_soup = BeautifulSoup(html, 'html.parser')

# In[113]:
valles_title = valles_soup.find("h2", class_='title').get_text()
valles_title

# In[114]:
# access the full resolution image
#schiaparelli = browser.links.find_by_partial_text('schiap_enhanced.tif')
valles = browser.links.find_by_partial_text('Sample')
valles.click()

# In[115]:
# Find the relative image url
valles_url_rel = img_soup.select_one('img.wide-image').get('src')
valles_url_rel

# In[116]:
# Use the base URL to create an absolute URL
valles_img_url = f'https://astrogeology.usgs.gov{valles_url_rel}'
valles_img_url

# In[117]:
# Cerberus dictionary
#valles_dict = {"img_url": valles_img_url, "title": valles_title}
#valles_dict

#%%
hemisphere_dict = [{"img_url": cerb_img_url, "title": cerberus_title},
{"img_url": schiap_img_url, "title": schiap_title},
{"img_url": syrtis_img_url, "title": syrtis_title},
{"img_url": valles_img_url, "title": valles_title}]
hemisphere_dict
#%%
# append dictionaries to a list
hemisphere_list = []
hemisphere_list.append(dict(hemisphere_dict))
hemisphere_list
#%%
browser.quit()

# %%
