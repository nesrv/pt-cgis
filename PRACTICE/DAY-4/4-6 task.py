def get_html(s, tag='h1'):

    return f'<{tag}> {s} </{tag}>'


# print(get_html('Hello Python'))
# print(get_html('Hello Python', 'div'))
# print(get_html('Hello Python', tag='p'))


def check_pallindrom(s):
    s = s.upper()
    return s == s[::-1]



print(check_pallindrom('шалаш'))
print(check_pallindrom('АННА'))
print(check_pallindrom('Анна'))
