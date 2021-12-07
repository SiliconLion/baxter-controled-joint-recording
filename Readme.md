# Controled Limb Recorder and Joint Position Playback

This is a program written by the undergrads of fall 2021, and lets you easily record poses you put Baxter in using the squeeze joint on his grippers. Then you can have Baxter playback the poses you put him in.
The advantage of this script over other methods is it only captures the poses you care about, rather than a ton of intermediate recordings as you get him into position. This makes it particularly useful for something like choreography. 

Note: We wrote the `controled_limb_recorder.py` script from scratch, but the `joint_position_file_playback.py` script was already written and can be found in baxter examples. We provide a copy of it here to make things easy. 

## Using these scripts 
1) Initialize Baxter like you normally would, (initializing the `eth0` port, and running `~/ros_ws/baxter.sh` in a seperate terminal)
2) In the terminal that ran `baxter.sh`, `cd` into the directory where the provided scripts are located.

### How To Take a Recording

1) Run the command, `python controled_limb_recorder.py path/to/output/file` where `path/to/output/file` is the relative path to where you want baxter to record his data.
2) Position baxter using his grippers however you like. Then press the circle button on his right gripper to record the position of all his joints.
3) Repeat step 4 for every position you want Baxter to record. 
4) When finished, press the pill shapped button on his right gripper. This will end the program. The recordings will be saved in the file you provided to the script initially.

### How To Play Back a recording
Note: The `controled_limb_recorder.py` script inserts default time stamps that go along with each recording. These start from when the program starts, and are in seconds elapsed. You can replace these timestamps with your own timestamps manually, if they are not what you wish. The rows of the file should remain chronological though.

1) Run the command `python joint_position_file_playback.py -f path/to/recording`
2) It may take a second to start but will playback the recording and terminate when done. 