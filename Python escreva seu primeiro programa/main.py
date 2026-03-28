from urllib import request
import sys 
import io

from dowload import dowload_length

def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("Saida.zip", mode="w")
    
    content_length = response.getheader('Content-Length')
    if content_length:
        length = int(content_length)
        dowload_length(response, out_file,length)
        
    else:
        dowload_length(response, out_file)
    
    response.close()
    out_file.close()
    print("Finished")

if __name__ == "__main__":
    main()
    
