import numpy as np


def star_main():
    # lst = [[1, 3, 5], [2, 4, 6]]
    # print(type(lst))
    # np_lst = np.array(lst)
    # print(type(np_lst))
    # np_lst = np.array(lst, dtype=np.int)
    # print(type(np_lst))
    # print(np_lst.shape)
    # print(np_lst.ndim)
    # print(np_lst.dtype)
    # print(np_lst.itemsize)
    # print(np_lst.size)
    # print(np.zeros([2, 4]))
    # print(np.ones([3, 5]))
    # print("Rand:")
    # print(np.random.rand(2, 4))
    # print(np.random.rand())
    # print("RandInt:")
    # print(np.random.randint(1, 10, 3))
    # print("Randn:")
    # print(np.random.randn(2, 4))
    # print("Choice:")
    # print(np.random.choice([10, 20, 30]))
    # print("Distribute:")
    # print(np.random.beta(1, 10, 100))
    # 3 Array Opes
    # print(np.arange(1, 11).reshape([2, -1]))
    # print("Exp")
    # print(np.exp(lst))
    # print("Exp2")
    # print(np.exp2(lst))
    # print("Sqrt")
    # print(np.sqrt(lst))
    # print("Sin")
    # print(np.sin(lst))
    # print("Log")
    # print(np.log(lst))
    # lst_1 = np.array([
    #     [
    #         [1, 2, 3, 4],
    #         [4, 5, 6, 7]
    #     ],
    #     [
    #         [7, 8, 9, 10],
    #         [10, 11, 12, 13]
    #     ],
    #     [
    #         [14, 15, 16, 17],
    #         [18, 19, 20, 21]
    #     ]
    # ])

    # print(lst_1.sum(axis=0))  # axis 越大越深入
    # print(lst_1.max())
    # print(lst_1.min())

    # lst1 = np.array([10, 20, 30, 40])
    # lst2 = np.array([4, 3, 2, 1])
    # # print(lst1**lst2)
    # # print(np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))
    # # print(np.concatenate((lst1, lst2), axis=0))
    # print(np.vstack((lst1, lst2)))
    # print(np.hstack((lst1, lst2)))
    # print(np.split(lst1, 2))

    # 4 liner
    # from numpy.linalg import inv
    # print(np.eye(3))
    st1 = np.array([
        [1, 2],
        [3, 4]
    ])

    # print(np.linalg.inv(st1))
    # print(st1.transpose())
    print(np.linalg.det(st1))


if __name__ == "__main__":
    star_main()
