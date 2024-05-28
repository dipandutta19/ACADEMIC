package Computernetwork;

//9) Write a program to implement Stop and Wait ARQ Protocol.(Using Java)

//Server Side

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Random;

public class StopAndWaitServer {
    private static final int PACKET_SIZE = 1024;
    private static final int TIMEOUT = 2000; // milliseconds

    private DatagramSocket socket;
    private int expectedSeqNum = 0;

    public StopAndWaitServer(int port) throws Exception {
        socket = new DatagramSocket(port);
        socket.setSoTimeout(TIMEOUT);
    }

    private boolean simulatePacketLoss() {
        return new Random().nextDouble() < 0.1;
    }

    private void receivePacket() throws Exception {
        byte[] buffer = new byte[PACKET_SIZE];
        while (true) {
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            try {
                socket.receive(packet);
                int seqNum = buffer[0];
                byte[] data = new byte[packet.getLength() - 1];
                System.arraycopy(buffer, 1, data, 0, data.length);

                if (simulatePacketLoss()) {
                    System.out.println("Simulated loss of packet " + seqNum);
                    continue;
                }

                if (seqNum == expectedSeqNum) {
                    System.out.println("Received packet " + seqNum + ": " + new String(data));
                    expectedSeqNum++;
                    byte[] ackData = new byte[] { (byte) seqNum, 'A', 'C', 'K' };
                    DatagramPacket ackPacket = new DatagramPacket(ackData, ackData.length, packet.getAddress(), packet.getPort());
                    socket.send(ackPacket);
                } else {
                    System.out.println("Received out-of-order packet " + seqNum + ", expected " + expectedSeqNum);
                }
            } catch (Exception e) {
                System.out.println("Timeout, waiting for packets...");
            }
        }
    }

    public static void main(String[] args) throws Exception {
        int port = Integer.parseInt(args.length > 0 ? args[0] : "12345");
        StopAndWaitServer server = new StopAndWaitServer(port);
        System.out.println("Server started at port " + port);
        server.receivePacket();
    }
}