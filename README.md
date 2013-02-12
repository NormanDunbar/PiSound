PiSound
=======

A small utility to manage sound on the Raspberry Pi. Where it goes, volume, mute etc. From the command line.

The "sound" utility allows you to adjust certain parameters of the Raspbery Pi
sound system. The usage is:
    
        sound a_parameter
    
Where a_parameter is one of the following:
    
*   AUTO            Sets the sound output to be automatically detected. Normally 
                this means that if a monitor or TV is connected to the HDMI 
                socket,  the sound will be directed to that device, otherwise, 
                it is directed to the headphone socket.
    
*   HDMI            Forces the sound to the HDMI connector.
    
*   HEADPHONES      Forces the sound to the headphone socket. This is 
                useful if your HDMI device doesn't have decent 
                (or any!) speakers.
    
*   DEVICE          This returns a value that tells you where the current sound 
                output is this will be one of "auto", "hdmi" or "headphones".
                   
*   MUTE            Mutes the sound.
    
*   UNMUTE          Unmutes the sound.
    
*   MUTED           This command returns a string "on" or "off" that tells you the 
                current muted state of the sound system. "muted" means that 
                there is no sound - it has been muted, "unmuted" means sound 
                should be audible.
                  
*   VOLUME          Returns a number representing the current volume as a 
                percentage.
    
*   n%              This command sets the volume to the desired percentage. If this
                is outside of the range 0% to 100% then it will be adjusted to 
                remain within the range of valid values. The actual '%' sign is optional.
    
*   HELP            Displays this help text.
    
*   SETTINGS        This command displays the current settings and is equivalent
                to calling DEVICE, MUTED and VOLUME.


