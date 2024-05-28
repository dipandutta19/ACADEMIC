package Computernetwork;
//Client Side

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class StopAndWaitClient {
    private static final int PACKET_SIZE = 1024;
    private static final int TIMEOUT = 2000; // milliseconds

    private DatagramSocket socket;
    private InetAddress serverAddress;
    private int serverPort;
    private int seqNum = 0;

    public StopAndWaitClient(String host, int port) throws Exception {
        socket = new DatagramSocket();
        socket.setSoTimeout(TIMEOUT);
        serverAddress = InetAddress.getByName(host);
        serverPort = port;
    }

    private void sendPacket(String message) throws Exception {
        byte[] data = message.getBytes();
        byte[] packetData = new byte[data.length + 1];
        packetData[0] = (byte) seqNum;
        System.arraycopy(data, 0, packetData, 1, data.length);

        DatagramPacket packet = new DatagramPacket(packetData, packetData.length, serverAddress, serverPort);
        socket.send(packet);

        try {
            byte[] buffer = new byte[PACKET_SIZE];
            DatagramPacket ackPacket = new DatagramPacket(buffer, buffer.length);
            socket.receive(ackPacket);

            int ackSeqNum = buffer[0];
            if (ackSeqNum == seqNum && new String(buffer, 1, 3).equals("ACK")) {
                System.out.println("Received ACK for packet " + seqNum);
                seqNum++;
            } else {
                System.out.println("Received incorrect ACK: " + ackSeqNum);
                sendPacket(message);
            }
        } catch (Exception e) {
            System.out.println("Timeout, resending packet " + seqNum);
            sendPacket(message);
        }
    }

    public static void main(String[] args) throws Exception {
        String host = args.length > 0 ? args[0] : "localhost";
        int port = Integer.parseInt(args.length > 1 ? args[1] : "12345");
        StopAndWaitClient client = new StopAndWaitClient(host, port);

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter messages to send to the server (type 'exit' to quit):");
        while (true) {
            String message = scanner.nextLine();
            if (message.equalsIgnoreCase("exit")) {
                break;
            }
            client.sendPacket(message);
        }
        scanner.close();
    }
}
