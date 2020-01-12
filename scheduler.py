import threading
import subprocess
import sys
import os
import time

def execute(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        nextline = process.stdout.readline()
        if nextline == b'' and process.poll() is not None:
            break
        if nextline != b'' and nextline != '':
            # print(nextline.decode("UTF-8"), end='')
            pass
    output = process.communicate()[0]
    exitCode = process.returncode
    if (exitCode == 0):
        return output
    else:
        print("Process Exception Occurs")

def tor_run():
    tor_program = ["C:\\Users\\dongbin\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Tor\\tor"]
    tor_config = ["CookieAuthentication", "1", "ControlPort", "9051", "HashedControlPassword",
                    "16:DB4D0D522B4946F560DBA4D9B0E47C8BA3BC2A3F7CD69C4E30581900BF"]
    execute(tor_program + tor_config)

def node_run():
    execute(["node", "run.js"])

def exit():
    os.system("taskkill /f /im tor.exe")
    os.system("taskkill /f /im node.exe")
    run()

def run():
    threading.Timer(600, exit).start()
    t1 = threading.Thread(target=tor_run)
    t1.start()
    time.sleep(1)
    t2 = threading.Thread(target=node_run)
    t2.start()

run()