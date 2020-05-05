
class Color:
    
    purple = '\033[95m'
    red = '\033[91m'
    green = '\033[92m'
    heavygreen = '\033[32m'
    yellow = '\033[93m'
    
    bold = '\033[1m'
    underline = '\033[4m'

    end = '\033[0m'






if __name__ == '__main__':

    print(Color.purple       +'test1' + Color.end)
    print(Color.red          +'test2' + Color.end)
    print(Color.green        +'test3' + Color.end)
    print(Color.heavygreen   +'test4' + Color.end)
    print(Color.yellow       +'test5' + Color.end)
    print(Color.bold         +'test6' + Color.end)
    print(Color.underline    +'test7' + Color.end)