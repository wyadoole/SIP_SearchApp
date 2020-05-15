# Code based on https://wikipedia-api.readthedocs.io/en/latest/README.html
# Find all examples you need at the URL above.

import wikipediaapi
import BeautifulSoup

# Get page and stuff it into vars
wiki_wiki = wikipediaapi.Wikipedia('en')
page_py = wiki_wiki.page('Linux')

# How To Check If Wiki Page Exists
print("How To Check If Wiki Page Exists")

page_py = wiki_wiki.page('Linux')
print("Page - Exists?: %s" % page_py.exists())

page_missing = wiki_wiki.page('NonExistingPageWithStrangeName')
print("Page - Exists?: %s" %     page_missing.exists())

# Get Page Summary
wiki_wiki = wikipediaapi.Wikipedia('en')

print("Title: %s" % page_py.title)
print("Summary of first 1000 characters of the Page: %s" % page_py.summary[0:1000])

# writes
#print(page_py.fullurl)
print(page_py.canonicalurl)


def print_links(page):
    links = page.links
    link_keys = sorted(page.links.keys())
    new_page = page.links[link_keys[0]]
    for title in sorted(links.keys()):
        print("%s: %s" % (title, links[title].fullurl))


print_links(page_py)

