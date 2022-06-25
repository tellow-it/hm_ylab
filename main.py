import math


def domain_name(url):
    if 'http://' in url:
        url: str = url.replace('http://', '')
    elif 'https://' in url:
        url: str = url.replace('https://', '')
    url_arr: list = url.split('.')
    if url_arr[0] != 'www':
        return url_arr[0]
    else:
        return url_arr[1]


def int32_to_ip(int32):
    int2: str = bin(int32)[2:]
    int2_full: str = '0' * (32 - len(int2)) + int2
    ip4_all = []
    for i in range(0, 4):
        ip4_i: str = str(int(int2_full[8 * i:8 * (i + 1)], base=2))
        ip4_all.append(ip4_i)
    ip4: str = '.'.join(ip4_all)
    return ip4


def zeros(n):
    if n > 0:
        k_max = int(math.log(n, 5))
        z = 0
        for i in range(1, k_max + 1):
            z += int(n / math.pow(5, i))
        return z
    else:
        return 0


def bananas(s) -> set:
    result = set()

    print("hello123")
    str_arr = list(s)
    print("hello")
    return result


def count_find_num(primesL, limit):
    # your code here
    product = math.prod(primesL)
    numbers = []
    for i in range(product, limit + 1, product):
        num = i
        if i % product == 0:
            product_count = []
            for pr in primesL:
                k = 0
                while i % pr == 0:
                    k += 1
                    i /= pr
                product_count.append(k)
                if i == 1:
                    numbers.append(num)
    if len(numbers) != 0:
        return [len(numbers), max(numbers)]
    else:
        return []


def test_for_task_1():
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"


def test_for_task_2():
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"


def test_for_task_3():
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7


def test_fot_task_4():
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


def test_for_task_5():
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_for_task_1()
    test_for_task_2()
    test_for_task_3()
    test_for_task_5()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
