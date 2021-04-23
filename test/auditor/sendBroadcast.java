import java.sql.Timestamp;
import java.util.Date;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class sendBroadcast {
	final static String admin_password = "password1.1";
	static String auditor_user = "testAuditor1";
	static String tenant_user = "testTenant1";

	public static void main(String[] args) throws InterruptedException {

		System.setProperty("webdriver.chrome.driver", "D:/Joon Kang/chromedriver.exe");
		WebDriver driver = new ChromeDriver();
//		driver.get("http://localhost:8000/");
		driver.get("http://13.250.116.16:8000/");

		WebElement username = driver.findElement(By.name("username"));
		WebElement password = driver.findElement(By.name("password"));
		WebElement submit_button = driver.findElement(By.cssSelector("button[name='login']"));

		username.sendKeys(auditor_user);
		password.sendKeys(admin_password);
		Thread.sleep(500);
		submit_button.click();

//		driver.get("http://localhost:8000/manage-tenant");
		driver.get("http://13.250.116.16:8000/notifications/broadcast");
		Thread.sleep(1000);

		// Send broadcast message
		Date date = new Date();
		Timestamp timestamp = new Timestamp(date.getTime());
		WebElement compName = driver.findElement(By.name("content"));
		compName.sendKeys("Broadcast selenium test at " + timestamp);
		Thread.sleep(1000);
		driver.findElement(By.name("content")).submit();
		driver.get("http://13.250.116.16:8000/logout");
//        WebElement create_button = driver.findElement(By.cssSelector("button[id='b1']"));
//        create_button.click();
		
		//Login to tenant page
//		driver.get("http://localhost:8000/");
		driver.get("http://13.250.116.16:8000/");

		WebElement username2 = driver.findElement(By.name("username"));
		WebElement password2 = driver.findElement(By.name("password"));
		WebElement submit_button2 = driver.findElement(By.cssSelector("button[name='login']"));

		username2.sendKeys(tenant_user);
		password2.sendKeys(admin_password);
		Thread.sleep(500);
		submit_button2.click();
		
		driver.get("http://13.250.116.16:8000/notifications/notifications");
	}
}
