import java.util.Scanner;
public class Main
{
public static void main(String[] args) {
int i;
        String str;
     
        int count[] = new int[256];
        Scanner s = new Scanner(System.in);
       
        System.out.print("Enter a String : ");
        str=s.nextLine();
       
         for (i = 0; i < str.length(); i++) {
            count[(int) str.charAt(i)]++;
        }
        for (i = 0; i < 256; i++) {
            if (count[i] != 0) {
                  System.out.println( (char) i  + " : " + count[i]);
            }
        }
}
}



program2

public class PingPong extends Thread {
static StringBuilder object = new StringBuilder("");

public static void main(String[] args) throws InterruptedException {

Thread t1 = new PingPong();
Thread t2 = new PingPong();

t1.setName("\nping");
t2.setName(" pong");

t1.start();
t2.start();
}

@override
public void run() {
working();
}

void working() {
while (true) {
synchronized (object) {
try {
System.out.print(Thread.currentThread().getName());
object.notify();
object.wait();
} catch (InterruptedException e) {
e.printStackTrace();
}
}
}
}
}