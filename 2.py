#2) Sliding Window Protocol
def main():
    w = int(input("Enter window size: "))
    
    f = int(input("Enter number of frames to transmit: "))
    
    frames = []
    print(f"Enter {f} frames: ")
    for i in range(f):
        frames.append(int(input()))
    
    print("\nWith sliding window protocol, the frames will be sent in the following way (assuming no corruption of frames):")
    
    i = 0
    while i < f:
        print(f"\nSending frames: {frames[i:i+w]}")
        if (i + w) <= f:
            print("Acknowledgement of above frames sent is received by sender\n")
        else:
            print("Acknowledgement of above frames sent is received by sender\n")
        
        i += w

if __name__ == "__main__":
    main()
