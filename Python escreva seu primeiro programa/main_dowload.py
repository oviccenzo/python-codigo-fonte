#coding: UTF-8
import io
import sys
import urllib.request as request

BUFF_SIZE = 1024

def dowload_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Dowloadade %d " % (((times * BUFF_SIZE)/length)* 100))
        
def dowload(response, output):
    total_dowloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_dowloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Dowloaded {bytes}'.format(bytes=total_dowloaded))

def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("Saida.zip",mode="w")
    
    content_length = response.getheader('Content-length')
    if content_length:
        length = int(content_length)
        dowload_length(response,out_file,length)
    else:
        dowload_length(response, out_file)
        
        response.close()
        out_file.close()
        print("Finished")

if __name__ == "__main__":
    main()