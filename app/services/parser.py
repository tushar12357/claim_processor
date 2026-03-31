def join_pages(pages, indices):
    return "\n".join([pages[i] for i in indices if i < len(pages)])