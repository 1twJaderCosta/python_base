from decouple import config

def example(self, *args):
    
    '''It's showing how the things works *args.

    Args:
        *args (list): example args

    Returns:
        double: The return a example string.

    '''
    ex = config('MY_EXAMPLE_KEY')
    print('a', ex)
    return ex

example('a','b')