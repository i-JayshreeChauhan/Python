# almost similar to switch case in C/C++

def http_status(status) -> None:   # returns nothing

    match status:

        case 200:
            print("OK")
        case 404:
            print("Not Found!")
        case 500:
            print("Internal Server Error!")
        case _:
            print("Unknown Status!")


http_status(404)
