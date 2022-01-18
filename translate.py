import json
import os
import re
from pathlib import Path

symbols = [' ', '(', ')', '[', ']', '-', '{', '}', '%', "'", '"']


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
        key = key.lower()
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

    def __get_longest(self, s: str) -> (str, str):
        node2 = None
        key2 = ''
        node = self.__root
        key = ''
        for idx in range(len(s)):
            c = s[idx]
            n = node.child.get(c.lower())
            if n:
                key += c
                node = n
                if node.value and (idx + 1 >= len(s) or s[idx + 1] in symbols):
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
            if not (len(s2) == 0 or s2[-1] in symbols):
                s2 += s[0]
                s = s[1:]
                continue
            key, value = self.__get_longest(s)
            if key:
                s2 += value
                s = s[len(key):]
            else:
                s2 += s[0]
                s = s[1:]
        return s2


trie = RuneTrie()

with open('translate.tsv', 'r', encoding='utf-8') as f:
    f.readline()
    while True:
        line = f.readline().strip()
        if line:
            arr = line.split('\t')
            if len(arr) >= 2:
                if not trie.put_if_absent(arr[0], arr[1]):
                    raise ValueError("repeat: " + line)
        else:
            break

lines = []
regexp = re.compile(r'Description\("(.*?)"\)')
regexp_space = re.compile(r'''(?<![()\[\]{}%'"A-Za-z]) (?![()\[\]{}%'"A-Za-z])''')

with open('hk-split-maker/src/asset/hollowknight/splits.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if line:
            result = regexp.search(line)
            if result:
                a = result.group(1)
                b = regexp_space.sub('', trie.replace_all(a))
                line = line.replace(a, b, 1)
            lines.append(line)
        else:
            break

with open('hk-split-maker/src/asset/hollowknight/splits.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

lines = []
regexp = re.compile(r'return\s+\[.*?(?<=[\[(])["`](.*?)["`].*?];')
regexp1 = re.compile(r'return\s+\[.*?["`](.*?)["`](?=[)\]]).*?];')
start_qualifier = False
regexp2 = re.compile(r'["/](.*?)["/]')

with open('hk-split-maker/src/lib/hollowknight-splits.ts', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if line:
            if not start_qualifier and 'switch (qualifier) {' in line:
                start_qualifier = True
            if start_qualifier and line[0] == '{':
                start_qualifier = False
            result = regexp.search(line)
            if result:
                a = result.group(1)
                b = trie.replace_all(a).replace(' ', '')
                line = line.replace(a, b, 1)
            result = regexp1.search(line)
            if result:
                a = result.group(1)
                b = trie.replace_all(a).replace(' ', '')
                line = line.replace(a, b, 1)
            if start_qualifier:
                result = regexp2.search(line)
                if result:
                    a = result.group(1)
                    b = trie.replace_all(a).replace(' ', '')
                    line = line.replace(a, b, 1)
            lines.append(line)
        else:
            break

with open('hk-split-maker/src/lib/hollowknight-splits.ts', 'w', encoding='utf-8') as f:
    f.writelines(lines)

file = Path('hk-split-maker/src/components/App.tsx')
content = file.read_text('utf-8')
content = content.replace('<h2>Input config JSON</h2>', '<h2>输入配置JSON</h2>')
content = content.replace('<h2>Output Splits File</h2>', '<h2>输出Splits文件</h2>')
content = content.replace('text="Generate"', 'text="生成"')
content = content.replace('text="Download"', 'text="下载"')
file.write_text(content, 'utf-8')

file = Path('hk-split-maker/src/components/CategorySelect.tsx')
content = file.read_text('utf-8')
content = content.replace('"Pre-made Category: Select or type to search..."', '"选择预设模板..."')
file.write_text(content, 'utf-8')

file = Path('hk-split-maker/src/components/SplitSelect.tsx')
content = file.read_text('utf-8')
content = content.replace('"Add autosplit: Select or type to search..."', '"增加片段..."')
file.write_text(content, 'utf-8')

file = Path('hk-split-maker/src/components/AlertBanner.tsx')
content = file.read_text('utf-8')
content = content.replace('Interested in contributing or suggesting ideas and splits? Check out the',
                          '''如果您想要为汉化做贡献，欢迎前往
      <a href="https://github.com/CuteReimu/hk-split-maker" target="_blank" rel="noopener noreferrer">
      我们的汉化Github工程</a>。如果您想要为网页功能或原英文版网页做贡献，欢迎前往''')
file.write_text(content, 'utf-8')

path = 'hk-split-maker/src/asset/hollowknight/categories'
files = os.listdir(path)
for file_name in files:
    file_path = os.path.join(path, file_name)
    if file_name == 'category-directory.json':
        file = Path(file_path)
        content = file.read_text('utf-8')
        json_result = json.loads(content)
        for d in json_result.values():
            for obj in d:
                obj['displayName'] = regexp_space.sub('', trie.replace_all(obj['displayName']))
        content = json.dumps(json_result, indent=4, ensure_ascii=False)
        file.write_text(content, 'utf-8')
    elif file_name.endswith('.json'):
        file = Path(file_path)
        content = file.read_text('utf-8')
        json_result = json.loads(content)
        if 'names' in json_result:
            j = json_result['names']
            for k, v in j.items():
                if isinstance(v, list):
                    for i in range(len(v)):
                        v[i] = regexp_space.sub('', trie.replace_all(v[i]))
                else:
                    j[k] = regexp_space.sub('', trie.replace_all(v))
        if 'endingSplit' in json_result:
            j = json_result['endingSplit']
            j['name'] = regexp_space.sub('', trie.replace_all(j['name']))
        content = json.dumps(json_result, indent=4, ensure_ascii=False)
        file.write_text(content + '\n', 'utf-8')
