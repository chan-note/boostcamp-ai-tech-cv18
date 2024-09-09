
from datetime import datetime, timedelta
now = datetime.now()
end = now + timedelta(days = 5)

__init__ = ['generate_week_title', 'generate_paper_title', 'generate_paper', 'generate_week_format']

def generate_week_title():
    return f"### {now.strftime('%y.%m.%d')} {now.strftime('%a').upper()} - {end.strftime('%y.%m.%d')} {end.strftime('%a').upper()}"

def generate_paper_title():
    return f"### {now.month}월 논문 발표"

def generate_paper_format():
    return f"\n{generate_paper_title()}\n\n| 논문 제목 | 리뷰어 |\n| ----- | --- |"

def generate_week_format():
    week_format = generate_week_title()
    data = '- **📍임찬혁**\n- **📍서동환**\n- **📍박지완**\n- **📍김태한**\n- **📍임정아**\n- **📍이은아**'
    return f'\n{week_format}\n\n{data}'

def check_format_and_return_title(format:str):
    if format == "## 👋주간 회고지" or format == "## 📝주간 정리 (optional)":
        return generate_week_title()
    elif format == '## 📚논문 정리':
        return generate_paper_title()
    else :return ''

def split_category_and_title(changed_file:str):
    # split directory and name
    directory_and_name = changed_file.split("/")
    directory, name = directory_and_name[0], directory_and_name[-1]

    # split title_name_version and extension
    title_name_version, _ = name.split(".")

    # title, 이름, 버전으로 분리
    title_name_version = title_name_version.split("_")
    if title_name_version[-1].isdigit():
        name = title_name_version[-2]
        name_index = -2
    else:
        name = title_name_version[-1]
        name_index = -1
    title = " ".join(title_name_version[0:name_index])
    return (directory,title,name)

def revise_paper_format(paper_name:str, reviewer:str, url:str):
    return f'|{paper_name}|[{reviewer}]({url})|'

def revise_week_format(title:str, url:str):
    return f"\t- [{title}]({url})"