text_file_path = "./README.md"


def change_file(text_file_path:str):
    new_contents = ''
    with open(text_file_path,'r',encoding = 'utf-8') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            new_string = lines[i].strip()
            if new_string == "### 9월 논문 발표":
                new_contents += new_string + '\n' + '\n'
                j = i+2
                fine_string = lines[j].strip()
                while fine_string != '':
                    new_contents += fine_string + '\n'
                    print(fine_string)
                    j += 1                    
                    fine_string = lines[j].strip()
                new_string = '|asdf|asdf|\n'
                i = j
            new_string += '\n'
            i += 1
            new_contents += new_string

    print(new_contents)


change_file(text_file_path)