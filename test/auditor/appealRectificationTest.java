import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class appealRectificationTest {
	final static String admin_password = "password1.1";
	static String auditor_user = "testAuditor1";
	static String tenant_user = "Kopitiam";

	public static void main(String[] args) throws InterruptedException {

		System.setProperty("webdriver.chrome.driver", "D:/Joon Kang/chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		driver.get("http://localhost:8000/");
//		driver.get("http://13.250.116.16:8000/");
		
		// maximize the browser window
		driver.manage().window().maximize();

		WebElement username = driver.findElement(By.name("username"));
		WebElement password = driver.findElement(By.name("password"));
		WebElement submit_button = driver.findElement(By.cssSelector("button[name='login']"));

		username.sendKeys(auditor_user);
		password.sendKeys(admin_password);
		submit_button.click();

		driver.get("http://localhost:8000/attention");
//		driver.get("http://13.250.116.16:8000/attention");
		Thread.sleep(1000);
		
//		// Reject Appeal
		WebElement reject_button = driver.findElement(By.className("btnReject"));
		reject_button.click();
		Thread.sleep(1000);
		
		// Open audit
		WebElement approve_button = driver.findElement(By.className("btnApprove"));
		approve_button.click();
		driver.get("http://localhost:8000/logout");
//		driver.get("http://13.250.116.16:8000/logout");
		
		//Login to tenant page
		driver.get("http://localhost:8000/");
//		driver.get("http://13.250.116.16:8000/");

		WebElement username2 = driver.findElement(By.name("username"));
		WebElement password2 = driver.findElement(By.name("password"));
		WebElement submit_button2 = driver.findElement(By.cssSelector("button[name='login']"));

		username2.sendKeys(tenant_user);
		password2.sendKeys(admin_password);
		Thread.sleep(500);
		submit_button2.click();
		Thread.sleep(1500);
		
		driver.get("http://localhost:8000/notifications/notifications");
//		driver.get("http://13.250.116.16:8000/notifications/notifications");
	}

}
