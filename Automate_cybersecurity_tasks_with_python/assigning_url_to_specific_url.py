# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url` 

ind = url.index(".com")

# Extract the domain extension in `url` and display it

print(url[ind:ind+4])
