
from main import getmsg
def test_message_case():
    tittle = "Message"
    assert getmsg(tittle) == "<h1>" +tittle+ "</h1>"