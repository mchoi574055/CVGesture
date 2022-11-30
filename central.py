import keypress
import serial

ser = serial.Serial("COM5", timeout=1, dsrdtr=False)
# constants
DEBOUNCER = 10

def main():
    
    line = ""
    isPlaying = False
    vol_up_counter = 0
    vol_down_counter = 0
    next_track_counter = 0
    prev_track_counter = 0
    play_counter = 0
    pause_counter = 0



    while(True):
        line = ser.readline().strip()
        print(line)

        # play
        if line == "fist":                  # Change this line
            if play_counter <= DEBOUNCER:
                play_counter += 1
            else:
                if not isPlaying:
                    keypress.play_pause()
                    isPlaying = True
                    play_counter = 0
                    print("Play")

            # reset other counters
            vol_up_counter = 0
            vol_down_counter = 0
            next_track_counter = 0
            prev_track_counter = 0
            pause_counter = 0

        # pause
        elif line == "highfive":           # Change this line
            if pause_counter <= DEBOUNCER:
                pause_counter += 1
            else:
                if isPlaying:
                    keypress.play_pause()
                    isPlaying = False
                    pause_counter = 0
                    print("Pause")
            
            # reset other counters
            vol_up_counter = 0
            vol_down_counter = 0
            next_track_counter = 0
            prev_track_counter = 0
            play_counter = 0


        # previous track
        elif line == "left":          # Change this line
            if prev_track_counter <= DEBOUNCER:
                prev_track_counter += 1
            else:
                keypress.prev_track()
                prev_track_counter = 0
                print("Previous track")

                # YouTube will automatically play when change track
                if isPlaying == False: isPlaying = True

            # reset other counters
            vol_up_counter = 0
            vol_down_counter = 0
            next_track_counter = 0
            play_counter = 0
            pause_counter = 0

        # next track
        elif line == "right":         # Change this line
            if next_track_counter <= DEBOUNCER:
                next_track_counter += 1
            else:
                keypress.next_track()
                next_track_counter = 0
                print("Next track")

                # YouTube will automatically play when change track
                if isPlaying == False: isPlaying = True

            # reset other counters
            vol_up_counter = 0
            vol_down_counter = 0
            prev_track_counter = 0
            play_counter = 0
            pause_counter = 0


        # volume up
        elif line == "up":            # Change this line

            if vol_up_counter <= DEBOUNCER:
                vol_up_counter += 1
            else:
                keypress.volume_up()
                vol_up_counter = 0
                print("Volume up")
            
            # reset other counters
            vol_down_counter = 0
            next_track_counter = 0
            prev_track_counter = 0
            play_counter = 0
            pause_counter = 0


        # volume down
        elif line == "down":          # Change this line
            if vol_down_counter <= DEBOUNCER:
                vol_down_counter += 1
            else:
                keypress.volume_down()
                vol_down_counter = 0
                print("Volume down")
            
            # reset other counters
            vol_up_counter = 0
            next_track_counter = 0
            prev_track_counter = 0
            play_counter = 0
            pause_counter = 0

        else:
            print("unknown")
            
            # reset all counters
            vol_up_counter = 0
            vol_down_counter = 0
            next_track_counter = 0
            prev_track_counter = 0
            play_counter = 0
            pause_counter = 0
         



if __name__ == "__main__":
    main()