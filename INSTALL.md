DOWNLOAD
--------

You will need to have the git-core package installed on your RaspberryPi. If you have not
already done so, the following will install it for you:

    $ sudo apt-get update
    $ sudo apt-get install git-core

You can now download PiSound as follows:

    $ git clone https://github.com/NormanDunbar/PiSound.git

This command will create a directory, beneath where you currently are, named PiSound and all
the required files will be copied into it.


TESTING
-------

You can test the software, to see if it is of any use to you, as follows:

    $ cd PiSound                    # Make sure we are in the right place
    $ ./sound.py 65%                # To set the volume to 65%
    $ ./sound.py headphones         # Set output to the headphone socket
    $ ./sound.py unmute             # To unmute audio
    

INSTALLING
----------

The file sound.py is all that is required. The easiest way to install it is as follows:

    $ cd PiSound                     # If necessary
    $ sudo cp sound.py /usr/local/bin/
    $ sudo chmod a+x /usr/local/bin/sound.py
    $ sudo ln /usr/local/bin/sound.py /usr/local/bin/sound

Now it can be executed as follows:

    $ sound.py a_parameter

or, simply:

    $ sound a_parameter

    
UNINSTALLING
------------

It could happen! You have tried it and don't like it. That's fine. If you didn't follow
the instructions in the INSTALLING section above, all you need to do is:

    $ cd ..                         # Make sure we are out of the PiSound directory
    $ rm -Rf ./PiSound              # Remove it.
    
If you have installed PiSound, then additionally, the following is required:

    $ sudo rm /usr/local/bin/sound.py
    $ sudo rm /usr/local/bin/sound
    
Hopefully, you will enjoy it!

Have fun.
