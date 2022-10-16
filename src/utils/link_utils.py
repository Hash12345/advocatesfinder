def add_advocate_to_links(links, id):
    response = []
    for link in links:
        link['advocate'] = id
        response.append(link)
    return response