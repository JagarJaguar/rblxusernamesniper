import string
import itertools

i = 0

def username_maker():
    base_chars = string.ascii_lowercase + string.digits

    for combo in itertools.product(base_chars, repeat=5):
        yield "".join(combo)

    for combo in itertools.product(base_chars, repeat=4):
        base_list = list(combo)

        yield "".join(base_list[:1] + ['_'] + base_list[1:])

        yield "".join(base_list[:2] + ['_'] + base_list[2:])

        yield "".join(base_list[:3] + ['_'] + base_list[3:])


max_bytes = 15728640
file_index = 0
current_bytes = 0
f = open(f'valid_names_new{file_index}.txt', 'w')

for name in username_maker():
    line = f'{name}\n'
    line_len = len(line)

    if current_bytes + line_len > max_bytes:
        f.close()
        file_index += 1
        f = open(f'valid_names_new{file_index}.txt', 'w')
        current_bytes = 0

    f.write(line)
    current_bytes += line_len

f.close()
print(f"Finished writing {file_index + 1} files.")

