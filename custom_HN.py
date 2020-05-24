import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k: k['scores'], reverse=True)

def custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			score = int(vote[0].getText().replace(' points',''))
			if score > 99:
				hn.append({'title': title, 'link': href, 'scores': score})
	return sort_stories_by_votes(hn)

pprint.pprint (custom_hn(links, subtext))

