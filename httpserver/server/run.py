import socket


def get_response(request):
    stringdata = request.decode()
    str1 = "GET "
    str2 = "HTTP"
    str3 = "User-Agent: "
    str4 = "Accept:"
    pos1 = stringdata.find(str1)
    answer=""
    if pos1==-1:
        answer = """<!DOCTYPE html><html><head><title1>404 Not found</title1></head><body><p>File not found</p></body></html>"""
        return answer
    pos2 = stringdata.find(str2)
    pos3 = stringdata.find(str3)
    pos4 = stringdata.find(str4)
    pos1 += len(str1)
    pos3 += len(str3)
    getRequest=stringdata[pos1:pos2]
    userAgent=stringdata[pos3:pos4]
    if getRequest=="/ " :
        answer="""<!DOCTYPE html>"""
        answer+="""<html><body><p>"""
        answer+="""Hello mister!<br> You are:"""
        answer+=userAgent
        answer += """</p></body></html>"""
        return answer
    elif getRequest=="/media/ ":
        answer="""<!DOCTYPE html>"""
        answer+="""<html><body><ul>"""
        answer+="""<li>test1.txt</li><li>test2.txt</li></ul>"""
        answer+="""</body></html>"""
        return answer
    elif getRequest=="/media/test1.txt ":
        my_file = open("files/test1.txt")
        answer = my_file.read()
        return answer
    elif getRequest=="/media/test2.txt ":
        my_file = open("files/test2.txt")
        answer = my_file.read()
        return answer
    else:
        answer = """<!DOCTYPE html><html><head><title1>404 Not found</title1></head><body><p>Page not found</p></body></html>"""
        return answer


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #binding of our socket with port and host
server_socket.listen(1)  #run for this socket listening mode

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #Returns the native socket address
        request_string = client_socket.recv(2048)  #Receiving TCP data, the data is returned
        # as a string, to specify the maximum amount of data that must be received BUFSIZE
        client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client_socket.send(get_response(request_string))  #Sending TCP data, sends the data string to the socket connection
        client_socket.close()
    except KeyboardInterrupt:  #is generated upon the interruption of the program by the user (usually Ctrl+C).
        print 'Stopped'
        server_socket.close()  #Close the socket
        exit()