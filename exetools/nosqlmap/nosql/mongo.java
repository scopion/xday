private boolean loginTest(String host,int timeout){
    try {
      byte[] b = new byte[]{0x3f,0x00,0x00,0x00,(byte) 0x97,0x75,(byte) 0xbc,0x60,(byte) 0xff,(byte) 0xff,(byte) 0xff,(byte) 0xff,(byte) 0xd4,0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x61,0x64,0x6d,0x69,0x6e,0x2e,0x24,0x63,0x6d,0x64,0x00,0x00,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x18,0x00,0x00,0x00,0x10,0x6c,0x69,0x73,0x74,0x44,0x61,0x74,0x61,0x62,0x61,0x73,0x65,0x73,0x00,0x01,0x00,0x00,0x00,0x00};
      InetSocketAddress address = new InetSocketAddress(host,27017);
      Socket socket = new Socket();
      socket.connect(address,timeout);
      socket.setSoTimeout(timeout);
      OutputStream out = socket.getOutputStream();
      out.write(b);
      socket.shutdownOutput();
      BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
      String str = "";
      StringBuilder sb = new StringBuilder();
      while((str=br.readLine())!=null){
        sb.append(str);
      }
      return sb.toString().contains("local");
    } catch (Exception e) {
      return false;
    }
  }