n = int(input())
name = []
address = []
region = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)

# Please write your code here.
class human:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region


arr = []
for i in range(n):
    arr.append(human(name[i], address[i], region[i]))

arr2 = name
arr2 = sorted(arr2)
last_index = name.index(arr2[-1])

print("""name {0}
addr {1}
city {2}""".format(arr[last_index].name, arr[last_index].address, arr[last_index].region))