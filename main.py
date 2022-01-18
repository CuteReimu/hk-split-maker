import re


class RuneTrieNode:
    def __init__(self):
        self.child = {}
        self.value = None


class RuneTrie:
    def __init__(self):
        self.__root = RuneTrieNode()

    def put_if_absent(self, key: str, value) -> bool:
        if not value:
            raise ValueError('cannot put a nil value')
        node = self.__root
        for c in key:
            n = node.child.get(c)
            if n:
                node = n
            else:
                new_node = RuneTrieNode()
                node.child[c] = new_node
                node = new_node
        if node.value:
            return False
        node.value = value
        return True

    def get_longest(self, s: str) -> (str, str):
        node2 = None
        key2 = ''
        node = self.__root
        key = ''
        for c in s:
            n = node.child.get(c)
            if n:
                key += c
                node = n
                if node.value:
                    node2 = node
                    key2 = key
            else:
                break
        if node2:
            return key2, node2.value
        return '', ''

    def replace_all(self, s: str) -> str:
        s2 = ''
        while s:
            key, value = self.get_longest(s)
            if key:
                s2 += value
                s = s[len(key):]
            else:
                s2 += s[0]
                s = s[1:]
        return s2


trie = RuneTrie()

with open('translate.tsv', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline().strip()
        if line:
            arr = line.split('\t')
            if len(arr) >= 2:
                if not trie.put_if_absent(arr[0], arr[1]):
                    raise ValueError(line)
        else:
            break

lines = []

regexp = re.compile(r'Description\("(.*?)"\)')

with open('hk-split-maker/src/asset/hollowknight/splits.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if line:
            result = regexp.search(line)
            if result:
                a = result.group(1)
                b = trie.replace_all(a).replace(' ', '').replace('（', ' (').replace('）', ')')
                line = line.replace(a, b, 1)
            lines.append(line)
        else:
            break

with open('hk-split-maker/src/asset/hollowknight/splits.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

with open('hk-split-maker/src/components/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()
    content = content.replace('<h2>Input config JSON</h2>', '<h2>输入配置JSON</h2>')
    content = content.replace('<h2>Output Splits File</h2>', '<h2>输出Splits文件</h2>')
    content = content.replace('text="Generate"', 'text="生成"')
    content = content.replace('text="Download"', 'text="下载"')

with open('hk-split-maker/src/components/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

with open('hk-split-maker/src/components/CategorySelect.tsx', 'r', encoding='utf-8') as f:
    content = f.read()
    content = content.replace('"Pre-made Category: Select or type to search..."', '"选择预设模板..."')

with open('hk-split-maker/src/components/CategorySelect.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

with open('hk-split-maker/src/components/SplitSelect.tsx', 'r', encoding='utf-8') as f:
    content = f.read()
    content = content.replace('"Add autosplit: Select or type to search..."', '"增加片段..."')

with open('hk-split-maker/src/components/SplitSelect.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
