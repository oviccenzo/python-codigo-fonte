BUFF_SIZE = 2024
def dowload_length(response, output, length):
    times = length/ BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Dowload %d " % (((time * BUFF_SIZE)/ length)*100))

def dowload(response, output):
    total_dowloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_dowloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Dowloaded {bytes}'.format(bytes=total_dowloaded))
        