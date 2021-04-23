import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class viewAuditDetails {
	final static String admin_password = "password1.1";
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
		
		// Select Tenant
		Select selTenant = new Select(driver.findElement(By.name("tenant")));
		selTenant.selectByIndex(1);
		Thread.sleep(1000);
		WebElement search_button = driver.findElement(By.cssSelector("button[id='b1']"));
		search_button.click();
		Thread.sleep(1000);
		
		// Open audit
		WebElement view_button = driver.findElement(By.cssSelector("button[id='b1']"));
		view_button.click();
		Thread.sleep(1000);
	}

}
