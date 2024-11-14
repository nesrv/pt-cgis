def get_html(s, tag='h1'):

    return f'<{tag}> {s} </{tag}>'


print(get_html('Hello Python'))
print(get_html('Hello Python', 'div'))
print(get_html('Hello Python', tag='p'))
