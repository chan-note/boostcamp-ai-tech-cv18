import sys,argparse
from datetime import datetime
from make_data import *

# set arguement
parser = argparse.ArgumentParser(description = 'Revise Readme')
parser.add_argument('-w','--week', action='store_true')
parser.add_argument('-m','--month', action='store_true')
parser.add_argument('-c','--changed')
parser.add_argument('-s','--save')

def return_index_next_matching(matching:str, lines:list, compare_string:str):
    '''
    lines에서 matching과 일치하는 곳이 있다면,
    내가 이전에 추가한 내용인지 아닌지를 확인한다. (날짜가 같으면 보통 내가 추가한 것이다.)
    그 곳의 index를 출력한다. (이는 줄 번호가 된다.)
    일치하는 곳이 없다면 그 파일의 마지막을 출력한다.
    '''
    for line_number, line in enumerate(lines):
        line = line.strip()
        # 날짜가 겹치는 지 확인한다. 겹치면 -1
        if line == compare_string:
            return -1
        elif matching == line[:len(matching)]:
            return line_number
    return line_number

def return_new_contents(contents:str, file_name:str, matching:str, next_string="## ", written_front= "True", paper_retro='False'):

    # 해당하는 곳을 찾는다.
    # 해당하는 곳에서 추가할 곳을 찾는다.
    # 내가 추가할 날짜와 겹친다면 내용을 수정하지 않는다.
    # 추가할 곳을 찾았다면, 바꾼다.
    # 변경된 data로 README.md를 update한다.
    # README.md를 읽는다.
    new_contents = ''
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line_number, line_content in enumerate(lines):
            new_contents += line_content
            line_content = line_content.strip() # 줄 개행 문자 제거

            # 만약, update를 원하는 곳을 찾았다면

            if line_content == matching:
                compare_format = check_format_and_return_title(matching) if not paper_retro else contents
                match_line_number = return_index_next_matching(next_string, lines[line_number+1:], compare_format)

                # 만약 contents가 겹친다면
                if match_line_number == -1:
                    # 뒤의 모든 내용을 새롭게 저장하고 break
                    new_contents += "".join(lines[line_number+1:])
                    return new_contents
                
                # contents가 겹치지 않는다면
                else:
                    if written_front: match_line_number -= 1
                    else: match_line_number += 1 
                    new_contents += "".join(lines[line_number+1:line_number+1+match_line_number])
                    # 그 matching된 곳에 써주고, 개행 문자를 남겨
                    new_contents += contents
                    new_contents += "".join(lines[line_number+1+match_line_number:])
                    return new_contents
                
        return  new_contents
    
def update_text(contents:str, file_name:str):
    with open(file_name,'w',encoding='utf-8') as f:
        f.write(contents)

if __name__ == "__main__":
    args = parser.parse_args()
    save_position = "./README.md" if args.save == None else args.save

    if args.week:
        week_data = generate_week_format()
        retro = return_new_contents(week_data+"\n", save_position, "## 👋주간 회고지")
        update_text(retro,save_position)
        
        note = return_new_contents(week_data+"\n", save_position, "## 📝주간 정리 (optional)")
        update_text(note,save_position)

    if args.month:
        # paper update 
        paper_data = generate_paper_format()
        paper = return_new_contents(paper_data+"\n", save_position, '## 📚논문 정리')
        update_text(paper,save_position)

    if args.changed:
        category,title,name = split_category_and_title(args.changed)
        print(category,title,name)
        print(category=='papers', category=='retros', category=='notes')
        if category == "papers":
            revise_data = revise_paper_format(title,name,args.changed)
            revise_ = return_new_contents(revise_data+"\n", save_position, '## 📚논문 정리', paper_retro=True)
            update_text(revise_, save_position)
            print("papers")
        elif category == "retros":
            next_string = f"- **📍{name}"
            revise_data = revise_week_format(title,args.changed)
            revise_ = return_new_contents(revise_data+"\n", save_position, "## 👋주간 회고지", next_string = next_string, written_front=False)
            update_text(revise_, save_position)
        elif category == "notes":
            next_string = f"- **📍{name}"
            revise_data = revise_week_format(title,args.changed)
            revise_ = return_new_contents(revise_data+"\n", save_position, "## 📝주간 정리 (optional)", next_string = next_string, written_front=False)
            update_text(revise_, save_position)