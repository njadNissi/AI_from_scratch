while True:
    try:
        answer = input("Enter your favorite number: ")
        print("yep,", int(100 / answer), "that's nice!")
        break
    except ValueError:
        print("are you sure", answer, "is a number?")
    except ZeroDivisionError:
        print("sorry, zero can't be chosen")
    except:
        break
    finally:
        print("Bye-Bye")
