def main():
    count = 0
    number = int(input(""))
    while (number > 0):
      number = number//10
      count = count + 1
    print (count)

if __name__ == '__main__':
    main()
