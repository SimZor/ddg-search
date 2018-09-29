import sys
from search.search import DDGSearch


if __name__ == '__main__':
    try:
        i = DDGSearch()

        # Make a copy of the list
        # and pop the python file name
        args = sys.argv
        args.pop(0)

        # Search
        r = i.query(args)

        print('Result from search') 
        print(r['AbstractURL'])
    except Exception as e:
        print('error', e)
