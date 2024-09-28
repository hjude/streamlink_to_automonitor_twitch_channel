import subprocess
import time
from datetime import datetime

def streamlink_loop(channel):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    """
    ниже измени под свою папку для сохраняемых стримов
    """    
    output_dir = r"C:\Users\User\Desktop\streamlink"
    
    
    output_file = os.path.join(output_dir, f"{channel} - {timestamp} - {{title}}.mp4")

    command = [
        "streamlink",
        f"https://www.twitch.tv/{channel}",
        "best",
        "--output",
        output_file,
        "--retry-streams",
        "180",
        "--ringbuffer-size",
        "128M",
        "--twitch-disable-hosting",
        "--hls-live-restart",
        "--twitch-disable-ads"
    ]

    subprocess.run(command)

def monitor_stream():
    channel_to_monitor = input("Enter the Twitch channel to monitor: ")
    
    while True:
        try:
            streamlink_loop(channel_to_monitor)
            print(f"Stream for {channel_to_monitor} is working correctly.")
        except Exception as e:
            print(f"Error: {e}")
            print(f"Retrying in 60 seconds...")
            time.sleep(60)

if __name__ == "__main__":
    monitor_stream()
