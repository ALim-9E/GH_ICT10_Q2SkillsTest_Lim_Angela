# working with dropdown made from css and html
from pyscript import when, display, document

@when("click", "clubinfo")

def club_info(e):
    club1 = document.querySelector('#CA').value
    club2 = document.querySelector('#MA').value
    club3 = document.querySelector('#MO').value
    club4 = document.querySelector('#RC').value
    club5 = document.querySelector('#CO').value

    document.querySelector('#output').innerText = ""

    messages = """
    This is the first multi-line message.
    It spans across several lines.
    """,

    """
    This is the second multi-line message,
    providing different information.
    """,

    """
    And here is the third message,
    with its own unique content.
    """
    

# Display the first message
display(messages[0], target="output")
