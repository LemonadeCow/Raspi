package help;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.PinPullResistance;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;


public class iunno {
	
	private static Gpio controller gpio = null;
	private static GpioPinDigitalOutput fan = null;
	
    public static void main(final String[] args) throws InterruptedException{
		
		Runtime.getRuntime().addShutdownHook(new Thread() {
      @Override
      public void run() {
        if (gpio != null) {
          fan.low();
          gpio.shutdown();
        }
      }
    });

 
	gpio = GpioFactory.getInstance();
    fan = gpioController.provisionDigitalOutputPin(RaspiPin.GPIO_7, "fan",PinState.LOW);
    
    while(true){
    pinOut.high();
    Thread.sleep(5000);
    pinOut.low();
    
    gpio.shutdown();
    System.out.println("Hello, Raspberry Pi!");
				}
    }
}

