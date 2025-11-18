def sort_string(s):
    nList = list(s)
    nList.sort()
    return ''.join(nList)
    
def main():
    strok = input()
    res = sort_string(strok)
    print(res)

if __name__ == "__main__":
    main()
