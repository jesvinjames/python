with open('test.txt', mode='wb+') as f:
    f.write(b'\x00\x00')
    f.seek(0)
    print(f.read())
