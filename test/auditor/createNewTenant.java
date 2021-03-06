import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class createNewTenant {
	final static String admin_password = "password1.1";
	static String admin_user = "admin";
	static String auditor_user = "testAuditor1";

	public static void main(String[] args) throws InterruptedException {

		System.setProperty("webdriver.chrome.driver", "D:/Joon Kang/chromedriver.exe");
		WebDriver driver = new ChromeDriver();
//		driver.get("http://localhost:8000/");
		driver.get("http://13.250.116.16:8000/");
		
		// maximize the browser window
		driver.manage().window().maximize();

		WebElement username = driver.findElement(By.name("username"));
		WebElement password = driver.findElement(By.name("password"));
		WebElement submit_button = driver.findElement(By.cssSelector("button[name='login']"));

		username.sendKeys(auditor_user);
		password.sendKeys(admin_password);
		submit_button.click();

//		driver.get("http://localhost:8000/manage-tenant");
		driver.get("http://13.250.116.16:8000/manage-tenant");
		Thread.sleep(1000);

		// Fill up new tenant details
		WebElement compName = driver.findElement(By.name("business_name"));
		compName.sendKeys("GongCha");
		Thread.sleep(500);
		WebElement ownerName = driver.findElement(By.name("name"));
		ownerName.sendKeys("Sarah");
		Thread.sleep(500);
		WebElement uen = driver.findElement(By.name("uen"));
		uen.sendKeys("Z48856922");
		Thread.sleep(500);
		WebElement contact = driver.findElement(By.name("contact"));
		contact.sendKeys("83654896");
		Thread.sleep(500);
		WebElement email = driver.findElement(By.name("email"));
		email.sendKeys("bob@gc.com");
		Thread.sleep(500);
		WebElement leaseDate = driver.findElement(By.name("lease_end_date"));
		leaseDate.sendKeys("02062024");
		Thread.sleep(500);
        WebElement create_button = driver.findElement(By.cssSelector("button[id='b1']"));
        create_button.click();
		driver.findElement(By.name("lease_end_date")).submit();
		
		driver.get("http://13.250.116.16:8000/admin");
		
		WebElement username2 = driver.findElement(By.name("username"));
		WebElement password2 = driver.findElement(By.name("password"));
		WebElement submit_button2 = driver.findElement(By.xpath("//input[@type='submit' and @value='Log in']"));
		
		username2.sendKeys(admin_user);
		password2.sendKeys(admin_password);
		submit_button2.click();
		Thread.sleep(500);
		
		driver.findElement(By.linkText("Tenants")).click();
		Thread.sleep(500);
		driver.findElement(By.linkText("GongCha")).click();
	}
}
