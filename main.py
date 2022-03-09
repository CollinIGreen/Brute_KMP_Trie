import timeit
#import line_profiler
import memory_profiler
def BruteForce(str, search):
    count = 0
    for i in range(len(str)):
        for x in range(len(search)):
            if len(search) <= int(len(str)-i):
                if str[i+x] != search[x]:
                    break
                if x+1 == len(search):
                    count += 1
            else:
                break
    return count
class kmpSearch:
    def __init__(self):
        self.string = ""
        self.key = [None]
        self.keyCode = [None]
    def MakeKey(self, Key):
        for i in range(len(Key)):
            self.key.append(Key[i])
        for i in range(1, int(len(Key)+1)):
            for x in range(0, i):
                if self.key[x] == self.key[i]:
                    self.keyCode.append(x)
            if len(self.keyCode) != i+1:
                self.keyCode.append(0)
        return self.keyCode
    def kmpSearch(self, string):
        i = 0
        j = 0
        count = 0
        while i != len(string):
            if string[i] == self.key[j+1]:
                j += 1
                if j == len(self.key)-1:
                    j = 0
                    count += 1
                i += 1
            elif j != 0:
                j = self.keyCode[j]
            else:
                i += 1
        return count
class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.locations = []
class Trie:
    def __init__(self):
        self.root = Node(None)
    def buildTree(self, str, wSearch):
        for i in range(len(str) - len(wSearch)):
            string = str[i: i + len(wSearch)]
            self.insert(string, i)
    def insert(self, text, location):
        curNode = self.root
        for char in text:
            if len(curNode.children) != 0:
                check = False
                for index in curNode.children:
                    if char == index:
                        curNode = curNode.children[char]
                        check = True
                        break
                if check == False:
                    curNode.children[char] = Node(char)
                    curNode = curNode.children[char]
            else:
                curNode.children[char] = Node(char)
                curNode = curNode.children[char]
        curNode.locations.append(location)
    def search(self, text, search):
        self.buildTree(text, search)
        curNode = self.root
        check = False
        for key in search:
            check = False
            for branch in curNode.children:
                if key == branch:
                    check = True
                    curNode = curNode.children[key]
            if check == False:
                break
        if check == True:
            return len(curNode.locations)
        else:
            return 0
file = open("macbeth.txt")
line = file.read().replace("\n", " ")
file.close()
@profile
def trieSearch():
    trie = Trie()
    print(trie.search(line, "MACBETH"))
@profile
def mbSearch():
    count = BruteForce(line, "MACBETH")
    print(count)
@profile
def kmpSearcher():
    KMP = kmpSearch()
    KMP.MakeKey("MACBETH")
    count = KMP.kmpSearch(line)
    print(count)
mbSearch()
kmpSearcher()
trieSearch()
#print("Brute Force")
#print(timeit.timeit(mbSearch, number=1))
#print("KMP")
#print(timeit.timeit(kmpSearcher, number=1))
#print("Trie")
#print(timeit.timeit(trieSearch, number=1))