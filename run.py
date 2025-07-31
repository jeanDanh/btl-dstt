import sys, os, subprocess
sys.path.append("./backend/")
from WebServer import WebServer

def main():
	if not os.path.exists("./local_storage"):
		subprocess.run(["python", "./data/CustomData.py"])
		subprocess.run(["python", "./data/ProductData.py"])
		subprocess.run(["python", "./data/PurchaseData.py"])

	server = WebServer()

	print ("chose mode: ")
	print ("1. run api")
	print ("2. console test")
	mode = input("write num: ")

	if (mode == "1"):
		server.run()
	elif (mode == "2"):
		server.console_test()

if __name__ == "__main__":
	main()
