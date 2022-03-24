types = dict(червячный={'nmrv', 'nrv', 'nmrv-p', 'nrv-p', 'nmvl', 'nmrv'}, соосный=['h', 'ha', 'hfa'])
sizes = dict(червячный={25, 30, 40}, соосный=[42, 52, 62])
select = input()

for na, ty in enumerate(select):
        if ty.isdigit():
                name = select[:na]
                size = int(select[na:])
                break
for type, names in types.items():
        for version in names:
                if name == version:
                        a = type

for type, sizes in sizes.items():
        for dimention in sizes:
                if dimention == size and a == type:
                        print(a, dimention)


