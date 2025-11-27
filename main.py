# working with dropdown made from html
from pyscript import when, document

@when("change", "#club_select")
def update_club_info(e):
        selected_club_key = document.querySelector('#club_select').value

        print(f"User selected key: {selected_club_key}")

        output_text = CLUB_INFO.get(selected_club_key, "")

        
        document.querySelector('#output').innerText = output_text
    
CLUB_INFO = {
        'CA': """
    # Club Info: Communication Arts
    Description: A club to express your talent in writing, hosting, and acting!
    Meeting time: 2:30 TO 4:30
    Location: Room 610
    Club Moderator: Sir Loreto
    No. of Members: 25
    """,

        'MB': """
    # Club Info: Marching Band
    Description: A club to express your talent in playing musical instruments!
    Meeting time: 3:00 TO 4:00
    Location: Gallery
    Club Moderator: Sir Almine
    No. of Members: 30
    """,

        'MO': """
    # Club Info: Monarchs
    Description: A club to express your talent in dancing!
    Meeting time: 2:00 TO 3:00
    Location: MM Hall
    Club Moderator: Sir Marutani
    No. of Members: 15
    """,

        'RC': """
    # Club Info: Rainbow Catering
    Description: A club to express your talent in baking and cooking!
    Meeting time: 2:30 TO 3:30
    Location: TLE Lab
    Club Moderator: Ma'am Jimenez
    No. of Members: 20
    """,

        'CO': """
    # Club Info: COCC
    Description: A club to express your talent in leadership and discipline!
    Meeting time: 1:30 TO 2:30
    Location: Quadrangle
    Club Moderator: Ma'am Mobilla
    No. of Members: 35
    """
}

