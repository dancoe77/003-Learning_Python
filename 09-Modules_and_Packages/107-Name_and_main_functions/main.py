# main.py
import one

print("Top level in main.py")

one.func()

if __name__ == "__main__":
    print("main.py is being run directly")
else:
    print("main.py has been imported")