from datetime import datetime, timedelta
# def generate_paper(change_contents:str, text_file_path = "./README.md"):
#     """
#     "README.md"의 paper를 월에 맞춰서 생성
#     """
#     new_contents = ''
#     with open(text_file_path,'r',encoding = 'utf-8') as f:
#         lines = f.readlines()
#         i = 0
#         while i < len(lines):
#             new_string = lines[i].strip()
#             new_contents += new_string + "\n"
#             if new_string == f"### {now.month}월 논문 발표":
#                 new_contents += '\n'
#                 j,result_string = change_table(lines[i+2:],change_contents)
#                 i = i+2+j
#                 new_contents += result_string + '\n'
#             i += 1
#     print(new_contents)

def find_topic(topic:str, content_list:list):
    i = 0
    now = datetime.now()
    end = now + timedelta(days = 5)
    date_format = f"### {now.strftime('%y.%m.%d')} {now.strftime('%a').upper()} - {end.strftime('%y.%m.%d')} {end.strftime('%a').upper()}\n\n"
    while i < len(content_list):
        new_string = content_list[i].strip()
        if new_string == date_format.strip():
            return -1
        elif new_string[:len(topic)] == topic:
            return i
        else:
            i += 1
    return i


# 임시 함수
def add_new_contents(topic:str, text_file_path = "./README.md"):
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
    name_format = '**📍임찬혁**\n**📍서동환**\n**📍박지완**\n**📍김태한**\n**📍임정아**\n**📍이은아**\n' #form 수정 필요
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

def update_week():
    add_new_contents("## 👋주간 회고지")
    add_new_contents("## 📝주간 정리 (optional)")

update_week()