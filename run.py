import sys
sys.path.append("./backend/")
from WebServer import WebServer

def main():
    server = WebServer()
    
    server.run()

if __name__ == "__main__":
    main()