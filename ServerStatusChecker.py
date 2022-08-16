import socket


def is_running(site):
    """Function attempts to connect to the given server using a socket. 
        Returns wheater or not it was ables to connect to the server"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # ".connect" takes the address and the number of bytes.
        sock.connect((site, 80))
        return True
    except:
        return False


if __name__ == "__main__":
    while True:
        site = input('Website to check: ')
        if is_running(f"{site}.com"):
            print(f"{site}.com is running!")
        else:
            print(f"There is a problem with {site}.com!")

        if input("Would you like to check another website(Y/N)? ") in {'n', 'N'}:
            break
