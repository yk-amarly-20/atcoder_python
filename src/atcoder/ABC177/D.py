# Union Find 木
from collections import defaultdict

def main():
    n, m = list(map(int, input().split()))

    tree = UnionFindTree(n)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        if not tree.same(a - 1, b - 1):
            tree.union(a - 1, b - 1)

    # 長さの最大値を計算すればよい
    max_len = 0
    for l in list(tree.all_group_members().values()):
        max_len = max(max_len, len(l))

    print(max_len)

class UnionFindTree():

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """ xの親を探す

        Args:
            x (int): 探したい値

        Returns:
            parent (int): xの親
        """

        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """ x, yを含むそれぞれのグループを併合

        Args:
            x (int): 値1
            y (int): 値2
        """

        x = self.find(x)
        y = self.find(y)

        if (x == y):
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """xを含むgroupのサイズを返す
        """
        return - self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        """ xを含むgroupのメンバーを全て返す
        """

        root = self.find(x)

        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """ 根を全て返す
        """

        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """ groupの数を数える
        """

        return len(self.roots)

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

main()
