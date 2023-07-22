import os

rust_file = open('../rust_file.rs', 'w')

print("""
use std::collections::HashMap;

fn create_bible() -> HashMap<&'static str, &'static str> {
\tlet bible = HashMap::from([""", file=rust_file)

is_first = True

for dir in os.listdir():
    if os.path.isdir(dir):
        os.chdir(dir)
        for file_name in os.listdir():
            file = open(file_name, 'r')

            for line in file:
                if line != '\n':

                    key = file_name.split('.')[0].replace('_', ' ')
                    verse = line.split(' ', 1)[0]

                    if is_first:
                        print(f"\t\t(\"{key} {verse}\", \"{line.split(' ', 1)[1].strip()}\")", file=rust_file, end='')
                        is_first = False
                    else:
                        print(f",\n\t\t(\"{key} {verse}\", \"{line.split(' ', 1)[1].strip()}\")", file=rust_file, end='')
        os.chdir('..')


print("""\n\t]);

\treturn bible;
    
}
""", file=rust_file)