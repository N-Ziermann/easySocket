# easySocket
"easySocket" is a module for Python that's based on the "socket" module and aims to make tasks like sending long texts or files easier/simpler.

To install it, just put the .py file into your Python module directory (/path/to/your/pythonfolder/Lib/site-packages)

Right now it can do the following:

	-Host a tcp connection with one function:			host_tcp(my_ip, port)
	-Connect to a tcp conenction with one function:			connect_tcp(ip, port)
	-Send a file over a tcp connection independent of size:		send_file(location, recipient)
	-Send a file over a tcp connection independent of size:		send_text(text, recipient)
	-Aswell as receiving the data send by those two functions:	rcv_data(sender)
	
I wrote this module, because I wanted to send an image with the socket module and found it annoying to always spend multiple lines of code to be able to send an image that was bigger than the maximum amount of bytes sendable with one socket.send command.

If you have any functions you think should be a part of this module just do a pull request or write your request under the Issues-Tab.
