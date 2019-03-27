#ElkaParse
#Created by redfr0g
#27-03-2019


from lxml import html
import requests

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


page = requests.get('http://www.elka.pw.edu.pl/pol/Aktualnosci/Ogloszenia')
tree = html.fromstring(page.content)

titles = tree.xpath('//div[@class="class-blog-post float-break"]//div[@class="attribute-header"]//h3//text()')
descriptions = tree.xpath('//p//text()')



for i in range(0,9):

	if titles[i] is not None and descriptions[i+10] is not None:
		print("\033[9" + str(i) + "m" + color.BOLD + titles[i] + color.END)
		print("\033[9" + str(i) + "m" + descriptions[i+10] + "\n")

