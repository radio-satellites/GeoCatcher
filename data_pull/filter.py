f = open("scrape.txt",'rb')


lines = f.read().decode(encoding="utf-8").split("\n")

filtered = list(set(lines))

f_out = open("scrape_filtered.txt",'wb')

f_out.write(str('\n'.join(str(i) for i in filtered)).encode(encoding="utf-8"))

f_out.close()
