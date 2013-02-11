#!/usr/bin/env python

import os,  sys,  subprocess

# Define a few constants.
ROUTE = 3         # Output device
SWITCH = 2        # Mute
VOLUME = 1        # Volume

HDMI = 2          # Use HDMI device
PHONES = 1        # Use headphone socket
AUTO = 0          # Decide automatically

MUTE = 0          # Mute sound
UNMUTE = 1        # Unmute sound

# Various helper functions to do the work.
def cset_command(numid,  value):
    stdout = os.popen("amixer cset numid=%d %s"  % (numid,  value))
    try:
        response = stdout.read()
    except:
        print "Error  exception detected."
    finally:
        stdout.close()
    
def cget_command(numid):
    response = None

    stdout = os.popen("amixer cget numid=%d"  % numid)
    try:
        response = stdout.read()
    except:
        print "Error  exception detected."
    finally:
        stdout.close()

    if response:
        return response.split(':')[1].split('\n')[0].split('=')[1].strip()
    else:
        return None

    
def do_auto():
    """do_auto - sets the sound output to be automatically determined. If there is an HDMI device connected, sound will go there, otherwise, to the headphone socket."""
    cset_command(ROUTE,  AUTO)

    
def do_hdmi():
    """do_hdmi - forces the sound output to use the HDMI device."""
    cset_command(ROUTE,  HDMI)

    
def do_headphones():
    """do_headphones - forces the sound output to use the headphone socket."""
    cset_command(ROUTE,  PHONES)

    
def do_device():
    """do_device - Finds out which device has the sound output."""
    route = cget_command(ROUTE)
    if route:
        return ['Auto','Headphones','HDMI'][int(route)]
    else:
        return 'Device unknown, cannot call amixer command.'

def do_mute():
    """do_mute - disables the sound."""
    cset_command(SWITCH,  MUTE)
    

def do_unmute():
    """do_unmute - enables the sound."""
    cset_command(SWITCH,  UNMUTE)

    
def do_muted():
    """do_muted - reads and returns the current mute status."""
    switch = cget_command(SWITCH)
    if switch:
        return {'on': 'unmuted', 'off': 'muted'}[switch]
    else:
        return 'Muted status unknown, cannot call amixer command.'


def do_volume():
    """do_volume - reads and returns the current volume."""
    volume = cget_command(VOLUME)
    if volume:
        return str(int(((float(volume) + 10240) / 10640) * 100)) + '%' 
    else:
        return 'Volume setting unknown, cannot call amixer command.'

    
def do_set_volume(percent):
    """do_set_volume sets the volume to a given percentage."""
    
    # Strip any leading or trailing whitespace from the volume setting.
    percent = percent.strip()

    # If there is a trailing '%' then remove that too. We need it later, but not
    # when supplied as a parameter - that's optional.
    if (percent.endswith("%")):
       percent = percent.strip("%")

    # Make sure what we are left with is indeed a number. If this works
    # then from here onwards, percent is numeric, no longer a string.
    try:
        percent = int(percent)
    except:
        print "Invalid percentage for volume setting. ('%s')." % percent
        return
        
    # Keep in range 0 to 100
    if (percent < 0):
        percent = 0
        
    if (percent > 100):
        percent = 100
        
    # Set the volume.
    cset_command(VOLUME,  "%d%%" % percent)

    
def do_settings():
    """do_settings - reads and returns the current settings."""
    print do_device() + ':' +  \
          do_muted() + ':' +         \
          do_volume()


def do_help():
    print """
The "sound" utility allows you to adjust certain parameters of the Raspbery Pi
sound system. The usage is:
    
\tsound <parameter>
    
Where <parameter> is one of the following:
    
AUTO\t\tSets the sound output to be automatically detected. Normally 
\t\tthis means that if a monitor or TV is connected to the HDMI 
\t\tsocket,  the sound will be directed to that device, otherwise, 
\t\tit is directed to the headphone socket.
    
HDMI\t\tForces the sound to the HDMI conector.
    
HEADPHONES\tForces the sound to the headphone socket. This is 
\t\tuseful if your HDMI device doesn't have decent 
\t\t(or any!) speakers.
    
DEVICE\t\tThis returns a value that tells you where the current sound 
\t\toutput is this will be one of "auto", "hdmi" or ;"headphones".
                   
MUTE\t\tMutes the sound.
    
UNMUTE\t\tUnmutes the sound.
    
MUTED\t\tThis command returns a string "on" or "off" that tells you the 
\t\tcurrent muted state of the sound system. "muted" means that 
\t\tthere is no sound - it has been muted, "unmuted" means sound 
\t\tshould be audible.
                  
VOLUME\t\tReturns a number representing the current volume as a 
\t\tpercentage.
    
n%\t\tThis command sets the volume to the desired percentage. If this
\t\tis outside of the range 0% to 100% then it will be adjusted to 
\t\tremain withing the range of valid values.
    
HELP\t\tDisplays this help text.
    
SETTINGS\tThis command displays the current settings and is equivalent
\t\tto calling DEVICE, MUTED and VOLUME.
    """
        
if __name__ == "__main__":
    #    Do stuff here if we executed this as a program.
    
    # We need only one parameter, so check for two!
    if len(sys.argv) != 2:
        do_help()
        sys.exit(1)
        
    # Get the parameter and lower case it.
    Command = sys.argv[1].lower()
    
    if Command == "help":
        do_help()
    elif Command == "auto":
        do_auto()
    elif Command == "hdmi":
        do_hdmi()
    elif Command == "headphones":
        do_headphones()
    elif Command == "device":
        print do_device()
    elif Command == "mute":
        do_mute()
    elif Command == "unmute":
        do_unmute()
    elif Command == "muted":
        print do_muted()
    elif Command == "volume":
        print do_volume()
    elif Command == "settings":
        do_settings()
    else:
        do_set_volume(Command)
    
    # All done. Exit.
    sys.exit(0)
