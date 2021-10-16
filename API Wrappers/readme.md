## Inshorts API wrapper

A simple API wrapper implementation for fetching short newses from inshorts.com

Since the wrapper depends only on a single third party lib you can easily install it via pip using ```pip3 install requests```


```py
ins = Inshorts("en")
print(ins.by_topic("technology"))
```
