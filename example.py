from streamline import StreamLine
def f1():
    for i in range(1000000):
        yield i * 2

def f2(n, add, third = 0.01):
    return n + add + third

def f3(n):
    return n + 1

if __name__ == "__main__":
    sl = StreamLine()
    sl.add_module(f1, 2)
    sl.add_module(f2, 2, args = [0.5], kwargs = {'third' : 0.02})
    sl.add_module(f3, 2)
    #sl.run_serial()
    sl.run()
    sl.join()
    print(sl.get_results())
