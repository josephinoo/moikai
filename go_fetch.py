
import click                                              # Make beautiful command line applications
from datetime import timedelta                            # Format times correctly
from platform import system, release, linux_distribution  # Get information about Linux distributions


"""Handle Exceptions"""
def handleExceptions(function):
    def handle(*args):
        try:
            return function(*args)
        except NotImplementedError as error:
            error = {"name": "not implemented error",
                     "description": str(error),
                     "action": "Give the developer a gentle prod.",
                    "code": 1}
        except ValueError as error:
            try:
                click.launch('http://https://github.com/DylanHamer/GoFetch/issues')
            except:
                click.secho("Warning: Could not open browser", fg="orange")
                error = {"name": "value error",
                         "description": str(error),
                         "action": "Report an issue on Github.",
                         "code": 2}
        except BaseException as error:
            error = {"name": "Not implemented error",
                     "description": str(error),
                     "action": "Give the developer a gentle prod.",
                     "code": 2}
   
@handleExceptions
def generateOSInfo():
    osType = system()
    osVersion = release()
    if osType == "Linux":
        linux = True
        distroName =  linux_distribution()[0]
        distroVersion = linux_distribution()[1]
    else:
        linux = False
        distroName = None
        distroVerson = None
    osInformation = {"os":osType,
                     "osVersion":osVersion,
                     "isLinux":linux,
                     "distro":distroName,
                     "distroVersion":distroVersion
                    }
    return osInformation

"Display OS Information"""
@handleExceptions
def displayOSInformation(highlight='cyan'):
    osInformation = generateOSInfo()
    click.secho("OS: ", nl=False)
    if osInformation["isLinux"]:
         click.secho(osInformation["distro"][0].upper() + osInformation["distro"][1:] + " " + osInformation["distroVersion"], fg=highlight)
         click.secho("Kernel: ", nl=False)
         click.secho("Linux " + osInformation["osVersion"], fg=highlight)

    else:
        click.secho(osInformation["os"] + osInformation["osVersion"])


"""Get uptime and return it in H:M:S format"""
@handleExceptions
def getUptime():
    with open('/proc/uptime', 'r') as f:
        totalUptime = float(f.readline().split()[0])
        uptime = str(timedelta(seconds = totalUptime)).split(":")
        hours = uptime[0]
        minutes = uptime[1]
        seconds = uptime[2]
    return hours, minutes, seconds

"""Display uptime"""
@handleExceptions
def displayUptime(highlight='cyan'):
    hours, minutes, seconds = getUptime()
    click.secho("Uptime: ", nl=False)
    click.secho(hours, fg=highlight, nl=False)
    click.secho(" hours ", nl=False)
    click.secho(minutes, fg=highlight, nl=False)
    click.secho(" minutes")


"""Main Function"""
@handleExceptions
@click.command()
@click.option('--highlight', default='cyan')
def main(highlight):
    displayOSInformation(highlight)
    displayUptime(highlight)

if __name__ == "__main__":
    main() 
