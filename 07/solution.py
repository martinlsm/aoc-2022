def get_subtree(file_tree, pwd):
    sub_tree = file_tree
    for d in pwd:
        sub_tree = sub_tree[d]

    return sub_tree

def file_sizes_part1(file_tree, output_list):
    if type(file_tree) == int:
        return file_tree

    res = sum([file_sizes_part1(file_tree[key], output_list) for key in file_tree])
    if res < 100000:
        output_list.append(res)

    return res

def file_sizes(file_tree, output_list):
    if type(file_tree) == int:
        return file_tree

    res = sum([file_sizes(file_tree[key], output_list) for key in file_tree])
    output_list.append(res)

    return res


file_tree = {}
pwd = []

with open('input', 'r') as file:
    lines = [l.strip() for l in file.readlines()]

i = 0
while i < len(lines):
    line = lines[i]
    assert line.startswith('$')

    line_split = line.split(' ')
    cmd = line_split[1]
    match cmd:
        case 'ls':
            sub_tree = get_subtree(file_tree, pwd)
            j = i + 1
            while j < len(lines) and not lines[j].startswith('$'):
                l = lines[j].split(' ')
                if l[0] == 'dir':
                    dir_name = l[1]
                    if dir_name not in sub_tree:
                        sub_tree[dir_name] = {}
                else:
                    file_name = l[1]
                    file_size = int(l[0])
                    if file_name not in sub_tree:
                        sub_tree[file_name] = file_size
                j += 1

            i = j - 1

        case 'cd':
            where = line_split[2]
            match where:
                case '/':
                    pwd = []
                case '..':
                    pwd = pwd[:-1]
                case other:
                    pwd.append(other)

    i += 1

# Part 1
sizes = []
file_sizes_part1(file_tree, sizes)
print(sum(sizes))

# Part 2
sizes = []
total_size = file_sizes(file_tree, sizes)
minimum_space_to_free = total_size - (70000000 - 30000000)
print(min([sz for sz in sizes if sz > minimum_space_to_free]))
