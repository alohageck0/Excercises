__author__ = 'royalfiish'

time = input()
arr = time.split(':')
if 'A' in arr[2]:
    arr[2] = arr[2].replace('AM', '')
    if int(arr[0]) == 12:
        arr[0] = '00'
    else:
        pass
else:
    arr[2] = arr[2].replace('PM', '')
    if int(arr[0]) == 12:
        pass
    else:
        arr[0] = str(int(arr[0]) + 12)
print(':'.join(arr))
