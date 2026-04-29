import speedtest as st


def Speed_Test():
    test = st.SpeedTest()
    
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)  # Convert to Mbps
    print(f"Download Speed: {down_speed} Mbps")

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)  # Convert to Mbps
    print(f"Upload Speed: {up_speed} Mbps")
    
    ping = test.results.ping
    print(f"Ping: {ping} ms")
    

if __name__ == "__main__":
    Speed_Test() 