from functools import wraps


def make_html(element):
    def real_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return '<{}>'.format(element) + fn(*args, **kwargs) + '</{}>'.format(element)
        return wrapper
    return real_decorator

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text

def main():
    print(get_text('a'))

if __name__ == '__main__':
    main()
