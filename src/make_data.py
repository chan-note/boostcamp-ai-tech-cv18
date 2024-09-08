
from datetime import datetime, timedelta
now = datetime.now()
end = now + timedelta(days = 5)

__init__ = ['generate_week_title', 'generate_paper_title', 'generate_paper', 'generate_week_format']

def generate_week_title():
    return f"### {now.strftime('%y.%m.%d')} {now.strftime('%a').upper()} - {end.strftime('%y.%m.%d')} {end.strftime('%a').upper()}"

def generate_paper_title():
    return f"## {now.month}월 논문 발표"

def generate_paper(paper_name:str, reviewer:str):
    return f'|{paper_name}|{reviewer}|'

def generate_week_format():
    week_format = generate_week_title()
    data = '- **📍임찬혁**\n- **📍서동환**\n- **📍박지완**\n- **📍김태한**\n- **📍임정아**\n- **📍이은아**'
    return f'\n{week_format}\n\n{data}'

def generate_paper_format(changed_file:str):
    # 확장자 분리
    name_list,_ = changed_file.split(".")

    # title, 이름, 버전으로 분리
    name_list = name_list.split("_")
    if name_list[-1].isdigit():
        name = name_list[-2]
        name_index = -2
    else:
        name = name_list[-1]
        name_index = -1
    return generate_paper(" ".join(name_list[0:name_index]),name)
        