from core.normal import  NormalMode

def runnexa():
    normal = NormalMode()

    command = "open_chrome"

    function = getattr(normal, command, normal.default)

    function()