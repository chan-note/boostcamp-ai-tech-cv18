from datetime import datetime, timedelta
now = datetime.now()
end = now + timedelta(days = 5)
new_contents = ''

date_format = f"### {now.strftime('%y.%m.%d')} {now.strftime('%a').upper()} - {end.strftime('%y.%m.%d')} {end.strftime('%a').upper()}\n\n"

def find_topic(topic:str, content_list:list):
    i = 0
    now = datetime.now()
    end = now + timedelta(days = 5)
    date_format = f"### {now.strftime('%y.%m.%d')} {now.strftime('%a').upper()} - {end.strftime('%y.%m.%d')} {end.strftime('%a').upper()}\n\n"
    while i < len(content_list):
        new_string = content_list[i].strip()
        # 만약 같은 폼이 있으면
        if new_string == date_format.strip():
            # update 안하게끔 만듬
            return -1
        elif new_string[:len(topic)] == topic:
            return i
        else:
            i += 1
    return i


# 임시 함수
def add_new_contents(topic:str, text_file_path = "../README.md"):
    """
    한 주마다 topic을 찾을 경우
    그 topic의 맨 아랫줄에 새로운 폼을 추가함.

    '### 24.09.02 MON - 24.09.06 FRI'를 만듬
    사람 이름 - 으로 시작하는 폼을 만듬
    
    """
    now = datetime.now()
    end = now + timedelta(days = 5)
    new_contents = ''

    date_format = f"### {now.strftime('%y.%m.%d')} {now.strftime('%a').upper()} - {end.strftime('%y.%m.%d')} {end.strftime('%a').upper()}\n\n"
    name_format = '- **📍임찬혁**\n- **📍서동환**\n- **📍박지완**\n- **📍김태한**\n- **📍임정아**\n- **📍이은아**\n' #form 수정 필요
    put_string = date_format + name_format

    with open(text_file_path,'r',encoding = 'utf-8') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            new_string = lines[i].strip()
            new_contents += new_string + "\n"

            if new_string == topic:

                next_line = i+1
                a = find_topic("## ",lines[next_line:])

                if a >= 0:
                    # 다음 topic 전까지 전부 추가
                    new_contents += "".join(lines[next_line:next_line+a])

                    # topic부분에 내용 추가
                    new_contents += put_string + "\n"

                    # # 뒷 내용 추가, break
                    new_contents += "".join(lines[next_line+a:])
                else:
                    new_contents += "".join(lines[next_line:])
                break
            i += 1


    with open(text_file_path,'w',encoding='utf-8') as f:
        f.write(new_contents)


def add_paper(change_contents:str, text_file_path = "../README.md"):
    """
    "README.md"의 paper를 월에 맞춰서 생성
    """
    new_contents = ''
    with open(text_file_path,'r',encoding = 'utf-8') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            new_string = lines[i].strip()
            new_contents += new_string + "\n"
            if new_string == f"### {now.month}월 논문 발표":
                new_contents += '\n'
                j,result_string = (lines[i+2:],change_contents)
                i = i+2+j
                new_contents += result_string + '\n'
            i += 1
    print(new_contents)

def return_index_next_matching(matching:str, lines:list):
    '''
    lines에서 matching과 일치하는 곳이 있다면,
    내가 이전에 추가한 내용인지 아닌지를 확인한다. (날짜가 같으면 보통 내가 추가한 것이다.)
    그 곳의 index를 출력한다. (이는 줄 번호가 된다.)
    일치하는 곳이 없다면 그 파일의 마지막을 출력한다.
    '''
    for line_number, line in enumerate(lines):
        line = line.strip()
        if matching == line[:len(matching)]:
            # 날짜가 겹치는 지 확인한다.
            # 겹치면 -1 (추가하지 말라)를 추가한다.
            # 안 겹치면 그 줄의 line_number를 출력한다.
                if matching == f"### {now.month}월 논문 발표" or matching == date_format:
                    return -1
                else:
                   return line_number
    line_number += 1 
    return line_number

def update_contents(contents:str, file_name:str, matching:str):
    # README.md를 읽는다.
    new_contents = ''
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line_number, line_content in enumerate(lines):
            new_contents += line_content
            line_content = line_content.strip() # 줄 개행 문자 제거

            # 만약, update를 원하는 곳을 찾았다면
            if line_content == matching:
                match_line_number = return_index_next_matching("## ", lines[line_number+1:])
                
                # 만약 contents가 겹친다면
                if match_line_number == -1:
                    # 뒤의 모든 내용을 새롭게 저장하고 break
                    new_contents = "".join(lines[line_number+1:])
                    return new_contents
                
                # contents가 겹치지 않는다면
                else:
                    new_contents += "".join(lines[line_number+1:line_number+1+match_line_number])
                    # 그 matching된 곳에 써주고, 개행 문자를 남겨
                    new_contents += contents
                    new_contents += "".join(lines[line_number+1+match_line_number:])


    # 해당하는 곳을 찾는다.
    # 해당하는 곳에서 추가할 곳을 찾는다.
    # 내가 추가할 날짜와 겹친다면 내용을 수정하지 않는다.
    # 추가할 곳을 찾았다면, 바꾼다.
    # 변경된 data로 README.md를 update한다.


def update_week():
    add_new_contents("## 👋주간 회고지")
    add_new_contents("## 📝주간 정리 (optional)")

update_week()