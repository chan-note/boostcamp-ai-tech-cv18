
from datetime import datetime, timedelta
now = datetime.now()
end = now + timedelta(days = 5)

def generate_paper(paper_name:str, reviewer:str):
    return f'|{paper_name}|{reviewer}|'

def generate_week_title():
    return f"### {now.strftime('%y.%m.%d')} {now.strftime('%a').upper()} - {end.strftime('%y.%m.%d')} {end.strftime('%a').upper()}"

def generate_week_format():
    week_format = generate_week_title()
    data = '- **📍임찬혁**\n- **📍서동환**\n- **📍박지완**\n- **📍김태한**\n- **📍임정아**\n- **📍이은아**\n'
    return f'{week_format}/n/n{data}'
