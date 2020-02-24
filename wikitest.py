import wikipedia


def display_output_divider():
    print("_" * 120)  # Divides sections


# Search Wikipedia for subjects which contain.
search_term = "programming"
print("I am searching for subjects which contain ", search_term)
print("Search results of subjects which contain ", search_term)
print(wikipedia.search(search_term))

display_output_divider()

# Extract Summary information from Wikipedia
search_term = "Linux"
print("I am searching for a summary of the content for a subject ", search_term)
print("Search Results below:")
print(wikipedia.summary("Linux"))

display_output_divider()

# Extract one or more sentences of information from Wikipedia
search_term = "Linux"
number_of_sentences_about_the_subject_to_return = 1
print("I am searching for ", number_of_sentences_about_the_subject_to_return,
      " sentence(s) of the content for a subject ", search_term)
print("Search Results below:")
print(wikipedia.summary("Linux", sentences=1))

display_output_divider()

# Extract the title of the page from Wikipedia
search_term = "Linux"
print("I am searching for the title of the content for a subject ", search_term)
print("Search Results below:")
print(wikipedia.page("Linux"))

display_output_divider()

# Extract the Complete content of the page from Wikipedia
search_term = "Linux"
print("I am searching for the Complete content of a subject ", search_term)
print("Search Results below:")
print(wikipedia.page("Linux").content)