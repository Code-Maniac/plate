import mymodule

def main():
    print("Hello World")

    x = 4
    y = 2
    print(f"{x} + {y} = {mymodule.add(x, y)}")
    print(f"{x} - {y} = {mymodule.sub(x, y)}")
    print(f"{x} * {y} = {mymodule.mul(x, y)}")
    print(f"{x} / {y} = {mymodule.div(x, y)}")

if __name__ == "__main__":
    main()
