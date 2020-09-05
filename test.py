#!/usr/bin/env python3
from luxand import luxand

client = luxand("12a42a8efedf4e24b84730ce440e5429")

brad = client.add_person("Brad Pitt", photos = ["/Users/u_rim/Desktop/test2/woorim.png"])

result = client.verify(brad, photo = "/Users/u_rim/Desktop/test2/hyewon.jpg")

print(result)