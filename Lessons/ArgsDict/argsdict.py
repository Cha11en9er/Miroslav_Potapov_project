def main_program(sort):
    if sort is True:
        for lines in sorted(sys.argv):
            keyvalue = lines.split('=')
            print("Key: " + keyvalue[0] + " Value: " + keyvalue[1])
    else:
        for lines in sys.argv:
            keyvalue = lines.split('=')
            print("Key: " + keyvalue[0] + " Value: " + keyvalue[1])


if __name__ == "__main__":
    import argparse        
    parser = argparse.ArgumentParser()
    parser.add_argument('--sort', '-sort', action='store_true', default=False)
    args = parser.parse_args()
    flag = False
    import sys  
    a = 0
    argsort = False
    for line in sys.argv[1:]:
        a += 1
        if line == '--sort':
            argsort = True
            del sys.argv[a:a + 1]
            flag = True
            break
        else:
            flag = False
    if flag:
        sys.argv = sys.argv[1:]
    else:
        sys.argv = sys.argv[1:]
    
    main_program(argsort)
